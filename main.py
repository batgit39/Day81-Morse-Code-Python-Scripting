import os
import pygame
import time

morse_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}


def play_morse(morse_code):
    pygame.mixer.init()
    audio_dot = pygame.mixer.Sound('./audio/-.mp3')
    audio_dash = pygame.mixer.Sound('./audio/--.mp3')

    for code in morse_code:
        print(code)
        for char in code:
            if char == '.':
                audio_dot.play()
                pygame.time.wait(int(audio_dot.get_length() * 1000))
                audio_dot.stop()
            else:
                audio_dash.play()
                pygame.time.wait(int(audio_dash.get_length() * 1000))
                audio_dash.stop()
            time.sleep(.5)


def get_users_morse_code():
    users_msg = input('Enter your message: ')
    users_morse_code = [morse_codes[char] for char in users_msg]
    print("Your Morse Code:")
    print(users_morse_code)
    return users_morse_code


def main():
    os.system('clear')
    users_morse_code = get_users_morse_code()
    user_input = input('Do you want to play audio? Y/N :').lower()
    if user_input == 'y':
        play_morse(users_morse_code)


while True:
    prompt = input("You want to get morse codes? Y/N: ").lower()
    if prompt != 'y':
        break

    main()
