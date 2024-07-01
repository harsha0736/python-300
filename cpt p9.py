def generate(numRows):
    if numRows == 0:
        return []
    triangle = []
    for row in range(numRows):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                num = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(num)
        triangle.append(current_row)
    return triangle

numRows=(5)
result= generate(numRows)
print(result)


