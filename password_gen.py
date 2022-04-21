import random

password_length_weak = 8
password_length_strong = 11
set_of_data1 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"
set_of_data2 = "abcdefghijklmnopqrstuvwxyz01234567890"

print("Welcome to password generator !")

while True:

    user_input= input('How do you want your password? type w or s to get your password! press y to stop\n')
    
    if user_input == "y":
        break

    if user_input == "w":
        password_weak = " ".join(random.sample(set_of_data2,password_length_weak))
        print("Your password is this :",password_weak)
        
    elif user_input == "s":
        password_strong = " ".join(random.sample(set_of_data1,password_length_strong))
        print("Your password is :",password_strong)


    else:
        print("Input is not valid, try w or s or y to end")

    
        
      
