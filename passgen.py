def password_generator(phrase: str, number: str)-> str:
    '''
    Generate a password based on the arguments given by the user
    '''
    words = phrase.split()
    initials = "".join(word[0] for word in words) #obtain a string with the first letter of each word
    initials_with_sym = replace_letters_with_symbols(initials)
    capitalized_initials = capitilize_2rd_character(initials_with_sym)

    return str(capitalized_initials) + number

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


if __name__ == "__main__":
    phrase = input("Enter a sentence: ").strip().lower()
    number = input("Enter a number: ").strip()
    print("Your password is: ", password_generator(phrase, number))