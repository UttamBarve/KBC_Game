"""
-----KBC GAME-----
Contains:
- Questions and 4 lifelines
- 4 Lifelines: a) 50-50. b) Audience poll. c) change question. d) 2 Chance
- After successfully completing a question get price money
- A wrong answer Game over!
- Good Interface
# Important Note: If You Are Running THis Program For The First Time
                You Need To Import Default Question File Here are the steps:
                1. Enter The Developer Mode Access Code: "0205" in main menu
                2. After You Gain Access To Developer Mode Choose Option 3. Import Question
                3. After Entering option third As Input The Question File Will Imported Successfully
-> There is a developer mode in this game program you can access it from typing 0205 code in main  menu and access "Add question", "Remove Question" and "Import question" functionalities.
"""
import time
import random
import json


# from pathlib import Path


def Greeting():
    print("\t\t\t---KBC GAME---")
    greeting = ["Good Morning", "Good Afternoon", "Good Evening", "Good Night"]
    using_time = time.localtime()
    using_hour_time = using_time.tm_hour
    current_date = time.strftime("%d/%m/%y", using_time)
    current_time = time.strftime("%H:%M", using_time)
    if 6 < using_hour_time < 12:
        greet = greeting[0]
    elif 12 <= using_hour_time < 17:
        greet = greeting[1]
    elif 17 <= using_hour_time < 20:
        greet = greeting[2]
    else:
        greet = greeting[3]
    print(f"Hello,{greet}\t\t\t\t{current_date}\n\t\t\t\t\t\t{current_time}")


def Main_Menu():
    print("\t\t\t\"MAIN MENU\"")
    print("1. Start Game\n2. Rules and life lines", )


def TERMINATED_Data_file_creator():
    """
        This function is created for creating default question file in the device if there is not a question file exists
        but this function causes time and performance issue.
        so the function is terminated
        :return:
        """
    global backend_process
    default_questions = {
        "1": {"Question": "Which planet is known as the Red Planet?",
              "Options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"], "Answer": "B) Mars"},
        "2": {"Question": "What is the capital of India?",
              "Options": ["A) London", "B) Delhi", "C) Paris", "D) Madrid"], "Answer": "B) Delhi"},
        "3": {"Question": "Which animal is known for having black and white stripes?",
              "Options": ["A) Lion", "B) Tiger", "C) Giraffe", "D) Elephant"], "Answer": "B) Tiger"},
        "4": {"Question": "How many sides does a triangle have?", "Options": ["A) 3", "B) 4", "C) 5", "D) 6"],
              "Answer": "A) 3"},
        "5": {"Question": "What is the color of a banana?", "Options": ["A) Red", "B) Blue", "C) Yellow", "D) Green"],
              "Answer": "C) Yellow"},
        "6": {"Question": "Who painted the Mona Lisa?",
              "Options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
              "Answer": "C) Leonardo da Vinci"},
        "7": {"Question": "Which is the largest planet in our solar system?",
              "Options": ["A) Jupiter", "B) Mars", "C) Earth", "D) Saturn"], "Answer": "A) Jupiter"},
        "8": {"Question": "What is the smallest prime number?", "Options": ["A) 0", "B) 1", "C) 2", "D) 3"],
              "Answer": "C) 2"},
        "9": {"Question": "Who wrote the play 'Romeo and Juliet'?",
              "Options": ["A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"],
              "Answer": "A) William Shakespeare"},
        "10": {"Question": "Which country is famous for the ancient pyramids?",
               "Options": ["A) Greece", "B) Egypt", "C) China", "D) Italy"], "Answer": "B) Egypt"}
    }

    # user_home = Path.home()
    # found_files = list(user_home.glob('**/*/*/*/*/question_file.txt'))
    # if not found_files:
    file_name = "QuestionBook.txt"
    with open(file_name, "w") as file:
        json.dump(default_questions, file)
    if backend_process:
        print("->Default Question File Loaded Into Directory")
    # else:
    #   print("file exists")


def Question_file_loader():
    global Question
    file_name = "QuestionBook.txt"
    with open(file_name, "r") as file:
        Question = json.load(file)
    if backend_process:
        print("->Question Imported From Question File")


def Add_question():
    global Question
    print("\"Entered Into Question Adding Function\"")

    flag = True
    while flag:
        question = input("Question: ")
        option_list = ["A) ", "B) ", "C) ", "D) "]
        i = 0
        print("Option")
        option = []
        for item in option_list:
            taking_option = input(f"{item}")
            if i == 0:
                A = f"A) {taking_option}\n"
                option.append(A)
            elif i == 1:
                B = f"B) {taking_option}\n"
                option.append(B)
            elif i == 2:
                C = f"C) {taking_option}\n"
                option.append(C)
            else:
                D = f"D) {taking_option}"
                option.append(D)
            i += 1
        answer = input("Answer: ")

        if not Question:
            serial = 1
        else:
            keys_list = list(Question.keys())
            last_serial = keys_list[-1]
            serial = int(last_serial) + 1

        Question[serial] = {"Question": question, "Options": option, "Answer": answer}
        with open("QuestionBook.txt", "w") as file:
            json.dump(Question, file)

        loop = input("Do You Want To Add More Questions? (yes/no): ")
        if loop == "no":
            flag = False
            print("Question Addition Function Exited Successfully!")
        print(Question)


def Remove_question():
    global Question
    element = input("Enter Question Number For Deleting That Question (Enter 0 to see questions): ")
    if element == "0":
        Question_File_Printer()
    else:
        del Question[element]
        print("->Question Has Deleted From The File")


def Audience_poll():
    print("\n\t\t\t\"AUDIENCE POLL LIFE LINE ACTIVATED\"")
    count = int(input("Enter Audience Count: "))
    a = 0
    b = 0
    c = 0
    d = 0
    trash = 0
    for i in range(count):
        vote = input("Enter Your Answer (A/B/C/D): ")
        if vote == "A" or vote == "a":
            a += 1
        elif vote == "B" or vote == "b":
            b += 1
        elif vote == "C" or vote == "c":
            c += 1
        elif vote == "D" or vote == "d":
            d += 1
        else:
            print("Enter Valid Choice: This vote will count in trash!")
            trash += 1
    print(f"\n\"Audience Poll Results\"\nA:{a}\nB:{b}\nC:{c}\nD:{d}\nTrash:{trash}\n")
    after_audience_poll_answer = input("Enter Your Answer: ")
    global player_answer
    player_answer = after_audience_poll_answer


def Twice_Chance():
    global first_char_answer
    global player_answer
    first_chance = input("Enter Your First Answer: ")
    if first_chance.upper() == first_char_answer:
        print("You Got In First Try!")
        return first_chance
    else:
        print("You Answered Wrong!")
        second_chance = input("Enter Your Second Answer:")
        if second_chance.upper() == first_char_answer:
            print("Second Answer Is Right!")
            return second_chance
        else:
            print("You Also Got Second Answer Wrong!")
            return player_answer


"""

"""


def Change_the_question():
    return False


def half_half():
    global Question
    global question_serial
    option_list = []

    for sequence, data in Question.items():
        if sequence == question_serial:
            presented_question_answer = data['Answer']
            for option in data["Options"]:
                option_data = option
                option_list.append(option_data)
            option_list.remove(presented_question_answer)
            for i in range(2):
                removed_option = random.choice(option_list)
                option_list.remove(removed_option)
            first_element_optionlist = option_list[0]
            if first_element_optionlist[0] == "A":
                f_q = 1
            elif first_element_optionlist[0] == "B":
                f_q = 2
            elif first_element_optionlist[0] == "C":
                f_q = 3
            elif first_element_optionlist[0] == "D":
                f_q = 4

            if presented_question_answer[0] == "A":
                f_a = 1
            elif presented_question_answer[0] == "B":
                f_a = 2
            elif presented_question_answer[0] == "C":
                f_a = 3
            elif presented_question_answer[0] == "D":
                f_a = 4

            if f_q < f_a:
                option_list.append(presented_question_answer)
            else:
                option_list.insert(0, presented_question_answer)
            print(f"{sequence}.{data['Question']}")
            for item in range(2):
                print(option_list[item])
            half_half_answer = input("Enter Your Answer: ")
            return half_half_answer
            # print(f"{option}")


def Question_presenter():
    global price_list
    global presented_question
    global player_answer
    global first_char_answer
    global presented_question_answer
    global question_serial
    function_flag = True
    earned_money = 0
    price_point = 0
    for sequence, data in Question.items():
        print(f"{sequence}.{data['Question']}")
        print("Options:")
        for option in data["Options"]:
            print(f"{option}")
        presented_question_answer = data['Answer']
        print("Lifelines Left: ", lifelines_list)
        first_char_answer = presented_question_answer[0]
        question_serial = sequence
        flag = True
        change_the_question_flag = 0
        while flag:
            player_answer = input("Enter Answer:")
            if player_answer.lower() == "a" or player_answer.lower() == "b" or player_answer.lower() == "c" or player_answer.lower() == "d":
                flag = False
            elif player_answer.lower == "audience poll" or player_answer == "1":
                lifelines_list.remove("1. AUDIENCE POLL")
                Audience_poll()
                flag = False
            elif player_answer == "50-50" or player_answer == "2":
                lifelines_list.remove("2. 50-50")
                player_answer = half_half().lower()
                flag = False
            elif player_answer.lower() == "change the question" or player_answer == "3":
                lifelines_list.remove("3. CHANGE THE QUESTION")
                change_the_question_flag = 1
                flag = False
            elif player_answer.lower() == "twice chance" or player_answer == "4":
                lifelines_list.remove("4. TWICE CHANCE")
                player_answer = Twice_Chance().lower()
                flag = False
            else:
                print("Input Error: Please Enter Choice As A/B/C/D. ")
        if change_the_question_flag == 0:
            if player_answer.upper() == first_char_answer:
                earned_money = price_list[price_point]
                price_point += 1
                print(
                    f"{random.choice(first_winning_message)} {earned_money}/- {random.choice(second_winning_message)}")
            else:
                print(
                    f"{random.choice(first_loosing_message)} Your Earned {earned_money}/-\n{random.choice(second_loosing_message)}")
                function_flag = False
                break
    if earned_money == price_list[-1]:
        print("Congratulations You Won The Game")


def Question_File_Printer():
    global Question
    for sequence, data in Question.items():
        print(f"{sequence}.{data['Question']}")
        print("Options:")
        for option in data["Options"]:
            print(f"{option}")
        print(f"Answer:{data['Answer']}")


def Answer_Checker(presented_question_answer):
    answer_status = False
    flag = True
    while flag:
        player_input = input("Enter Answer:")
        if player_input.lower() == "a" or player_input.lower() == "b" or player_input.lower() == "c" or player_input.lower() == "d":
            flag = False
        else:
            print("Input Error: Please Enter Choice As A/B/C/D. ")
    if player_input.lower() == presented_question_answer.lower():
        answer_status = True
    return answer_status


def Rules_and_lifelines_and_prizepool():
    rules = "\n\t\t\t\tRules\nEach marks contain a prize money\nif you choose correct answer you get the prize\n"
    lifelines = "\t\t\t\tFour lifelines\n" \
                "1. Audience Poll: Get option vote count from the audience\n" \
                "2. 50-50: Two wrong answer eliminated\n" \
                "3. 2 chance: Player get two chance to attempt question\n" \
                "4. Change The Question: Change The Question\n"
    prizepool = "\t\t\t\tPrize\n" \
                "01. 2000/-\n" \
                "02. 5000/-\n" \
                "03. 10000/-\n" \
                "04. 20000/-\n" \
                "05. 50000/-\n" \
                "06. 100000/-\n" \
                "07. 250000/-\n" \
                "08. 500000/-\n" \
                "09. 1000000/-\n" \
                "10. 5000000/-\n"
    print("\t\t\t\"Rules And Lifelines\"")
    print(rules)
    print(lifelines)
    print(prizepool)


def Developer_mode():
    global backend_process
    backend_process = True
    print("\"Entered Into Developer Mode\"")
    print("Options:\n1) Add Questions\n2) Remove Questions\n3) Import Question")
    choice = input("Enter Your Choice: ")
    flag = True
    while flag:
        if choice == "1" or choice.lower() == "add" or choice.lower() == "add question":
            Add_question()
            flag = False
        elif choice == "2" or choice.lower() == "remove" or choice.lower() == "remove question":
            Remove_question()
            flag = False
        elif choice == "3" or choice.lower() == "import" or choice.lower() == "import question":
            TERMINATED_Data_file_creator()
            flag = False
        else:
            print("Please Enter Valid Input: ")


# Create function for Lifelines


# global variables
price_list = [2000, 5000, 10000, 20000, 50000, 100000, 250000, 500000, 1000000, 5000000, 10000000, 70000000, 100000000, 500000000, 750000000, 1000000000]
earned_money = 0
Question = None
question_serial = 0
lifelines_list = ["1. AUDIENCE POLL", "2. 50-50", "3. CHANGE THE QUESTION", "4. TWICE CHANCE"]
backend_process = False
first_loosing_message = ["Better luck next time!", "Sorry, you didn't win this time.", "Keep trying!", "Hard luck!"]
second_loosing_message = ["You Earned"]
first_winning_message = ["Congratulations!", "Well done!", "Amazing job!", "Fantastic!"]
second_winning_message = ["You Won", "You Earned", "You Made It"]
presented_question_answer = 0
presented_question = 0
player_answer = 0
first_char_answer = 0

# main
Greeting()
Main_Menu()
flag = True
while flag:
    main_menu_choice = input("Enter Your Choice: ")
    if main_menu_choice == "1" or main_menu_choice.lower() == "start game":
        Question_file_loader()
        Question_presenter()
        return_mainmenu = input("Want To Play Again? (Yes/No):")
        if return_mainmenu.lower() == "yes":
            flag = True
            Main_Menu()
        else:
            print("Exited From The Game")
            flag = False
    elif main_menu_choice == "2" or main_menu_choice.lower() == "rules and lifelines" or main_menu_choice == "rules & lifelines":
        Rules_and_lifelines_and_prizepool()
        return_mainmenu = input("Want To Back To Main Menu? (Yes/No):")
        if return_mainmenu.lower() == "yes":
            flag = True
            Main_Menu()
        else:
            print("Exited From The Game")
            flag = False
    elif main_menu_choice == "0205":
        backend_process = True
        Developer_mode()
        return_mainmenu = input("Want To Back To Main Menu? (Yes/No):")
        if return_mainmenu.lower() == "yes":
            flag = True
            Main_Menu()
        else:
            print("Exited From The Game")
            flag = False
    else:
        print("Error: Please Enter Valid Input")
