class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # what da hell is this
        # list within a list??? -> specific indexing then


        # well checking for duplicates i would use a set
        # loop through the list and add them to the set?



        # from video solution

        # want to default to cols, rows, and squares to be a set --> since it doesn't contain duplicates but also need a key to look up

        # video showed a smart way to find the specific index of the sub squares
        # divide the rows // 3 and cols // 3 to get the sub square index

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        # we know its only going to be a 9x9 so hardcode the range

        for r in range(9):
            for c in range(9):
                # iterating through each col and row in the 9x9 grid. if it finds an empty number, just continue
                if board[r][c] == ".":
                    continue
                # else if there is a duplicate --> want to return false
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3,c // 3)]:
                    return False
            
                # no duplicate --> add them to the set

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True






    





        