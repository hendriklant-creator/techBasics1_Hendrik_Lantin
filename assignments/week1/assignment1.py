# Frame 1
print("Frame 1:")
# ASCII art

# Frame 2
print("Frame 2:")
# ASCII art (slightly modified)


       .-""-.
      /-.{}  \         
      | _\__.|      OOOOO
      \/^)^ \/       OOO
       \ =  /       OOOOO
       I    I         I
       I    I---------I
       I    I---------I
       I    I         I
       I    I         I
       I    I         I           
________________________________________________ ________

       O              OOOOO
      /|\             OOO
       / \           OOOOO



import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Frame 1 - Character on left
frame1 = """
    .-""-.
   /-.{}  \\         
   | _\__.|      OOOOO
   \\/^)^ \\/       OOO
    \\ =  /       OOOOO
    I    I         I
    I    I---------I
    I    I---------I
    I    I         I
    I    I         I
    I    I         I
"""

# Frame 2 - Character moves right
frame2 = """
        .-""-.
       /-.{}  \\         
       | _\__.|      OOOOO
       \\/^)^ \\/       OOO
        \\ =  /       OOOOO
        I    I         I
        I    I---------I
        I    I---------I
        I    I         I
        I    I         I
        I    I         I
"""

# Frame 3 - Character moves more right
frame3 = """
            .-""-.
           /-.{}  \\         
           | _\__.|      OOOOO
           \\/^)^ \\/       OOO
            \\ =  /       OOOOO
            I    I         I
            I    I---------I
            I    I---------I
            I    I         I
            I    I         I
            I    I         I
"""

frames = [frame1, frame2, frame3, frame2, frame1]

# Play animation
for i in range(5):  # Loop 5 times
    clear_screen()
    print(frames[i % len(frames)])
    time.sleep(0.5)  # Wait 0.5 seconds between frames

