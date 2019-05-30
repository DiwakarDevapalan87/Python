low = 0
high = 100
while True:
    x = (low + high)//2
    print("Is your secret number " + str(x) + "?")
    y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y == 'h':
        high = x
    elif y == 'l':
        low = x
    elif y == 'c':
        print("Game over. Your secret number was: " + str(x))
        break
    else:
        print("Sorry, I did not understand your input.")
