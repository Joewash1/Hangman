import time
name= input("Please enter your name.")
class Hangman():
    name= input("Please enter your name.")
    def __init__(self):
        print ("Welcome to 'Hangman'" +name,", are you ready to die?")
        print ("(1)Let's get playing \n(2)No, get me outta here!")
        user_choice_1 = input("->")
        if user_choice_1 == '1':
            print ("Loading all things evil. Pleas wait why we load your destiny.")
            self.start_game()
            time.sleep(2)
        elif user_choice_1 == '2':
            print ("Until next time.....")
            time.sleep(2)
            exit()
        else:
            print ("Already messing up I see. Please select a valid option.")
            self.__init__()
            time.sleep(2)

    def start_game(self):
        print ("The games about to begin. Let's go over the rules, shall we?")
        print ("Okay, first things first, you have come to challenge your life")
        print ("You will try to guess what word we have in store for you. Sounds easy right?")
        print ("Not right. You will guess till either you win your life back")
        print ("or you die.")
        time.sleep(5)
        print ("Now lets get started")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print ("GO")
        self.main_part_of_game()

    def main_part_of_game(self):
        guesses = 0
        letters_used = ""
        the_word = "knife"
        progress = ["?", "?", "?", "?", "?"]
        while guesses < 6:
            
            if guess in the_word:
                print ("Somehow your guess was RIGHT!")
                letters_used += "," + guess
                self.hangm_The_actual_graphic(guesses)
                print ("Progress: " + self.progress_updater(guess, the_word, progress))
                print ("Letter used: " + letters_used)
                if progress == 'knife':
                    print("CONGRATS You spared your life")
                    self.__init__()
            else:
               print ("GAME OVER!")
               self.__init__() 
            
             guess not in the_word :
                guesses += 1
                print ("Things aren't looking so good, that guess was WRONG!")
                print ("Too bad. I thought you would at least try to make")
                print ("this somewhat interesting.")
                letters_used += "," + guess
                self.hangm_The_actual_graphic(guesses)
                print ("Progress: " + "".join(progress))
                print ("Letter used: " + letters_used)
                
            else:
                print ("That's the wrong letter, you wanna be out here all day?")
                print ("Try again!")
                guesses += 1
                self.hangm_The_actual_graphic(guesses)
    def hangm_The_actual_graphic(self, guesses):
        if guesses == 0:
            print ("________      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")

        elif guesses == 1:
            print ("________      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            
        elif guesses == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /       ")
            print ("|             ")
            
        elif guesses == 3:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|      ")
            

        elif guesses == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            
        elif guesses == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
        
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("The string tightens around your neck, and you feel the")
            print ("sudden urge to pass out")
            print ("GAME OVER!")
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1
        return"".join(progress)

game = Hangman()




		      	   

