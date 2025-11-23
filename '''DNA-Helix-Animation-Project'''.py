'''DNA-Helix-Animation-Project'''

import random, sys, time

PAUSE = 0.08 

# These are the individual rows of the DNA animation:
ROWS = [
    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

try:
    print('Press Ctrl-C to quit.')
    time.sleep(2)
    rowIndex = 0

    while True:  # Main program loop.
        # Increment rowIndex to draw next row:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # Row indexes 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # Select random nucleotide pairs, guanine-cytosine and
        # adenine-thymine:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'D', 'N'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'N', 'D'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'A', 'D'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'D', 'A'

        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE) 
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
