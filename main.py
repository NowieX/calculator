# Creating a calculator with python!
first_row_calculator = [7, 8, 9, "X"]
second_row_calculator = [4, 5, 6, "-"]
third_row_calculator = [1, 2, 3, "+"]
fourth_row_calculator = [0, ",", "="]

def calculator_board():

    print("""
       -----------------
       | 7 | 8 | 9 | X |
       | 4 | 5 | 6 | - |
       | 1 | 2 | 3 | + |
       | 0 | , | = | R |
       -----------------
        """)

def main():
    print("*** Welcome to the calculator! ***")
    print("Here you are free to calculate everything you want to!")
    print("The R stands for reset!")

    calculator_board()
    
if __name__ == '__main__':
    main()