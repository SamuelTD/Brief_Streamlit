import json_handler as jh

class Question:
    
    def __init__(self, title:str, answers: list[str], correct_answers: int) -> None:
        self.title = title
        self.answers = answers
        self.correct_answer = correct_answers
    
    @staticmethod
    def return_questions_as_list(json: any) -> list:
        results = []
        if json == "":
            return results
        for item in json:
            # print(item)
            results.append(Question(item["title"], item["answers"], item["correct_answer"]))
        return results          
    
    def __str__(self) -> str:
        return f"Question : {self.title} ; Réponses possibles : {self.answers} ; Bonne réponse : {self.correct_answer}"
    

if __name__ == "__main__":
    questions = [
        Question("title 1", [1, 2, 3, 4], 1),
        Question("title 2", [5, 6, 7, 8], 2),
        Question("title 3", [9, 10, 11, 12], 3),
    ]
    jh.write_dataset(questions)