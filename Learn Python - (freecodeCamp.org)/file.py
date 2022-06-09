#Drawing a Shape 


print("   /|")
print("  / |")
print(" /  |")
print("/___|")
#Variables and stuff!
is_male = True
is_dumb = False

#Played around for a bit
character = {
    "name" : "adrian",
    "age" : 20
}
name = "adrian"
age = 20
print(f"that is crazy {name} you are {age} ")
print(f"that is crazy {character['name']} you are {character['age']} ")

def create_character(name, age):
    character1 = {
        "name": name,
        "age": age
    }
    return character1

char_daniel = create_character("daniel", 19)

print(char_daniel)

print('my name is', char_daniel['name'] , 'and I am sick') #comma gives a space
print('my name is' + char_daniel['name'] + 'and I am sick') #plus does not give a space

#working with Strings
print("giraffe\nacademy") #NEW line!!!! \n makes it in to a new line
print("Yeah you're \"so funny\"") #back slash makes the next character to someting also can help you
phrase = "Whats up"
print(phrase, "you busy tomorrow?")
print(phrase.upper()) #turns everything to upper case
print(phrase.lower()) #turns everything to lower case
print(phrase.isupper(), phrase.islower()) #checks if phrase is all upper/lower case
print(len(phrase)) # checks length of string
print(phrase[0]) #prints first index of string.. which is 'W'
print(phrase.index('s')) #checks where the letter is in the function
#print(phrase.index('z')) #if letter is not in string it creates an ERROR
print(phrase.replace("Whats", "I'm")) #replace certain words or even letters in string variable

#working with numbers
print(-2)
print(2.0982)
print(3 +4.67) # can do math
my_num = 5
print(my_num)
print(str(my_num)) #comes in handy when you want to print out numbers with string
#print(my_num + 'yes') # does not allow to do that you need to use the str()
neg_num = -3
print(abs(neg_num)) #absolute value of num will print 3
print(pow(3,2)) #3^2 = 9
print(max(4, 6)) # gets the max of both numbers 
print(min(3,9)) #gets the min of both numbers
print(round(3.7)) #rounding numbers


from math import *
import re # how to import the next math functions!!!
print(floor(3.7)) # like javascript floor just takes away the decimal
print(ceil(7.2)) # ceil goes up to the next number
print(sqrt(36)) # square root is square root

#getting input from users

#name = input("Enter you name: ")
#age = input("Enter your age: ")
#print("Hello, " + name + "! You are " + age)


#Building a basic calculator
num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")

result = int(num1) + int(num2) #without int() it will be considered a string 
#you can use a float() to get decimal numbers 
print(result)