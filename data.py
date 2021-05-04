import requests

question_data = []


def get_questions():
    response = requests.get("https://opentdb.com/api.php?amount=20&category=9&type=boolean")
    response.raise_for_status()

    data = response.json()
    for i in range(20):
        question_data.append(data["results"][i])


get_questions()


