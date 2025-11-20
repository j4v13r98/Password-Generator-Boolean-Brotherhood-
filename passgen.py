import math
from collections import Counter

def password_generator(context:str, phrase: str, number: str)-> str:
    '''
    Generate a password based on the arguments given by the user
    '''
    min_lengt, entropy_target = account_type(context)
    words = phrase.split()
    initials = "".join(word[0] for word in words) #obtain a string with the first letter of each word
    initials_with_sym = replace_letters_with_symbols(initials)
    capitalized_initials = capitilize_2rd_character(initials_with_sym)

    password = str(capitalized_initials) + number
    
    while entropy_test(password) < entropy_target:
        password = password #por poner algo
    return password

def replace_letters_with_symbols(initials: str)-> str:
    '''
    Replace specific letters to a symbol
    '''
    substitutions = {
        "a": "@", "s": "$", "o": "0", "e": "3", "i": "¡", "t": "+"
    }

    result = ""
    for character in initials:
        result += substitutions.get(character, character)

    return result

def capitilize_2rd_character(text: str)-> str:
    characters = list(text)

    for position, character in enumerate(characters):
        if position % 2 == 0:
            characters[position] = character.upper()

    return "".join(characters)

def account_type(text: str)-> tuple:
    '''
    Associates the use of the password with their minimun lenght and entropy target
    '''
    types = {'banking': (20, 90), 'email': (16, 70), 'gaming': (12, 50), 'social media': (18, 80),}
    
    while text not in types:
        text = input("Whats your password for?(banking, email, gaming, social media)")

    return types.get(text)

def entropy_test(text: str)-> int:
    counts = Counter(text)
    total = len(text)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy


if __name__ == "__main__":
    context = input("Whats your password for?(banking, email, gaming, social media)")
    phrase = input("Enter a sentence: ").strip().lower()
    number = input("Enter a number: ").strip()
    print("Your password is: ", password_generator(context, phrase, number))