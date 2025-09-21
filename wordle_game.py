import random

def load_words(filename):
    with open(filename, "r") as f:
        return [word.strip().lower() for word in f if len(word.strip()) == 5]

def choose_word(words):
    return random.choice(words)

def get_feedback(guess, secret):
    feedback = []
    for i, letter in enumerate(guess):
        if letter == secret[i]:
            feedback.append("G")
        elif letter in secret:
            feedback.append("Y")
        else:
            feedback.append("X")
    return feedback

def play_game(words):
    secret = choose_word(words)
    attempts = 6
    for _ in range(attempts):
        guess = input("Enter a 5-letter word: ").lower()
        if guess not in words:
            print("Invalid word. Try again.")
            continue
        feedback = get_feedback(guess, secret)
        print(" ".join(feedback))
        if guess == secret:
            print("You win!")
            return
    print("You lose! The word was:", secret)

if __name__ == "__main__":
    words = load_words("words.txt")
    play_game(words)