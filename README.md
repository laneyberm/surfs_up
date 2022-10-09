# Temperature data for June and December in Oahu

## Overview
W. Avy wants invest in a new surf and ice cream shop business in Oahu since his last location recieved too much rain and had to close. He has given us weather data to determine where will be the best location and if an ice cream shop is sustainable year-round.

We will find information about temperature trends before opening the surf shop. We have loaded the data into a SQLite database and will make statistical analysis—such as the mean, standard deviation, minimum, and maximum. 


## Resources
- Data Source: hawaii.sqlite
- Software: Jupyter Notebook 6.4.8, Python 3.7.13, SQLAlchemy 
- Library: Pandas 1.3.5, NumPy


## Results
<img src="https://github.com/laneyberm/surfs_up/blob/main/june_temp.png" width="150"><img src="https://github.com/laneyberm/surfs_up/blob/main/dec_temp.png" width="170">

Above are the statistical analysis of the June and December Temperatures in Oahu. We can note the following:
- June is warmer in Oahu than the month of December. The average temperature in June is about 75°F  and in December is abour 71°F .
- June's low temperture is 64°F  and December's low temperature is 56°F . 
- June and December high temperatures are similar, 85°F and 83°F respectfully. 


## Summary
Oahu is a great location for the new surf shop. 

While the June temp is hotter by a few degress, this isn't too significant to make a big difference. Meaning that probably between them for those 6 months we can tell investors that we could capitalize on people fleeing colder temps from the northern hemisphere or US mainland: that means good tourism = consistent potential revenue at least with regard to stable parameters. We get to this conclusion looking at either the averages or even the max temps above.

Heat and good temp is great to consider for a surf shop, but W. Avy mentioned the last surf shop he invested in went under because it got "rained out." We'd want to go above this and also gather data on wave patterns near the specific location we are looking at to attract more of the surfer crowd and also explore the data set with more queries on the weather at large.

Also, as noted above, the temps for the minimum / lowest temp are what are most different between June and December. I would run queries to determine what time of the day is colder, and how long that cold temp in June lasts.

Stations and times of day weather 


Thankfully, you know you can run a query on the SQLite database to find this information quickly. You respond, "Glad the analysis is helping you with your decision-making! Great question about the number of stations. Let me do some quick queries and find out for us." And, with that, you get back to work.
Now we know there are 9 stations from which precipitation data is being collected.

W. Avy tells you that he's interested in the most active station; he believes it will provide the most data and help you determine the best location for the surf shop. However, you know that more data doesn't necessarily equate to more accurate results. But W. Avy is passionate about the location—he's convinced that it will provide the best weather for surfing and eating ice cream. So you tell him that you'll investigate this location further.

It occurs to you that he hasn't asked for an analysis of the temperature yet, so you decide to dive into temperature data.
Let's get to work on our temperature analysis! We'll be using the results from our last query, which gave us the most active station, to gather some basic statistics. For our most active station, we'll need to find the minimum, maximum, and average temperatures.
