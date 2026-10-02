def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		means = [sum(i)/len(i) for i in matrix]
	else:
		
		wt = list()
		for i in range(len(matrix[0])):
			col = list()

			for j in range(len(matrix)):

					col.append(matrix[j][i])

			wt.append(col)    
			
			
		means = [sum(i)/len(i) for i in wt]
			

	print(sum(matrix[0]),len(matrix[0]),means)
	return means