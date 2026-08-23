import random
letters=['a','b','c','d','e','f','g','h',
         'i','j','k','l','m,'
    ,'n','o','p','q','r','s',
         't','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
print("Welcome to the password generator!")
nr_letters=int(input("How many letters would you like?"))
nr_numbers=int(input("How many numbers would you like?"))
nr_symbols=int(input("How many symbols would you like?"))
password=[]
for i in range(nr_letters):
    shuffled_letters = random.choice(letters)
    password+=shuffled_letters
for j in range(nr_numbers):
    shuffled_numbers = random.choice(numbers)
    password+=shuffled_numbers
for k in range(nr_symbols):
    shuffled_symbols= random.choice(symbols)
    password+=shuffled_symbols

random.shuffle(password)
string_convertion="".join(password)
print(f"your password is {string_convertion}")