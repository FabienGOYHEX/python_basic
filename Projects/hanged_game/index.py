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

new_word = list(game['starter_word'])
while True:
    print(f"| vies : {game['player_life']}")
    letter = input("? => ")
    index_of_match_letter = secret_word.find(letter)
    if index_of_match_letter != -1:
        new_word[index_of_match_letter] = letter
        print(str(new_word))
"""
    #for i in secret_word:
        comparative_word_letter = i
        if comparative_word_letter == letter:
            print('yeah')
        elif comparative_word_letter != letter:
            player_life += 1
        else:
            print("C'est faux !")
"""
