log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):  #set function up 
    for line in log_file:              #iterrates through every line in the file
        line = line.rstrip()           #removes characted at  the right of a str 
        day = line[0:3]                #assigning variable day to the first 3 items in the line
        if day == "Mon":               #if day is Tue   
            print(line)                #then print the line


generate_sales_reports(log_file)       #calling the function with log file as the parameters?

