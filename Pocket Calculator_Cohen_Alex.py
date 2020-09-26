#!/usr/bin/env python
# coding: utf-8

# In[104]:



#sets menu text
menu_text = "\nEnter the number of the corresponding operation: \n 1. Addition \n 2. Subtraction  \n 3. Multiplication \n 4. Division or \n 5. Exponentiation \n"

#loop until quit (perform_again != "Y")
perform_again = "y"
while perform_again == "y":
    
    #Get operation
    user_choice = input("Hello, and thank you for choosing my calculator." + menu_text)


    #Test for a valid operation
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4" and user_choice != "5": 
        print("\nINVALID OPERATION")
        user_choice = input(menu_text)

    #confirm operation chosen    
    if user_choice == "1":
        print("You have chosen addition.")
    elif user_choice == "2":
        print("You have chosen subtraction.")
    elif user_choice == "3":
        print("You have chosen multiplication.")
    elif user_choice == "4":
        print("You have chosen division.")
    elif user_choice == "5":
        print("You have chosen exponentiation.")

    #set correct wording for operation and obtain inputs    
    if user_choice == "5":
        #asking the user for the base number
        first_number = float(input("What is your base number? " )) 
        #asking the user for exponential number
        second_number = float(input("What is your exponent? " )) 
    else:
        #asking the user for the first number
        first_number = float(input("What is your first number? " )) 
        #asking the user for second number
        second_number = float(input("What is your second number? " )) 

    #run calculation
    if user_choice == "1":
        #add the numbers
        result = first_number + second_number
    elif user_choice == "2":
        #subtract the numbers
        result = first_number - second_number
    elif user_choice == "3":
        #Multiply the numbers
        result = first_number * second_number
    elif user_choice == "4":
        while second_number == 0:
            print("Error: can't divide by 0. ")
            second_number = float(input("What is your second number? " )) 
        #Divide the numbers
        result = first_number / second_number
    elif user_choice == "5":    
    #exponentiate the numbers
        result = first_number ** second_number
    
    #print the result
    print("The answer is " + str(result) + ".")
    
   
  
    #check to see if the user wants to perform another calculation
    perform_again = input("Do you want to perform another calculation (y/n)?")
    
    
    


# In[ ]:





# In[ ]:




