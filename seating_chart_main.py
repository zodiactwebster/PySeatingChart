import os
import csv
import room_file_reader
import student_list_fileio
'''
This is the main file for seat assignments. It can be used to loop over all the
sections and all the tests. This current version loops only over test.
This requires a csv file by section of students and a csv file of seats. 
Left handed seat assignments were not automated. 

File paths for student lists and rooms are in those functions hardcoded. 
'''
##----------------- variables to define ------------
testList = ['_mt3', '_mt2' ,'_final']
section = '205_200' # this is prefix to csv for student list reader
examRoom = 'Dabney222' # this is prefix to csv used in room file reader
leftFlag = False; # are you doing lefties

#--------------------------------------
##       initialize things  
#--------------------------------------------
for test in testList :
    people = dict();
    seats = []
    cell = 0 ; 
#--------------------------------------
# ------ read in room file of seats
#--------------------------------------
    seats = room_file_reader.room_file_reader(examRoom, leftFlag)
#--------------------------------------
# left handed flag functionality limited. this just makes a list of left seats.
# print out left seats to assign manually. 
#--------------------------------------
    if leftFlag:
        leftList = []
        while cell < (len(seats)-1) : 
            if seats[cell].endswith('L') :
                leftList.append(seats.pop(cell))
            cell += 1
        print(leftList)
#--------------------------------------
# get people in the section file, get random seat, put in a dictionary
# then output the list of seats assgined to students to a file. 
#--------------------------------------
    else:  
        people = student_list_fileio.student_list_reader(section, people, seats, leftFlag)
        student_list_fileio.student_list_writer(section, people, test)


