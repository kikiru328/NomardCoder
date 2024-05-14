a = 10
if a == 10:
    print('True!')

password_correct = False
if password_correct:
    print("here is your money")
else:
    print("Wrong password")
    
###########################################    
winner = 10
if winner > 10:
    print("Winner is greater than 10")
elif winner < 10:
    print("Winner is less than 10")
else:
    print("Winner is 10")
    
###########################################
age = input("How old are you")

if int(age) < 18:
    print("You Can't Drink")
elif int(age) > 18 and int(age) < 35:
    print("Drink resposibility")
elif int(age) == 60 or int(age) == 70:
    print("Drink only wine")
else:
    print("You Can Drink")
    
    
# True and True = True
# True and False == False
# False and True == False
# False and False == False 

# True or True == True
# True or False == True
# False or True == True
# False or False == False