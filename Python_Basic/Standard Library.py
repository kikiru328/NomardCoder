from random import randint

print("Welcome to python casino")
playing = True
count = 1
pc_choice = randint(1, 50)
while playing:
    user_choice = int(input("Choose number. "))
    if user_choice == pc_choice: 
        print(f"you Won! Just match on {count} times")
        playing = False
    elif user_choice > pc_choice: 
        print(f"Lower! (playing Count : {count}) ")
        count += 1
    elif user_choice < pc_choice: 
        print(f"Higher! (playing Count : {count})")
        count += 1
        