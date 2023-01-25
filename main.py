#imrancoding
import random
lst=["Rock", "Paper", "Scissor"]
while True:
    user_count=0
    computer_count=0
    user_choice=int(input("\n1.Press 1 to play game\n2.Press 2 to exit\n"))
    if user_choice==1:
        print("\nR = Rock\nP = Paper\nS = Scissor")
        for x in range(1, 4):
            user_input=input("\nYour choice: ")
            computer_choice=random.choice(lst)
            if (user_input=="R") or (user_input=="r"):
                user_choice="Rock"
            elif (user_input=="P") or (user_input=="p"):
                user_choice="Paper"
            elif (user_input=="S") or (user_input=="s"):
                user_choice="Scissor"
            else:
                print("Invalid Input!")
                break
            print(f"\nYour choice: {user_choice}")
            print(f"Computer choice: {computer_choice}")
            if user_choice==computer_choice:
                print(f"Round {x} is Draw")
            elif (user_choice=="Rock" and computer_choice=="Scissor") or (user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Scissor" and computer_choice=="Paper"):
                print(f"\nRound {x}: You win")
                user_count+=1
               
            else:
                print(f"\nRound {x}: Computer win")
                computer_count+=1
        if user_count==computer_count:
            print(f"\n\nYour score: {user_count}\nComputer score{computer_count}\n\nFinal result: Match draw.") 
        elif user_count>computer_count:
            print(f"\n\nYour score: {user_count}\nComputer score: {computer_count}\n\nFinal result: You is winner.") 
        else:
            print(f"\n\nComputer score: {computer_count}\nYour score: {user_count}\n\nFinal result: Computer is winner.")
             
    else:
        break
