# Temperature data for June and December in Oahu

## Overview
W. Avy likes your analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

You have the last 12 months of precipitation data already loaded into your SQLite database, so you are ready to go. W. Avy supplied you with the data he wants us to use and has asked you to look at a full year of data.

we want to make sure to provide W. Avy with some solid statistical analysis—such as the mean, standard deviation, minimum, and maximum. He needs hard results if he's going to invest his money.

"This is great! It's clear from your analysis that Oahu is a great location for the new surf shop. We're almost ready to switch out our suit and ties for some sandals! My only question is, how many stations are being used to collect this information? Is it possible that we don't have enough data collection stations for this information to be valid?"

Thankfully, you know you can run a query on the SQLite database to find this information quickly. You respond, "Glad the analysis is helping you with your decision-making! Great question about the number of stations. Let me do some quick queries and find out for us." And, with that, you get back to work.
Now we know there are 9 stations from which precipitation data is being collected.

W. Avy tells you that he's interested in the most active station; he believes it will provide the most data and help you determine the best location for the surf shop. However, you know that more data doesn't necessarily equate to more accurate results. But W. Avy is passionate about the location—he's convinced that it will provide the best weather for surfing and eating ice cream. So you tell him that you'll investigate this location further.

It occurs to you that he hasn't asked for an analysis of the temperature yet, so you decide to dive into temperature data.
Let's get to work on our temperature analysis! We'll be using the results from our last query, which gave us the most active station, to gather some basic statistics. For our most active station, we'll need to find the minimum, maximum, and average temperatures.

## Resources
- Data Source: hawaii.sqlite
- Software: Jupyter Notebook 6.4.8, Python 3.7.13, SQLAlchemy, 
- Library: Pandas 1.3.5

## Results
There is a bulleted list that addresses the three key differences in weather between June and December.

<img src="https://github.com/laneyberm/surfs_up/blob/main/june_temp.png" width="150">
<img src="https://github.com/laneyberm/surfs_up/blob/main/dec_temp.png" width="150">

## Summary
There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December.
