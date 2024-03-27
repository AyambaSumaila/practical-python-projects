from check_sudoku_solution import isValid

def main():
    grid=read_solution()
    
    if isValid(grid):
        print('Valid solution')
    else:
        print('Sorry Invalid solution')
    
def read_solution():
        print('Enter a Suduku puzzle solution:')
        grid=[]
        for i in range(9):
            line=input().strip().split()
            grid.append([eval(x) for x in line])
        return grid
main()
            