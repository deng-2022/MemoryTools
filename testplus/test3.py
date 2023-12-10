import tkinter as tk


class MemoryNotepad:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MemoryNotepad")


class MemoryTools:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MemoryTools")

    def create_window(self):
        mn = MemoryNotepad()
        self.window.mainloop()


if __name__ == '__main__':
    mt = MemoryTools()
    mt.create_window()
