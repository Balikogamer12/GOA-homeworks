secret = 7  
attempts = 3

while attempts > 0:
    guess = int(input("მოიხმე 1-დან 10-მდე რიცხვი: "))
    
    if guess == secret:
        print("You win!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong number. დარჩენილი ცდები:", attempts)
        else:
            print("You lose.")
