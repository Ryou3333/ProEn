import tkinter as tk

#TKクラス生成
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
root.mainloop()
