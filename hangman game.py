#hangman game
import random 
# list of predefine words
words=[ "python","apple","computer"," school","program"]
# select a random word
word= random.choice(words)

guessed_letters=[]
wrong_guesses=0
max_wrong=6
print("welcome to hangman game!")
while wrong_guesses<max_wrong:
    display_word=""
    for letter in word:
        if letter in guessed_letters:
           display_word+="_"
    print("\n word:", display_word)
    if"_"not in display_word:
        print(" congratulations1you guessed the word:",word)
        break
    guess=input("enter a letter:").lower()
    if len (guess)!= 1or not guess.isalpha():
        print(" please enter a single  alphabate.")
        continue
    if guess in guessed_letters:
        print(" you already  guessed that letters.")
        continue
    guessed_letters.append("guess!")
    if guess in word:
        print("correct guess1")
    else:
        wrong_guesses+=1
        print(" wrong guess!")
        print(" remainning chances:",max_wrong-wrong_guesses)
if wrong_guesses==max_wrong:
    print("\n game over!")
    print("the correct word was:",word)

