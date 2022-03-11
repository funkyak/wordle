##wordlists from https://www.nytimes.com/games/wordle/main.bfba912f.js

## Scrape word from https://yesterdayswordle.com/



with open("words1.txt","r") as words:
    contents = words.read()
    

def search():
        lines = []
        with open("words1.txt","r") as words:
            lines = words.readlines()

                   
            Yesterdays_Wordle = input("Yesterdays Wordle:")
            
            
            if Yesterdays_Wordle in contents:
                print('Word found!')
            


            
            else:
                print("Fail")

            # loop didnot work 
            

            ## possible loop function needed to search through this. 
            
            #Todays_wordle = Yesterdays_Wordle + len(words + 1)
            #print("Todays_wordle")
            ##print(f'line{count}: {line}')
            ## not jumping to the new lines always line 1
            

       
search()