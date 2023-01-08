import csv
import os
import seat_picker
global seatList
global leftList
# this function reads in the file AND picks a random seat from list using seat picker
def student_list_reader(section, people, seatList, leftFlag):
    '''
    This function will read a file of students and pick a seat for them if they are not lefthanded.
    The function returns a dictionary to calling function. Lefthanded students are assigned "err#" to be processed by hand. 
    The function requires 4 variables. (section, people, seatList, leftFlag). 
    seatList is a global variable. section is part of the filename.
    people is the dictionary of seats and their assigned students. 
    This function calls function seat_picker from a different file. 
    The forrmat of student file should be (assumes no header line):
    the three columns that come from WebAssign or Moodle rosters (ID, email, name) and a manually added column for instructor 
    since there were sometimes multiple instructors in one room. 
    the fifth column is a comment if student is left handed. 
    Example format for a right handed student and a left handed student. 
    "Aog, Goa",200123,email@domain.com,instructor1
    "Tlef, Left",200128,left@otherschool.edu,instructor2,left

    File path is hard coded into this function. 
    '''
    leftList = []
    i = 0
# read in line of a person - stick into a list 
    filepath = './' 
# ----------------------------------------------------------------------------
    with open(os.path.join(filepath,section+'.csv')) as file:  # open the list of students file
        csv_reader = csv.reader(file, delimiter=',') 
        for row in csv_reader:
            person_record = row
            
# person_record item 4 is the word left if they are lefthanded. this is added manually to wa list file
# this cell is blank if it is not a left handed person. 
            if (person_record[4] == '') : #don't assign a leftie a seat. important in not enough seats context
                seatnum = seat_picker.seat_picker(seatList, leftList, leftFlag)
                people.update({seatnum: person_record})
              
            else:
                seatnum = 'err' + str(i)
                people.update({seatnum: person_record})
                i+=1 
    file.close()
	
    return people
def student_list_writer(section, people, test):
    ''' 
    This function will sort the dictionary of students assigned to seats by seat number and format the output file.
    This function takes 3 arguments. (section, people, test)
    Filepath is hardcoded into this function. The section is part of the file name. The test is also part of the file name. 
    people is the dictionary of seats and their assigned students.
    '''
    filepath = './'
# -----------------------------------------------------------
# add the seat number as the key for the dictionary
# sort the list by seat number
    sorted_people=sorted(people.items())
    with open(os.path.join(filepath,section+test+'.csv'), mode='w') as seatingchart_file:
        file_writer = csv.writer(seatingchart_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')  
        for person in sorted_people: # make a temporary list of the cells you want in the order you want
        # this includes code for converting the row letter to a number to upload to WebAssign as a "grade". 
            temp=[person[0],person[1][1],  person[1][2], person[1][3], person[1][0],  ord(person[0][0])-64,person[0][1:3], person[1][4] ]
            file_writer.writerow(temp)
    seatingchart_file.close()