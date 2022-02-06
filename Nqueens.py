# Implementation of N Queens Problem in Python 
N = int(input("Enter the number of queens: "))

#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def in_attack(i, j):
    #checking if there is a queen already placed in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_Queen_Algo(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place can be attacked by other queen
            or already occupied'''
            if (not(in_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                # using recursion to check whether we can put the next queen with this arrangment or not
                if N_Queen_Algo(n-1)==True:
                    return True
                board[i][j] = 0

    return False

# Driver Code:
    
N_Queen_Algo(N)


print("\n")
for i in range(0,N):
        for j in range(0,N):
            if(board[i][j] == 1):
                print("Location:",i+1,",",j+1)

print("\n Board Layout:\n")
for i in board:
    print (i)
print("\n")