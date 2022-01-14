print("\nSwallow Speed Analysis: Version 1.0\n")
#Creation of list
reading_list = []          
reading = input("Enter the Next Reading: ")
#condition validation
if reading == "":
    print("No readings entered. Nothing to do.")
else:
    #While loop for condition
    while reading != "":
        #if,elif,else for multiple conditions
        if (reading[0] == "U"):    
            print("Reading saved")
            reading_list.append(float(reading[1:])*1.61)            
            reading = input("Enter the Next Reading: ")

        elif (reading[0] == "E"):  
            print("Reading saved.")
            reading_list.append(float(reading[1:]))                 
            reading = input("Enter the Next Reading: ")

        else:
            print("Please enter valid reading.")
            reading = input("Enter the Next Reading: ")


    if (len(reading_list)!= 0):           
        print("\nReading summary\n")
        #Prints how many reading were analysed
        print(len(reading_list), "Reading Analysed\n")
        #calculates maximum reading 
        maximum = max(reading_list)/1.61
        #calculates minimum reading
        minimum = min(reading_list)/1.61
        #calculates average reading
        average = sum(reading_list) / len(reading_list)
        #Prints max, min along with average speed of Swallow 
        print(f"Max Speed : {maximum *1.6:.1f} KPH {maximum:.1f} MPH.")
        print(f"Min Speed : {minimum *1.6:.1f} KPH {minimum:.1f} MPH.")
        print(f"Avg Speed : {average:.1f} KPH {average/1.6:.1f} MPH.")
    else:
        print("Please enter valid reading.")