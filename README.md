# Data-Science

A collection of analyses and visualizations of mostly public sector datasets.


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
