import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
import sys
import time
import threading
import random

QUESTION = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Application(tk.Frame):
    # 呪文
    def __init__(self, *args, **kwargs):
        # 呪文
        tk.Tk.__init__(self, *args, **kwargs)

        # ウィンドウタイトルを決定
        self.title("Tkinter change page")

        # ウィンドウの大きさを決定
        self.geometry("800x600")

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
        #self.frame1.grid(row=0, column=0, sticky="nsew")
        def create_widgets(self):
            self.q_label = tk.Label(self.frame1, text="問題：", font=("",20))
            self.q_label.grid(row=0, column=0)
            self.q_label2 = tk.Label(self.frame1, text=QUESTION[self.index2], width=10, anchor="w", font=("",20))
            self.q_label2.grid(row=0, column=1)
            self.ans_label = tk.Label(self.frame1, text="解答：", font=("",20))
            self.ans_label.grid(row=1, column=0)
            self.ans_label2 = tk.Label(self.frame1.frame1, text="", width=10, anchor="w", font=("",20))
            self.ans_label2.grid(row=1, column=1)
            self.result_label = tk.Label(self, text="", font=("",20))
            self.result_label.grid(row=2, column=0, columnspan=2)

            #時間計測用のラベル
            self.time_label = tk.Label(self.frame1, text="", font=("",20))
            self.time_label.grid(row=3, column=0, columnspan=2)

            self.flg2 = True

        #キー入力時のイベント処理
        def type_event(self, event):
            #入力値がEnterの場合は答え合わせ
            if event.keysym == "Return":
                if self.q_label2["text"] == self.ans_label2["text"]:
                    self.result_label.configure(text="ピンポン！", fg="red")
                    self.correct_cnt += 1
                    i = 1
                else:
                    self.result_label.configure(text="ブブー！", fg="blue")

                #解答欄をクリア
                self.ans_label2.configure(text="")

                #次の問題を出題
                self.index += 1
                if self.correct_cnt == 10:
                    self.flg = False
                    self.q_label2.configure(text="終了！")
                    messagebox.showinfo("リザルト", f"あなたのスコアは{self.correct_cnt}/{self.index}問正解です。")
                    sys.exit(0)

                self.index2 = random.randint(0,14)
                self.q_label2.configure(text=QUESTION[self.index2])

            elif event.keysym == "BackSpace":
                text = self.ans_label2["text"]
                self.ans_label2["text"] = text[:-1]
            else:
                #入力値がEnter以外の場合は文字入力としてラベルに追記する
                self.ans_label2["text"] += event.keysym

        def timer(self):
            self.second = 0
            self.flg = True
            while self.flg:
                self.second += 1
                self.time_label.configure(text=f"経過時間：{self.second}秒")
                time.sleep(1)
        # タイトルラベル作成
        #self.titleLabel = tk.Label(self.frame1, text="Frame 1", font=('Helvetica', '35'))
        #self.titleLabel.pack(anchor='center', expand=True)
        # フレーム1からmainフレームに戻るボタン
        #self.back_button = tk.Button(self.frame1, text="Back", command=lambda : self.changePage(self.main_frame))
        #self.back_button.pack()
#--------------------------------------------------------------------------

        #main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, page):
        '''
        画面遷移用の関数
        '''
        page.tkraise()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
