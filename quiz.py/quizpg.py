print("WELCOME TO ASKPYTHON QUIZ")
answer=input("ARE YOU READY TO PLAY OUR QUIZ? (YES/NO):")
score=0
total_questions=3
if answer.lower()=="yes":
    answer=input("question 1: What is your favourite programming language?")
    if answer.lower()=="python":
        score+=1
        print("correct")
    else :
        print("wrong answer")

    answer=input("question 2: Do you follow any author on Ask python?")
    if answer.lower()=="yes":
        score+=1
        print("correct")
    else :
        print("wrong answer")


    answer=input("question 3: What is the name of you favourite website for learning python?")
    if answer.lower()=="askpython":
        score+=1
        print("correct")
    else :
        print("wrong answer")

print("thankyou for playing this small quiz game,you attempted",score,"questions correctly!")
mark=(score/total_questions)*100
print("marks obtained:",mark)
print("BYE")
  
  