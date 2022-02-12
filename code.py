"""Shortest and longest word in text
   - text is given in .txt file (variable text) or as string (variable text2)
   - difficulty: 4 """
from functions import open_load, min_max_str

# opening .txt file and converting to var 
text = open_load("testing_file.txt")
text2 = "Popo4catepetl21, tree82. Bautiful 24 5days. "

f_words = min_max_str(text)

print(f"The longest word in the string: {f_words[3].lower()} (length: {f_words[2]}).\n"
      f"The shortest word in the string: {f_words[1].lower()} (length: {f_words[0]}).")

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