def say_score(score0,score1):
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_score

def announce_lead_changes(previous_leader=None):
    def say(score0,score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != previous_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f,g):
    def say_both(score0,score1):
        return both(f(score0,score1),g(score0,score1))
    return say_both


h0 = both(say_score,announce_lead_changes())
h1 = h0(10,0)
h2 = h1(10,6)
h3 = h2(13,6)
h4 = h3(13,22)
