# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)
# 
# Remember the rules:
# 
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

print("This is a rock paper scissors game!")
user1_choice = input("What will player 1 choose - Rock, Paper or Scissors: ")
user2_choice = input("What will player 2 choose - Rock, Paper or Scissors: ")

# check user1_choice versus user2_choice
def compare(u1, u2):

    # if their choices are the same
    if u1 == u2:
        return("It's a tie") 
        
    # if player 1 chooses Rock 
    elif u1 == 'Rock':
        
        # player 2 chooses Scissors
        if u2 == 'Scissors':
            return("Player 1 wins")
    
        # player 2 chooses Paper
        if u2 == 'Paper':
            return("Player 2 wins")

    # if player 1 chooses Paper:            
    elif u1 == 'Paper':
        
        # player 2 chooses Rock
        if u2 == 'Rock':
            return("Player 1 wins")
        
        # player 2 chooses Scissors
        if u2 == 'Scissors':
            return("Player 2 wins")
        
    # if player 1 chooses Scissors
    elif u1 == 'Scissors':
    
        # player 2 chooses Rock
        if u2 == 'Rock':
            return("Player 2 wins")
        
        # player 2 chooses Paper
        if u2 == 'Paper':
            return("Player 1 wins")
            
    else:
        return("Invalid input")
    
    
    

print(compare(user1_choice, user2_choice))




