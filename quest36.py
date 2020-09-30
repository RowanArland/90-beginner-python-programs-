WordListsize = int(input("Enter the size of the word List:"))
wordList = list()
temp = list()
for i in range(0,WordListsize):
    wordList.append(input("Enter Item:"))
count = 0
def listSize(WordListsize,wordList,count):
    for j in range(0,WordListsize):
         if len(wordList[j]) >= 5:
             count = count + 1
             temp = wordList[j]
             print("Word greater than 5 letters:",temp)
    print("No of word greater than 5 is :",count)
listSize(WordListsize,wordList,count)
