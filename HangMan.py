import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
word = words[random.randint(0, len(words)-1)]
joon = (len(word)+2)
answer = []
for i in range(len(word)): answer.append('-')
w = []
for i in range(len(word)): w.append(word[i])
while joon > 0:
    for j in range(len(answer)):
         print(answer[j], end=' ')
    print("your chances : " , joon )
    user_character = input("user_character: ").lower()
    if user_character in w:
        while user_character in w:
            answer[w.index(user_character)] = user_character
            w[w.index(user_character)] = ''
        if '-' not in answer: break
    else: joon -= 1
if joon==0: 
    print("You lost that -_-")
else: 
    for j in range(len(answer)): print(answer[j], end=' ')
    print('yes , you won *.*')