print('''
_______________
|𝓣𝓮𝔁𝓽 𝓽𝓸 𝓜𝓸𝓻𝓼𝓮 |
|𝓒𝓸𝓭𝓮 𝓬𝓸𝓷𝓿𝓮𝓻𝓽𝓮𝓻 |
|_______________|

''')
'@#$%^&*()'
# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' ', ',': '--..--',
                   '!': '-.-.--',
                   }


def converter(message):
    unsupported_Character = []
    res = ""

    for i in message:
        if i in MORSE_CODE_DICT:
            res += MORSE_CODE_DICT[i]
        else:
            unsupported_Character.append(i)

    print(f"Result: {res}")
    print(f'Unsupported Characters : {unsupported_Character}')
    print("_______________________________________________________")


text = input("Enter your text : \n").upper()
converter(text)
