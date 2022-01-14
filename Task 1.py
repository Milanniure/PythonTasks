print("Stop, Who would cross the Bridge of Death, Must answer my questions !!! ")
name= input("What is your name? : ")
if name == "Arthur" or name == "arthur":
    print("My Liege! You may pass!")
else:
    sentence= input("What is your Quest? : ")
    if "grail" in sentence or "Grail" in sentence:
        colour=input("What is your favorite colour? :")
        a = name[0].upper()
        b = colour[0].upper()
        if a==b:
            print("You may pass.")
        else:
            print("You must face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek grail may pass.")