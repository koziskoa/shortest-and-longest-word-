from functions import open_load, is_number, separators

# opening .txt file and converting to var 
text = open_load("testing_file.txt")
text2 = "Popo4catepetl21, tree82. Bautiful 24 5days. "

# defining var
word=""
min_length = 100000000
max_length = 0

#iterating through string Poznámka:  
for element in text2:
    if separators(element):
        length = len(word)
        if length > max_length:
            max_length = length
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
print(f"The longest word in the string: {max_word.lower()} (length: {max_length}).\n"
      f"The shortest word in the string: {min_word.lower()} (length: {min_length}).")

"""comment CZ:
- když je urpostřed stringu číslo,  tak se nepočítá, ale písmena za číslem se počítají k předchozímu slovu
- algoritmus neumí více stejně dlouhých nejktaších nebo nejdelších slov
- nepočítá čísla jako slovo
nejdelší slovo:
    - v tomto příadě je za slovo považován řetězec složený čistě z písmen
    - pokud se v řetězci vyskytne číslice, nebude se do slova počítat
        - tedy u řetězce tree82 bude algoritmus počítat jako slovo jenom tree
    - pokud bude v řetězci zapsaná emailová adresa a její název bude mít největší 
      počet znaků, pak bude jméno adresy počítáno za nejdelší slovo
nejkratší slovo:
    - v tomto algoritmu považováno slovo, které se zkládá minimálně ze dvou znaků
    - slova složená z jednoho písmene jsou jednoduše okem vyhledatelná
    - pokud tedy bude uživatele zajímat nejkratší jednoznakové slovo, může si ho celkem jednoduše dohledat
    - zatímco slova ze dvou znaků už mohou být složitěji hledatelná, proto je tento algoritmus nastaven takto"""