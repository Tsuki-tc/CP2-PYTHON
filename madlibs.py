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

'''Card = "1267-2546-7674-9672"

print(f"The credit card number ends with: {Card[-4:]}")
print(f"The reversed card number is: {Card[::-1]}")'''

#LOOPS
#While

'''username = input("Enter your username: ")

while username == "":
    print("You did not enter a username")
    username = input("Enter your username: ")

print(f"Welcome {username}!!")'''

'''number = int(input("Enter a number: "))

while number < 1 or number > 20:
    if number < 1:
        print("The number you've inputted is lower than 1")
        number = int(input("Enter a number: "))
    elif number > 20:
        print("The number you have inputted is higher than 20")
        number = int(input("Enter a number: "))

print(f"Number is {number}")'''

'''faveFood = input("Enter your favorite food (enter q to quit): ")

while not faveFood == "q":
 print(f"Your Favorite food is {faveFood}!!")
 faveFood = input("Enter another favorite food (enter q to quit): ")

print("Thank you for giving us your favorite food")'''

'''for x in range (1,10):
    print(x, end=",")'''

'''for x in range (1,10):
    if x == 6:
        #print(x)
        #break
        continue
    else:
        print(x, end=" ")'''

#List

'''fruits = ["apple","orange","banana","coconut"]
fruits.append("pineapple")
fruits.append("grapes")

print(fruits[::-1])'''

#list to while
'''fruits = ["apple","orange","banana","coconut"]
fruits.append("pineapple")
fruits.append("grapes")

index = 0
while index < len(fruits):
    print(f"fruits: {fruits[index]}")
    index += 1

print ("That's all the available fruits.")'''

#list for loop
'''fruits = ["apple","orange","banana","coconut"]
fruits.append("pineapple")
fruits.append("grapes")

#for x in fruits:
    #print(f"fruits: {x}")
#print("That's all the fruits available")

for x in range(2, len(fruits)):
    print(f"fruits: {fruits [x]}")

print("That's all the fruits available")'''

#Function

'''def addition():
    numberOne = 34
    numberTwo = 33
    sum = numberOne + numberTwo
    print(f"The sum of two numbers is {sum}")


addition()'''

'''def addition(numberOne, numberTwo):
    sum = numberOne + numberTwo
    print(f"The sum of two numbers is {sum}")

addition(12, 55)'''

#Exercise

'''def display_info(Name, Age, Country):
    print("HERE ARE MY DETAILS: ")
    print(f"Name: {Name}")
    print(f"Age: {Age}")
    print(f"Country: {Country}")

display_info("Sidnei", 20, "Philippines")'''

#Class

class Student:
    
    total_student = 0
    total_gpa = 0

    def __init__(self, name, course, gpa):
        self.name = name
        self.course = course
        self.gpa = gpa
        Student.total_student += 1
        Student.total_gpa += gpa

    def get_info(self):
        print(f"My Name is {self.name}, My course is {self.course}")

    @staticmethod
    def isValid_course(course):
        valid_course = ["BSCS", "BSIS", "BSEMC", "BMMA"]
        for x in valid_course:
            if x == course:
                print("This is a valid course")
#Class Method
    @classmethod
    def get_average_gpa(cls):
        ave = cls.total_gpa / cls.total_student
        print(f"The average GPA of all students is: {ave}")

StudentOne = Student("Alex", "BSCS", 96.75)
StudentTwo = Student("John", "BSIS", 95.00)
StudentThree = Student("Jane", "BSEMC", 94.15)
StudentFour = Student("Mary", "BMMA",98.75)

Student.isValid_course(StudentOne.course)
Student.get_average_gpa()

#StudentOne.get_info()

'''print("Here are the students details:")
print(f"StudentOne name: {StudentOne.name}, Course: {StudentOne.course}")
print(f"StudentTwo name: {StudentTwo.name}, Course: {StudentTwo.course}")
print(f"StudentThree name: {StudentThree.name}, Course: {StudentThree.course}")
print(f"StudentFour name: {StudentFour.name}, Course: {StudentFour.course}")'''

