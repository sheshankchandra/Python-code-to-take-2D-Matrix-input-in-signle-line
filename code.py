# R = Rows of a Matrix
# C = Columns of a Matrix
R, C = map(int, input().split())

ans = list(map(int, input().split()))
# Temporary list to take input from single line

matrix = [[0 for j in range(C)] for i in range(R)]
# Initialising matrix and setting up length's

k = 0
for i in range(R):
	for j in range(C):
		matrix[i][j] = ans[k]
		k = k+1
		
print(matrix)
