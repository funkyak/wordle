##wordlists from https://www.nytimes.com/games/wordle/main.bfba912f.js

## Scrape word from https://yesterdayswordle.com/



from asyncio import create_subprocess_shell
import gettext



with open("words1.txt","r") as words:
    contents = words.read()
    

def search():
        lines = []
        with open("words1.txt","r") as words:
            lines = words.readlines()

                   
            Yesterdays_Wordle = input("Yesterdays Wordle:")
            
            
            if Yesterdays_Wordle in contents:
                print('Word found!')

               # today_wordle = Yesterdays_Wordle 
                def getNext(words):                
                    next_el = None
                    for index, elem in enumerate(contents):
                        for index, elem in enumerate(contents):
                            if index + 1 <len(contents) and index - 1 >= 0:
                                contents = elem - 1
                                if words == contents:
                                    next_el = contents[index]
                                    print(next_el)
                    return next_el
                print(gettext)
            getNext()

            

                    

            ## possible loop function needed to search through this. 
            
            #Todays_wordle = Yesterdays_Wordle + len(words + 1)
            

       
search()