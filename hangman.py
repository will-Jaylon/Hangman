import random

def choose_word():
    user_word = input("\nEnter the word for the game: ").lower()
    return user_word

def display_word(word, guessed_letters):
    display = ''
    for i in word: 
        if i in guessed_letters:
            display += i
        else:
            display += '_'
    return display
def hangman():
    print("Welcome to Hangman!")

    word_guess = choose_word()
    guessed_letters = []
    user_max_attempts = input("Enter the max number of attempts: ")
    max_attempts = int(user_max_attempts) if user_max_attempts.isdigit() else 6

    attempts_left = max_attempts

    while attempts_left > 0:
        current_display = display_word(word_guess, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue
        if guess in guessed_letters:
            print("you have already guessed that. Try again")
            continue

        guessed_letters.append(guess)

        if guess not in word_guess:
            attempts_left -= 1
            print(f"Incorrect guess! {attempts_left} {'guesses' if attempts_left != 1 else 'guess'} left")

        if '_' not in display_word(word_guess, guessed_letters):
            print(f"\nCongrats! You guessed the word: {word_guess}")
            break
    if '_' in display_word(word_guess, guessed_letters):
        print(f"\nSorry, you ran out of attempts. The word was: {word_guess}")

if __name__ == "__main__":
    hangman()