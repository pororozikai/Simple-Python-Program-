import random
import time

print("\n Selamat datang di game hangman \n")
name = input ("Silahkan masukan nama anda : ")
print ("Hello {} Welcome to The Game".format(name))
time.sleep(1)
load = ["L", "O", "A", "D", "I", "N", "G", ".", ".", "."]
for i in load:
    print (i, end=" ")
    time.sleep(1)
print("\n Prepare your soul")

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["ikan","kucing","anjing","paus","kera","gorila","singa"]

    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_ ' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["Y", "n", "y", "N"]:
        play_game = input ("Do you want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print ("Thanks FOr Playing!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid Input, Try a letter\n")
        hangman()

    
    
