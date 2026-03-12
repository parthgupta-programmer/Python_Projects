import random 
import time as t

def result(a,b):
    if(a==b):
        return 3
    elif ((a==0 and b==1) or (a==2 and b==0) or (a==1 and b==2) ):
        return 4
    else:
        return 5

def SPS_GAME_Function():

    print("Throw your move:",end=" ")
    user=int(input()) 
    computer=random.randint(0,2)

    names=['Stone','Paper','Scissor']
    
    if( ( user==0 )or ( user == 1 ) or  ( user == 2) ):
        r=result(computer,user)
        if(r==3):
            print(f"  You   : {names[user]}")
            print(f"Computer: {names[computer]}\n")

            print("DRAW!!  Try AGAIN....")
                
    
        elif(r==4):
            print(f"   You  : {names[user]}")
            print(f"Computer: {names[computer]}\n")

            print("Bravo,You WIN!!")
        else:
            print(f"   You  : {names[user]}")
            print(f"Computer: {names[computer]}\n")

            print("Opps...Computer WIN!! Play Again....")
    else:
        print("Wrong Number Entered...Try Again!!")



print("STONE PAPER SCISSOR GAME\n")


print("How to play:")
print("1.READ the below instructions carefully.")
print("2.Type 0 for STONE , 1 for PAPER and 2 for SCISSOR")
print("3.0 - STONE")
print("  1 - PAPER ")
print("  2 - SCISSOR\n")
print("Now,If you have read the above instructions carefully,then press ENTER : ",end="")

reply=input()

if(reply=="" or reply==" "):
    SPS_GAME_Function()
                    
else:
    print("\nWrong Key Pressed!! Please start the game again.")


print("\nPRESS P if you want to play AGAIN.")
print("OR PRESS E to EXIT THE GAME!!")

ans=input()
while(ord(ans)==112 or ord(ans)==80):
    SPS_GAME_Function()
    print("\nPRESS P if you want to Play AGAIN.")
    print("OR PRESS ANY KEY to EXIT from the SPS-GAME!!")
    ans=input()

print("You have been exited from the SPS GAME.")
t.sleep(1)
print("\nThank You For Playing.....")