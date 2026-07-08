from art import logo
print(logo)
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,
             "-":subtract,
            "*" :multiply,
            "/" :divide,
}
def calculator():
    first_number = float(input("what is your first number?"))
    still_accumulate=True
    while still_accumulate:
        for key,value in operations.items():
            print(key)
        operator = input("pick an  operator?")
        next_number = float(input("what's the next number?"))
        answer = operations[operator](first_number, next_number)
        print(f"{first_number} {operator} {next_number} = {answer}")
        continue_calculating=input(f"Type 'yes' to continue with {answer},'no' to start a new calculation? or press 'stop'"
                                   f"to end the calculation: ").lower()

        if continue_calculating=="yes":
            first_number=answer
        elif continue_calculating=="no":
            print("\n"*100 )
            calculator()
            return
        else:
            print("This is the end of the calculation")
            still_accumulate=False
calculator()