## Wealth Inequality
It’s no secret that the US has seen increasing wealth inequality for a few decades. In fact, the Census reports a Gini index in their American Community Survey down to the block level of detail, the smallest geographic unit for the Census. The Gini index is a measure of the distribution of wealth1, expressed as
$$G = \frac {\sum_{i=1}^{n} \sum_{j=1}^{n} |x_i - x_j  |}{2 \sum_{i=1}^{n} \sum_{j=1}^{n} x_j} = \frac {\sum_{i=1}^{n} \sum_{j=1}^{n} |x_i - x_j  |}{2n \sum_{j=1}^{n}x_j} = \frac {\sum_{i=1}^{n} \sum_{j=1}^{n} |x_i - x_j  |}{2n^2 \bar{x}}$$ 
where i and j are every possible combination of paired individuals in the population, x
is the income of an individual, and x ̄ is the average population income. It ranges from 0 to 1, where 0 is absolute control of all of a population’s wealth by a singular individual and 1 is equal distribution of a population’s entire wealth to its people.
The FBI’s Crime Data Explorer hosts the data collected from the Uniform Crime Reporting program,2 the national crime reporting database. Annual reports of violence and property related crimes are compiled from the National Incident-Based Reporting System and the Summary Reporting System. Over 60 types of crime are summarized in these reports from every level of law enforcement.
In these visual analyses, the correlation between wealth disparity and financial- related crimes will be explored. The rationale is that higher Gini communities will see less small-scale financial crimes than an area with high wealth inequality.
### Objective
The goal is to be able to partially explain financial related crimes in high inequality communities. Although this will not be a simple causal relationship, there may be an explanation for why financial crimes are happening in these communities.
Communities may be able to use these visuals as evidence for providing more social support and encouraging more community-wide activities.
### Datasets
Crime data is retrieved from the FBI’s Crime in the United States annual reports from 2013 to 2019 (the latest available year).  The Census American Community Survey 5-year estimates from 2013 to 2020, table B19083 to be exact, were used for Gini index information.  The 5-year estimate was chosen over the 1-year estimate because the 5-year has more granularity for level of detail, is more precise, and is available for every size of population, whereas the 1-year only provides data for populations over 65,000 people.  As mentioned, the FBI dataset provides data from every level of law enforcement.  Although the ACS dataset goes down to the block level, the county level is the lowest level of detail where the FBI and ACS datasets intersect.  
	The two datasets were imported using data interpreter since both had merged cells that can’t be interpreted properly by Tableau.  The crime dataset was filtered to keep only metropolitan and non-metropolitan counties.  Finally, the two were left-joined (Gini data on the left) and the resulting data shape was 663,200 x 88.  
### Findings
To get an idea of overall inequality, comparing the Gini index of all counties in the US seemed like a good first start.  To view changes in inequality over time, the years were placed in the pages box.  The Gini index was reporting using binary colors; either above or below 0.5.  The full visualization is available [here, on Tableau Public](https://public.tableau.com/app/profile/vijay1900/viz/WealthInequalityandCrimeattheCountyLevel/GiniIndxesCounty).

![Pic](https://github.com/VijayAT123/Data-Science/blob/6a6969c451c0157a312456e7064fe7bcacb13dda/Wealth%20Inequality%20Tableau/Gini%20Indxes%20County.png)

As seen, a Gini index above 0.5 is a rarity in the contiguous US and Alaska.  Puerto Rico however is green for most counties for all reporting years.  There isn’t a drastic change in wealth inequality over the years and not many counties flip their wealth disparity. 

Next, the distribution of Gini indexes was plotted to explore descriptive statistics.  Again, years were used as pages to view changes over time, and the full visualization can be [viewed here](https://public.tableau.com/app/profile/vijay1900/viz/DistributionofGiniIndexes2011-2020/GiniDistribution?publish=yes).  The median and average Gini for all counties were very close to each other every year.  The spread of the indexes slightly narrowed from 2013-2017, as indicated by a decrease in the distance from +1 and -1 SD over those years.  Both the mean and median indexes had increased by about 0.1, so there is a minuscule shift towards more wealth equality nationwide.

After examining Gini related metrics, the correlation between Gini index and crime rate can be examined.  Financial crimes, including `Larceny/Theft`, `Shoplifting`, `Theft from Building`, and `Robbery` were plotted against the county’s Gini index.  Again, years were used for pages in animation and can be [viewed here](https://public.tableau.com/app/profile/vijay1900/viz/FinancialCrimesvsGini/FinancialCrimesvsGini?publish=yes)
![](https://github.com/VijayAT123/Data-Science/blob/6a6969c451c0157a312456e7064fe7bcacb13dda/Wealth%20Inequality%20Tableau/Financial%20Crimes%20vs%20Gini.png)

In fact, the counties with the least wealth equality did not have the most number of financial-related crimes.  The orange Gini had the most crimes across all years.  This could be due to a number of factors:
* Orange counties have higher reporting of crimes or red counties exhibit habitual under-reporting
* More counties within the orange Gini cluster so there is a bigger sample available
* Red counties may have high wealth inequality, but not be considered low income
* Wealth inequality vs occurrence of financial-related crimes has a bell-curve relationship instead of a linear relationship and requires a multifaceted analysis
There weren’t enough counties with a Gini index above 0.6.  Of those counties, less than 10 had reported financial-related crimes.  These phenomena were about the same every year, but 2020 saw reports of crime across a wider range of Gini indexes.

Lastly, the correlation between drug-related crimes and wealth disparity was investigated.  The FBI reported “Drug/Narcotic Offenses”, “Drug Equipment Violations”,  “Drug/Narcotic Violations” for counties across the years.  This time, data was aggregated for every year in one view instead of viewing change in offenses over time, also [available here](https://public.tableau.com/app/profile/vijay1900/viz/DrugCrimesvsGini/DrugCrimesvsGini?publish=yes)
![](https://github.com/VijayAT123/Data-Science/blob/6a6969c451c0157a312456e7064fe7bcacb13dda/Wealth%20Inequality%20Tableau/Wealth%20Inequality%20vs.%20Financial%20and%20Drug-Related%20Crimes.pdf) 
Similar to the financial crimes, drug offenses follow a bell shape instead of a linear relationship.  This could be due to similar factors explained earlier, or completely different underlying explanations.

In conclusion, financial and drug related crimes may be loosely correlated to wealth inequality within a community.  Other relationships to consider include Gini-population, population-crime, and taking population into account when looking at the Gini-crime relation.  Analyzing at the county level may be too low-level of detail; state metrics may provide better evidence for a conclusion.
