import random
import string
from string import ascii_letters

length=3
chars=string.ascii_letters

text = input("Enter message")
words = text.split(" ")

coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      ran = ''.join(random.choice(chars) for i in range(length))
      ran1 = ''.join(random.choice(chars) for i in range(length))
      stnew = ran+ word[1:]+word[0]  + ran
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  