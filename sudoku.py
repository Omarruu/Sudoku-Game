import tkinter as tk

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def isValid(grid, row, col, value):
    row_check = value not in grid[row]
    column_check = value not in [grid[i][col] for i in range(9)]
    square_check = value not in [grid[i][j] for i in range(row//3*3, row//3*3+3) for j in range(col//3*3, col//3*3+3)]
    return row_check and column_check and square_check

def CSP_recursion(grid, row=0, col=0):
    if row == 9:
        return True
    elif col == 9:
        return CSP_recursion(grid, row+1, 0)
    elif grid[row][col] != 0:
        return CSP_recursion(grid, row, col+1)
    else:
        for value in range(1, 10):
            if isValid(grid, row, col, value):
                grid[row][col] = value
                if CSP_recursion(grid, row, col+1):
                    return True
                grid[row][col] = 0      #there is no possible solution so it backtracking
        return False
                

class MatrixGUI:
    def __init__(self, root, matrix):
        self.root = root
        self.root.title("Sudoku")
        self.create_widgets(matrix)   # set up the giu for the passed matrix

    def create_widgets(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                label = tk.Label(self.root, text=str(matrix[i][j]), width=5, height=3, relief="solid", borderwidth=1)
                label.grid(row=i, column=j, padx=2, pady=2)

CSP_recursion(grid)

if __name__ == "__main__":    # going to display the matrix for the game
    matrix = grid
    root = tk.Tk()
    app = MatrixGUI(root, matrix)   # pass grid to matrix gui class so it can draw and label it 
    root.mainloop()