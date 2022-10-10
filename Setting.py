from tkinter import Tk


class Setting:
    def __init__(self) -> None:
        self.SUFFIX = {"c": "C/C++", "cpp": "C/C++", "java": "Java", "py": "Python", "js": "Type/JavaScript",
                       "ts": "Type/JavaScript", "asm": "Assembly", "html": "Html/CSS", "h": "C/C++", "css": "Html/CSS"}
        self.FILETYPE = {"C/C++": ['c', 'cpp', 'h'], "Java": ['java'], "Python": ['py'],
                         "Type/JavaScript": ['js', 'ts'], "Html/CSS": ['html', 'css'], "Assembly": ['asm']}

    def creatWindow(self):
        self.Root = Tk()
        self.Root.geometry('200x300+450+250')
        self.Root.title("Settings")
        self.creatWidget()
        self.Root.mainloop()

    def creatWidget(self):
        pass
