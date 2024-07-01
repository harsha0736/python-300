def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    row = [1] 
    for i in range(1, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)
    
    return row
 
rowIndex=(7)
result=getRow(rowIndex)
print(result)