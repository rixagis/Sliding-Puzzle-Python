import tkinter as tk

class NewGameDialog:

    def __init__(self, parent, start_game):
        self.start_game = start_game

        self.top = tk.Toplevel(parent)
        self.label = tk.Label(self.top, text="Enter the size of the board")
        self.label.grid(row=0)
        self.label_width = tk.Label(self.top, text="Width:")
        self.label_width.grid(row=1)
        self.label_height = tk.Label(self.top, text="Height:")
        self.label_height.grid(row=2)

        self.entry_width = tk.Entry(self.top)
        self.entry_width.grid(row=1, column=1)
        self.entry_height = tk.Entry(self.top)
        self.entry_height.grid(row=2, column=1)

        self.button_cancel = tk.Button(self.top, text="Cancel", command=self.cancel)
        self.button_cancel.grid(row=3)
        self.button_start = tk.Button(self.top, text="Start", command=self.start)
        self.button_start.grid(row=3, column=1)

        x = parent.winfo_x()
        y = parent.winfo_y()
        self.top.geometry("+%d+%d" % (x + 100, y + 100))
    
    def cancel(self):
        self.top.destroy()
    
    def start(self):
        w = int(self.entry_width.get())
        h = int(self.entry_height.get())
        self.start_game(w, h)
        self.top.destroy()