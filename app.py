# Dependancies
import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependancies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask dependancies
from flask import Flask, jsonify

# Database Set Up
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Define our app for our Flask application
app = Flask(__name__)

# 
# If we wanted to import our app.py file into another Python file named example.py, 
# the variable __name__ would be set to example.
# When we run the script with python app.py, the __name__ variable will be set to __main__. 
# This indicates that we are not using any other file to run this code

#import app
#print("example __name__ = %s", __name__)
#if __name__ == "__main__":
#    print("example is being run directly.")
#else:
#    print("example is being imported")

# define the welcome route
@app.route("/")

# Add the routing information for each of the other routes
# Our return statement will have f-strings as a reference to all of the other routes
def welcome():
    return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # use jsonify() to format our results into a JSON structured file
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
# Query the primary station for all the temperature observations from the previous year
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # Unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    # Jsonify our temps list, and then return it. Add the return statement to the end of your code
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Add parameters to our stats()function: a start parameter and an end parameter. Set them both to None.
def stats(start=None, end=None):
    # Create a query to select the minimum, average, and maximum temperatures from our SQLite database. 
    # We'll start by just creating a list called sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Add an if-not statement to determine the starting and ending date
    if not end:
        # Asterisk is used to indicate multiple results: minimum, average, and maximum temperatures
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Unravel the results into a one-dimensional array and convert that array into a list
        temps = list(np.ravel(results))
        return jsonify(temps)
    # Calculate the temperature minimum, average, and maximum with the start and end dates. 
    # Use the sel list, which is simply the data points we need to collect
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)