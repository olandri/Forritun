


row = 1
col = 1

gameOver = False    
while not gameOver:

    print("You can go ", end="")
    
    if col == 1: 
        if row == 1:
            print("(N) orth")
        if row == 2:
            print("(N) orth or (S) outh or (E) ast.")
        if row == 3:
            print("(S) outh or (E) ast.")
    if col == 2:
        if row == 1:
            print("(N) orth")
        if row == 2:
            print("(S) outh or (W) est.")
        if row == 3:
            print("(E) ast or (W) est.")
    if col == 3:
        if row == 1:
            print("(N) orth")
        if row == 2:
            print("(S) outh or (N) orth.")
        if row == 3:
            print("(E) ast or (W) est.")

    # Get where to go
    whereTo = input("Direction: ").upper()

    if whereTo in "NWES":
        gameOver = False

    legal = True
    if whereTo == 'N':
        if col == 1: 
            if row == 1:
                row = 2
            if row == 2:
                row = 3
            if row == 3:
                legal = False
        if col == 2:
            if row == 1:
                row = 2        
            if row == 2:
                legal = False
            if row == 3:
                legal = False
        if col == 3:
            if row == 1:
                row = 2
            if row == 2:
                row = 3
            if row == 3:
                legal = False

    if whereTo == 'S':
        if col == 1: 
            if row == 1:
                legal = False
            if row == 2:
                row = 1
            if row == 3:
                row = 2
        if col == 2:
            if row == 1:
                legal = False
            if row == 2:
                row = 3
            if row == 3:
                legal = False
        if col == 3:
            if row == 1:
                legal = False
            if row == 2:
                row = 3
            if row == 3:
                legal = False

    if whereTo == 'W':
        if col == 1: 
            if row == 1:
                legal = False
            if row == 2:
                legal = False
            if row == 3:
                legal = False
        if col == 2:
            if row == 1:
                legal = False
            if row == 2:
                col = 1
            if row == 3:
                legal = False
        if col == 3:
            if row == 1:
                legal = False
            if row == 2:
                legal = False
            if row == 3:
                col = 2
    if whereTo == 'E':
        if col == 1: 
            if row == 1:
                legal = False
            if row == 2:
                col = 2
            if row == 3:
                col = 2
        if col == 2:
            if row == 1:
                legal = False
            if row == 2:
                legal = False
            if row == 3:
                col = 3
        if col == 3:
            if row == 1:
                legal = False
            if row == 2:
                legal = False
            if row == 3:
                legal = False



