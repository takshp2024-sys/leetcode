class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Alice's first move is always 10
        current_move = 10
        is_alice_turn = True
        
        while n >= current_move:
            # The player makes the move
            n -= current_move
            # The next player must remove 1 fewer stone
            current_move -= 1
            # Switch turns
            is_alice_turn = not is_alice_turn
            
        # If the loop ends, it means the player whose turn it is cannot make a move.
        # If it's Alice's turn and she can't move, she loses (Bob wins).
        # If it's Bob's turn and he can't move, Alice wins.
        return not is_alice_turn