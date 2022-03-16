import webbrowser
import time
from pynput.keyboard import Key, Controller


keyboard = Controller()

#Word list file (Same Directory as this script)
with open("words1.txt","r") as words:
    # changing the 
    contents = words.read()
    

def search():
     # Adding auto loader for yesterdays answer. Could use this for V3 
    with open("yesterdays.txt","r") as yesterdays:
        yesterdays = yesterdays.read()
        print("Yesterdays wordle is : "+ yesterdays)
  
     # https://www.delftstack.com/howto/python/python-overwrite-file/

     #input yesterdays wordle
    Yesterdays_Wordle = yesterdays
     #checking that the input is in the list
    if Yesterdays_Wordle in contents:
  #redundent change (Not needed)
        words = contents
  
  # Counts from input + 9,10,11,12,13 for the seperate letter of todays word. 
  # Index command breaks down words to number position
  #letter 1
  #scrapes the individual leters at a set distance ahead 
        next_word = words[words.index(Yesterdays_Wordle)+ 9]
  #letter 2
        next_word1 = words[words.index(Yesterdays_Wordle)+ 10]
  #Letter 3
        next_word2 = words[words.index(Yesterdays_Wordle)+ 11]
  #Letter 4
        next_word3 = words[words.index(Yesterdays_Wordle)+ 12]
  #Letter 5
        next_word4 = words[words.index(Yesterdays_Wordle)+ 13]
  #Output 
        today = next_word + next_word1 + next_word2 + next_word3 + next_word4
        print("Todays wordle is : "+ today)

        def previous():
            back1 = words[words.index(Yesterdays_Wordle)- 13]
            back2 = words[words.index(Yesterdays_Wordle)- 12]
            back3 = words[words.index(Yesterdays_Wordle)- 11]
            back4 = words[words.index(Yesterdays_Wordle)- 10]
            back5 = words[words.index(Yesterdays_Wordle)-9]
            previous = back1 + back2+ back3 + back4 + back5
            print("Previous wordle is :" + previous)
        

    else:
        #Prints Error Message
        print("Not Found")
    

    # Entering todays word on the website
    def Entering():
        time.sleep(2)
        #Working DO NOT change!!!!!!!
        time.sleep(.12)
        keyboard.press(next_word)
        keyboard.release(next_word)
        time.sleep(.12)
        keyboard.press(next_word1)
        keyboard.release(next_word1)
        time.sleep(.12)
        keyboard.press(next_word2)
        keyboard.release(next_word2)
        time.sleep(.12)
        keyboard.press(next_word3)
        keyboard.release(next_word3)
        time.sleep(.12)
        keyboard.press(next_word4)
        keyboard.release(next_word4)
        time.sleep(.12)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    

    def website():

        
        print ('1 -- Test website' )
        print ('2 -- Live Website' )
        # Live Website Loads new wordle into the text file 
        print ('3 -- Checking word' )
        print ('4 -- New word' )
        print ('5 -- Load yesterdays word')
        print ('6 -- Exit' )
        option = int(input('Enter your choice: ')) 

        if option == 1:
            print("Loading Test website")
            webbrowser.open('file:///C:/Users/Rory/Documents/wordle.html')
            
            Entering()


        elif option == 2:
            print("Loading Live Website")
            webbrowser.open('https://www.nytimes.com/games/wordle/index.html')
            Entering()

        elif option == 3:
            print(yesterdays)

        elif option == 4:
            with open('yesterdays.txt', "w") as today_wordle:
                today_wordle.write(today)
                print(today)
        
        elif option == 5:
            with open('yesterdays.txt', "w") as today_wordle:
                today_wordle.write(previous)
                print(previous)


        elif option == 6:
            #exit function
            print('BYE :-)')
            exit()

        else:
            #Error function
            print("Please enter between 1 - 3")

        time.sleep(3)
        
    website()

search()