def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	output =[]
	for i in matrix:
		l = []
		for j in i:
			l.append(j*scalar)
		output.append(l)


	return output
	pass