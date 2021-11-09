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

**Modification #1**

One modification would be counting the votes for each candidate in each county.

  **Code**

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            jefferson_dict[candidate_name] = 0
            denver_dict[candidate_name] = 0
            arapahoe_dict[candidate_name] = 0

        # Add a vote to that candidate's count for each county
        if county_name == "Jefferson":
            jefferson_dict[candidate_name] += 1

        if county_name == "Denver":
            denver_dict[candidate_name] += 1
        
        if county_name == "Arapahoe":
            arapahoe_dict[candidate_name] += 1

    print(f"The vote distribution in Jefferson is: {jefferson_dict}")
    print(f"The vote distribution in Denver is: {denver_dict}")
    print(f"The vote distribution in Arapahoe is: {arapahoe_dict}")
    
  **Output** 

The vote distribution in Jefferson is: {'Charles Casper Stockham': 19723, 'Diana DeGette': 17963, 'Raymon Anthony Doane': 1169}

The vote distribution in Denver is: {'Charles Casper Stockham': 57188, 'Diana DeGette': 239282, 'Raymon Anthony Doane': 9585}

The vote distribution in Arapahoe is: {'Charles Casper Stockham': 8302, 'Diana DeGette': 15647, 'Raymon Anthony Doane': 852}

**Modification #2**

Another modification would be printing who the winner in each county is.

**Code**

    winning_count = 0
    for candidate_name in jefferson_dict:
        votes = jefferson_dict.get(candidate_name)

        if votes > winning_count:
            winning_count = votes
            jefferson_winner = candidate_name
    print(f"The winner in Jefferson is: {jefferson_winner}")

    winning_count = 0
    for candidate_name in denver_dict:
        votes = denver_dict.get(candidate_name)

        if votes > winning_count:
            winning_count = votes
            denver_winner = candidate_name
    print(f"The winner in Denver is: {denver_winner}")

    winning_count = 0
    for candidate_name in arapahoe_dict:
        votes = arapahoe_dict.get(candidate_name)

        if votes > winning_count:
            winning_count = votes
            arapahoe_winner = candidate_name
    print(f"The winner in Arapahoe is: {arapahoe_winner}")

**Output**

The winner in Jefferson is: Charles Casper Stockham

The winner in Denver is: Diana DeGette

The winner in Arapahoe is: Diana DeGette
