# Module_3_Challenge_Election_Results


## Overview of Election Audit 

The Colorado Election Commission has requested help with determining the results of this years election. They have sent us a CSV file that contains the data from the election but the results are unclear. To help them we need to transform the csv file into with thousands of lines of information into concise results.

## Election Audit Results (See Code Print Out Below)


-How many votes were cast in this congressional election?
The Total Number of votes cast in this elections was 369,711

-Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-Which county had the largest number of votes?
Largest County Turnout: Denver

-Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%


Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------


### Election Audit Summary

The script written for the election commission can be used for years to come simply by loading in next year's CSV of data, as long as that CSV is structured the same way as this year's. If election rules changed the script could be modified to allow for ranked choice voting by completing who would win initally, eliminating the candidates that did not recieve enough 1st rank votes, then redistributing the votes as needed. Additionally we could add data about each candidates platform and cross-reference with number of votes and determine what platforms were the most popular regardless of candidate.
