import csv
import os
def room_file_reader(examRoom, leftflag):
    '''
    This function reads in an exam room file and makes a list of seats from that file. 
    The room file is a map of the room with seats in the format of A21 for a valid seat. 
    A seat you don't want to assign ends with -R, e.g. A04-R. 
    A broken seat or missing seat end in -X, e.g. L11-X. 
    A left handed seat ends in -L. e.g. K15-L. 
    We used X for the aisles or blank spaces. An example file is provided. Dabney222.csv
    This function takes 2 arguments. The first is the room/file name prefix. The second is whether you are doing left handed seats. There is no code for left handed seats yet built. The function returns a list of seats. 

    File path is hardcoded into this function. 
    '''
# --- set the path for the room maps --------------
    filepath = './'
#----------
# -- which room to assign
#------- assume the room file has a csv version of it
    examRoomFile = examRoom + '.csv'
    seatsInRoom_list = [] # make empty entire room file list of cells
    with open(os.path.join(filepath,examRoomFile)) as room_file:
        csv_reader = csv.reader(room_file, delimiter=',') 
    #lines = len(list(csv_reader))
    # for each row in the file, pull out every seat number individually and add to one great big list
        for row in csv_reader:
    #------------- combine the rows into one big list
            seatsInRoom_list +=row 
        
    room_file.close()
    return seatsInRoom_list
