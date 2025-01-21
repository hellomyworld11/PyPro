import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, keylists, dictionary):
        super().__init__()
        self.geometry("400x400")
        self.title("词库")
        self.resizable(False, False)
        self.keylists = keylists
        self.dictionary = dictionary

        self.scrollbar = tk.Scrollbar(orient='vertical', relief='groove')
