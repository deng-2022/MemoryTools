import tkinter as tk


class MemoryNotepad:
    def __init__(self):
        self.window = None

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("MemoryNotepad")


class MemoryTools:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MemoryTools")
        self.button = tk.Button(self.window, text="英汉互译", font=("Arial", 12))
        self.button.pack(side=tk.LEFT, padx=10)

        mn = MemoryNotepad()
        self.button.bind("<Button-1>", lambda event: mn.create_window())

    def create_window(self):
        self.window.mainloop()


if __name__ == '__main__':
    mt = MemoryTools()
    mt.create_window()
