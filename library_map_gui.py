import tkinter as tk
import csv

subject_classmark_file = 'subject_n_classmark.csv'
location_classmark_file = 'location_n_classmark.csv'

csv_column1= 'subject_name'
csv_column2= 'class_mark'
csv_column3= 'location'

root= tk.Tk()

#setting the dimensions of tkinter frame using geometry function
root.geometry("1000x300")


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

def check_user_input():
    # storing  input gotten from user in user_input variable
    user_input = first_entry.get()

    if (user_input == "1"):
        response = "\nEnter the subject name/part-name:\n"
    if (user_input == "2"):
        response = "\nEnter the classmark:\n"
    if (user_input == "3"):
        response = "\nLocation options are:\n\tTop Floor Back left, \tTop Floor Back right,\n\tTop Floor Front left, \tTop Floor Front Right, \n\tMiddle floor, \t\tGround floor\nEnter any of the location listed above:\n"
    elif (user_input <="0" or user_input >="4"):
        response = "invalid input, you are to enter 1 or 2 or 3\n"
    
    # Display corresponding response after checking user input
    label = tk.Label(text=response)
    label.pack()

    global second_entry

    second_entry = tk.Entry(root, width=15, textvariable=tk.StringVar())
    second_entry.pack()

    button2 = tk.Button(root, text="Search", command= search_for_string)
    button2.pack()

#search for corresponding entry made by user
def search_for_string():
    user_input2 = second_entry.get()
    # Using list comprehension to search for user_input2 and append search_loop1 to search_result
    search_result = [ search_loop1 for search_loop1 in list1 for search_loop2 in search_loop1 if user_input2 in search_loop2]
    # print("\n{}".format(search_result))

    if len(search_result) != 0:
        label = tk.Label(text="Subject/part-name\tClassmark\t\tLocation\n")
        label.pack()
        for result in search_result:
            label = tk.Label(text='\t\t'.join(result))
            label.pack()
    else:
        label = tk.Label(text="No result found")
        label.pack()



#calling function to load csv file
dict1 = read_csv_file(subject_classmark_file)
dict2 = read_csv_file(location_classmark_file)

# merge dictionary as a single list
list1 = merge_dict(dict1, dict2)
    
# first display that user sees
first_display = tk.Label(text="\tPress:\t1 to enter a subject name or part-name\nOR\n    2 to enter a classmark\nOR\n  3 to enter a location\n")
first_entry = tk.Entry(root, width=15, textvariable=tk.StringVar())
first_display.pack()
first_entry.pack()

button = tk.Button(root, text="Enter", command= check_user_input)
button.pack()


root.mainloop()


# References:
# https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter

# https://stackoverflow.com/questions/67268399/i-want-to-take-user-input-and-output-it-inside-gui

# https://www.pythontutorial.net/tkinter/

# https://realpython.com/python-gui-tkinter/