#Credentials:
#   Program written by Aidan Evans
#   Terms and Definitions from Myers Psychology 10th Edition, By: David G. Myers



import os
import shutil
import colorama
from termcolor import colored, cprint
from random import randint



colorama.init()



def get_window_size():      #Returns number of columns in window
    size = shutil.get_terminal_size(fallback=(80, 24))
    width = size[0]
    return width



def print_title():      #Prints the main menu page
    print(chr(27) + "[2J")  #Clears the window
    print(' Press Ctrl+C at Anytime to Return to the Main Menu')
    width = get_window_size()
    if (width < 180):       #Checks for window size, i.e. number of columns, and formats accordingly
        cprint(
        '''
    ____________   ____________    _         _   ____________   _           _
    |          |   |                \       /    |              |           |
    |          |   |                 \     /     |              |           |
    |__________|   |__________        \___/      |              |___________|
    |                         |         |        |              |           |
    |                         |         |        |              |           |
    |              ___________|         |        |___________   |           |
           ___________   _________   _________    ____     ____  _________
                |        |           |        |   |   \   /   |  |
                |        |_______    |________|   |    \_/    |  |_______
                |        |           |      \     |           |          |
                |        |________   |       \    |           |  ________|
     {}    {}
        '''.format(colored('Words and Definitions From Myers Psychology 10th Ed.', color='white'), colored('Made By: Aidan Evans', color='green', attrs=['bold'])), 
            color='cyan', 
            attrs=['bold'])  #Prints Title

        cprint(
        '''     
        1. View Terms Alphabetically     3. Search Terms
        2. View Terms by Chapter         4. View Random Term
        ''', color='magenta', attrs=['bold'])  #Prints Options
    else:
        cprint(
        '''
    _____________   _____________   _           _   _____________   _           _
    |           |   |                \         /    |               |           |
    |           |   |                 \       /     |               |           |       _________________   ___________   __________    ____      ____  ___________
    |           |   |                  \     /      |               |           |               |           |             |         |   |   \    /   |  |
    |___________|   |___________        \___/       |               |___________|               |           |             |         |   |    \  /    |  |
    |                           |         |         |               |           |               |           |_________    |_________|   |     \/     |  |_________
    |                           |         |         |               |           |               |           |             |      \      |            |            |
    |                           |         |         |               |           |               |           |             |       \     |            |            |
    |               ____________|         |         |____________   |           |               |           |__________   |        \    |            |  __________|
                                                                                    {}    {}
        '''.format(colored('Words and Definitions From Myers Psychology 10th Ed.', color='white'), colored('Made By: Aidan Evans', color='green', attrs=['bold'])), 
            color='cyan', 
            attrs=['bold'])  #Prints Title

        cprint(
        '''     
        1. View Terms Alphabetically       2. View Terms by Chapter       3. Search Terms       4. View Random Term
        ''', color='magenta', attrs=['bold'])  #Prints Options



def print_masthead():
    print(' Press Ctrl+C at Anytime to Return to the Main Menu')
    cprint(
    '''
    _____  ______  _     _  _____  _    _    _______ ______ _____  _    _ _____
    |    | |        \   /  |       |    |       |    |      |    | |\  /| |
    |____| |____     \_/   |       |____|       |    |____  |____| | \/ | |___
    |           |     |    |       |    |       |    |      |   \  |    |     |
    |      _____|     |    |_____  |    |       |    |_____ |    \ |    | ____|
                                                         {}
    '''.format(colored('Made By: Aidan Evans', color='green', attrs=['bold'])), 
        color='cyan', 
        attrs=['bold'])  #Prints Masthead



def all_terms():    #Displays the terms in alphabetical order
    global term_definition
    global term_format
    global terms


    print(chr(27) + "[2J")

    print_masthead()
    cprint('\n    To Get Terms Alphabetically - \n        Please Input the First Letter or Letters the Term Starts With:', color='magenta', attrs=['bold'])


    while (1==1):
        starts_with = input('\n    Input What the Term Start With: ').lower()

        to_print = []

        for term in terms:  #For each term in terms
            if (term[0:len(starts_with)].lower() == starts_with):   #if the term starts with the inputed text
                to_print.append(term_format[terms.index(term)])

        print(chr(27) + "[2J")
        print_masthead()

        if (to_print != []):
            to_print.sort()     #Sorts the desired output elements alphabetically

            print('\nSearch For "{}"'.format(colored(starts_with, color='green', attrs=['bold'])))
            cprint('Search Results:', color='magenta', attrs=['bold'])
            for element in to_print:    #Prints outputed terms
                print(element)
            print('\n')
        else:
            cprint('\n\tNo Results Found - Please Revise Your Search', color='magenta', attrs=['bold'])

        

def by_chapter(err):   #Allows the terms to be sorted and viewed by chapter
    global term_definition
    global term_format
    global chapter
    global terms


    print(chr(27) + "[2J")

    print_masthead()


    while(1==1):
        cprint('\n    Input a Chapter Number to find its Vocabulary Terms:', color='magenta', attrs=['bold'])
        print(      #Prints List of Chapters
        '''
        {}:
             {} {}: The Story of Psychology
             {} {}: Thinking critically With Psychological Science
             {} {}: The Biology of Mind
             {} {}: Consciousness and the Two-Track Mind
             {} {}: Nature, Nurture, and Human Diversity
             {} {}: Developing Through the Life Span
             {} {}: Sensation and Perception
             {} {}: Learning
             {} {}: Memory
             {} {}: Thinking and Language
            {} {}: Intelligence
            {} {}: Motivation and Work
            {} {}: Emotions, Stress, and Health
            {} {}: Personality
            {} {}: Social Psychology
            {} {}: Psychological Disorders
            {} {}: Therapy
        '''.format(colored('Chapters', color='green', attrs=['bold']),
                   colored('0.', color='cyan', attrs=['bold']), colored('Prologue', color='white', attrs=['bold']),
                   colored('1.', color='cyan', attrs=['bold']), colored('Chapter 1', color='white', attrs=['bold']),
                   colored('2.', color='cyan', attrs=['bold']), colored('Chapter 2', color='white', attrs=['bold']),
                   colored('3.', color='cyan', attrs=['bold']), colored('Chapter 3', color='white', attrs=['bold']),
                   colored('4.', color='cyan', attrs=['bold']), colored('Chapter 4', color='white', attrs=['bold']),
                   colored('5.', color='cyan', attrs=['bold']), colored('Chapter 5', color='white', attrs=['bold']),
                   colored('6.', color='cyan', attrs=['bold']), colored('Chapter 6', color='white', attrs=['bold']),
                   colored('7.', color='cyan', attrs=['bold']), colored('Chapter 7', color='white', attrs=['bold']),
                   colored('8.', color='cyan', attrs=['bold']), colored('Chapter 8', color='white', attrs=['bold']),
                   colored('9.', color='cyan', attrs=['bold']), colored('Chapter 9', color='white', attrs=['bold']),
                   colored('10.', color='cyan', attrs=['bold']), colored('Chapter 10', color='white', attrs=['bold']),
                   colored('11.', color='cyan', attrs=['bold']), colored('Chapter 11', color='white', attrs=['bold']),
                   colored('12.', color='cyan', attrs=['bold']), colored('Chapter 12', color='white', attrs=['bold']),
                   colored('13.', color='cyan', attrs=['bold']), colored('Chapter 13', color='white', attrs=['bold']),
                   colored('14.', color='cyan', attrs=['bold']), colored('Chapter 14', color='white', attrs=['bold']),
                   colored('15.', color='cyan', attrs=['bold']), colored('Chapter 15', color='white', attrs=['bold']),
                   colored('16.', color='cyan', attrs=['bold']), colored('Chapter 16', color='white', attrs=['bold']),
                    ))

        if (err == 1):
            cprint('\tInvalid Input - Please Try Again', color='magenta', attrs=['bold'])

        chapter_num = input('\n    Please Choose a Number: ')

        chapter_index = 0
        got_results = 0
        continue_input_check = 1

        print('\n')

        try:
            err = 0
            while (chapter_index <= 16 and continue_input_check == 1):    #Checks to see if input is correct and prints results
                if (chapter_index == int(chapter_num)):

                    print(chr(27) + "[2J")
                    print_masthead()

                    if (chapter_index == 0):
                        title = 'Prologue'
                    else:
                        title = 'Chapter {}'.format(chapter_index)

                    cprint('\n{} Terms:'.format(title), color='magenta', attrs=['bold'])

                    got_results = 1
                    term_loc = []

                    for term in chapter[chapter_index]:
                        term_loc.append(terms.index(term))

                    for loc in term_loc:
                        print(term_format[loc])

                    continue_input_check = 0

                else:
                    chapter_index += 1
        except ValueError:
            by_chapter(1)

        if (got_results == 0):
            by_chapter(1)



def search_terms(): #Allows for the input of a search parameter and displays most likely results
    global term_definition
    global term_format
    global terms
    global term_format_long
    global term_definition_long


    end_chars = [' ', '.', ')', ';', '-', "'", '\n', ':']
    start_chars = [' ', '-', '"', '(']


    print(chr(27) + "[2J")
    print_masthead()
    cprint('    Input a keyword or term to search for it:', color='magenta', attrs=['bold'])


    while (1==1):
        results = []
        result_num_1 = 0
        term_loc_best = []
        term_loc_rest = []
        term_loc_best_original = []

        search = input('\n    Search For: ')

        search_words = search.split()

        for term in term_definition:      #Creates an array counting each time the words in the inputed search term is found in each vocabulary term
            term_num = 0
            for word in search_words:
                if (word.isupper() == True):  #If entire word in caps search for matches in caps (strict)
                    term_num += term.count(word)
                else:                           #Else search any cases that match, regardless of capitalization (unstrict)
                    for end_char in end_chars:
                        for start_char in start_chars:
                            term_num += term.lower().count(start_char + word.lower() + end_char)
                        if (term.lower().find(word.lower() + end_char) == 1):
                            term_num += 1
            results.append(term_num)

        search_max = max(results)               #Makes search_res equal to the maximum integer in the count results
        for result in results:          #Calculates number of results
            if result != 0:
                result_num_1 += 1

        if (search_max != 0):   #Checks for results
            if (result_num_1 <= 30):
                for element in enumerate(results):  #Appends the position of the resulting term locations to "term_loc"s
                    if (element[1] != 0):
                        if (element[1] == search_max): 
                            term_loc_best.append(element[0])    #Appends to term_loc_best and term_loc_best_original for most results
                            term_loc_best_original.append(element[0])
                        else:
                            term_loc_rest.append(element[0])    #Appends to term_loc_rest for all others

                for term in terms:                  #Adds terms mentioned in best results to best results
                    for loc in term_loc_best_original:
                        for end_char in end_chars:
                            for start_char in start_chars:
                                if (term_definition[loc].find(start_char + term + end_char) != -1 or
                                    term_definition[loc].find(term + end_char) == 1):
                                    if (terms.index(term)) not in term_loc_best:
                                        term_loc_best.append(terms.index(term))

                for loc in term_loc_best:       #Removes elements from term_loc_rest if in both term_loc_best and term_loc_rest
                    if loc in term_loc_rest:
                        term_loc_rest.remove(loc)

                result_num_2 = len(term_loc_best) + len(term_loc_rest)
                cprint('\n {} Results Found\n'.format(result_num_2), color='green', attrs=['bold'])

                width = get_window_size()   #Adjusts Result Printing Depending on Window Size
                if (term_loc_rest != []):

                    print(chr(27) + "[2J")
                    print_masthead()

                    print('Search Results for "{}"'.format(colored(search, color='green', attrs=['bold'])))

                    if (width < 180):   #If window small
                        cprint('Best Results:', color='magenta', attrs=['bold'])                #Prints best results: indexes from term_loc_best
                        for loc in term_loc_best:
                            print(term_format[loc])

                        cprint('\nOther Possible Results:', color='magenta', attrs=['bold'])    #Prints all other results: indexes from term_loc_rest
                        for loc in term_loc_rest:
                            print(term_format[loc])
                    else:   #If window large enough to display results side-by-side
                        result_format_count = 0
                        best_results = []
                        best_results_for_spaces = []    #Used to calculate number of spaces between best and other result on each line
                        other_results = []

                        for loc in term_loc_best:
                            for element in term_format_long[loc]:
                                best_results.append(element)
                            for element in term_definition_long[loc]:
                                best_results_for_spaces.append(element)

                        for loc in term_loc_rest:
                            for element in term_format_long[loc]:
                                other_results.append(element)

                        cprint('Best Results:{}Other Possible Results'.format(' ' * 77), color='magenta', attrs=['bold'])

                        while (result_format_count < max([len(best_results), len(other_results)])):     #If result_format_count is less than the number of lines that should be printed
                            spaces_till_next_term = 0
                            try:
                                spaces_till_next_term = 90 - len(best_results_for_spaces[result_format_count])  #Calculates number of spaces that should be between best results and other results
                                print('{}{}{}'.format(best_results[result_format_count], ' ' * spaces_till_next_term, other_results[result_format_count]))  #Prints results
                            except IndexError:  #If an index is out of range
                                try:    #Tests to see if best_results is out of range
                                    test = best_results[result_format_count]
                                except IndexError:  #If so, appends element to best_results and best_results_for_spaces
                                    best_results.append('')
                                    best_results_for_spaces.append('')
                                try:    #Tests to see if other_results is out of range
                                    test = other_results[result_format_count]
                                except IndexError:  #If so, appends element to other_results
                                    other_results.append('')
                                result_format_count -= 1
                            result_format_count += 1
                else:
                    print(chr(27) + "[2J")
                    print_masthead()

                    print('Search Results for "{}"'.format(colored(search, color='green', attrs=['bold'])))

                    cprint('Best Results:', color='magenta', attrs=['bold'])                #Prints best results: indexes from term_loc_best
                    for loc in term_loc_best:
                        print(term_format[loc])
            else:
                print(result_num_1)
                cprint('\n\tToo Many Possible Results - Please Be More Specific\n', color='magenta', attrs=['bold'])
        else:
            cprint('\n\tNo Results Found - Please Refine Your Search\n', color='magenta', attrs=['bold'])
        


def rand_term():        #Returns a random term and definition
    global term_format

    max_val = len(term_format) - 1      #Sets max_val equal to the number of elements in term_format minus 1 (represents the maximum limit integer)
    term_val = randint(0, max_val)      #Sets term_val equal to a random integer between 0 and max_val

    return term_format[term_val]



def menu(print_rand):   #Displays main menu and allows input for what to do
    print_title()


    if (print_rand == 1):   #print_rand is true then print a random term
        print('\n' + colored('Random Term:', color='magenta', attrs=['bold']) + '\n' + rand_term())


    choice = input('\n   Please Input a Number: ')

    if (choice == '1'): #View All Terms
        try:
            all_terms()  
        except KeyboardInterrupt:   #Loads menu interface when Ctrl+C pressed in all_terms()
            menu(0)
        except EOFError:
            menu(0)

    elif (choice == '2'):   #View Terms by Chapter
        try:
            by_chapter(0)  
        except KeyboardInterrupt:   #Loads menu interface when Ctrl+C pressed in by_chapter()
            menu(0)
        except EOFError:
            menu(0)

    elif (choice == '3'):   #Search Input
        try:
            search_terms()  
        except KeyboardInterrupt:   #Loads menu interface when Ctrl+C pressed in search_terms()
            menu(0)
        except EOFError:
            menu(0)

    elif (choice == '4'):   #Returns Random Vocab Term
        menu(1)

    else:
        menu(0)  #Else return to menu, i.e. restarts option input



def main():
    global term_definition
    global term_format
    global terms
    global term_format_long
    global term_definition_long
    global chapter


    ex_terms = []
    terms = []

    read_file = open('term_definitions.txt', 'r')  #Loads terms and definitions to display from text file
    terms_read_file = open('term_list.txt', 'r')    #Loads term list from text file

    for line in read_file:  #Appends each line of text file to value in an array
        ex_terms.append(line)
    for line in terms_read_file:
        line = line.replace('\n', '')
        terms.append(line)

    read_file.close()
    terms_read_file.close()


    term_definition = ['']
    term_format = ['']
    term_count = 0
    terms_array_count = 0

    while (term_count < len(ex_terms)-1):   #Formats the terms and definitions so each term-definition pair is its own element in the array (Used for searching)
        if (ex_terms[term_count] != '\n'):
            term_definition[terms_array_count] += ' ' + ex_terms[term_count]
            term_format[terms_array_count] += ' ' + ex_terms[term_count]
        else:
            term_definition.append('')
            term_format.append('')
            terms_array_count += 1
        term_count += 1


    chapter_count = 0
    chapter = []

    while (chapter_count <= 16):    #Reads each chapter.txt file and extracts the terms for each chapter
        chapter_append = []

        chapter_file = open('chapter{}.txt'.format(chapter_count), 'r')

        for line in chapter_file:
            line = line.replace('\n', '')
            chapter_append.append(line)

        chapter_append.sort()   #Alphabetizes each chapter file

        chapter.append(chapter_append)

        chapter_count += 1


    term_format_count = 0

    for element in term_format:     #Colors and bolds terms in term-definition pairs (Used for formated printed results)
        element = element.replace(terms[term_format_count], colored(terms[term_format_count], color='yellow', attrs=['bold']))
        term_format[term_format_count] = element
        term_format_count += 1


    term_format_long = []
    
    for element in term_format:     #Creates array for printing formatted results when window enlarged
        term_format_long.append(element.splitlines())


    term_definition_long = []

    for element in term_definition:     #Creates arrary for calculating spaces for formatted results when window enlarged
        term_definition_long.append(element.splitlines())


    try:
        menu(0)
    except KeyboardInterrupt:   #Closes when Ctrl+C pressed in menu()
        print('\n')
        quit()
    except EOFError:
        print('\n')
        quit()

main()