# psych-terms
**A search database of psychology terms and definitions from Myers Psychology 10th Edition.**

(My vocabulary final project for my AP Psychology class)

## Overview
This is a program written in the Python programming language that allows the user to do one of 4 things:
1. View all the terms in alphabetical order given an inputed letter on what the terms should start with
2. View terms by each specific chapter in the book
3. Search for requested keywords and receive most likely results based on their search
4. View a randomly generated vocabulary term and definition from the 585 different words


## How To Use The Running Program
- When running the program, the program first opens to the main menu
- On the main menu there are four options, each option being one of the 4 described in the Overview
- To Choose an option, type in the corresponding number next to it and press the enter key

### To Use Option 1: View Terms Alphabetically
- Enter a letter or group of letters that the desired terms start with and the program will return all terms that start with the inputed text alphabetically

### To Use Option 2: View Terms by Chapter
- The program will display available chapters
- Then enter the number that corresponds to the desired chapter and the program will return each of the words in that chapter

### To Use Option 3: Search Terms
- Input a desired keyword or term and press the enter key
- The program will then return the best results in two catagories: "Best Results" and "Other Possible Results"
- "Best Results" contains the terms that have the most matches and vocabulary terms that are mentioned in the terms that had the most matches
  - For Example:
    - If "ego" was searched, the term with the most matches is "ego."
    - However, the definition also contains two other terms in it: "id" and "personality."
    - "Best Results" will then not only return the definition for "ego," but also for "id" and "personality."
- "Other Results" contains any other terms that had matches, but had neither the most matches nor was it mentioned in the definition of a "Best Match" term.

### To Use Option 4: View Random Term
- When selected, this option will return a random term from one of the 585 terms and display it on the main menu page

### To Return to the Main Menu
- To return to the Main Menu, press on the keyboard: Ctrl+C
- When pressed the program will take you directly back to the Main Menu
- Note: When pressing Ctrl+C on the Main Menu the program will close
