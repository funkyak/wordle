##wordlists from https://www.nytimes.com/games/wordle/main.bfba912f.js

## Scrape word from https://yesterdayswordle.com/


with open("words1.txt","r") as words:
    contents = words.read()
    print(contents)

def search():
        lines = []
        with words:
            lines = words.readline()

        count = 0 
        for line in lines:
            count += 1
            print(f'line{count}: {line}')
            
search()