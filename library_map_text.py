#Author: madaki
#Purpose: system design and programming coursework

import csv

subject_classmark_file = 'subject_n_classmark.csv'
location_classmark_file = 'location_n_classmark.csv'

csv_column1= 'subject_name'
csv_column2= 'class_mark'
csv_column3= 'location'


#definition of function to request first input from user
def request_first_user_input():
	user_input = str(input("\nPress:  1 to enter a subject name or part-name\n\t\tOR\n\t2 to enter a classmark\n\t\tOR\n\t3 to enter a location\n"))
	return user_input
	
#definition of function to request second input from user
def request_second_user_input(response):
	if (response == "invalid input, you are to enter 1 or 2 or 3\n"):
		print('Caution: {}'.format(response))
		exit()
	else:
		user_input2 = str(input(response))
	return user_input2

#definition of function to check first input and return response
def check_user_input(user_input):
	if (user_input == "1"):
		response = "\nEnter the subject name/part-name:\n"
	if (user_input == "2"):
		response = "\nEnter the classmark:\n"
	if (user_input == "3"):
		response = "\nLocation options are:\n\tTop Floor Back left, \tTop Floor Back right,\n\tTop Floor Front left, \tTop Floor Front Right, \n\tMiddle floor, \t\tGround floor\nEnter any of the location listed above:\n"
	elif (user_input <="0" or user_input >="4"):
		response = "invalid input, you are to enter 1 or 2 or 3\n"
	return response


#definition of function to read csv file
def read_csv_file(csv_file_):
	with open(csv_file_, 'r') as file1:
		file_content_read = csv.DictReader(file1)
		map_dict = {}
		for row in file_content_read:
			for column, value in row.items():
				map_dict.setdefault(column,[]).append(value)
		# print("{}\n".format(map_dict))
	return map_dict


#Merge dictionary, convert and return a list
def merge_dict(dict1, dict2):
	# merging two dictionaries into one
	combined_dict = {**dict1, **dict2}

	#get the no of rows in combined_dict dictionary
	for key,value in combined_dict.items():
		no_of_rows = len(value)

	#custom conversion of dictionary to list, to get: subject,classmar,location
	list1 = []
	for x in range(no_of_rows):
		list1.append([combined_dict[csv_column1][x], combined_dict[csv_column2][x], combined_dict[csv_column3][x]])
	# print(list1)
	return list1


#search for corresponding entry made by user
def search_for_string(user_input2, list1):
	# Using list comprehension to search for user_input2 and append search_loop1 to search_result
	search_result = [ search_loop1 for search_loop1 in list1 for search_loop2 in search_loop1 if user_input2 in search_loop2]
	# print("\n{}".format(search_result))
	return search_result		


#first display when program is run
print("***************** LIBRARY MAP SOFTWARE *****************")

#calling function for first prompt to recieve selection option made by user
user_input = request_first_user_input()

#calling function for checking user input and returning the appropriate response
response = check_user_input(user_input)

#calling function for second prompt to recieve input from, based on option chosen by user
user_input2 = request_second_user_input(response)

#calling function to load csv file
dict1 = read_csv_file(subject_classmark_file)
dict2 = read_csv_file(location_classmark_file)

list1 = merge_dict(dict1, dict2)

if len(search_for_string(user_input2, list1)) != 0:
	print("Subject/part-name\tClassmark\t\tLocation\n")
	for result in search_for_string(user_input2, list1):
		print('\t\t'.join(result))
else:
	print("No result found")


# References:
# https://www.studytonight.com/python-howtos/how-to-read-csv-file-in-python

# https://stackoverflow.com/questions/53189427/how-to-open-multiple-csv-files-from-a-folder-in-python

# https://www.business-science.io/python/2021/09/21/python-read-csv.html

# https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file

# https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file

# https://www.adamsmith.haus/python/answers/how-to-read-a-%60.csv%60-file-into-a-dictionary-in-python

# https://stackoverflow.com/questions/20072870/combining-two-dictionaries-into-one-with-the-same-keys

# https://stackoverflow.com/questions/69460444/merge-dictionaries-with-same-key-from-two-lists-of-dicts-in-python

# https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression

# https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374

# https://www.pythonforbeginners.com/basics/read-csv-into-a-list-of-lists-in-python

# https://www.freecodecamp.org/news/merge-dictionaries-in-python/

# https://www.w3schools.com/python/python_lists.asp

# https://www.scaler.com/topics/merge-two-list-in-python/

# https://stackoverflow.com/questions/19843457/counting-how-many-values-were-attributed-to-a-key-an-a-python-3-2-dictionary

# https://stackoverflow.com/questions/10106901/elegant-find-sub-list-in-list

# https://www.geeksforgeeks.org/python-find-index-containing-string-in-list/

# https://www.geeksforgeeks.org/how-to-count-the-number-of-lines-in-a-csv-file-in-python/

# https://www.folkstalk.com/tech/python-counting-dictionary-with-code-examples/

# https://www.codeproject.com/Questions/5322097/Use-one-list-as-search-key-for-another-list-with-s

# https://stackoverflow.com/questions/38054897/python-searching-nested-lists

# https://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python