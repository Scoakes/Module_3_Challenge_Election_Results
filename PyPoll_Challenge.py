#Import Dependencies 
import csv
#Dont need for direct path
import os

#Direct File Path
file_to_load = ("/Users/christopheroakes/Documents/Coding Bootcamp/Module 3/Election_Analysis/Resources /election_results.csv")
# Add a variable to save the file to a path.
file_to_save = ("/Users/christopheroakes/Documents/Coding Bootcamp/Module 3/Election_Analysis/Resources /Analysis.txt")

# Initialize a total vote 
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# County variables
county_list = []
county_votes = {}

# Track winners
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track turnout
largest_county_turnout = ""
largest_county_turnout_count = 0
largest_county_percentage = 0

# Read the csv 
with open(file_to_load) as election_data:
    # Read the file 
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Candidate name from each row.
        candidate_name = row[2]

        # 3: County name from each row.
        county_name = row[1]

        # Add to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Track that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Add counties
        if county_name not in county_list:

            
            county_list.append(county_name)

            
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results 
with open(file_to_save, "w") as txt_file:

    # Print the final vote count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Repetition statement to get the county from the county dictionary
    for county in county_list:

        #Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary
        county_vote = county_votes.get(county)

        #Calculate the percent of total votes for the county.
        county_vote_percentage = float(county_vote) / float(total_votes) * 100

        
        county_results = f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n"

        #Print the county results
        print(county_results)

        #Save the county votes to a text file
        txt_file.write(county_results)

        # Write a decision statement to determine the winning county 
        if (county_vote > largest_county_turnout_count) and (
            county_vote_percentage > largest_county_percentage
        ):
            # True
            largest_county_turnout_count = county_vote
            largest_county_percentage = county_vote_percentage
            largest_county_turnout = county

    # 7: Print the county with the largest turnout 
    winning_county = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
    )
    print(winning_county)

    #Save the county with the largest turnout to a text file
    txt_file.write(winning_county)

    #Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:

        #Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        #Print each candidate's voter count and percentage 
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's info
    txt_file.write(winning_candidate_summary)