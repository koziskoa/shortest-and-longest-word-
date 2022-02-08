from tokenize import Number

def open_load (name):
    """opens .txt file
    - parametr needs name of file e.g. "file.txt"
    - returns content of file as str"""
    try:
        with open(name, encoding="utf-8") as file:
            reader = file.read()
        return reader
    except FileNotFoundError:
        print(f"Soubor {name} se nepodařilo najít.")
        exit()
    except PermissionError:
        print(f"Soubor {name} není programu přístupný.")
        exit()

def is_number (value): # můžu mít ve funkcích stejný název - value
    """Tries convert value to number
    - if number: returns True
    - if not number: returns False"""
    try:
        value = float(value)
        return(True)
    except ValueError:
        return(False)

def separators (val):
    """ Finds if value is separator
    - e.g. of separators: . , ? ! – : / " ' "space" etc.
    - if is separator: returns True"""
    sep = ['-', '.', ',', '?', '!', '–', ':', '/', '"', "'", ' ', '*',
           '(', ')', '[', ']', '{', '}', '<', '>', '°', '@']
    for i in sep:
        if i == val:
            return(True)
    return(False)