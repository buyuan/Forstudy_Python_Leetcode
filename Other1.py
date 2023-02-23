count = 0
def dfs(node, visited,circle,input):
    global count
    if node in visited:
        #if the node is visited, check if it is in a circle, then go to next node
        if node in circle:
            #found a circle, them remove the circle
            circleStartPoint = circle.index(node)
            circle = circle[:circleStartPoint+1]
            count+=1
            return
        return
    visited.append(node)
    circle.append(node)

    if node:
        #nodes that current node point to
        nexts = input[node]
        for next in nexts:
            #keep visit next nde
            dfs(next)
    #backtrace,back to status that currenct not is not appended
    circle.pop()

if __name__ == '__main__':
    input = {}
    #input = {A: (B, E), B: (C), C: (A, D) …};
    # for record the node that is visited
    visited = []
    # to record the node that maybe a circlea
    circle = []
    # count the number of circle
    dfs('A',visited,circle,input)
    print(count)



