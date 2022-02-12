def open_load (name):
    """opens .txt file
    - parametr needs name of file e.g. "file.txt"
    - returns content of file as str
    - """
    try:
        with open(name, encoding="utf-8") as file:
            reader = file.read()
        return reader
    except FileNotFoundError:
        print(f"File {name} not found")
        exit()
    except PermissionError:
        print(f"no permission to the file {name}")
        exit()

def is_number (value): 
    """Tries convert value to number
    - if number: returns True
    - if not number: returns False"""
    try:
        value = int(value)
        return(True)
    except ValueError:
        return(False)

def separators (val):
    """ Finds if value is separator
    - e.g. of separators: . , ? ! – : / " ' "space" etc.
    - if is separator: returns True"""
    sep_list = ['-', '.', ',', '?', '!', '–', ':', '/', '"', "'", ' ', '*', '#'
           '(', ')', '[', ']', '{', '}', '<', '>', '°', '@', '+', ';', '=', '%']
    for separator in sep_list:
        if separator == val:
            return(True)
    return(False)

def min_max_str (str):
    """ Finds the shortest and longest length in string
    - returns word and length of the shortest word in string
    - returns word and length of the longest word in string"""
    data = str
    word = ""
    min_length = 100000
    max_length = 0
    # iterrating trough string
    for element in data:
        if separators(element):
            length = len(word)
            if length > max_length:
                max_length = length # the highest number of characters in a word
                max_word = word
            if length < min_length and length > 1:
                min_length = length
                min_word = word
            word = ""
            continue
        if is_number(element):
            continue
        word += element

    length = len(word)
    if length > max_length:
        max_length = length
        max_word = word
    if length < min_length and length > 1:
        min_length = length
        min_word = word
    return (min_length, min_word, max_length, max_word)