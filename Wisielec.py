# This is Hangman game. Computer randomly picks a word, and player needs to
# guess what is the word. The player also has to guess the word before
# hangman is completely drawn.
# Check also flowchart.pdf for more info.

from random import randint
from hangs import HANGMAN_PICS # import rysunku wisielca

def main():
    gameEnd = False

    while gameEnd == False:
        playGame()

        # Zapytanie o ponowną grę
        while True:
            decision = input('Chciałbyś zagrać jeszcze raz? (tak czy nie): ').lower()
            if decision == 'tak':
                break
            if decision == 'nie':
                gameEnd = True
                break

def playGame():
    ''' Zagraj w wisielca '''
    # Wartości początkowe
    secretWord = pick_word()
    guessedLetters = ['_'] * len(secretWord)
    wrongLetters = ''

    print('\n' * 2 + 'H A N G M A N')

    while True:
        print('\n' + 'Ukryte słowo: ' + ' '.join(guessedLetters).capitalize())
        print('Niepoprawne litery: ' + ' '.join(wrongLetters))
        print(HANGMAN_PICS[len(wrongLetters)])

        # Sprawdzenie statusu wygranej lub przegranej
        if ''.join(guessedLetters).isalpha():
            print('Wygrałeś! :]')
            break
        if len(wrongLetters) >= len(HANGMAN_PICS) - 1:
            print('Spróbuj jeszcze raz! :(. Ukrytym słowem było: {}'.format(secretWord.title()))
            break

        inputLetter = getLetter()

        # Spawdź czy gracz zgadł literę
        if inputLetter in secretWord:
            for charNum in range(len(secretWord)):
                if inputLetter == secretWord[charNum]:
                    # Add letter to guessed letters
                    guessedLetters[charNum] = inputLetter
        # Sprawdź czy gracz użył już tej litery
        elif inputLetter in wrongLetters:
            print('Zdążyłeś jużuzyc tej litery!')
        # W przeciwnym razie doda do niewłaściwych liter
        else:
            wrongLetters = wrongLetters + inputLetter

def getLetter():
    '''
    Gets letter from user as input and validates if the input
    is actually a letter.
    '''

    while True:
        letter = input('Zgadnij literę: ')
        if len(letter) == 1 and letter.isalpha() == True:
            return letter.lower()


def pick_word():
    '''
    Stworzenie listy słów z minimum 4 literami z pliku tekstowego.
    '''

    filePath = 'words.txt'
    file = open(filePath, 'r')
    words = []

    # słowa z minimum 4 literami
    for line in file:
        line = line.rstrip('\n')
        if len(line) >= 4:
            words.append(line.lower())

    file.close()

    # Losowanie słów z listy
    word = words[randint(0, len(words))]
    return word

if __name__ == '__main__':
    main()
