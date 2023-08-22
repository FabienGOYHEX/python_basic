import random
# Define the word randomly
words = "chien chat souris lapin cheval vache poule pigeon ours lion"
words_list = words.split()
secret = random.randint(0, len(words_list)-1)

secret_word = words_list[secret]
# Define the game
game = {
    "secret_word": secret_word,
    "starter_word": "_" * len(secret_word),
    "player_life": 9
}
print(secret_word.split())

print(f"{game['starter_word']} | vies : {game['player_life']}")

while True:
    print(f"| vies : {game['player_life']}")
    letter = input("? => ")
    comparative_word_letter = ""
    player_life = game['player_life']
    for i in secret_word:
        comparative_word_letter = i
        if comparative_word_letter == letter:
            print('yeah')
        else:
            player_life = player_life - 1

    print(letter)
