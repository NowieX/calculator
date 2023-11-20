# Creating a calculator with python!
first_row_calculator = [7, 8, 9, "X"]
second_row_calculator = [4, 5, 6, "-"]
third_row_calculator = [1, 2, 3, "+"]
fourth_row_calculator = [0, ",", "=", "R"]
options = [1, 2, 3, 4, 5]

def calculator_board():

    print("""
-----------------
| 7 | 8 | 9 | X |
| 4 | 5 | 6 | - |
| 1 | 2 | 3 | + |
| 0 | , | = | R |
-----------------
        """)
    
    print("""
What do you want to calculate?
1. Multiply numbers.
2. Substract numbers.
3. Add numbers.
4. Reset.
5. Exit the program
          """)
    while True:
        what_to_calculate = input("Please choose an option: ")
        
        if not what_to_calculate.isdigit():
            print("That's not an option!")
            continue

        what_to_calculate = int(what_to_calculate)
        
        choose_calculate_option(what_to_calculate)

def choose_calculate_option(what_to_calculate):
    if not what_to_calculate in options:
        print("That's not an option!")
        return
    
    if what_to_calculate == options[0]:
        multiply_input()
    elif what_to_calculate == options[1]:
        print("option 2")
    elif what_to_calculate == options[2]:
        print("Option 3")
    elif what_to_calculate == options[3]:
        print("Option 4")
    elif what_to_calculate == options[4]:
        print("Thanks for trying us out!")
        exit()
    
def multiply_input():
    # 1. make an input
    # 2. create an empty list and add the numbers the user puts in
    # 3. multiply the numbers from the empty list
    pass

def main():
    print("*** Welcome to the calculator! ***")
    print("Here you are free to calculate everything you want to!")
    print("The R stands for reset!")

    calculator_board()
    
if __name__ == '__main__':
    main()