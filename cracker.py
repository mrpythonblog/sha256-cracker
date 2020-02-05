import hashlib

def checkHash(hash,word):
    #print(word)
    obj = hashlib.sha256()
    obj.update(word.encode())
    h = obj.hexdigest()
    if h == hash:
        return True
    return False


dic = input("Dictionary : ")
hash = input("hash : ")

f = open(dic,"r")
words = f.readlines()

for i in range(len(words)):
    words[i] = words[i].strip("\n")
state = False
correct = ""
for word in words:
    if checkHash(hash,word):
        state = True
        correct = word
        break

if state:
    print ("Hash Cracaked !")
    print ("{} : {}".format(hash,correct))
    exit()
    
else:
    print ("Sorry ! . I Can't Crack Your Hash :(")
    exit()

