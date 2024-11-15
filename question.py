from pydantic import BaseModel, field_validator

class Question(BaseModel):
    
    
    title: str
    answers: list[str]
    correct_answer: int 
        
    @field_validator('correct_answer')
    def validate_correct_answer(cls, values):
        if values <= 0:
            raise ValueError("La bonne réponse ne peut pas être inférieure à 1.")
        return values
    
    @staticmethod
    def return_questions_as_list(json: any) -> list:
        """
        Return a list of Question objects from a JSON formated file.
        """
        results = []
        if json == "":
            return results
        for item in json:
            results.append(Question.model_validate({'title':item["title"], 'answers':item["answers"], 'correct_answer': item["correct_answer"]}))           
        return results          
    
    def __str__(self) -> str:
        return f"Question : {self.title} ; Réponses possibles : {self.answers} ; Bonne réponse : {self.correct_answer}"


#--------------------------------------------------------------
#NO PYDANTIC

# class Question:
    
#     def __init__(self, title:str, answers: list[str], correct_answers: int) -> None:
#         self.title = title
#         self.answers = answers
#         self.correct_answer = correct_answers
    
#     @staticmethod
#     def return_questions_as_list(json: any) -> list:
#         """
#         Return a list of Question objects from a JSON formated file.
#         """
#         results = []
#         if json == "":
#             return results
#         for item in json:
#             # print(item)
#             results.append(Question(item["title"], item["answers"], item["correct_answer"]))
#         return results          
    
#     def __str__(self) -> str:
#         return f"Question : {self.title} ; Réponses possibles : {self.answers} ; Bonne réponse : {self.correct_answer}"
