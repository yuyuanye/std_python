import random
'''
words = ('python','jumble','easy','c++','java','ruby','fortran','lisp','go')
word = random.choice(words)
print(word)
jumble = ''
while word:
    postion = random.randrange(len(word))
    jumble += word[postion]
    word = word[:postion] + word[postion+1:]
print('disorder word: ' + jumble)
'''
'''
print(random.random())
print(random.uniform(10,20))
print(random.uniform(20,10))
'''
import random as rd
'''
print(rd.randint(12,20))
print(rd.randint(20,20))
#print(rd.randint(20,10))
print(rd.randrange(10,200,2))
'''
'''
print(rd.choice('studypython'),end='\n======\n')
print(rd.choice(['python','jumble','easy','c++']),end='\n======\n')
print(rd.choice(('java','ruby','fortran','lisp')),end='\n======\n')
'''
words = ['python','jumble','easy','c++','java','ruby','fortran','lisp','go']
rd.shuffle(words)
print(words)