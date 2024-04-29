import random

def getWords():
    wordlist = []  
    words = open("words.txt", "r").read().splitlines()
    return words
    
def main():
    wordplist = []
    words = getWords()
    wordcount = input("text length: ")
    for i in range(int(wordcount)):
        wordplist.append(random.choice(words))
    wordpara = " ".join(wordplist)
    print(wordpara)
    print("\ntext generated")
    
main()