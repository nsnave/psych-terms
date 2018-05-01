import os
import csv
import shutil
import colorama
import wikipedia
from termcolor import colored, cprint

colorama.init()

def get_window_size():      #Returns number of columns in window
    size = shutil.get_terminal_size(fallback=(80, 24))
    width = size[0]
    return width

def print_masthead():
    cprint(
    '''
    ______  ______  _     _  _____  _     _    _________ ______ ______  _     _ ______
    |     | |        \   /  |       |     |        |     |      |     | |\   /| |
    |_____| |____     \_/   |       |_____|        |     |____  |_____| | \_/ | |____
    |            |     |    |       |     |        |     |      |   \   |     |      |
    |       _____|     |    |_____  |     |        |     |_____ |    \  |     | _____|
                                                                {}
    '''.format(colored('Made By: Aidan Evans', color='green', attrs=['bold'])), 
        color='cyan', 
        attrs=['bold'])  #Prints Masthead

def all_terms():    #Displays the terms in alphabetical order
    global term_definition
    global term_format
    print(chr(27) + "[2J")
    print_masthead()
    input('Input the First Letter Of the Term: ')

def by_chapter():   #Allows the terms to be sorted and viewed by chapter
    global term_definition
    global term_format
    print(chr(27) + "[2J")
    print_masthead()
    print('Chapters:')

def search_terms(): #Allows for the input of a search parameter and displays most likely results
    global term_definition
    global term_format
    global terms
    global term_format_long


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
                    if (width < 180):
                        cprint('Best Results:', color='magenta', attrs=['bold'])                #Prints best results: indexes from term_loc_best
                        for loc in term_loc_best:
                            print(term_format[loc])

                        cprint('\nOther Possible Results:', color='magenta', attrs=['bold'])    #Prints all other results: indexes from term_loc_rest
                        for loc in term_loc_rest:
                            print(term_format[loc])
                    else:
                        result_format_count = 0
                        best_results = []
                        other_results = []

                        for loc in term_loc_best:
                            for element in term_format_long[loc]
                                best_results.append(element)

                        for loc in term_loc_rest:
                            for element in term_format_long[loc]
                                other_results.append(element)

                        cprint('Best Results:{}Other Possible Results'.format(' ' * 77), color='magenta', attrs=['bold'])

                        while (result_format_count < max([len(term_loc_best), len(term_loc_rest)])):
                            spaces_till_next_term = 0
                            print(best_results[result_format_count])
                            result_format_count += 1
                else:
                    cprint('Best Results:', color='magenta', attrs=['bold'])                #Prints best results: indexes from term_loc_best
                    for loc in term_loc_best:
                        print(term_format[loc])
            else:
                print(result_num_1)
                cprint('\n\tToo Many Possible Results - Please Be More Specific\n', color='magenta', attrs=['bold'])
        else:
            cprint('\n\tNo Results Found - Please Refine Your Search\n', color='magenta', attrs=['bold'])
        

def menu():
    print(chr(27) + "[2J")
    print('Press Ctrl+C at Anytime to Return to Menu')
    width = get_window_size()
    if (width < 180):       #Checks for window size, i.e. number of columns, and formats accordingly
        cprint(
        '''
    _____________   _____________   _           _   _____________   _           _
    |           |   |                \         /    |               |           |
    |           |   |                 \       /     |               |           |
    |           |   |                  \     /      |               |           |
    |___________|   |___________        \___/       |               |___________|
    |                           |         |         |               |           |
    |                           |         |         |               |           |
    |                           |         |         |               |           |
    |               ____________|         |         |____________   |           |
            _________________   ___________   __________    ____      ____  ___________
                    |           |             |         |   |   \    /   |  |
                    |           |             |         |   |    \  /    |  |
                    |           |_________    |_________|   |     \/     |  |_________
                    |           |             |      \      |            |            |
                    |           |             |       \     |            |            |
                    |           |__________   |        \    |            |  __________|
        {}    {}
        '''.format(colored('Words and Definitions From Myers Psychology 10th Ed.', color='white'), colored('Made By: Aidan Evans', color='green', attrs=['bold'])), 
            color='cyan', 
            attrs=['bold'])  #Prints Title

        cprint(
        '''     
        1. View All Terms          3. Search Terms
        2. View Terms by Chapter   4. View Random Term
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
        1. View All Terms       2. View Terms by Chapter       3. Search Terms       4. View Random Term
        ''', color='magenta', attrs=['bold'])  #Prints Options

    choice = input('\n   Please Input a Number: ')

    if (choice == '1'): #View All Terms
        all_terms()
    elif (choice == '2'):   #View Terms by Chapter
        by_chapter()
    elif (choice == '3'):   #Search Input
        search_terms()
    else:
        menu()  #Else return to menu, i.e. restarts option input

def main():
    global term_definition
    global term_format
    global terms
    global term_format_long


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


    #term_definition.sort()    #Alphabetizes Terms-Definition list
    #terms.sort()    #Alphabetizes Terms list


    term_format_count = 0

    for element in term_format:     #Colors and bolds terms in term-definition pairs (Used for formated printed results)
        element = element.replace(terms[term_format_count], colored(terms[term_format_count], color='yellow', attrs=['bold']))
        term_format[term_format_count] = element
        term_format_count += 1


    term_format_long = []
    
    for element in term_format:     #Creates array for printing formatted results when window enlarged
        term_format_long.append(element.splitlines())


    try:
        menu()  #Loads menu interface
    except KeyboardInterrupt:
        menu()  #Loads menu when Ctrl+C pressed

main()