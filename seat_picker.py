import random 
import time
from random import randint
####### - define functions ----------------------
def seat_picker(seatList, leftList, leftFlag):
    '''------------------------------------------------------------
    This function will pick a seat randomly. If it is a valid seat, 
    the seat will be returned to the calling funciton to be assigned to a student. 
    #-----------------------------------------------------------------------------
    '''
# ------ get a random number between 0 and current length of list 
# -- first element of list is 0
# --- last element of list is len(seatList)-1
   
#check the potential seat for goodness or lefthanded ness... if lefthand - make a new list of it remove it, if bad/empty/x try remove and try again
    bad_chars = set('XRL ') # seat notation includes X, R, and L. Do not assign those seats. 
    left_chars = set('-L') 
    while leftFlag is False:
        if len(seatList)==0 : # check to see if you have seats available
            print("error. ran out of seats.")
            exit(1)
        # the list of seats changes length as you pop them out. use the dynamic length to keep in bounds
        cell= randint(0, len(seatList)-1) # get a seat to check and possibly assign. 
        # check for X, R, L seats
        if (any((c in bad_chars and seatList[cell].endswith(c)) for c in seatList[cell]) ) :
            seatList.pop(cell) # remove the seat from list
        elif (seatList[cell] == ' '): # seats that are just a space need to be deleted
            seatList.pop(cell)       # found it remove it from the list and don't iterate to next person. still in while loop
        else: # if good assign to a student
            potential_seat = seatList.pop(cell)
            return potential_seat
        # if not reuturned... goes back to while loop and gets another cell. 
#----------------------------------------------------------------------------------------  
#       I ran the left seat code once to make a list of left handed seats in each room.
#       then I manually cut and pasted the left handed students into seats. Fixing this was on the wish list. 
#-----------------------------------------------------------------------------------
       # - This will make a list of left handed seats---
        #elif seatList[cell].endswith('L') : # left handed seats labeled with -L. so need to check to see if the last letter in seat is L
		#print('leftie')
        # remove left seat from list 
            #leftList.append(seatList.pop(cell)) # add the removed left seat to the left list
			# 	make_left = [] # make empty list of left hand seats available
        #    seatList.pop(cell)
        # leftlist += seatList.pop(cell) # this added each character
   
    #---------- leftie --------------
	
    print("leftie flag on. finish coding this")
    return '0'
#-----------------------------------------------------------------------------------------------
