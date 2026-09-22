def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculates the mean of a 2D matrix by row or by column.
    Handles irregular matrix dimensions and string formatting.
    """
    if not matrix or not matrix[0]:
        return []
    
    # Normalize mode string to lowercase to handle casing differences
    mode = mode.lower()
    
    if mode == 'row':
        # Each row's mean depends on its own length (handles non-rectangular matrices)
        return [sum(row) / len(row) for row in matrix if row]
    
    elif mode == 'column':
        num_rows = len(matrix)
        num_cols = max(len(row) for row in matrix)
        
        column_means = []
        for col_idx in range(num_cols):
            # Gather valid elements present at col_idx across all rows
            col_values = [row[col_idx] for row in matrix if col_idx < len(row)]
            if col_values:
                column_means.append(sum(col_values) / len(col_values))
                
        return column_means
    
    else:
        raise ValueError("Mode must be either 'row' or 'column'")