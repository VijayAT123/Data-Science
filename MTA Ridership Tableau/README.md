## Overview 
The New York City subway system is the largest subway system in the world by number of stations; over 460.  What began as three independent private companies in the early 1900s moves over 2 million people per day.  All kinds of New Yorkers use the subway to commute across the city; Brooklyn residents near Coney Island to Wall St bankers and executives.  Despite it's vastness, it is the least on-time system in the world.  Only 76.4% of trains operate on schedule, compared to a global average of over 90%<sup>1</sup>.  It has been estimated that train schedule deviation costs New Yorkers nearly 1 million hours of lost time; almost 35,000 each day<sup>2</sup>.  The MTA (Metropolitan Transporation Authority) attributes most of these tardies due to aged traffic control and signaling systems that regularly fail<sup>3</sup>.  The pace of construction and renovation for MTA systems is known for being notoriously slow and over budget.  Thankfully, the MTA is working towards transparency and posts much of its data on New York State’s OpenData portal<sup>4</sup>.

The scope of this visual analysis is aimed towards ridership analytics.  Although the MTA produces their own metrics for passengers, consider this visualization the beginning of many analyses of the New York subway; both visually and through machine learning.  OpenData NY has many datasets concerning train delays and other performance data; this will be used in future analyses.
The objective of this visualization is to view ridership analytics of every station.

## Datasets
The first dataset is entrance and exit geospatial data for every station.  This table includes the lines available at every station, ADA accessibility, division, staffing, cross streets, and crossover (transfer) ability.  This was primarily used to get geographic information for every station.  It’s shape is 1869 x 32.

The second table is turnstile information for each station; number of entries and exits, aggregated every 4 hours.  Eight of these are used, one for each year from 2014-2021.  Each table’s shape is 60,000+ x 9 and has a file size of at least 1 GB, which added significant time importing data and making worksheet changes (even using an extract).  Due to large file size, I had the chance to learn about Tableau’s hyperd, the back-end mechanics of data importing.

Every turnstile year was unioned together, and this union was related to the entrance/exit dataset.  The station naming scheme was different for each dataset.  The turnstile dataset named each station based off of how MetroCards and bank payment cards present the transaction on their ledgers while the entrance/exit used the name presented on station signage.  Even after using Data Interpreter, this required lengthy preprocessing.

## Analysis
The MTA published an official subway map in 1979, and maps since then have been iterations on that design.  Presenting rapid transit maps accurately but in an easily digestible form is a topic of debate among global transit experts.  A map was constructed in Tableau where each station is represented as a dot.
![](https://github.com/VijayAT123/Data-Science/blob/ec2ec15586500a22c34fee8c4fd07b6fcbdc17bc/MTA%20Ridership%20Tableau/MTA%20Stations.png)

Next, each station’s ADA compliance was examined.  ADA stations are equipped with an elevator/escalator for station entry and an “autogate”, a retrofitted emergency exit gate that opens upon the swipe of a “Reduced-Fare AutoGate MetroCard”.  It is well known that stations aren’t accessible friendly, but the degree of such was underestimated.
![](https://github.com/VijayAT123/Data-Science/blob/ec2ec15586500a22c34fee8c4fd07b6fcbdc17bc/MTA%20Ridership%20Tableau/ADA%20Compliant%20Stations.png) 
Of the 472 service stations, only 90 are accessible, with most of them being in mid-lower Manhattan.  Arguably, residents of the outer boroughs are the ones who would most benefit from ADA services, but negligence of the outer boroughs is an underlying theme of the MTA.  Since publishing the entrance/exit dataset, which contains station ADA compliance, the MTA has made 40 additional stations accessible.

Next, average yearly ridership was plotted per station.  A density graph was used in combination with color to show stations that have the most entries through the turnstile.  Green stations have lower average yearly entires compared to red.  Years were used in pages for the animation.
![](https://github.com/VijayAT123/Data-Science/blob/ec2ec15586500a22c34fee8c4fd07b6fcbdc17bc/MTA%20Ridership%20Tableau/Avg%20Entries%20Density.png) 
Interestingly, uptown Manhattan and the Bronx saw a steady increase in average entries, with the White Plains Road line have a similar appearance to mid-town.  Dumbo and the surrounding areas saw similar growth.  The Stuyvesant and Medical City neighborhoods saw a sharp decrease after 2018, as well as Meatpacking, Chelsea, and the West Village.  Why is the area between midtown and downtown Manhattan experiencing lower average yearly entries?



Finally, a bar graph was created to illustrate monthly year-over-year change in entries.  Color was used to supplement the percent difference and years were again used in the animation pages.
![](https://github.com/VijayAT123/Data-Science/blob/ec2ec15586500a22c34fee8c4fd07b6fcbdc17bc/MTA%20Ridership%20Tableau/%25%20Change%20Entries%20Monthly.png) 
The first major COVID lockdown is clearly visible in 2020’s YoY graph.  Overall, 2020 ridership was 8% of 2019.  In fact, ridership took longer to reach “pre-pandemic levels” than the MTA expected and a task force was established.  2017 experienced little deviation from 2016 ridership.  Other than these insights, all other monthly YoY information have no clear explanation.  No month experiences consistent increased growth or decline for any year.  Each month fluctuates its average entries every year and does not seem to be isolated to a season/quarter.  Even holiday entries seems to grow and shrink outside of 2020.  


<sup>1</sup> Griffin, Anthony. “Clearing Clearing Up Misconceptions about Train Punctuality”, Kokoro Media, 12 Jun. 2020, https://kokoro-jp.com/unfiltered/103/

<sup>2</sup> Walker, Ameena (2017). “NYC commuters collectively spend 35,000 hours each day waiting on delayed trains”, Curbed New York, 25 Oct. 2017, https://ny.curbed.com/2017/10/25/16548750/mta-subway-delays-average-wait-time-report 

<sup>3</sup> Walker, Ameena (2017). “MTA data reveals the most delayed subway lines”, Curbed New York, 17 Jun. 2017, https://ny.curbed.com/2017/6/17/15824804/mta-most-delayed-subway-lines-data-nyc

<sup>4</sup> “Agencies & Authorities > Metropolitan Transportation Authority”, New York State, https://data.ny.gov/browse?Dataset-Information_Agency=Metropolitan%20Transportation%20 Authority&limitTo=datasets

<sup>5</sup> “Accessible by Subway”, MTA, https://new.mta.info/accessibility/travel/subway
