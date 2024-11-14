import json

def get_dataset() -> any:
    try:
        with open("quiz.json") as file:
            return json.load(file)
    except:
        with open("quiz.json", "w") as file:
            file.write("")
            return ""
        
def write_dataset(dataset: list) -> None:
    with open("quiz.json", "w") as file:
        file.write(json.dumps([question.__dict__ for question in dataset]))