
answer = input("Would you like to play? (yes/no)")
if answer.lower().strip() == "yes":
    input("Welcome to the Game, You come accross a two way street. Which way do you want to go (left/right)")
    if answer == "left" :
        input("You were walking and encountered a monster. Do you want to attack or run?(attack/run)")
        if  answer == "attack" :
             print("aaww!! You're too week to fight. GAME OVER")
        elif answer == "run":
            print("You escaped succussfully. On to next level. MISSIOM ACCOMPLISHED. RESULT : WINNER. Wait for next level")
        else:
            print(" INCORRECT VALUE : GAME OVER")
    elif answer == "right":
        input("You are in a garden. You saw fruits. Do you want to eat or let go (eat/let go)")
        if answer == "eat":
            print("Health is good. On to next level. MISSION ACCOMPLISED : WINNER. Wait for next level")
        else:              
            print("bad health conditions. GAME OVER")
    else:
        print("GAME OVER")
else: 
    print("That's bad")    
        