from Connect4 import *
from algorithms import *

def visualize(state):
    for row in state:
        for cell in row:
            print(cell, end='\t')
        print()
    print('--------------------')


while(True):
    print("Enter the game that you want to play (1 for Connect4 otherwise exit)")
    game_type = input()
    if game_type =='1' :
        game = Connect4()
    else:
        break
    
    print("Enter the Agent type that you want (1 for MiniMax otherwise AlphaBeta)")
    Agent_type = input()
    
    
    state = game.init_state
    while(not game.terminal_test(state)):
        print("Agent Move")
        
        if Agent_type == '1' :
            action = minimax(game, state)
        else:
            action = alpha_beta(game, state)
            
        state = game.result(state, action)
        
        visualize(state)
        
        if(game._won(state,game.PLAYERS[0])):
            print("Agent wins")
            break
        
        
        print("Computer Move")
        action = game.random_action(state)
        
        state = game.result(state, action)
        
        visualize(state)
        
        if(game._won(state,game.PLAYERS[1])):
            print("Computer wins")
            break