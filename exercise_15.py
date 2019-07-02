# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right
# and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?
'''I feel like there is some trick here. I know I need equal number of down and right moves.
The number of moves is n *2.

'''

import pdb
import timeit

class Grid():


    def __init__(self, size):
        '''Number of squares in the grid'''
        self.size = size
        self.X = 0
        self.Y = 0
        self._at_end_node = False

    def _isValidMove(self, direction):
        if direction == 'r' and self.X+1 <= self.size:
            return True
        elif direction == 'd' and self.Y+1 <= self.size:
            return True
        else:
            return False
    def _is_at_end_node(self):
        if self.X == self.size and self.Y == self.size:
            self._at_end_node = True
            #print(f"At end node {self.X}, {self.Y}")

    def move(self, direction):
        if self._isValidMove(direction):
            if direction == "r":
                self.X += 1
            elif direction == "d":
                self.Y +=1
            else:
                raise ValueError(f"direction {direction} is not valid.")
            # print(f"New position {self.X}, {self.Y}.")
            self._is_at_end_node()
        else:
            raise ValueError(f"current position {self.X}, {self.Y} cannot move {direction} in a gride of size {self.size}")



class Grid2(Grid):

    def __init__(self, n):
        Grid.__init__(self, n)
        self.reset()

    def reset(self):
        self.X = 0
        self.Y = 0
        self._at_end_node = False



grid = Grid(2)
grid.move("r")
print(grid)


grid = Grid(2)
grid.move("r")
grid.move("r")
grid.move("d")
grid.move("d")


from itertools import product

def calcMaxMoves(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0

    for route in allRoutes:
        i +=1
        grid = Grid(n)
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole sequence isn't valid
            # do remove it from our counter and go on to the next list of moves.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i



# TODO: I should be able to take advantage of the symmetery. For example R, R, D, D, is the same as D, D, R, R


def calcMaxMoves2(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0

    for route in allRoutes:
        # No need to test moveLists where one move is > n (ie all r moves)
        # If that happens, just continue to the next element in the loop.
        if route.count('r') > n:
            continue
        i +=1
        grid = Grid(n)
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole sequence isn't valid
            # do remove it from our counter and go on to the next list of moves.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i







def maxRoutes(n, moves):
    return(len(moves)**(n*len(moves)))


# Test the function
moves = ['r', 'd']
for i in range(2, 10):
    assert(maxRoutes(i, moves) == len(list(product(moves, repeat = i*2))))


def calcMaxMoves3(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes

    j = 0 # Counter for the routes
    maxRouteCandidate = maxRoutes(n, moves)/2
    for route in allRoutes:
        # The counter will output in lexographic order, so we should be able to break teh loop halfway
        if j > maxRouteCandidate:
            #print(route)
            break
        i +=1
        j +=1
        grid = Grid(n)
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole route isn't valid
            # do remove it from our counter and go on to the next route.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i*2

def calcMaxMoves4(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes

    j = 0 # Counter for the routes
    maxRouteCandidate = maxRoutes(n, moves)/2
    for route in allRoutes:
        # The counter will output in lexographic order, so we should be able to break teh loop halfway
        if j > maxRouteCandidate:
            #print(route)
            break
        j +=1
        # No need to test moveLists where one move is > n (ie all r moves)
        # If that happens, just continue to the next element in the loop.
        # BUT, I do need to increment j (as previously done)
        if route.count('r') > n:
            continue
        i +=1
        grid = Grid(n)
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole route isn't valid
            # do remove it from our counter and go on to the next route.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i*2





def calcMaxMoves5(n=8):
    '''Somehow this is slower.'''
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes

    j = 0 # Counter for the routes
    maxRouteCandidate = maxRoutes(n, moves)/2
    grid = Grid2(n)
    #Instead of instantiating grid everytime, create a method called reset that puts
    # everything back to original values. Then just call then for each loop in the execution.
    # Should save significant time.
    for route in allRoutes:
        # The counter will output in lexographic order, so we should be able to break teh loop halfway
        if j > maxRouteCandidate:
            #print(route)
            break
        j +=1
        # No need to test moveLists where one move is > n (ie all r moves)
        # If that happens, just continue to the next element in the loop.
        # BUT, I do need to increment j (as previously done)
        if route.count('r') > n:
            continue
        i +=1
        grid.reset()
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole route isn't valid
            # do remove it from our counter and go on to the next route.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i*2



def calcMaxMoves6(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes

    j = 0 # Counter for the routes
    maxRouteCandidate = maxRoutes(n, moves)/2
    for route in allRoutes:
        # The counter will output in lexographic order, so we should be able to break teh loop halfway
        if j > maxRouteCandidate:
            #print(route)
            break
        j +=1
        # No need to test moveLists where one move is > n (ie all r moves)
        # If that happens, just continue to the next element in the loop.
        # BUT, I do need to increment j (as previously done)
        if route.count('r') != n:
            continue
        i +=1
        grid = Grid(n)
        for move in route:
            # Try a certain move, if we encounter an error, we know that whole route isn't valid
            # do remove it from our counter and go on to the next route.
            try:
                grid.move(move)
            except:
                i -=1
                break
    #print(i)
    return i*2


def calcMaxMoves7(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes
    for route in allRoutes:
        if route.count('r') == n:
            i +=1
        else:
            continue
    return i


def calcMaxMoves8(n=8):
    moves = ['r', 'd']
    allRoutes = product(moves, repeat = n*2)
    i = 0 # Counter for the total number of acceptable routes
    j = 0 # Total counter for the executed routes
    mxRoutes = maxRoutes(n, moves)/2
    for route in allRoutes:
        if j > mxRoutes:
            break
        if route.count('r') == n:
            i +=1
            #print(j, i)
        j += 1
    return i*2

# TODO: I think I can just skip a bunhc of the allRoutes. We know that the first X will not have enough
# of one move in them.

#TODO: make the moves 0,1 and then sum them? May be faster than route.count()


for i in range(2, 9):
    mxMoves1 = calcMaxMoves(i)
    mxMoves2 = calcMaxMoves2(i)
    mxMoves3 = calcMaxMoves3(i)
    mxMoves4 = calcMaxMoves4(i)
    mxMoves5 = calcMaxMoves5(i)
    mxMoves6 = calcMaxMoves6(i)
    mxMoves7 = calcMaxMoves7(i)
    mxMoves8 = calcMaxMoves8(i)
    assert(mxMoves1 == mxMoves2 == mxMoves3 == mxMoves4 == mxMoves5 == mxMoves6==mxMoves7 == mxMoves8)


t1= timeit.timeit(calcMaxMoves, number =1)
t2= timeit.timeit(calcMaxMoves2, number = 1)
t3= timeit.timeit(calcMaxMoves3, number = 1)
t4= timeit.timeit(calcMaxMoves4, number = 1)
t5 = timeit.timeit(calcMaxMoves5, number = 1)
t6 = timeit.timeit(calcMaxMoves6, number = 1)
t7 = timeit.timeit(calcMaxMoves7, number=1)
t8 = timeit.timeit(calcMaxMoves8, number=1)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)

t = calcMaxMoves8(15)
t















