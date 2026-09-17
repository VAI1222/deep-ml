def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not a[0]:
		return -1
	num_rows = len(a)
	num_cols = len(a[0])
	if num_cols != len(b):
		return -1
	result = []
	for row in a:
		row_sum=0
		for i in range(num_cols):
			row_sum+=row[i]*b[i]
		result.append(row_sum)
	return result
	pass