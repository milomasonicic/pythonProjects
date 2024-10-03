print("Welcome to the quiz!")

playing = input("Do you wanna play? ").lower()

score = 0

if playing == 'yes':
    print("Ok, let's play!")
    

    answer = input("Capital city of France? ").lower()
    if answer == 'paris':
        score += 1  
      
        answer1 = input("Capital city of Spain? ").lower()
        
        if answer1 == 'madrid':
            score += 1  
            print("You got both questions right! Your score is " + str(score))
        else:
            print("Wrong! Your score is " + str(score))
            print("End Game")
    else:
        print("Wrong! End Game")
else:
    print("Maybe next time!")
    quit() 


