from collections import deque
def BFS(a, b, target):
    visited = set()
    isSolvable = False
    path = []
    q = deque()
    q.append((0, 0))
    
    while q:
        u = q.popleft()
        if u in visited:
            continue
        visited.add(u)
     
        path.append(u)
      
        if u[0] == target or u[1] == target:
            isSolvable = True
            break
        
        # Fill Jug1
        q.append((a, u[1]))
        # Fill Jug2
        q.append((u[0], b))
        # Empty Jug1
        q.append((0, u[1]))
        # Empty Jug2
        q.append((u[0], 0))
        
        # Pour water from Jug1 to Jug2
        pour = min(u[0], b - u[1])
        q.append((u[0] - pour, u[1] + pour))
        # Pour water from Jug2 to Jug1
        pour = min(u[1], a - u[0])
        q.append((u[0] + pour, u[1] - pour))

    if isSolvable:
        print("Solution found. Path from initial state to solution state:")
        for state in path:
            print(state)
    else:
        print("No solution found")

if __name__ == '__main__':
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target amount: "))
    
    print("Path from initial state to solution state:")
    BFS(Jug1, Jug2, target)
