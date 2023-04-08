import math
# to know the type of operator in the argument
line = "------------------------------------------------------"
def find_operator(argument) -> list:
    operators = ["+", "-", "/", "%", "*"]
    for op in operators:
        if op in argument:
            index = argument.index(op)
            return (op, index)
    return None

# to perform basic maths process
def BasicProcess(op1, operation, op2) -> float:
    if (operation == "+"):
        return (op1+op2)
    elif (operation == "-"):
        return (op1-op2)
    elif (operation == "/"):
        return (op1/op2)
    elif (operation == "%"):
        return (op1 % op2)
    elif (operation == "*"):
        return (op1*op2)

# to guide the user
def flow():
    changeLine(1)
    print("HelloW! Welcome to THEcAlculator")
    changeLine(3)
    print("1)Basic Math", "\n"
          "2)Advanced Maths")
    changeLine(3)
    choice = int(input("What type of Fuction do you want to perform? : "))
    if isinstance(choice, int):
        if (choice == 1):
            changeLine(3)
            argument = input("Enter your Experssion : ")
            info = find_operator(argument)
            changeLine(1)
            print("The Answer is", BasicProcess(int(argument[0:info[1]]), info[0], int(argument[info[1]+1])))
        elif (choice == 2):
            AdvancedMenu()
            changeLine(1)
            choice = int(input("What do you want to Perform? : "))
            if(choice>=0 and choice<=6):
                operand = int(input("Enter the Expression : "))
                result = AdvancedMathsProcess(choice, operand)
                changeLine(1)
                print("The Answer to the Question is", result)
            
#to print Advaned Maths Menu            
def AdvancedMenu():
    print("Menu : ","\n"
          "1)SquareROOT","\n"
          "2)Absolute Value","\n"
          "3)CubeROOT","\n"
          "4)Sine Fucntion","\n"
          "5)Cosine Function","\n"
          "6)Tangent Function","\n")
    
#to perform Advanced Maths Processes
def AdvancedMathsProcess(operation, operand) -> float:
    if(operation == 1):
        return math.sqrt(operand)
    elif(operation == 2):
        return math.abs(operand)
    elif(operation == 3):
        return math.cbrt(operand)
    elif(operation == 4):
        return math.sin(operand)
    elif(operation == 5):
        return math.cos(operand)
    elif(operation == 6):
        return math.tan(operand)
    
#for looks
def changeLine(type1):
    if type1 == 1:
        print(line)
        print('\n')
    elif type1 == 2:
        print("\n")
    elif type1 == 3:
        print(line)
flow()