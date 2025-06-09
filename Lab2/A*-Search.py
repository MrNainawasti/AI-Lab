from queue import PriorityQueue

G = {
    'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
    'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
    'dharan' : {'itahari' : 20},
    'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10}, 
    'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40}, 
    'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
    'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
    'damak' : {'urlabari' : 6}
}


h = {
    'biratnagar' : 46,
    'itahari' : 39,
    'dharan' : 41,
    'rangeli' : 28,
    'biratchowk' : 29,
    'kanepokhari' : 17,
    'urlabari' : 6,
    'damak' : 0
}

def aStar(G, h, start, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited = set()
    # The entries in PQ are in the format (f-score, (state,g-score))
    PQ.put((0+h[start], (start, 0)))
    prev[start] = " "
    while(PQ.empty() == False):
        outStateFScore , (outState, outStateGScore) = PQ.get()
        visited.add(outState)

        if outState == goal:
            return True, prev, outStateFScore
        
        for chimeki in G[outState]:
            if chimeki not in visited:
                chimekiGScore = outStateGScore + G[outState][chimeki]
                PQ.put((chimekiGScore+h[chimeki], (chimeki, chimekiGScore)))
                prev[chimeki] = outState
    return False, prev, -1
                
def reconstruct_path(previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + " -> "+ path
        goal = previous[goal]
    return path

start = 'biratnagar'
goal = 'damak'
goalFound, previous, goalFScore = aStar(G, h, start, goal)
if(goalFound):
    print(reconstruct_path(previous, goal))
    print(goalFScore)
else:
    print("NO SOLUTION!!")
    
