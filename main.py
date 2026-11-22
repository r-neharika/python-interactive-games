import random 
import pickle
import os



def ask_question(question):
    while True:
        print(question)
        answer = input("Enter A or B: ").strip().upper()

        if answer in ["A", "B"]:
            return answer

        print("Invalid input. Please enter A or B.")

def get_user_answers():
    questions = [
        "1. After a long day, what makes you feel better?\nA) Hanging out with people.\nB) Being alone.",
        "2. In group projects, do you usually:\nA) Share ideas with others.\nB) Work quietly.",
        "3. When making choices, you trust:\nA) Feelings.\nB) Facts.",
        "4. Talking is more fun when it's about:\nA) Possibilities and dreams.\nB) Real-life events.",
        "5. When you have a deadline, you:\nA) Finish at the last minute.\nB) Finish early."
    ]

    answers = []

    for question in questions:
        answers.append(ask_question(question))

    return answers

def calculate_mbti(answers):
    mbti = ""

    mbti += "E" if answers[0:2].count("A") > answers[0:2].count("B") else "I"
    mbti += "N" if answers[3] == "A" else "S"
    mbti += "F" if answers[2] == "A" else "T"
    mbti += "P" if answers[4] == "A" else "J"

    return mbti

def main():
    print("WELCOME TO THE MBTI TEST\n")

    name = input("Enter your name: ")

    answers = get_user_answers()

    mbti_type = calculate_mbti(answers)

    print("\nYour MBTI Type is:", mbti_type)

    
    file = open("game.dat", "wb")
    pickle.dump([name, mbti_type], file)
    file.close()

    # Read from binary file
    file = open("game.dat", "rb")
    data = pickle.load(file)
    file.close()

    print("\nData stored in game.dat")
    print("Name :", data[0])
    print("MBTI :", data[1])




def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    def write () :
        file =open("game. dat",'wb') 
        choices = ["rock", "paper", "scissors"]
        pickle.dump (choices, file) 
        file. close() 
    write()
    def read () :
        try:
            file =open("game. dat",'rb') 
            wins, losses, draws = 0, 0, 0
            data=pickle.load(file) 
            while True:
                player_choice = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()
                if player_choice. lower() == 'exit':
                    break
                if player_choice not in data:
                    print("Invalid input. Please choose rock, paper, or scissors.")
                    continue
                computer_choice = random.choice(data)
                print("Computer chose:", computer_choice)
                if player_choice == computer_choice:
                        print("It's a draw!")
                        draws += 1
                elif (player_choice == "rock" and computer_choice == "scissors") or \
                    (player_choice == "scissors" and computer_choice == "paper") or \
                    (player_choice == "paper" and computer_choice == "rock"):
                        print("You win🥳!!!!")
                        wins += 1
                else:
                    print("You lose!")
                    losses += 1
                total_games = wins + losses + draws
                print( "Wins:" , wins, "Losses:", losses, "Draws:", draws)
                print("Total games:", total_games )
        except:
            file.Close()
    read()
                       
 
def three_roses() :
    def write ():
        file=open("game. dat", "wb" )
        a=int(input("enter how to many inputs from a topic:"))
        print ("Choose a topic!!!!! ")
        l=[ ]
        i=0
        for i in range (0,a):
            i=input("enter a input of that topic :")
            l.append(i)
        pickle.dump(l,file)
        file.close ()
    write()
    def read():
        file=open("game. dat", "rb" )
        try:
            x=0
            n=int(input("enter no of round:"))
            data=pickle.load(file)
            for i in range (n) :
                a1=random.choice(data)
                a2=random.choice(data)
                a3=random.choice(data)
                print("[", a1, a2, a3, "]")
                if a1==a2==a3:
                    x+=1
                    print ("You win!!!!")
                else:
                    print("Best luck next time!!! ")
        except:
            file.close ()
        finally:
            if x==0:
                print ("your got", x, "point")
    read()
    def deletion():
        delete = input("Delete saved game? (yes/no): ").strip().lower()
        if delete == "yes" :
            try:
                data=pickle. load(file)
                os.remove(data)
            except :
                print("Game data deleted.")
            else:
                print("Game data kept.")
    deletion()

def fun_facts():
    def write():
        file=open("game. dat","wb")
        fun_facts_list = ["Octopuses have three hearts.",
                          "Bananas are berries, but strawberries are not." ,
                          "A group of flamingos is called a 'flamboyance.'",
                          "Sharks existed before trees.","Wombat poop is cube-shaped.",
                          "You can hear a blue whale's heartbeat from over 2 miles away.",
                          "There's a species of jellyfish that can live forever (technically).",
                          
                          "Scotland has 421 words for 'snow'.","Some cats are allergic to humans.", 
                          "Sloths can hold their breath longer than dolphins."]
        pickle. dump(fun_facts_list, file)
        file.close()
    write () 
    def read():
        file=open("game. dat", "rb")
        try:
            data=pickle. load (file )
            while True:
                for i in data:
                    print (i)
                    a=input ("do you want to continue?? (n/y) :")
                    if a. lower() =='n':
                        break
                break   
        except:
            file. close()
    read()    
    def updatef():
        file=open("game. dat", "rb+")
        try:
            data=pickle. load (file )
            pos=file.tell()
            fact=input ("do want to add a new fun fact (n/y)??? :")
            if fact.lower()=='y':
                new=input("enter a new funfact:")
                file. seek(pos)
                data. append (new)
                pickle.dump(data,file )
                print("Your fact updated!! ")
                print("Hope it's interesting and you had enjoyed!!! ") 
        except:
            file. close()
    updatef()
        
def riddle():
    def write():
        file =open("game. dat", "wb")
        riddles =["What type of music do rabbits listen to?",
                "Why did the scarecrow win an award?",
                "What do you call a fake noodle?",
                "What starts with an E, ends with an E, but only contains one letter?",
                "Why did the bicycle fall over?" ]
        answers = ["Hip hop!",
                "Because he was outstanding in his field.",
                "An impasta.",
                "An envelope.",
                "Because it was two-tired." ]
        pickle.dump(riddles, file)
        pickle.dump(answers, file)
        file. close()
    write()
    def read2():
        file =open("game. dat", "rb")
        riddles = pickle.load(file)
        answers = pickle.load(file)
        try:
            n = int(input("Enter how many jokes you want to see (1–5): "))
            if 1 <= n <= 5:
                for i in range(n):
                    print("Riddle:", riddles[i])
                    print("Answer:", answers[i])
            else:
                print("Please enter a number between 1 and 5.")
        except :
            print("Invalid input. Please enter a number.")
        file. close()
    read2()

def menu(): 
    while True:
        print("1.PERSONALITY TEST")
        print("2.ROCK PAPER AND SCISSORS/THREE ROSES")
        print("3.FUNFACTS/RIDDLES") 
        print ("4.EXIT")
        choice = int(input("Enter from 1/2/3/4: "))
        if choice == 1:
            main()
        if choice == 2:
            while True :
                print("1.ROCK PAPER SCISSORS" )
                print("2.THREE ROSES")
                print ("3.EXIT")
                Choose=int(input("Enter from 1/2/3: "))
                if Choose==1:
                    rock_paper_scissors()
                if Choose==2:
                    three_roses()
                if Choose==3:
                    break
        if choice == 3:
            while True :
                print("1.FUNFACTS")
                print("2.RIDDLES")
                print ("3.EXIT")
                Choose=int(input("Enter from 1/2/3: "))
                if Choose==1:
                    fun_facts()
                if Choose==2:
                    riddle()
                if Choose==3:
                    break
        if choice==4:
            print("Hope you have enjoyed✨✨✨!!!! ")
            print("You have Exited the game")
            break 
        if choice >4:
            print("❌Invalid choice!")
menu()
             






