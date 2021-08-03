# Modules
import os
import csv

canidate_names = []


#Create relative csv path
csvpath = os.path.join("Resources",'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    #initialize Vote Counter and create empty list for Canidate_Names
    #total_vote_count = 3521002
    canidate_names = []
    vote_count = 0
   
#count number of votes   
    rows = list(csvreader)
    rows = rows[1:]

#Create Counter Variables
    Khan_counter = 0 
    Correy_counter = 0 
    Li_counter = 0
    Tooley_counter = 0 
    
    for row in rows:

        vote_count += 1
    print(f' the Total Vote Count is {vote_count}') 

#create conditional to tease out Canidate Names  
    for row in rows: 
        if row[2] not in canidate_names:
            canidate_names.append(row[2])
    print(f'These are the canidates: {canidate_names}')

    #Create Khan Canidate counter
    for row in rows:
        if row[2] == "Khan": 
            Khan_counter +=1
        if row[2] == "Correy": 
            Correy_counter +=1 
        if row[2] == "Li": 
            Li_counter +=1
        if row[2] == "O'Tooley": 
            Tooley_counter +=1 
    # Calculate Kahn's number of votes
    print(f'Total votes for Khan is: {Khan_counter}')
    # Calculate Kahn's Popular Vote %
    Kahn_percentage = (Khan_counter/vote_count) * 100
    print(f'Kahn won {Kahn_percentage} of the Popular Vote')
    
    # Calculate Correy's number of votes
    print(f'Total votes for Correy is: {Correy_counter}')
    # Calculate Correy's Popular Vote %
    Correy_percentage = (Correy_counter/vote_count) * 100
    print(f'Correy won {Correy_percentage} of the Popular Vote')

    #Calculate Li  number of votes
    print(f'Total votes for Li is: {Li_counter}')
    # Calculate Li's Popular Vote %
    Li_percentage = (Li_counter/vote_count) * 100
    print(f'Li won {Li_percentage} of the Popular Vote')

    #Calculate O'Tooley number of votes
    print(f"Total votes for O'Tooley is: {Tooley_counter}")
    # Calculate O'Tooley's Popular Vote %
    Tooley_percentage = (Tooley_counter/vote_count) * 100
    print(f"O'Tooley won {Tooley_percentage} of the Popular Vote")
    
    #pick a winner 
    if max(Khan_counter,Correy_counter,Li_counter,Tooley_counter) == Khan_counter: 
        print(f"Khan is the Winner")
    if max(Khan_counter,Correy_counter,Li_counter,Tooley_counter) == Correy_counter: 
        print(f"Correy is the Winner")
    if max(Khan_counter,Correy_counter,Li_counter,Tooley_counter) == Li_counter: 
        print(f"Li is the Winner")
    if max(Khan_counter,Correy_counter,Li_counter,Tooley_counter) == Tooley_counter: 
        print(f"O'Tooley  is the Winner")      