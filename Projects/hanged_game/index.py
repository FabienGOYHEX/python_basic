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

    if game['player_life'] == 1:
        print('you lose !')
        break
    elif new_word.count('_') == 1:
        print('you win')
        break
    elif index_of_match_letter != -1:
        new_word[index_of_match_letter] = letter
        game['starter_word'] = ''.join(new_word)
        print(game['starter_word'])
    elif index_of_match_letter == -1:
        game['player_life'] = game['player_life'] - 1
        game['starter_word'] = ''.join(new_word)
        print(game['starter_word'])
    else:
        break
