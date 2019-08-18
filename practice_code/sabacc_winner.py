def sabacc_winner(cards,player0,player1):
    if cards == 0:
        return player0
    if cards == 1:
        return player1

    take_one = sabacc_winner(cards-1,player1,player0)
    take_two = sabacc_winner(cards-2,player1,player0)

    if take_one == player0 or take_two == player0:
        return player0
    return player1

print(sabacc_winner(4,'Han','lando'))
"""
  Tree Recursion can be used to explore different possibilities.
  
"""
