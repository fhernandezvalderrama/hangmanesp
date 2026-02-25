// Hangman Game Logic

const hangman = (word, maxAttempts) => {
    let attempts = 0;
    let guessedLetters = [];
    let wordStatus = Array(word.length).fill('_');

    const isGameOver = () => attempts >= maxAttempts;
    const isWordGuessed = () => !wordStatus.includes('_');

    while (!isGameOver() && !isWordGuessed()) {
        const guess = prompt(`Current word: ${wordStatus.join(' ')}\nGuess a letter:`);
        if (guessedLetters.includes(guess)) {
            console.log(`You've already guessed the letter: ${guess}`);
            continue;
        }

        guessedLetters.push(guess);
        if (word.includes(guess)) {
            word.split('').forEach((letter, index) => {
                if (letter === guess) {
                    wordStatus[index] = guess;
                }
            });
            console.log(`Good guess!`);
        } else {
            attempts++;
            console.log(`Wrong guess! Attempt ${attempts} of ${maxAttempts}`);
        }
    }

    if (isWordGuessed()) {
        console.log('Congratulations! You guessed the word: ' + word);
    } else {
        console.log('Game over! The word was: ' + word);
    }
};

// Example usage:
// hangman('javascript', 6);