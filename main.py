'''
import tkinter as tk
import tkinter.ttk as ttk

def change_app():
    frame_app.tkraise()

def change_main():
    frame.tkraise()

if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("tkinter application")
    root.geometry("600x400")

    # rootメインウィンドウのグリッドを 1x1 にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="メインウィンドウ")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="アプリウィンドウに移動", command=change_app)

    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()

    # アプリフレームの作成と設置
    frame_app = ttk.Frame(root)
    frame_app.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text="アプリウィンドウ")
    entry1_frame_app = ttk.Entry(frame_app)
    button_change_frame_app = ttk.Button(frame_app, text="メインウィンドウに移動", command=change_main)

    # 各種ウィジェットの設置
    label1_frame_app.pack()
    entry1_frame_app.pack()
    button_change_frame_app.pack()

    # frameを前面にする
    frame.tkraise()

    root.mainloop()
'''
import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
import sys
import time
import threading
import random

class App(tk.Tk):
    # 呪文
    def __init__(self, *args, **kwargs):
        # 呪文
        tk.Tk.__init__(self, *args, **kwargs)

        # ウィンドウタイトルを決定
        self.title("Tkinter change page")

        # ウィンドウの大きさを決定
        self.geometry("800x600")

        '''
        self.index = 0
        self.index2 = random.randint(0,25)

        #正解数カウント用
        self.correct_cnt = 0

        self.create_widgets()

        #経過時間スレッドの開始
        t = threading.Thread(target=self.timer)
        t.start()

        #Tkインスタンスに対してキーイベント処理を実装
        self.master.bind("<KeyPress>", self.type_event)
        '''

        # ウィンドウのグリッドを 1x1 にする
        # この処理をコメントアウトすると配置がズレる
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
#-----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = tk.Label(self.main_frame, text="Main Page", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # フレーム1に移動するボタン
        self.changePageButton = tk.Button(self.main_frame, text="Go to frame1", command=lambda : self.changePage(self.frame1))
        self.changePageButton.pack()
#--------------------------------------------------------------------------
#-----------------------------------frame1---------------------------------
        # 移動先フレーム作成
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = tk.Label(self.frame1, text="Frame 1", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # フレーム1からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame1, text="Back", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack()
#--------------------------------------------------------------------------

        #main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, page):
        '''
        画面遷移用の関数
        '''
        page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
