import random
import time


def displayIntro():
    print('+--------------------------------------------------------------------------+')
    print('''   You are in a land full of dragons. In front of you, you see two caves.''')
    time.sleep(2)
    print('''   In one cave, the dragon is friendly and will share his treasure with you.''')
    time.sleep(2)
    print('''   The other dragon is greedy and hungry, and will eat you on sight!''')
    print('+--------------------------------------------------------------------------+')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

        return cave
    
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(4)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print ('Gives you his treasure!')
        print ("""
             __.-/|
             \`o_O'
              =( )=  +---------+
                U|   |  FREE   |
                /|   |TREASURE!|
      /\  /\   / |   +---------+
     ) /^\) ^\/ _)\       |
     )   /^\/   _) \      |
     )   _ /  / _)  \_____|_
 /\  )/\/ ||  | )_)\_____,|))
<  >      |(,,) )__)      |
 ||      /    \)___)\
 | \____(      )___) )____
  \______(_______;;;)__;;;)
               
               """)
    else:
        print ('Gobbles you down in one bite! ')
        print ("""
                  /|               |\                              
                 / | ___-------___ | \                             
                /  \/ ^ /\   /\ ^ \/  \                            
               |   (  O-. \ / .-O  )   |                           
            /-\/   ^-----^-V-^-----^   \/-\                        
          /-      (~ 0O0 ~) (~ 000 ~)     -\                       
         <        (~ OOO ~) (~ 000 ~)       >                      
          \-      (____---===---____)     -/                       
           \-   /\ \ \|         |/ / /\  -/                        
           -/\-/  \ \ V         V / /  \-/\-                       
              v    \ \           / /    v                          
                    \ \ A     A / /                                
                     \_\^-----^/_/                                 
                      \_/\___/\_/                                  
                        \_____/
               
               """)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if(playAgain == "no" or playAgain == "n"):
        print("Thanks for playing, Created by J0hun1 - 2021")
        break