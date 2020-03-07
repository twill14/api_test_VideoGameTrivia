import requests
import json
import pprint
import random
import html


def print_answers(star_num):
    for answer in answers:
        print(str(star_num) + ". " + html.unescape(answer))
        star_num += 1


url = "https://opentdb.com/api.php?amount=10&category=15&type=multiple"
endgame = ""
score = 0
rounds = 0

while endgame != "quit":
    r = requests.get(url)
    if r.status_code != 200:
        endgame = input(
            "There was a problem receiving a question. Press Enter to try again or type 'quit' to quit the game.")
    else:
        rounds += 1
        answer_number = 1
        valid_answer = False
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        cor_answer = data['results'][0]['correct_answer']
        answers.append(cor_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        while not valid_answer:
            print("\n Round - " + str(rounds) + "\n")
            print_answers(answer_number)
            user_answer = input("\n Type the number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Answer is invalid \n")
                else:
                    valid_answer = True
            except:
                print("Please enter a valid answer")

        user_answer = answers[int(user_answer) - 1]

        if user_answer == cor_answer:
            print("\n That is correct! " + cor_answer + " was the correct answer!")
            score += 1
        else:
            print("\n Sorry, " + cor_answer + " was the correct answer.")

        endgame = input("\n Press enter to play again or type 'quit' to exit.")

print("\n Thanks for Playing!")
print("\n------------------------------")
print("\n Your final score: " + str(score))
print("\n Total Rounds - " + str(rounds))
print("\n------------------------------")
