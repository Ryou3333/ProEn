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

class Application(tk.Frame):
    def _init_(self, game):
        super()._init_(game)
        self.pack()

        game.geometry("600x400")
        game.title("一文字タイピング")

        self.create_widgets()

    def create_widgets(self):
        self.q_label = tk.Label(self, text="問題：", font=("",20))
        self.q_label.grid(row=0, column=0)
        self.q_labe2 = tk.Label(self, text="tkinter", width=5, anchor="w", font=("",20))
        self.q_labe2.grid(row=0, column=1)
        self.ans_label = tk.Label(self, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)


"""
_init_のアンダーバーを__init__にしたら動いた（アンダーバー2つと2つ）
"""
