import random
wtp='y'
counb=0
countp=0
final=0
print("enter your name")
name=input()
while wtp!='n':
    while wtp=='y':
        choice=['stone','paper','scissor']
        print("enter y to start the game or n to quit the game")
        wtp=input()
        print("score:")
        print("bot-",counb)
        print(name,"-",countp)
        if wtp=='n':
            if countp>counb:
                print(name," won")
            elif counb>countp:
                print("the bot won")
            else:
                print("no one won its a tie")
                break       
        bot=random.choice(choice)
        print("enter stone paper or scissor")
        player=input()
        if bot=='stone' and player=='paper' : #1
            winner=name
            print("paper captures stone",winner, "won")
            countp+=1
        elif  player=='stone' and bot=='paper': #2
            winner='bot'
            print("paper captures stone",winner, "won")
            counb+=1
        elif player=='paper' and bot == 'scissor': #3
            winner='bot'
            print("scissor cuts paper",winner, "won")
            counb+=1
        elif player=='scissor' and bot == 'paper': #4
            winner=name
            print("scissor cuts paper",winner, "won")
            countp+=1
        elif player=='scissor' and bot == 'stone': #5
            winner='bot'
            print("stone breaks scissor",winner, "won")
            counb+=1
        elif player=='stone' and bot == 'scissor': #6
            winner=name
            print("stone breaks scissor",winner, "won")
            countp+=1
        elif player==bot:
            print("its a tie")
        else:
            print("invalid output try again")
