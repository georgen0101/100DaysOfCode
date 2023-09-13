# Day 26 - List Comprehension and the NATO Alphabet

## List Comprehension Syntax

```python
# new_list = [new_item for item in list]
```

## Python Sequences
- Strings
- Lists
- Tuples
- Range

## Challenges

### List Comprehension in Strings

```python
name = "Angela"
letters_list = [letter for letter in name]

# Output: ['A', 'n', 'g', 'e', 'l', 'a']
```

### List Comprehension with range()

```python
double_range = [n * 2 for n in range(1, 5)]
# Output: [2, 4, 6, 8]
```

## Conditional List Comprehension

```python
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
```

## NATO Alphabet

First attempt:
```python
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
with open("./nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)
    print(data)
    phonetic_dictionary = {row["letter"]: row["code"] for (index, row) in data.iterrows()}
    print(phonetic_dictionary)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
phonetic_list = [code for (key, code) in phonetic_dictionary.items() if key in user_word]  # Looped into the phonetic dict rather than the user word.
print(phonetic_list)
```

Obtained the desired output, but can be simplified.

Simplified version:

```python
import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")  # Read and create the DataFrame
# Create the dictionary
phonetic_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}  # Create the dictionary. List Comprehension

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()  # Upper because the letters from the dict are in upper case
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
```



