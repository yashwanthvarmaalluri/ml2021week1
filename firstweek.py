"""
-> This is a simple multifunctional bot.
-> This bot helps you in currency conversion.It is done using an API
-> This bot can also give current time,evaluate expressions,providing some interesting facts.
-> This bot starts by greeting the user by his name
-> Then it lists down the tasks it can do and asks the user to choose the required task to be done

"""

# importing required modules

import datetime
import random
import time
from currencyconverter import currency_converter
current_time = datetime.datetime.now()

#This is an intro function
def intro():
    print("I am a bot and I am here to help you")

#welcomes the user
def welcome():
    #List of welcome sentences
    wel_sentences=[" A very warm welcome"," Nice to meet you"]
    #returning a random sentence from the list 
    return random.choice(wel_sentences)


#It greets the user based on the time of the day
def greeting():
    
    name=input("Your good name please: ")
    part_of_the_day=""
    if(current_time.hour<12):
        part_of_the_day="Morning"
    elif(current_time.hour<17):
        part_of_the_day="Afternoon"
    else:
        part_of_the_day="Evening"
    print(f"Hey {name} Good {part_of_the_day} !,{welcome()}")
    intro()
    print("-----------------------------------------------")

#Prints current time
def curr_time():
    print(f"The current time is {current_time.time()}")
    print()


#Calculates the  expression by the user 
def calculator():
    expression=input("Enter an expression,I will give you the answer:")
    try:
        print(f"The answer for the expression is {eval(expression)}")
        print()
    except:
        print("Enter a mathematical expression.For ex: 2+3*5")

#Prints amazing facts
def facts():
    list_of_facts=["Flamingos bend their legs at the ankle, not the knee","Supermarket apples can be a year old","It’s impossible to hum while holding your nose","People used to say “prunes” instead of “cheese” when having their pictures taken"]
    print(random.choice(list_of_facts))
    print()

#list of tasks bot can perform
def menu():
    print("These are the things I can help you with .Please enter your choice [0-4]")
    print("0. Currency converter")
    print("1. Current time")
    print("2. Calculator")
    print("3. Interesting Fact")
    print("4. Quit")
    print("-----------------------------------------------")
    try:
       return int(input("Choice : "))
    except:
        print("Enter a number between 0-4")

#bot function
def bot():
    greeting()
    time.sleep(1) # sleep() can be used to suspend execution of the calling thread for however many seconds you specify.
    choice= 0
    while(choice!=4):
        choice=menu()
        print()
        if(choice==0):
            currency_converter()
        elif(choice==1):
            curr_time()
        elif(choice==2):
            calculator()
        elif(choice==3):
            facts()
        elif(choice==4):
             print("Thanks for using me . Have a great day :)")
        else:
            print("Enter a number between 0-4")
        
        time.sleep(1)

bot()



