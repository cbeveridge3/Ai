#!/usr/bin/python
import Queue
class snode:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


def bfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    

    count = 0
    frontier = Queue.Queue() 
    explored = []
    
    moves = [(-1,0), (0,-1), (0,1), (1,0)]
    
    
    frontier.put(snode((pacman_r, pacman_c), 0))
    frontierStates = []
    
    
    while True:
        
        if frontier.qsize()==0:
            print('error')
            return
        
        pop = frontier.get()
        
        explored.append(pop.state)
        
        
        #check if goal is found
        if pop.state[0]==food_r and pop.state[1]==food_c:
            print(len(explored))
            for node in explored:
                print((str(node[0]) + ' ' + str(node[1])))
                
            #length of solved path
            dcount = 0
            output = []
            node = pop
                    
            while True:
                    
                output.append(node.state)
                
                
                if node.state[0] == pacman_r and node.state[1] == pacman_c:
                    break
                else:
                    dcount += 1
                    node = node.parent
                
                
            print(dcount)
            
            for node in reversed(output):
                print((str(node[0]) + ' ' + str(node[1])))
                
            return
        
        
        #add new states to frontier
        for move in moves:
            new_spot = tuple(map(lambda i, j: i + j, pop.state, move))
            r2 = int(new_spot[0])
            c2 = int(new_spot[1])
            
            #if new state is a spot in the maze and not in explored or on frontier, add it to frontier
            if r2 > 0 and c2 > 0 and r2 < r and c2 < c and (grid[r2][c2]=='-' or grid[r2][c2]=='.') and (not new_spot in explored) and (not new_spot in frontierStates):
                
                frontier.put(snode(new_spot, pop))
                frontierStates.append(new_spot)
                
                
            
    
    
    return

pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

bfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)
