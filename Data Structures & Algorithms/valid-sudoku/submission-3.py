class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # from what i remember last time:
        # make list of lists to add rows and col?
        # use a set to get rid of duplicates
        # i want to look at 3x3 squares for any duplicates but idk how
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        # looked at solution but since we know it must be a 9x9, we can just hardcode the range
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue # don't want to add to set but continue 
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                

                # if no duplicates then add
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True
                

        