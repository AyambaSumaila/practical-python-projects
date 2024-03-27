from tkinter import *
import tkinter.messagebox
from check_sudoku_solution import isValid

class SudokuGUI:
    
    def __init__(self):
        window=Tk()
        window.title("Check Sudoku Solution")
        frame=Frame(window)
        frame.pack()
        
        self.cells=[]
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())
        for i in range(9):
            for j in range(9):
                Entry(frame, width =2, justify=RIGHT, textvariable=self.cells[i][j]).grid(row=1, column=j)
                
        Button(window, text="validate",
                command=self.validate).pack()
        
        window.mainloop()


def validate(self):
    values=[[eval(x.get() ) for x in self.cells[i]] for i in range(9)]
    
    if isValid(values):
        tkinter.messagebox.showinnfo("Check Sudoku Solution", "The solution is valid")

    else:
        tkinter.messagebox.showwarning("Check Sudoku Solution is", "Ths Solution is invalid")
SudokuGUI()

            