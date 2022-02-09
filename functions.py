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