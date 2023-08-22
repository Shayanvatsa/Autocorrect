Auto-Correct Jupyter Notebook

This Jupyter Notebook contains a simple auto-correct function implemented using the Natural Language Toolkit (NLTK) library in Python. The function aims to correct misspelled words by finding the closest matching word from the English language corpus.

Getting Started

Prerequisites

Before running the code, make sure you have the following prerequisites installed:

Python (>=3.6)
NLTK library
You can install the required NLTK library using the following command:

pip install nltk

Running the Notebook
Clone this repository to your local machine or download the notebook file.
Open the Jupyter Notebook in your preferred environment.
Execute the code cells in the notebook to run the auto-correct function.
Code Overview
The notebook contains the following sections:

Importing Required Libraries: Importing the necessary libraries, including NLTK and its submodules.

Loading English Words: Downloading the list of English words from the NLTK corpus.

Auto-Correct Function: Defining the auto_correct function, which takes an input word and attempts to correct it by finding the nearest word from the English words corpus using edit distance.

Main Loop: Implementing a loop that repeatedly takes user input for a word and returns the corrected word using the auto_correct function. The loop continues until the user types 'exit'.

Usage

Run the Jupyter Notebook code cells.
Enter a word when prompted. The auto-corrected word will be displayed.
To exit the loop, type 'exit' when prompted.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or submit an issue in this repository.

