text=(input("Enter a sentence "))
text=text.split()
bigword=0
for word in text:
    wordlen=len(word)
    if wordlen>bigword:
        bigword=wordlen
for word in text:
    wordlen=len(word)
    if wordlen==bigword:
        print("The biggest word is ",word)
