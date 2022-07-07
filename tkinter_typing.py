import tkinter as tk

'''#TKクラス生成
root = tk.Tk()
#画面サイズ
root.geometry('600x400')
#画面タイトル
root.title('一文字タイピング')
#ラベル
label = tk.Label(text='文字')
label.place(x=30, y=70)
#テキストボックス
text = tk.Entry(width=20)
text.place(x=90, y=70)

#text.delete(0, tk.END)
#text.insert(tk.END,"1234")
#画面をそのまま表示
root.mainloop()'''

QUESTION = ["tkinter", "geometry", "widgets", "messagebox", "configure", "label"]

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("600x400")
        master.title("一文字タイピング")

        self.index = 0

        self.create_widgets()

        self.master.bind("<KeyPress>", self.type_event)

    def create_widgets(self):
        self.q_label = tk.Label(self, text="問題：", font=("",20))
        self.q_label.grid(row=0, column=0)
        self.q_label2 = tk.Label(self, text="tkinter", width=10, anchor="w", font=("",20))
        self.q_label2.grid(row=0, column=1)
        self.ans_label = tk.Label(self, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)
        self.ans_label2 = tk.Label(self, text="", width=10, anchor="w", font=("",20))
        self.ans_label2.grid(row=1, column=1)
        self.result_label = tk.Label(self, text="正否", font=("",20))
        self.result_label.grid(row=2, column=0, columnspan=2)

    def type_event(self, event):
        if event.keysym == "Return":
            if self.q_label2["text"] == self.ans_label2["text"]:
                self.result_label.configure(text="正解！", fg="red")
            else:
                self.result_label.configure(text="残念！", fg="blue")

            self.ans_label2.configure(text="")

            self.index += 1
            self.q_label2.configure(text=QUESTION[self.index])

        else:
            self.ans_label2["text"] += event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root)
    root.mainloop()
