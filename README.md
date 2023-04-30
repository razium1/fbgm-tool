# fbgm-tool
# Football GM Draft Tool

This is a Python program that helps football GMs draft players by grading them based on various attributes. 

## Getting Started

To use this program, you need to have Python 3 installed on your computer. You can download Python 3 from the official website [here](https://www.python.org/downloads/).

You also need to have the following Python packages installed:

- pandas
- tkinter

You can install these packages by running the following command in your terminal or command prompt:

pip install pandas tkinter

## How to Use

1. Open the program by running `tool.py` in Python.

2. Click on the "Open CSV File" button to select a CSV file containing the player data. The CSV file must have the following columns: Name, Position, Overall, Speed, Strength, Agility, Awareness.

3. The program will display the player data in a table. You can sort the table by clicking on the column headers.

4. You can search for a specific player by typing their name in the search bar.

5. The program will automatically grade the players based on their attributes and position. The grades are displayed in the "Grade" column of the table.

6. You can select a player by clicking on their row in the table. The program will display the player's attributes and grade in the "Selected Player" section.

7. You can click on the "Draft Player" button to draft the selected player. The program will remove the player from the table and display a message saying that the player has been drafted.

8. You can save the drafted players to a CSV file by clicking on the "Save Drafted Players" button.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
