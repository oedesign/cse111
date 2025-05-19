# Password Strength Checker
# Author: Elujoba Oluwaseyi Ebenezer
# Description:
# This program checks the strength of a password based on:
# - Length
# - Presence in common password lists
# - Presence in an English dictionary
# - Character variety (lowercase, uppercase, digits, symbols)
# Optional Enhancement:
# If the password is weak, the program suggests ways to improve it.

def word_has_character(word, character_list):
    for ch in word:
        if ch in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, "abcdefghijklmnopqrstuvwxyz"):
        complexity += 1
    if word_has_character(word, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        complexity += 1
    if word_has_character(word, "0123456789"):
        complexity += 1
    if word_has_character(word, "!@#$%^&*()-=_+[]{}|;:'\",.<>?/`~"):
        complexity += 1
    return complexity

def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False


def password_strength(password, min_length=10, strong_length=16):
    # Check if the password is in the dictionary file
    if word_in_file(password, "wordlist.txt"):
        print("That password is a word in the dictionary!")
        return 0

    # Check if the password is in the top passwords file
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("That password is on the list of most common passwords!")
        return 0

    # Check if the password is too short
    if len(password) < min_length:
        print("That password is too short!")
        return 1

    # Check if the password is very long and likely strong
    if len(password) > strong_length:
        print("That is a strong password due to its length.")
        return 5

    # Base score is 1 + complexity (0-4)
    complexity_score = word_complexity(password)
    total_score = 1 + complexity_score
    print(f"Complexity score: {complexity_score}, Total score: {total_score}")

    # Optional enhancement: Suggest improvement
    if total_score <= 2:
        print("Tip: Try adding a mix of uppercase letters, digits, and symbols to strengthen your password.")

    return total_score
# Main function to run the password strength checker
def main():
    while True:
        password = input("Enter a password (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        score = password_strength(password)
        print(f"Password Strength Score: {score}\n")

if __name__ == "__main__":
    main()
