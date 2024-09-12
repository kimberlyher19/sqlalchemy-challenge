# ___SQLAlchemy Challenge (Module 10)___

## __Background__
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

### __Part 1:__ Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 

- Precipitation Analysis
- Station Analysis

### __Part 2:__ Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

### __1.__ /
    - Start at the homepage.
    - List all the available routes.

### __2.__ /api/v1.0/precipitation
    - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the  value.
    - Return the JSON representation of your dictionary.

### __3.__ /api/v1.0/stations
    - Return a JSON list of stations from the dataset.

### __4.__ /api/v1.0/tobs
    - Query the dates and temperature observations of the most-active station for the previous year of data.
    - Return a JSON list of temperature observations for the previous year.

### __5.__ /api/v1.0/<start> and /api/v1.0/<start>/<end>
    - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

## __Footnotes__
__'Resources'__ folder contains CSV and sqlite files.
Codes were referenced from the class activities and I used ChatGPT for assistance when my codes weren't running properly. 


### __Thank you for visiting!__