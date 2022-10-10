from tkinter import Tk, ttk, IntVar, messagebox
from tkinter import CENTER, N, W


class Setting:
    def __init__(self) -> None:
        self.SUFFIX = {"c": "C/C++", "cpp": "C/C++", "java": "Java", "py": "Python", "js": "Type/JavaScript",
                       "ts": "Type/JavaScript", "asm": "Assembly", "html": "Html/CSS", "h": "C/C++", "css": "Html/CSS"}
        self.TARGETLANG = ["C/C++", "Java", "Python",
                           "Type/JavaScript", "Html/CSS", "Assembly"]
        self.ALLLang = {"C/C++": ['c', 'cpp', 'h'], "Java": ['java'], "Python": ['py'], "Type/JavaScript": [
            'js', 'ts'], "Html/CSS": ['html', 'css'], "Assembly": ['asm'], "C#": ['cs'], "Julia": ['jl'], "PHP": ['php'], "Golang": ['go']}

    def creatWindow(self):
        self.Root = Tk()
        self.Root.geometry('200x300+450+250')
        self.Root.title("Settings")

        self.var_C = IntVar(self.Root)
        self.var_C.set(1)
        self.var_Java = IntVar(self.Root)
        self.var_Java.set(1)
        self.var_Python = IntVar(self.Root)
        self.var_Python.set(1)
        self.var_Html = IntVar(self.Root)
        self.var_Html.set(1)
        self.var_JS = IntVar(self.Root)
        self.var_JS.set(1)
        self.var_Asm = IntVar(self.Root)
        self.var_Asm.set(1)
        self.var_Julia = IntVar(self.Root)
        self.var_Julia.set(0)
        self.var_CS = IntVar(self.Root)
        self.var_CS.set(0)
        self.var_PHP = IntVar(self.Root)
        self.var_PHP.set(0)
        self.var_Go = IntVar(self.Root)
        self.var_Go.set(0)

        self.var_List = [self.var_C, self.var_Java, self.var_Python, self.var_JS,
                         self.var_Html, self.var_Asm, self.var_Julia, self.var_CS, self.var_PHP, self.var_Go]
        self.lang_List = ['C/C++', 'Java', 'Python', 'Type/JavaScript',
                          'Html/CSS', 'Assembly', 'Julia', 'C#', 'PHP', 'Golang']

        self.creatWidget()
        self.Root.mainloop()

    def creatWidget(self):
        self.label01 = ttk.Label(
            self.Root, text="Target language", font=("Consolas", 11), width=200, anchor=CENTER, background="#E8E8E8")
        self.label01.pack(anchor=N)

        self.frame01 = ttk.Frame(self.Root)

        r = 0
        c = 0
        for lang in self.lang_List:
            self.choice = ttk.Checkbutton(
                self.frame01, text=self.lang_List[r*2+c], variable=self.var_List[r*2+c], onvalue=1, offvalue=0, )
            self.choice.grid(row=r, column=c, sticky=W)
            if c == 0:
                c += 1
            else:
                r += 1
                c = 0

        self.frame01.pack(pady=10)

        self.frame02 = ttk.Frame(self.Root)

        self.btn01 = ttk.Button(
            self.frame02, text="Confirm", command=self.updateTargetLang, padding=5)
        self.btn01.grid(row=0, column=0)

        self.btn02 = ttk.Button(
            self.frame02, text="Reset", command=self.resetTargetLang, padding=5)
        self.btn02.grid(row=0, column=1)

        self.frame02.pack(pady=8)

    def updateTargetLang(self):
        ct = 0
        for var in self.var_List:
            if var.get() == 1:
                ct += 1
        if ct > 6:
            messagebox.showinfo("Warning", "No more than 6 languages")
            self.resetTargetLang()

    def resetTargetLang(self):
        for i in range(6):
            self.var_List[i].set(1)
        for i in range(6, 10):
            self.var_List[i].set(0)


if __name__ == "__main__":
    app = Setting()
    app.creatWindow()
