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
                print("yor wrngs : ", wrongs)
            if '-' not in answer: break
        else:
             joon -= 1
             wrongs.append(user_character)
             print("yor wrngs : ", wrongs)
    else :
        print("just one letter -_-")
if joon==0: 
    print("You lost that -~-")
else: 
    for j in range(len(answer)): print(answer[j], end=' ')
    print('\nyes , you won *.*')
