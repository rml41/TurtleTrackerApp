#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Rachel Landman (rachel.landman@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# Create a variable pointing to the data file 
file_name = './data/raw/sara.txt'

# Create a file object from the file 
file_object = open(file_name, 'r')

# Read contents of file into a list
line_list = file_object.readlines()

# Close the file because you have already read the contents of the file 
file_object.close()

# pretend we read one line of data from the file
### lineString ='20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'
### lineString = line_list[750]

# Iterate through all lines in the lineList
for lineString in line_list:
    if lineString[0] == "#" or lineString[0] == "u": continue

    # split the string into a list of data items 
    lineData = lineString.split()
    
    #extract items in list into variables 
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    # Print the location of sara
    print(f'Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_long} on {obs_date}')
