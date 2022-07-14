import re

novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']

uniqueWordLength = []
novelWordList = []

for novelName in novels:
    file = open(novelName,encoding="utf8")
    fileRead = file.read()
    result=re.search(r'START OF',fileRead)
    startindex=fileRead.find('\n',result.end())
    result=re.search(r'END OF',fileRead)
    fread=fileRead[startindex:result.start()]
    stringline=re.sub(r"[^a-zA-Z]+", ' ',fileRead)
    temp =stringline.strip().split()
    novelWordList.append(temp)
    uniqueLength=len(set(temp))
    uniqueWordLength.append(uniqueLength)
    file.close()

maxIndex=uniqueWordLength.index(max(uniqueWordLength))
bestNovel=novelWordList[maxIndex]
bestNovelName=novels[maxIndex]

best=set(bestNovel)
totalWordsInAllNovel=set(bestNovel)

for novel in novelWordList:
    if bestNovel!=novel:
        best=set(best)-set(novel)
    totalWordsInAllNovel=set(totalWordsInAllNovel) & set(novel) 
    
fopen=open("Unique_Word_File.txt","w")
for word in list(best):
    fopen.write(word)
    fopen.write("\n")
fopen.close()

print("Name of Best Novel( Having Maximium Unique Word ) :",bestNovelName)
print("\nTotal Number of Words in Best Novel : ",len(bestNovel))
print("\nNo of Unique Words Best Novel Individually Have : ",max(uniqueWordLength))
print("\nNo of Unique Words of Best Novel by Comparing with All Novels :",len(best))
print("\nNo of Words Common in All Files :",len(totalWordsInAllNovel))