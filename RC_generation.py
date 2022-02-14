import csv
import os

second_choice_list = []
third_choice_list = []

candidate_1 = "Charles Casper Stockham"
candidate_2 = "Diana DeGette"
candidate_3 = "Raymon Anthony Doane"

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save_2 = os.path.join("Resources", "second_choice_vote.txt")
file_to_save_3 = os.path.join("Resources", "third_choice_vote.txt")

with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        if (int(row[0]) % 2 == 0) & (row[2] == candidate_1):
            second_choice_list.append(candidate_2)
            third_choice_list.append(candidate_3)
        
        elif (int(row[0]) % 2 != 0) & (row[2] == candidate_1):
            second_choice_list.append(candidate_3)
            third_choice_list.append(candidate_2)

        elif (int(row[0]) % 2 == 0) & (row[2] == candidate_2):
            second_choice_list.append(candidate_1)
            third_choice_list.append(candidate_3)
        
        elif (int(row[0]) % 2 != 0) & (row[2] == candidate_2):
            second_choice_list.append(candidate_3)
            third_choice_list.append(candidate_1)

        elif (int(row[0]) % 2 == 0) & (row[2] == candidate_3):
            second_choice_list.append(candidate_1)
            third_choice_list.append(candidate_2)

        else:
            second_choice_list.append(candidate_2)
            third_choice_list.append(candidate_1)

#second_third_zip = zip(second_choice_list, third_choice_list)

with open(file_to_save_2, "w") as txt_file_2:
    txt_file_2.writelines("%s/n" % name for name in second_choice_list)

with open(file_to_save_3, "w") as txt_file_3:
    txt_file_3.writelines("%s/n" % name for name in third_choice_list)