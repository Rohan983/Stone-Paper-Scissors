import random as rn

def game(comp, user):
    if comp == user:
        return None 
    elif comp == "s" and user == "p":
        return True
    elif comp == "p" and user == "sc":
        return True
    elif comp == "sc" and user == "s":
        return True
    else:
        return False
    

print("Computer is Choosing....")
valid = ("s", "p", "sc")
comp = rn.choice(valid)
o = True
while o == True:
    user = input("Choose between Stone(s), Paper(p) or Sciscors(sc) ")
    if user in valid:
        break
    else:
        print("Enter Valid option.")

print(f"Computer chose {comp}\nYou chose {user}")
result = game(comp, user)
if result == None:
    print("It's a Tie")
elif result:
    print("Congratulation!! you Won")
else:
    print("Sad, Computer Won")