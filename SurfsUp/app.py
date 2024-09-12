# Import the dependencies.
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#Start at the homepage.
#List all the available routes.
@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Climate App!<br/>"
        f"<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"<br/>"
        "Enter date ranges below (MM-DD-YYYY):<br/>"
        f"<br/>"
        f"(01-01-2010 to 08-23-2017)<br/>"
        f"<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
    )

#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) 
#to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()
    
    session.close()

    precipitation1 = {date: prcp for date, prcp in precipitation}

    return jsonify(precipitation1)

"""-------------------------------------------------------------------------------------------------------------"""

#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations ():
    stations = session.query(Station.id, Station.station, Station.name).all()

    session.close()

    stations1 = list(np.ravel(stations))

    return jsonify(stations=stations1)

"""-------------------------------------------------------------------------------------------------------------"""

#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def monthly_temp ():
    last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    monthly_temp = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_year).all()
    
    session.close()

    monthly_temp1 = list(np.ravel(monthly_temp))

    return jsonify(temps=monthly_temp1)

"""-------------------------------------------------------------------------------------------------------------"""

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def start_end(start = None, end = None):
    info = [func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    if not end:
        start = dt.datetime.strptime(start, "%m-%d-%Y")
        results = session.query(*info).filter(Measurement.date >= start).all()
        
        session.close()

        temperatures = list(np.ravel(results))

        return jsonify(temps=temperatures)
    
    start = dt.datetime.strptime(start, "%m-%d-%Y")
    end = dt.datetime.strptime(end, "%m-%d-%Y")

    results = session.query(*info).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    temperatures = list(np.ravel(results))

    return jsonify(temps=temperatures)
 

if __name__ == '__main__':
    app.run(debug=True)