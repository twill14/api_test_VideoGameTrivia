import requests
import json
import pprint
import random
import html

url = "https://opentdb.com/api.php?amount=10&category=15&type=multiple"
endgame = ""

while endgame != "quit":
    r = requests.get(url)
    if r.status_code != 200:
        endgame = input("There was a problem receiving a question. Press Enter to try again or type 'quit' to quit the game.")
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        cor_answer = data['results'][0]['correct_answer']
        answers.append(cor_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + ". " + html.unescape(answer))
            answer_number += 1


        input("\n Press enter to get a new question.")