"""
Program: 
    The program looping from the user the real number x (float type) 
    and printing x and the third power of x. 
    The program is stopped after typing 'stop' from the keyboard. 
Author:      
    Katarzyna Miałkowska
"""

value = str("")
print("To stop the program type 'stop'")

while(value != "stop"):
    try:
        raw_input = input
        value = raw_input("Enter a number: ")
        value = float(value)
        print(f"{value}., {pow(value, 3)}.")
        
    except NameError as e:
        print(f"Error: {e}.")
    except ValueError as e:
        if(value == 'stop'): print("End of program ") ; break
        print("The input was not a number or command 'stop'.")
        print(f"Error: {e}.")
    