import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict={key:value for key,value in data.iterrows()}
print(phonetic_dict)
user_word=input("Enter your name: ").lower()
output_list=[phonetic_dict[user_word] for  letter in user_word ]
print(output_list)