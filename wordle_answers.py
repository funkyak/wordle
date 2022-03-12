with open("words1.txt","r") as words:
    contents = words.read()
    

def search():
        lines = []
        #file with word list 
        with open("words1.txt","r") as words:
            lines = words.readlines()
            
            #input yesterdays wordle
            Yesterdays_Wordle = input("Yesterdays Wordle: ")
            
            if Yesterdays_Wordle in contents:
                index = contents
                
                #letter 1
                next_word = index[index.index(Yesterdays_Wordle)+ 9]
                #letter 2
                next_word1 = index[index.index(Yesterdays_Wordle)+ 10]
                #Letter 3
                next_word2 = index[index.index(Yesterdays_Wordle)+ 11]
                #Letter 4
                next_word3 = index[index.index(Yesterdays_Wordle)+ 12]
                #Letter 5
                next_word4 = index[index.index(Yesterdays_Wordle)+ 13]
                #Output 
                print("Todays wordle is : "+ next_word + next_word1 + next_word2 + next_word3 + next_word4)
                
search()