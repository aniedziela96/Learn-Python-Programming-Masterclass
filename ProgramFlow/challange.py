list_of_activities = """Please choose your option from the list below:  
1.\tLearn Python  
2.\tLearn Java  
3.\tGo swimming  
4.\tHave dinner 
5.\tGo to bed 
0.\tExit"""

chosen_option = "-"
while chosen_option != "0":
    if chosen_option in "12345":
        print("You've chosen option number {}.".format(chosen_option))
    else:
        print(list_of_activities)
    chosen_option = input("Your choice: ")
else:
    print("Bye, bye")
