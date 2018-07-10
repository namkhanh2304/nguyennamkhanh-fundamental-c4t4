from random import choice
words = ["champion","dungeon",'vodka']
word=choice(words)
chars = list(word)
randoming=True
while randoming:
    rand_char = choice(chars)
    print(rand_char, end = ', ')
    chars.remove(rand_char)
    if len(chars)== 0:
        randoming = False

answer = input("your answer:")
while True:
    if answer==word:
        print("you win")
        break 
    else:
        print("again")
