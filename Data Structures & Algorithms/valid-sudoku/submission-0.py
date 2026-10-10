# for each row/col -> check if set(elements) == elements (minus . chars)
#                       iterate through 0-9 indexes
# for each squares -> same, for indexes, get index of first top-left element then iterate through all 9 elements in the 3x3 grid
class Solution:
    def __hasNoDuplicates(self, elements: List[str]) -> bool:
        digits = list(filter(lambda e: e != '.', elements))
        return len(digits) == len(set(digits))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols: List[List[str]] = [[] for _ in range(9)]
        squares: List[List[str]] = [[] for _ in range(9)]
        for rowIndex, row in enumerate(board):
            print('checking row: ', row)
            if not self.__hasNoDuplicates(row): return False
            for colIndex, e in enumerate(row):
                cols[colIndex].append(e)
                squares[colIndex // 3 + (rowIndex // 3) * 3].append(e)

        for col in cols:
            print('checking col: ', col)
            if not self.__hasNoDuplicates(col): return False
            
        for square in squares:
            print('checking square: ', square)
            if not self.__hasNoDuplicates(square): return False

        return True