import math
from collections import Counter

def password_generator(entropy_target: int, phrase: str, number: str)-> str:
    '''Generates a password based on the arguments given by the user '''

    words = phrase.split()
    initials = "".join(word[:5] for word in words) #obtain a string with the first letter of each word
    initials_with_sym = replace_letters_with_symbols(initials)
    capitalized_initials = capitilize_even_character(initials_with_sym)
    password = str(capitalized_initials) + number
    if entropy_test(password) < entropy_target:
        print('⚠ Warning: entropy too low, consider using a longer phrase or number.')
    return password

def replace_letters_with_symbols(initials: str)-> str:
    '''Replaces specific letters with symbols'''

    substitutions = {"c": "<", "s": "$", "o": "0", "e": "3", "i": "¡", "t": "+" }

    result = ""
    for character in initials:
        result += substitutions.get(character, character)

    return result

def capitilize_even_character(text: str)-> str:
    '''Capitalizes every even character in the string'''
    characters = list(text)

    for position, character in enumerate(characters):
        if position % 2 == 0:
            characters[position] = character.upper()

    return "".join(characters)

def valid_account_type()-> tuple[int, int]:
    '''Associates the use of the password with their minimun lenght and entropy target'''

    types = {'banking': 90, 'email': 70, 'gaming': 50, 'social media': 80}

    while True:
        pw_type = input("Whats your password for?(banking, email, gaming, social media): ").strip().lower()
        if pw_type in types:
            return types[pw_type]
        print("Invalid type. Please try again.")

def valid_phrase():
    '''Ensures the phrase entered by the user is valid based on the number of words'''

    while True:
        phrase = input("Enter a sentence (with at least 5 words): ").strip().lower()
        words = phrase.split()
        if len(words)>=5 and all(word.isalpha() for word in words):
            return phrase
        print("Invalid phrase. Please enter at least 5 words without numbers or symbols.")

def valid_num():
    '''Ensures the number entered by the user is valid based on its length and numeric content'''

    while True:
        number = input("Enter a number: ").strip()
        if number.isdigit() and len(number) >= 4:
            return number
        print("Invalid number. Please enter a numeric value with at least 4 digits.")

def entropy_test(password: str)-> float:
    '''Calculates the entropy of the password'''
    counts = Counter(password)
    total = len(password)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy * total


if __name__ == "__main__":
    while True:
        entropy_target = valid_account_type()
        phrase = valid_phrase()
        number = valid_num()

        password = password_generator(entropy_target, phrase, number)
        print("Your password is:", password)
        print("Entropy:", round(entropy_test(password), 2))

        while True:
            restart_program = input('Would you like to create another password? (y/n): ').lower()
            if restart_program in ("y", "n"):
                if restart_program == "y":
                    break
                else:
                    exit()
            else:
                print('Invalid input. Please write "y" (yes) or "n" (no).')
