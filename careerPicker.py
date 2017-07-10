start = '''
Are you confused as to what you want to do in your future career! Use this program to find out what you're really meant to do. :^)
'''


print(start)


print("Do you prefer a. Literature and Arts or b. STEM topics?")
user_input = input()
if user_input == "a":
    print("What sounds like a better day to you? a. Sitting outside on the porch reading a good book; or b. Listening to your favorite music while painting a picture of the Sierra Mountains?") # finished the story by writing what happens
    user_input = input()
    if user_input == "a":
        print("Do you enjoy a. reading and writing bizarre stories from your own imagination, or b. exploring the realms of historical culture and real world issues? ")
        user_input = input()
        if user_input == "a":
            print("You should pursue the path of novel writing! With a passion like yours, you can become the next J.K. Rowling.")
        else:
            print("Go pursue your obvious dream of becoming a non-fiction writer! You were always meant to study the world and discover what comes next.")

    else:
        print("Which artist do you prefer: a. Picasso or b. Tchaikovsky?")
        user_input = input()
        if user_input == "a":
            print("You would be an amazing designer or artist. It's clear that you have talent and the potential to bring the world unique art that gives joy to all.")
        else:
            print("Pursue the field of musical and performing arts! Your future work will surely match up with that of Mozart.")
##STEM
elif user_input == "b":
    print("Would you rather a. spend your time with a computer or b. in a lab?") # finished the story writing what happens
    user_input = input()
    if user_input == "a":
        print("If you were a roboticist, would you rather a. build the robot or b. code it?")
        user_input = input()
        if user_input == "a":
            print("You should become a hardware engineer. Someday, you might build the long awaited time machine!")
        else:
            print("Looks like you were born to code! You should attend Girls Who Code SIP! If you're not a girl, too bad.")
    else:
        print("Would you rather a. go out into the wilderness to explore, or would you b. stay at the lab making things explode?")
        user_input = input()
        if user_input == "a":
            print("Looks like you really care about the world. You're fit to become a doctor, or maybe even a vet!")
        else:
            print("You'd better become a chemist! One day, you'll be the master of titration.")
else:
    print("You're no good to anyone if you can't even enter a valid choice.")
