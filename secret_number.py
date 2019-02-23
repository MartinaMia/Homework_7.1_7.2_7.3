secret = 7
                                                                    # int(input("user, guess the secret number between 1-10!"))
guess = int(input("user, guess the secret number between 1-10!"))   # Gewinnen: int(7)
                                                                    # Verlieren: int(10)

if guess == secret:
    print("CONGRATULATION! You win!")
else:
    print("I`m sorry, " + str(guess) + ", is wrong! TRY AGAIN")
