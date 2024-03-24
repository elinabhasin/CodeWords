import random
import string

message=input("Enter your message : ")
words=message.split()

encodedstr=""
charlst=[]
encodedlst=[]

#Encoding
for word in words:
    
    if(len(word)<3):
        newWord=word[::-1]
        encodedlst.append(newWord)

    else:
        charlst=[char for char in word]
        charlst.append(charlst[0])
        charlst.pop(0)
        for i in range(0,3):
            rand=random.choice(string.ascii_letters)
            charlst.insert(i,rand)
        for i in range(1,4):
            rand=random.choice(string.ascii_letters)
            charlst.append(rand)
        
        # for i in charlst:
        #     encodedstr=i+encodedstr
        encodedstr=''.join(charlst)
        encodedlst.append(encodedstr)
    
encodedstr=' '.join(encodedlst)
print(f"Encoded message : {encodedstr}")

#Decoding

decodedlst=[]
Words=[]
decodedstr=''
Words=encodedstr.split()

for word in Words:

    if(len(word)<3):
        neword=word[::-1]
        decodedlst.append(neword)

    else:
        nword=word[3:len(word)-3]
        nword=nword[len(nword)-1]+nword[0:len(nword)-1]
        decodedlst.append(nword)

decodedstr=' '.join(decodedlst)
print(f"Decoded message : {decodedstr}")