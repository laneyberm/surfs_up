# Temperature Data for June and December in Oahu, Hawaii

## Overview
W. Avy wants invest in a new surf and ice cream shop business in Oahu since his last location recieved too much rain and had to close. He has given us weather data to determine where will be the best location and if an ice cream shop is sustainable year-round.

We will find information about temperature trends before opening the surf shop. We have loaded the data into a SQLite database and will make statistical analysis—such as the mean, standard deviation, minimum, and maximum to determine the sustainability of the surf and ice cream shop. 


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
Oahu is a great location for the new surf shop. When looking at average temperatures from the above information, the temperatures are ideal in both months for the surf and ice cream shop to be sustainable.

One opportunity to research is the low temperature in December. We should find how often this happens or what time the temperature is taken. Typically, temperature is lower in the eveing and early morning which is not when the shop would be open. So, this information might not be relevant the shop operating hours. 

Additionally, W. Avy mentioned that the previous location got "rained out". We shoudl also provide information on precipation for the area to have the client aware of this data in his go farward with the investment.
