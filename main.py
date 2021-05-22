import tkinter as tk
from tkinter.constants import LEFT
tkWin=tk.Tk()
tkWin.title="New phthon Win"

# Set the absolute window size
tkWin.geometry("600x400")

# Create Label and add to window grid
# sticky - stick to top N, Left W, Right E, and Bottom S
tkLabel1=tk.Label(text="Label1",justify=LEFT)
tkLabel1.grid(column=0, row=0, ipadx=5, pady=10, sticky=tk.E+tk.N)

# Create text field and add to grid next to Label 1
# Width and hiegt are characters and rows
tkField1=tk.Text(width=40,height=1)
tkField1.grid(column=1,row=0, ipadx=5, pady=5, sticky=tk.W)

# Grid row two is the same as row 1 with different label and field length
tkLabel2=tk.Label(text="Longer Label2",justify=LEFT)
tkLabel2.grid(column=0,row=1,ipadx=5, pady=10, sticky=tk.E+tk.N)
tkField2=tk.Text(width=60,height=1)
tkField2.grid(column=1,row=1, ipadx=5, pady=5, sticky=tk.W)

# start the window
tkWin.mainloop()