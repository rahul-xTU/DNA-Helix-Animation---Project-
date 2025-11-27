DNA Helix Animation

A simple Python program that creates a cool rotating DNA helix animation in your terminal!

What is this?
This project shows a DNA double helix spinning in your terminal using ASCII art. The letters on the sides represent the nucleotide base pairs that make up DNA. It's a fun way to visualize what DNA looks like while learning Python!

Requirements
* Python 3
* No extra libraries needed - everything comes with Python
* 
How to Run
1. Save the code as dna_helix.py
2. Open your terminal
3. Run: python dna_helix.py
4. Watch the DNA spin!
5. Press Ctrl-C to stop
   
What I Learned
While making this project, I learned about:
* Using loops to create animations
* Working with lists and strings
* Formatting text with .format()
* Handling keyboard interrupts
* Making random selections in Python
  
How It Works
The program has 18 different ASCII art patterns stored in a list. It cycles through them one by one, creating the illusion of a rotating helix. For each frame (except the crossover points), it randomly picks base pairs to display - just like real DNA has different combinations of nucleotides!
The PAUSE variable controls how fast it spins. You can make it faster or slower by changing that number.

Customization Ideas
Want to make it your own? Try:
* Changing the PAUSE value to speed up or slow down the animation
* Using the actual DNA letters (G, C, A, T) instead of D, N, A
* Adding colors using the colorama library
* Making the helix bigger or smaller
  
Known Issues
* Uses D, N, A letters instead of the real DNA notation (G, C, A, T)
* No color - just plain text
* Can't pause the animation once it starts
  
Future Ideas
If I work on this more, I'd like to:
* Add color coding for different nucleotides
* Make it possible to pause and resume
* Show statistics about which base pairs appear most
* Create different helix patterns to choose from

