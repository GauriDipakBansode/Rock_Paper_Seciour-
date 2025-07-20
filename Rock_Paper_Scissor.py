"""Design
   a two-player Rock-Paper-Scissor game"""

RSP=["rock","paper","scissor"]
m="MENU"
c=m.center(30,"=")
while 1:
    print(c)
    print("1.Single player\n2.Double player\n3.Exit\n")

    ch=int(input("Enter nuber for how you want to play::"))

    if ch==1:
                print(RSP)
                m=str(input("My turn::"))
                import random
                r=random.choice(RSP)
                print("Computer's turn::")
                print(r)
                if r==m:
                    print("Same")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                elif m==RSP[0] and r==RSP[1] :
                    print("Computer win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (m==RSP[0] and r==RSP[2]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (m==RSP[1] and r==RSP[0]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (m==RSP[1] and r==RSP[2]):
                    print("Computer win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (m==RSP[2] and r==RSP[0]):
                    print("Computer win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (m==RSP[2] and r==RSP[1]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")

    if ch==2:
                n=str(input("Your turn::"))
                p=str(input("Sec player::"))
                if n==p:
                    print("Same")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                elif (n==RSP[0] and p==RSP[1]):
                    print("Friend win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (n==RSP[0] and p==RSP[2]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (n==RSP[1] and p==RSP[0]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (n==RSP[1] and p==RSP[2]):
                    print("Friend win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (n==RSP[2] and p==RSP[0]):
                    print("Friend win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                elif (n==RSP[2] and p==RSP[1]):
                    print("You win")
                    print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)\n")
                
        

    if ch==3:
            break
