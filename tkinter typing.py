import tkinter as tk

#TKクラス生成
frm = tk.Tk()
#画面サイズ
frm.geometry('600x400')
#画面タイトル
frm.title('一文字タイピング')
#画面をそのまま表示
frm.mainloop()
#ラベル
lbl = tk.Label(text='数値')
lbl.place(x=30, y=70)
