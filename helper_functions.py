import os

def clear():
    '''Clears command line screen'''
    os.system('cls' if os.name=='nt' else 'clear')

def input_n_clear(input_question):
    '''custom input function that takes user input and
       then clears command line'''
    response = input(input_question)
    clear()
    return response
