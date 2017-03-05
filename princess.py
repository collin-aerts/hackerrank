#!/bin/python
def displayPathtoPrincess(n,grid):

    current_x = current_y = int(math.floor(n/2))
    
    if grid[0][0]=="p":
        dest_x = dest_y = 0
    elif grid[0][n-1]=="p":
        dest_x = n-1
        dest_y = 0
    elif grid[n-1][0]=="p":
        dest_x = 0
        dest_y = n-1
    else:
        dest_x = dest_y = n-1
        
    while dest_x<current_x:
        current_x += -1
        print "LEFT"
    
    while dest_x>current_x:
        current_x += 1
        print "RIGHT"
    
    while dest_y<current_y:
        current_y += -1
        print "UP"
        
    while dest_y>current_y:
        current_y += 1
        print "DOWN"

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)