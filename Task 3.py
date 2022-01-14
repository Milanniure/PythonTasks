import random
from tokenize import Number
#Function to return random string from the list
def random_string():  
    """Function that Returns random string"""
    answer = ['Oh my.', 'Oh I see', 'Yes', 'May be', 'No its not', 'OK','Really', 'Tell me more']
    response = random.choice(answer)
    print(response)
#Error handling    
def error():
    data = random.randint(1, 10)
    
    if data == 5:
        print("Network Error!!")
        print(f"Thanks, {username}, for using PopChat. See you again soon!")
        exit()



#Email
print("Welcome to Pop Chat")
print("One of our operators will be pleased to help you today.\n")

Email = input("Please enter your Poppleton email address: ")
Number = 0
if len(Email) >= 12:
    if Email[0].isalpha():
        if "@pop.ac.uk" in Email:
            if ("@" in Email) and (Email.count("@") == 1) and (Email[-10] == "@"):
                for x in Email:
                    if x == " ":
                        Number = 1
                if Number == 1:
                    print("Invalid Email")
                else:
                    username = Email.split("@")[0]
                    print(f"Hi, {username}! Thank you, and Welcome to PopChat!")
                    Operators = ["Jane", "John", "Rose", "George"]
                    print(f"My name is {random.choice(Operators)} and it will be my pleasure to help you.")
                    data = random.randint(1,10)
                    if data == 5:
                        print("Network Error!!")
                    else:
                        user_input = str()
                        while(("exit" not in user_input) and ("bye" not in user_input)):
                            error()
                            user_input = input("---> ").lower()
                            if "library" in user_input or "Library" in user_input:
                                print("The library is closed today.")
                            elif "wifi" in user_input or "WiFi" in user_input:
                                print("WiFi is excellent across the campus")
                            elif "coffee" in user_input or "Coffee" in user_input:
                                print("Teekee is open until 9 pm this evening.")
                            elif "deadline" in user_input or "Deadline" in user_input:
                                print("Your deadline has been extended by two working days.")
                            elif "exams" in user_input or "Exams" in user_input or "Exam" in user_input:
                                print("Exams are coming!!")
                            elif ("exit" not in user_input) and ("bye" not in user_input):
                                random_string()
                            else:
                                print(f"Thanks, {username}, for using PopChat. See you again soon!")
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")


