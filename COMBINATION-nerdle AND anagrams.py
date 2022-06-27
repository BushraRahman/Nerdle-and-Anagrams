import time
import random

potential_words = [("bury","ruby"),("ape","pea"),("idea","aide"),("are","ear"),("iceman","cinema"),("secure","rescue"),("angel","glean"),("triangle","integral"),("wed","dew"),("bake","beak"),("Geneva","average"),("sales","seals"),("rinse","siren"),("fringe","finger")]
choices = ["5*7-30=5", "3/7*21=9", "8*4-1=31","96-43=53", "14*1/2=7", "114/57=2","3*45=135","35-16=19"]
green = "\x1b[1;32;42m"
cyan = "\x1b[1;36;46m"
grey = "\x1b[1;30;47m"
print(green + "color" + '\x1b[0m')
def begin():
    print("Enter 'E' for the equations game, 'A' for anagrams, and 'I' for info.")
    game_choose = input("").strip().upper()
    if game_choose == 'E':
        nerdleplay_game()
    elif game_choose == 'A':
        anagrambegin_game()
    elif game_choose == 'I':
        info()

def anagrambegin_game():
    print("Enter 'T' for timer mode or 'C' for continous mode. Enter 'I' for info. Enter 'Q' at any time to quit game.")
    game_mode = input("")
    if game_mode.strip() != "t" and game_mode.strip() != "c" and game_mode.strip() != "T" and game_mode.strip() != "C" and game_mode.strip() != "I" and game_mode.strip() != "i" and game_mode.strip().upper() != 'Q':
        print("Enter T, C, or I.")
    elif game_mode.strip().upper() == "I":
        info()
    elif game_mode.strip().upper() == "Q":
        begin()
    else:
        modified_words = potential_words
        anagramplay_game(game_mode, modified_words)
        
def anagramplay_game(game_mode, modified_words):
    start = time.time()
    while True:
        pair = random.choice(modified_words)
        print(pair[0].upper())
        wordguess = input("").strip()
        end = time.time()
        if game_mode == "t".strip() or game_mode == "T".strip():
            if end - start >= 30:
                print("Time's up! You completed " + str(len(potential_words) - len(modified_words)) + " anagrams!")
                break
        if wordguess.lower() == pair[1]:
            print("Success!")
            modified_words = [rest for rest in modified_words if rest != pair]
        elif wordguess.upper() == "Q":
            begin()
            break
        else:
            print("Failure!")
            if game_mode == "c".strip() or game_mode == "C".strip():
                print("You completed " + str(len(potential_words) - len(modified_words)) + " anagrams in " + str(int(end - start)) + " seconds!")
            break
        if len(modified_words) == 0:
            print("Wow! You beat all " + str(len(potential_words)) + " anagrams!! It took " + str(int(end - start)) + " seconds.")
            break
    anagrambegin_game()

def check_input():
    while True:
        guess = input("Equation: ").strip()
        if guess.upper() == "Q":
            begin()
        index = guess.find("=")
        status = "good"
        for x in guess:
            if x > "9" and x != "=" and x != "-" or x < "*" or x=="," or x=="." or index == -1:
                print("Input an equation with acceptable characters.")
                status = "bad"
        if guess.count("=") > 1:
            print("Only one '=' allowed!")
            continue
        elif len(guess) != 8:
            print("Input exactly 8 characters.")
            continue
        for x in guess[index + 1:]:
            if x != "-" and x < "0" and x > "9":
                print("The right side must be a number, not an expression.")
                status = "bad"
        try:
            if eval(guess[:index]) != float(guess[index + 1:]):
                print("Enter a true equation.")
                continue
        except (ValueError, SyntaxError):
            print("Input an acceptable equation. No leading zeros allowed.")
            continue
        if status == "bad":
            continue
        return list(guess)
    
def evaluate_input(guess, equation):
    modified_input = list(''.join(guess))
    modified_equation = equation
    for index, element in enumerate(guess):
        if guess[index] == equation[index]:
            modified_input[index] = green + guess[index] + '\x1b[0m'
            modified_equation = modified_equation.replace(element, '',1)
    for index, element in enumerate(guess):
        if element in modified_equation:
            modified_input[index] = cyan + guess[index] + '\x1b[0m'
            modified_equation = modified_equation.replace(element, '',1)
    for index, element in enumerate(modified_input):
        if element in guess:
            modified_input[index] = grey + modified_input[index] + '\x1b[0m'
    print(''.join(modified_input))
    if ''.join(guess) == equation:
        return "done"
    
def nerdleplay_game():
    while True:
        print("Enter 'I' for info. Enter 'Q' at any time to quit game. Enter 'S' to start.")
        nerdleanswer = input("").strip().upper()
        if nerdleanswer == 'I':
            info()
        elif nerdleanswer == 'Q':
            begin()
        elif nerdleanswer == "S":
            equation = random.choice(choices)
            guesses = 6
            while True:
                a = evaluate_input(check_input(), equation)
                guesses = guesses - 1
                if guesses == 0 or a == "done":
                    break
            if guesses == 0:
                print("The answer was " + "\x1b[1;30;47m" + equation + '\x1b[0m')
            else:
                print("You got the answer right!")
        else:
            print("Enter the letter S, I, or Q with no quotation marks.")
def info():
    print("Equations: ")
    print("   Goal: Within 6 tries, enter an equation with 8 characters that is exactly the same as the secret chosen equation.")
    print("   The accepted characters are the numbers 1-9,+,-,/, *, and =. No decimals allowed.")
    print("   The left side of the equation must have at least one operation.")
    print("   The right side has no operations.")
    print("   " + green + " " + '\x1b[0m' + "is a correct character in the right spot.")
    print("   " + cyan + " " + '\x1b[0m' + "is a correct character in the wrong spot.")
    print("   " + grey + " " + '\x1b[0m' + "is a wrong character or your guess has more of that character than the solution.")
    print("Anagrams: ")
    print("   The goal is to enter the anagram of the word given. In timer mode, there's a 30 second time limit. There is no time limit in continuous.")

while True:
    begin()
        
