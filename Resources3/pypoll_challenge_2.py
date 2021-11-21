
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

jefferson_dict = {}
denver_dict = {}
arapahoe_dict = {}

Jefferson_votes = 0
Denver_votes = 0
Arapahoe_votes = 0

jefferson_winner = ""
denver_winner = ""
arapahoe_winner = ""

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
turnout_county = ""
turnout_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
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
