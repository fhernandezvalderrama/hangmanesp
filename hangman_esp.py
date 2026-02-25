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

    print("****************************" + str(lives) + "/6 vidas restantes ****************************")
    guess = input("Elige una letra: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, skip processing
    if guess in correct_letters:
        print("Esa letra " + str(guess) + " ya ha sido utilizada")
        continue  # ADD THIS LINE to skip the rest of the loop
    
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

    if guess not in chosen_word:
        lives -= 1
        print("La letra " + str(guess) + ", no esta en la palabra elegida. Pierdes una vida, te quedan " + str(lives))

        if lives == 0:
            game_over = True
            print(f"*********************** HAS PERDIDO **********************")
            print("La palabra era " + chosen_word)

    if "_" not in display:
        game_over = True
        print("**************************** ENHORABUENA, GANASTE ****************************")

    print(hangman_art.stages[lives])