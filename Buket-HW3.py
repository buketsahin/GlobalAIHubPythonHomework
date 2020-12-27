import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['rainbow', 'storm', 'scientist', 'sunshine',
         'rabbit', 'pollution', 'honey', 'condition',
         'fashion', 'bird', 'expectation', 'atmosphere']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print(i)

        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")