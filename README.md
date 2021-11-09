# election-analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the toal number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election baed on popular vote. 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election shows that: 
- There were x votes in the election. 
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham received 23% of the vote and 85,213 votes 
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote adn 11,606 votes
- The winner of the election was 
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes

## Challenge Overview
**Overview of Election Audit**

The purpose of the election audit analysis was to tally the votes from each county to determine which county had the highest voter turnout. 

**Election-Audit Results**

- Total votes cast: 369,711
- Total votes per county: 
  - Jefferson: 10.5% (388,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Largest County Turnout: Denver
- Total votes per candidate: 
  - Stockham: 23% (85,213)
  - DeGette: 73.8% (272,892)
  - Doane: 3.1% (11,606)
- Winner: Diana DeGette (73.8%, 272,892)

A key piece of the code is the following: 
<img width="499" alt="Screenshot 2021-11-08 203523" src="https://user-images.githubusercontent.com/92737670/140845646-3f50e1c2-f04c-42c4-adcf-c440ad0267aa.png">


## Challenge Summary
**Election-Audit Summary**

This script can be used in the same way to count the votes in other elections, but can also be easily modified to address different analysis needs.

One modification would be counting the votes for each candidate in each county.


Another modification would be printing who the winner in each county is.
