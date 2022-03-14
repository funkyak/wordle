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
        with open('yesterdays.txt', "w") as today_wordle:
            today_wordle.write(today)
        time.sleep(1)

    else:
        #Prints Error Message
        print("Not Found")

    def website():
        print("Now opening website to enter word")
        time.sleep(1.5)
        #opening the TEST website
        webbrowser.open('file:///C:/Users/Rory/Documents/wordle.html')
        time.sleep(3)
    website()

  # Entering todays word on the website
    def Entering():
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
        
    Entering()
search()