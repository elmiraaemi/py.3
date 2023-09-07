import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
wrongs=[]
word = words[random.randint(0, len(words)-1)]
joon = (len(word)+3)
answer = []
w = []
for i in range(len(word)): answer.append('-')
for i in range(len(word)): w.append(word[i])
while joon > 0:
    for j in range(len(answer)):
         print(answer[j], end=' ')
    print("\nyour chances : " , joon )
    user_character = input("user_character: ").lower()
    if len(user_character)==1:
        if user_character in w:
            while user_character in w:
                answer[w.index(user_character)] = user_character
                w[w.index(user_character)] = ''
                print("your wrongs : ", wrongs)
            if '-' not in answer: break
        elif user_character not in w and user_character not in wrongs:
             joon -= 1
             wrongs.append(user_character)
             print("your wrongs : ", wrongs)
        elif user_character in wrongs:
            print("you have made this mistake before @_@")
            print("your wrongs : ", wrongs)
            print("\nyour chances : " , joon )
        elif user_character in w and user_character not in wrongs:
            print("you already typed this letter")
            print("your wrongs : ", wrongs)
            print("\nyour chances : " , joon )
    else :
        print("just one letter -_-")
if joon==0: 
    print("You lost that -~-")
else: 
    for j in range(len(answer)): print(answer[j], end=' ')
    print('\nyes , you won *.*')
    print('\nyes , you won *.*')
