from functions import open_load, is_number, separators

# opening .txt file and converting to var 
text = open_load("testing_file.txt")
text2 = "Popo4catepetl21, tree82. Bautiful 24 5days. "
# defining var
word=""
min_length = 100000000
max_length = 0

#iterating through string 
for element in text2:
    if separators(element) or is_number(element):
        length = len(word)
        if length > max_length:
            max_length = length
            max_word = word
        if length < min_length and length > 0.1:
            min_length = length
            min_word = word
        word = ""
        continue    
    word += element

length = len(word)
if length > max_length:
    max_length = length
    max_word = word
if length < min_length and length > 0.1:
    min_length = length
    min_word = word

print(f"The longest word in the string: {max_word.lower()} (length: {max_length}).\n"
      f"The shortest word in the string: {min_word.lower()} (length: {min_length}).")
