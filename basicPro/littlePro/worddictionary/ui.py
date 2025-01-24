import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, keylists, dictionary):
        super().__init__()
        self.geometry("400x400")
        self.title("词库")
        self.resizable(False, False)
        self.keylists = keylists
        self.dictionary = dictionary
        self.config(bg="#C2FCEE")
        # relief定义边框样式，groove是凹槽样式
        self.scrollbar = tk.Scrollbar(orient='vertical', relief='groove')

    def create(self):
        self.initControls()
        self.initLayouts()
        self.initKeys(keyid=self.keylists)

    def initControls(self):
        self.listControl = tk.Listbox(bg='#83FCE3', border=1, width=8, height=12, yscrollcommand=self.scrollbar.set)
        for n, line in enumerate(self.keylists):
            self.listControl.insert(n, line)

        self.listControl.bind("<<ListboxSelect>>", self.initKeys)
        self.scrollbar.config(command=self.listControl.yview)
        self.canvas = tk.Canvas(bg='#83FCE3', border=1, width=190, height=190, relief='groove')
        # cursor 游标样式
        self.quitBtn = tk.Button(cursor='target', bg='#C2FCEE', text='quit', command=self.quit)

        self.frame = tk.Frame(bg="#C2FCEE",width=180,height=180)

        self.btnTranslation = tk.Button(self.frame, cursor='target', bg="#C2FCEE", text='Translation', command=self.showTranslation)
        self.btnRole = tk.Button(self.frame, cursor='target', bg="#C2FCEE", text='Role', command=self.showRole)
        self.btnDefinition = tk.Button(self.frame, cursor='target', bg="#C2FCEE", text='Definition', command=self.showDefinition)

        self.labelTranslation = tk.Label(self.frame, bg='#C2FCEE', text='', font=('Roboto', '15'))
        self.labelRole = tk.Label(self.frame, bg='#C2FCEE', text='', font=('Roboto', '15'))
        self.labelDefinition = tk.Label(self.frame, bg='#C2FCEE', text='', font=('Roboto', '15'))


    def initLayouts(self):
        self.listControl.grid(column=0,row=0,padx=15,pady=10)
        self.scrollbar.grid(column=1,row=0,sticky="NS",pady=10)
        self.canvas.grid(column=2,row=0,padx=15,pady=15,sticky='N')
        self.quitBtn.grid(columnspan=1,row=1,pady=20,sticky='S')
        self.frame.grid(column=2,row=1)

        self.btnTranslation.grid(column=2,row=1,pady=5,padx=5,ipadx=10)
        self.btnRole.grid(column=2,row=2,pady=5,padx=1,ipadx=14)
        self.btnDefinition.grid(column=2,row=3,pady=5,padx=5,ipadx=4)

        self.labelTranslation.grid(column=3,row=1,pady=5,padx=20)
        self.labelRole.grid(column=3,row=2,pady=5,padx=20)
        self.labelDefinition.grid(column=3,row=3,pady=5,padx=20)

    def initKeys(self, keyid):
        global select_keys
        keyid = self.listControl.curselection()
        keylists = self.listControl
        select_keys = ",".join(keylists.get(i) for i in keyid)
        self.canvas.delete('all')
        self.canvas.create_text(100, 100, text=select_keys, font=('Roboto', '45'))


    def showTranslation(self):
        self.labelTranslation['text'] = self.dictionary[select_keys][0]

    def showRole(self):
        self.labelRole['text'] = self.dictionary[select_keys][1]

    def showDefinition(self):
        self.labelDefinition['text'] = self.dictionary[select_keys][2]
