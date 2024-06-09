from src.cache import scores
import random
import math

def make_bot_move(game, black = True):
    position, move = next_move(game, black)
    game.state.make_move(position, (move[0], move[1]), move[2])

def next_move(game, black = True):
    print("Bot is thinking...")
    best_move = None
    best_position = None
    best_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    current_moves = tuple(game.state.current_player_moves.items())
    for position, moves in current_moves:
        depth = calulate_depth(game)
        for move in moves:
            game.state.make_move(position, (move[0], move[1]), move[2])
            score = minimax(game, alpha, beta, not black, depth)
            game.state.undo_move()
            
            if score > best_score:
                best_score = score
                best_move = move
                best_position = position
            
            alpha = max(alpha, best_score)
    
    return best_position, best_move


def minimax(game, alpha, beta, maximizing_player, depth=3):
    print("Depth: ", depth)
    from_cache = scores.get(str(game.state))
    if from_cache is not None:
        return from_cache
    
    if game.state.is_game_over():
        return game.state.calucalte_heuristic()
    if depth == 0:
        return game.state.calucalte_heuristic()
    
    if maximizing_player:
        max_score = float('-inf')
        current_moves = tuple(game.state.current_player_moves.items())
        for position, moves in current_moves:
            for move in moves:
                game.state.make_move(position, (move[0], move[1]), move[2])
                score = minimax(game, alpha, beta, False, depth - 1)
                game.state.undo_move()
                
                max_score = max(max_score, score)
                alpha = max(alpha, max_score)
                
                if beta <= alpha:
                    break
        
        scores.put(str(game.state), max_score)
        return max_score
    
    else:
        min_score = float('inf')
        current_moves = tuple(game.state.current_player_moves.items())
        for position, moves in current_moves:
            for move in moves:
                game.state.make_move(position, (move[0], move[1]), move[2])
                score = minimax(game, alpha, beta, True, depth - 1)
                game.state.undo_move()
                
                min_score = min(min_score, score)
                beta = min(beta, min_score)
                
                if beta <= alpha:
                    break
        scores.put(str(game.state), min_score)
        return min_score
    
def randomizer(game):
    current_moves = tuple(game.state.current_player_moves.items())
    position, moves = random.choice(current_moves)
    move = random.choice(list(moves))
    game.state.make_move(position, (move[0], move[1]), move[2])

def f(x, y):
    alpha = 0.25
    max_depth = 8
    min_depth = 4
    return int(round(min_depth + (max_depth - min_depth) * math.exp(-alpha * math.sqrt(x**2 + y**2)), 0))

def calulate_depth(game):
    pieces = game.state.number_white_pieces + game.state.number_black_pieces
    queens = game.state.number_white_queens + game.state.number_black_queens
    return f(pieces, queens)

if __name__ == "__main__":
    import math
    def f(x, y):
        alpha = 0.2
        return int(round(2 + (7 - 2) * math.exp(-alpha * math.sqrt(x**2 + y**2)), 0))

    # Test the function with given points
    print(f(0, 1))  # Should be close to 7
    print(f(1, 0))  # Should be close to 7
    print(f(24, 0))  # Should be close to 2
    print(f(0, 24))  # Should be close to 2
    print(f(24, 24))  # Should be close to 2
    print("   ", end=" ")
    for x in range(0, 25):
        print(f"   {x}", end=" ")
    print()
    for y in range(0, 25):
        print(f"{y}", end=" ")
        for x in range(0, 25):
            if (x + y) > 24:
                print("    ", end=" ")
                continue
            print(f"   {f(x,y)}", end=" ")
        print()