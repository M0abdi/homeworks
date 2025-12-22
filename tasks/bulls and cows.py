import random

def main():
    
    digits = list('123456789') + ['0']
    secret = ''.join(random.sample(digits, 4))
    print(secret)
    
    print("Bulls and Cows Game!")
    print("Guess my 4-digit number (all digits unique)")
    print("Bulls = correct position, Cows = wrong position")
    
    attempts = 0
    
    while True:
        guess = input("\nYour guess: ").strip()
        attempts += 1
        
    
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid! Enter 4 unique digits.")
            continue
        
        
        bulls = sum(1 for i in range(4) if guess[i] == secret[i])
        cows = sum(1 for d in guess if d in secret) - bulls
        
        if bulls == 4:
            print(f"Correct! You won in {attempts} attempts!")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")

if __name__ == "__main__":
    main()
