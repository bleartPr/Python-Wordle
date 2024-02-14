import random
import Python2nd


# generate a random 5-letter word
def random_word_generator():
    word = random.choice(Python2nd.words) 
    if len(word) == 5:
        return word 

# if player wins this happens
def winner_message(word):
    print(f"YOU GOT IT! the word was {word}!")

# check if input valid. here True means that the input is not an alphabet or not a 5 letter word
def user_input_error_handling(input, word):
    if len(input) != 5 or not input.isalpha():
        print("Please enter only 5-letter alphabetical real words.")
        return True
    if input not in word:
        print("Please enter only 5-letter alphabetical real words.")
        return True
    return False

# when player wins this gives the option for the player to play again
def play_again():
    response = str(input("want to play again?(yes/no): ")).lower()
    if response == "yes":
        play_game()
    else:
        return True
    return False

# green and yellow letters displaying algorythm
def line_and_letters_display_algo(input_str, random_word, display):
    display = list(display)
    display_yellow = []
    yellow_candidates = set()
    for i in range(5):

        if input_str[i] == random_word[i]:
            display[i] = input_str[i]
        else:
            if input_str[i] in random_word:
                yellow_candidates.add(input_str[i])

    for i in yellow_candidates:
        display_yellow.append(f' "{i}" IS YELLOW')
    return "".join(display), display_yellow

# this is the logic of the game and starts it
def play_game():
    the_random_word = random_word_generator()
    the_display = len(the_random_word) * "-"
    while True:
        user_guess = str(input("type a 5 letter word: "))
        
        if user_input_error_handling(user_guess, Python2nd.words):
            continue
        
        if user_guess == the_random_word:
            winner_message(the_random_word)
            if play_again() == True:
                break
        
        else:
            the_display, yellow_storage = line_and_letters_display_algo(user_guess, the_random_word, the_display)
            print("green words: ", the_display)
            print("".join(yellow_storage))

# start the game when file is ran
def main():
    play_game()

if __name__ == "__main__":
    main()