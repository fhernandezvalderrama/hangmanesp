from mimetypes import inited



import random
import hangman_art
import hangman_palabras

lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_palabras.lista_palabras)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Palabra a adivinar: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print("****************************" + str(lives) + "/6 vidas restantes ****************************")
    guess = input("Elige una letra: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
            print("Esa letra" + str(guess) +" ya ha sido utilizada")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Palabra a adivinar: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print("La letra " + str(guess) + ", no esta en la palabra elegida. Pierdes una vida, te quedan " + str(lives))

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"*********************** HAS PERDIDO **********************")
            print("La palabra era " + chosen_word)

    if "_" not in display:
        game_over = True
        print("**************************** ENHORABUENA, GANASTE ****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
