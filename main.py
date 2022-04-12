import sys
import random

ans = True

while ans:
    user_question = input("What would you like to ask the Magic 8 ball: ")
    
    answers = random.randint(1,9)
    
    if user_question == "":
        print("Please ask a question\n" + user_question)
    
    elif answers == 1:
        print("Yes - definitely.")
    
    elif answers == 2:
        print ("It is decidedly so")
    
    elif answers == 3:
        print ("Without a doubt")
    
    elif answers == 4:
        print ("Reply hazy, try again")
    
    elif answers == 5:
        print ("Ask again later")
    
    elif answers == 6:
        print ("Better not tell you now")
    
    elif answers == 7:
        print ("My sources say no")
    
    elif answers == 8:
        print ("Outlook not so good")
      
    elif answers == 9:
      print ("Very doubtful")
      
    else:
      print("Error")