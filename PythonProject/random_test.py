# import random
# import myModule
# from myModule import myWifeBirthDay


# random_integer = random.randint(0, 1)
# print(random_integer)

# print(myModule.myFavouriteNumber)
# print(myWifeBirthDay)

# Số thực bất kỳ chỉ định trong 1 khoảng nào đó
# random_float = random.uniform(1, 68)
# print(random_float)

# random_heads_or_tails = random.randint(0 ,1)
#
# if random_heads_or_tails == 0 :
#     print("Heads")
# else:
#     print("Tails")

# Hàm chọn string bất kỳ trong list có trước đó
# myFriends = ["Yuki", "Hana", "Taro", "Sora"]

# 1st option
# print(random.choice(myFriends))

#2nd option
# random_index = random.randint(0, 3)
# print(myFriends[random_index])


# じゃんけんゲームを作成
# import random
# user_act = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : \n "))
# act_list = ["Rock", "Paper", "Scissors"]
# computer_choice = random.choice(act_list)
#
# if user_act == 0:
#     print(f"You chosen Rock and computer chose {computer_choice}")
#     if computer_choice == "Rock":
#         print("You Draw")
#     elif computer_choice == "Paper":
#         print("You lose")
#     else :
#         print("You won")
# elif user_act == 1:
#     print(f"You chosen Rock and computer chose {computer_choice}")
#     if computer_choice == "Rock":
#         print("You won")
#     elif computer_choice == "Paper":
#         print("You Draw")
#     else :
#         print("You lose")
# elif user_act == 2:
#     print(f"You chosen Rock and computer chose {computer_choice}")
#     if computer_choice == "Rock":
#         print("You lose")
#     elif computer_choice == "Paper":
#         print("You won")
#     else:
#         print("You draw")
# else:
#     print("Please choose again. You can only choose 0 , 1 or 2 ")
#
# print("See you soon !")


# Tìm số lớn nhất:
student_scores = [230, 142, 456, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

# print(max(student_scores))

# max_score = 0
# for score in student_scores:
#     if max_score <= score:
#         max_score = score
#     # else:
#     #     pass
# print(f"Max Score is : {max_score}")

# sum = 0
# for number in range(1, 101):
#     sum += number
# print(f"Tổng từ 1 đến 100 là : {sum}")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)