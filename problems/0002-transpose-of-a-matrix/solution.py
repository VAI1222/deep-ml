def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    num_rows = len(a)
    num_cols = len(a[0])
    
    result = []
    
    # Loop through each column
    for col_index in range(num_cols):
        new_row = []
        
        # Collect items for the new row
        for row_index in range(num_rows):
            new_row.append(a[row_index][col_index])
            
        result.append(new_row)
        
    return result