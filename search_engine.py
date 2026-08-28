import random
from time import perf_counter
import os 

##########################################################

##########################################################
global start 
global end 

def get_folder(get_directory):
    """
    a func that get folder from user and give files to file_reader function
    argumant:
            get_folder : like this -> 'c:/users/documents/saman/project:'
    return :
            give n files name of directory: like -> [file1, file2, file3, ... , file'n']
    """
    files_content = {}
    files = os.listdir('C:/Users/201/Documents/VS Code/tamrin e quera/project the last/dickens')
    for file in files:
        with open(file, 'r', encoding = 'utf-8', errors = 'ignore') as f:
            content = f.read()
            files_content[file] = content 
    return files_content
    


def  logic():
    """
    get functions and do the logic of program
    """
    query = user_get_input()
    ret = files_reader()
    final_results:list = query_filter(ret, query)
    board_and_render(query, final_results)


def user_get_input():
    """
    this function get input from user 
    argumet:
            none!
    
    return: 
            a string object: 'python' or 'child' or 'another string'
    
    """
    global start
    query = input("Please insert your search query :")
    start = perf_counter()
    return query


def files_reader():
    """
    get one or many text files and copy their content

    argument:
            a pack of files or function: file1.txt, file2.txt, . . . , filen.txt
    return:
            a dataset like this: data_list = 
            [{file1 : {Line {a}: {lines[i]}}}, {file2 : {Line {a}: {lines[i]}}}, {file3 : {Line {a}: {lines[i]}}}, ... , {file n : {Line {a}: {lines[i]}}}].
            it could be a combine of tuple and list and dictionary.
    """
    user_file_name_input = '98-0.txt'
    f = open(user_file_name_input, 'r', encoding = 'utf-8', errors = 'ignore')
    ordi = []
    lines_list = []
    char = f.read()
    lines = char.split('\n')
    for i in range(len(lines)-1):
        ordi.append([f'Line {i+1}' , lines[i].split()])
    return ordi



def query_filter(open_func, user_input):
    """
    a function that get string and sorted and filtered list and unzip that data and 
    check there is any query on result dataset list

    argument:
            a string: 'quera'
            a dataset list: [{file1 : [{line1 : ['hello', 'every', 'one', 'I', 'am', 'quera'] } ] } ] 
    return : 
            a list that have final rasults into a much smaller than dataset
    """
    global end 
    new_list = []
    for i in range(len(open_func)):
        a = open_func[i][1]
        for j in a:
            if user_input == j: # also we can use :'if user_input.lower() == j.lower()' for Not Sensitive to capital letters: and == And
                new_list.append(open_func[i])
                break
    end = perf_counter()
    return new_list


def board_and_render(user_input, final_results):
    """
    get show ten random result from final results with user-friendly, attractive and practical along
    with the name of the file and line and the number of searches found in the file and the  example text.
    and colored and into the box 

    argument:
            query : 'python' .
            final result list: a list with results
    return:
            file 1 , 'quera'
            line 13: ...there is quera a website for learn python...
             .
             .
             .
            and also we found 3413697 results more in 3.15 seconds

    
    """
    
    print('your input : ', user_input)
    if len(final_results) < 1 or len(final_results) == None:
        print(f'sorry!\twe found nothing  \nplease try again.')
    else:
        print(f'we found {len(final_results)} results : ')
        print(f'At {end - start} seconds !')
    n = len(final_results)
    for i in range(n):
        test = final_results[i]
        print(test[0], ':',end = '\t')
        for j in range(len(test[1])):
            a = test[1]
            print(a[j], end = ' ')
        print('\n')
    


def main():
    while True:
        state = input("if you want to start an search please insert 'y' otherwise insert 'n' .")
        if state == 'y':
            logic()
        elif state == 'n':
            print("bye! :)")
            break
        else:
            print("Invalid input !\nplease try again .")

main()