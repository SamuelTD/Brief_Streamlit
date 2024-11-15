# <p align="center">Simplon_Wa-Tor</p>
<p align="center">
    <img src="images/lepers_3points.gif" alt="Wa-Tor Simulation">
</p>

This is a simple streamlit project that enable a user to create Quiz by manually inputting questions and then playing said Quiz.

## ➤ Menu

* [➤ Project Structure](#-project-structure)
* [➤ How to run](#-how-to-run)
* [➤ Requirements](#-requirements)
* [➤ Quiz Creation](#-quiz-creation)
* [➤ Playing a Quiz](#-play-a-quiz)
* [➤ Author](#-author)

## Project Structure

This project includes the following primary Python files:

- **main.py**: The entry point of the app. It contains the logic of the Quiz creator.
- **pages/page_1.py**: Contains the lofic of the Play Quiz page.
- **general_func.py**: Contains some general case functions used in all applicative scripts.
- **question.py**: Contains the `Question` class.
- **json_handler.py**: Contains all the functions tied to the reading and writing of JSON files.


## How to Run

To execute the simulation, follow these steps:

1. Ensure Python is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```
5. Run the following console command to start the simulation:
```bash
streamlit run main.py
```

## Quiz Creation

The first page of the app contains the Quiz Creator, which allow a user to create a Quiz from scratch by manually inputing Questions.

After inputting a valid title, possibles answers and the right answer, the user must click the "Ajouter ma question" to enter the Question into the queue. When satisfied with their question set, the user must click "Créer le quiz" to create a JSON file of the current Quiz.

## Play a Quiz

On the Play a quiz page, the user will be able to play the created Quiz, read from the JSON file. This process has 3 distincts steps :

**1°) Settings**

First the user is presented with a small sets of settings to customize their game.

**2°) Quiz**

Secondly, the user play the quiz, selecting one answer between the availlable one and doing so for each question.

**3°) Results**

Lastly, once the final question has been answered, the user is taken to a result screen where their performance is evaluated and where they have the opportunity to restart the quiz.

**Bonus features**:

- *Question Treshold*: The user is able to limite the maximum amount of questions in the Quiz. 
- *Random Question Distribution*: The user is able to randomize the order in which the Question are presented each game.


## License

MIT License

Copyright (c) 2024 Samuel Thorez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author

Samuel Thorez 
<a href="https://github.com/SamuelTD" target="_blank">
    <img loading="lazy" src="images/github-mark.png" width="30" height="30" style="vertical-align: middle; float: middle; margin-left: 30px;" alt="GitHub Logo">
</a>