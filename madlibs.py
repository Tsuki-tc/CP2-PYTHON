#madlib
'''adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb (action word): ")
adjective3 = input("Enter one last adjective: ")
verb2 = input ("Enter another verb:")

print("\n--- YOUR STORY ---")
print(f"Today I went to a {adjective1} river.")
print(f"In the river, I saw a {noun1}.")
print(f"The {noun1} was {adjective2} and started to {verb1} at me.")
print(f"I was {adjective3} so I {verb2} away!")'''

#W9 Example1
'''Number = 67

result = "Positive" if Number > 0 else "Negative"

print (f"The Result is {result}")'''

#W9 Example2
'''min = int(input("Enter a minimum value:"))
max = int(input("Enter a maximum value:"))

result = min if min < max else max

print(f"The Result is {result}")'''

#Length/len
'''text = input("enter a text: ")

print(f"The length of the text is {len(text)}")'''

#find
'''text = input("Enter a Text: ")

resultOne = text.find("f")
resultTwo = text.rfind("f")

print(f" The resultone is {resultOne}, and resultTwo is {resultTwo}")'''

#capitalize,uppercase,lowercase
'''text = input("Enter a Text: ")

#result = text.capitalize()
#result = text.upper()
resultOne = text.capitalize()
resultTwo = resultOne.upper()
resultThree = resultTwo.lower()

print(f"Capitalized is  {resultOne}, Uppercase is {resultTwo}, Lowercase is {resultThree}")'''

#isdigit,isalpha
'''text = input("Enter a Text: ")

#result = text.isdigit()
result = text.isalpha()
print(result)'''

#count
'''text = input("Enter a Text: ")

result = text.count("a")
print(result)'''

#replace
'''text = input("Enter a Text: ")

result = text.replace("m", "p")
print(result)'''

#Exercise
'''Username = input("Enter a Username: ")

if len(Username) > 12:
    print("Valid Username")
elif not Username.find (" ") == -1:
    print ("Your Username contains a space")
elif not Username.isalpha():
    print("Your Username contains a digit")
else:
    print(f"Welcome {Username}!")'''

#indexing
'''Text = "CIIT College of Innovation and Integrated Techology"

#index = Text[16]
#index = Text[16:26]
index = Text[::2]

print(index)'''

#Exercise 2

Card = "1267-2546-7674-9672"

print(f"The credit card number ends with: {Card[-4:]}")
print(f"The reversed card number is: {Card[::-1]}")