print("Bookbot analysis by Tilman Eichfelder")
words=0

def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    wdcount = Erbsenzähler(text)
  
    tokens=tokencount(text)

    print(f"The text contains {wdcount} words")
    tokenlist=list(tokens.items())
    tokenlist=sorted(tokenlist, reverse=True, key=lambda d: d[1])
    for i in tokenlist:
        print(f"The letter '{i[0]}' came up {i[1]} times.")


def get_book_text (path):
    with open(path) as f:
        return f.read()
    
def Erbsenzähler (text):
    words = text.split()
    return len(words)

def tokencount(text):
    countdict={}
    textlow=text.lower()
    for i in textlow:
        if i.isalpha()!=True:
            pass
        elif i not in countdict:
            countdict[i]=1
        else:
            countdict[i]+=1
    return countdict


        



main()

