Hi! This was my attempt at the coding challenge as well as my first attempt at a GUI-based project. 

In this challenge I used python & tkinter to implement the GUI. 

I was unfortunately not able to dockerize the application but, on the bright side, there aren't any dependencies required to run the application since tkinter comes pre-installed with Python! 

With that being said, my application does require having Python installed. 

HOW TO RUN: 
- Create a directory somewhere on your local machine
- CD into this directory
- in the CL run: git clone https://github.com/Alexei-Ionov/Bertram-Coding-Challenge
- CD into the created directory: cd Bertram-Coding-Challenge
- in the CL run: python3 main.py
- The GUI *should* appear on the same window but might appear on another (oftentimes appears on whatever window is running Chrome). Please Full Screen the application!

INSIDE THE GUI:
- The general idea is that the application incorporates a story-like flow where each day Bob, Jeremey, and the other coworkers (who were given random names) go to their beloved coffee shop 
- While at the coffee shop display, there will be opportunities for you to interact with the gui as you get to choose the drink of choice for Bob, Jeremey, and the other coworkers. These dropdowns are given default options in case you don't want to so don't worry about choosing a drink for each person every time!
- After the drinks have been chosen, please click the corresponding button on screen to "calculate the total price". This step must be done before advancing further!
- The program decides who pays based on the person who has paid the LEAST so far (we do want to be fair after all). Ties are broken via a random number generator. The amount paid for by each coworker is available next to their name while at the coffee shop (e.g. Bob $0.0 on the first day). 
- After the "unlucky" coworker gets chosen for who has to pay, the GUI will ask you to hit 'ENTER' in your CL so as to "continue onto the next day". 
- Once you're ready to quit the application (as it loops infinitely), simply Control-C in the terminal. 

ABOUT THE CHALLENGE: 
- For me, the goal was to first learn about tkinter and put what I had learned into practice. 
- With that being said, just as a heads up, the project is by no means flashy nor visually appealing by any means :)

Thank you for checking it out!

