import cv2
import tkinter as tk
import random
import time
import sys
from mediapipe import *
#import mediapipe as mp
import math
import threading
import winsound
import threading


landmark_line_ids = [
    (0, 1), (1, 5), (5, 9), (9, 13), (13, 17), (17, 0),  # 掌
    (1, 2), (2, 3), (3, 4),         # 親指
    (5, 6), (6, 7), (7, 8),         # 人差し指
    (9, 10), (10, 11), (11, 12),    # 中指
    (13, 14), (14, 15), (15, 16),   # 薬指
    (17, 18), (18, 19), (19, 20),   # 小指
]

mp_hands = mediapipe.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,                # 最大検出数
    min_detection_confidence=0.7,   # 検出信頼度
    min_tracking_confidence=0.7     # 追跡信頼度
)

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.master.geometry("700x700")
        self.master.title("じゃんけん")

        global JANKEN_EVENT_TIMES,index,janken_game_count,win_count,confirm_count,start_count,img,img_gu,img_pa,img_choki,aiko_flag
        JANKEN_EVENT_TIMES = 10 #じゃんけん回数をいじれる

        self.img_gu = tk.PhotoImage(file = "dataset/gu.png", width = 500, height = 500)
        self.img_choki = tk.PhotoImage(file = "dataset/.png", width = 500, height = 500)
        self.img_pa = tk.PhotoImage(file = "dataset/pa.png", width = 500, height = 500)

        self.create_widgets()

        self.cap = cv2.VideoCapture(0)
        self.capread()#処理を速くするために事前にreadしておく

    def end():
        root.destroy()

    def end_button(self,event):
        sys.exit()

    def capread(self):
        global success,media_img,media_img,results
        self.success, self.media_img = self.cap.read()
        self.media_img = cv2.flip(self.media_img, 1)
        self.results = hands.process(cv2.cvtColor(self.media_img, cv2.COLOR_BGR2RGB))

    def create_widgets(self):
        global canvas1
        self.canvas1 = tk.Canvas(self.master, bg = "#deb887", height = 300, width = 300)
        self.canvas1.place(x=0,y=0)

        self.canvas1.create_image(30,30,image='', anchor = tk.NW,tag ='im')

        self.Button2 = tk.Button(self.master, text = '終わる', width = 0, height = 0)
        self.Button2.place(x=40)
        self.Button2.bind("<Button-1>",self.end_button)
        self.Button3 = tk.Button(self.master, text = 'ゲームスタートボタン', width = 0, height = 0)
        self.Button3.place(x=100)
        self.Button3.bind("<Button-1>",self.start_timer)

        self.text1 = tk.StringVar()
        self.text1.set("あなたが出したのは")
        self.label1 = tk.Label(self.master,textvariable = self.text1)
        self.label1.place(x=300,y=300)
        self.text2 = tk.StringVar()
        self.text2.set("")
        self.label2 = tk.Label(self.master,textvariable = self.text2)
        self.label2.place(x=300,y=320)
        self.text3 = tk.StringVar()
        self.text3.set("")
        self.label3 = tk.Label(self.master,textvariable = self.text3)
        self.label3.place(x=300,y=340)
        self.text4 = tk.StringVar()
        self.text4.set("")
        self.label4 = tk.Label(self.master,textvariable = self.text4)
        self.label4.place(x=300,y=360)
        self.text5 = tk.StringVar()
        self.text5.set("")
        self.label5 = tk.Label(self.master,textvariable = self.text5)
        self.label5.place(x=300,y=360)


    def start_state(self):
        self.confirm_count = 0
        self.start_count = 0
        self.win_count = 0
        self.janken_game_count = 1
        self.aiko_flag = 0
        self.text2.set("")
        self.text3.set("")
        self.text4.set("")
        self.text5.set("")

    def start_timer(self,event):
        self.start_state()#初期化
        self.text1.set("勝った回数は："+ str(self.win_count)+"　/　勝負回数は：" + str(self.janken_game_count))
        self.playsound()
        self.after(1700,self.random_img)
        self.after(1725,self.janken)

    def start_timer2(self):
        self.confirm_count = 0
        self.start_count = 0
        self.text1.set("勝った回数は："+ str(self.win_count)+"　/　勝負回数は：" + str(self.janken_game_count))
        self.playsound()
        self.after(1700,self.random_img)
        self.after(1725,self.janken)

    def aiko_state(self):
        self.after(1700,self.random_img)
        self.after(1730,self.janken)

    def reStart(self):
        if self.start_count ==  0:
            self.start_count = 1
            self.janken_game_count += 1
        if self.janken_game_count <= JANKEN_EVENT_TIMES:
            self.after(1000,self.start_timer2)
        else:
            self.after(1,self.display_result)

    def playsound(self):
        if self.aiko_flag == 0:
            sound = lambda: winsound.PlaySound("dataset/jankenpon_01.wav", winsound.SND_FILENAME)
            thread_playsound_jankenpon = threading.Thread(target = sound)
            thread_playsound_jankenpon.start()
        else:
            sound = lambda: winsound.PlaySound("dataset/aikodesho_01.wav", winsound.SND_FILENAME)
            thread_playsound_aiko = threading.Thread(target = sound)
            thread_playsound_aiko.start()
            self.aiko_flag = 0

    def win_state(self):
        self.text3.set("勝ち")
        if self.confirm_count == 0:
             self.confirm_count = 1
             self.win_count += 1

    def display_result(self):
        self.text5.set("おしまい")


    def random_img(self):
        self.index = random.randint(0,2)
        self.canvas1.delete('im')#一旦削除してimgを上書き
        if self.index == 0:
            self.canvas1.create_image(30,30,image=self.img_gu, anchor = tk.NW,tag = 'im')
        elif self.index == 1:
            self.canvas1.create_image(30,30,image=self.img_choki, anchor = tk.NW,tag = 'im')
        else:
            self.canvas1.create_image(30,30,image=self.img_pa, anchor = tk.NW,tag = 'im')

    def janken(self):#mediapipe
        self.success, self.media_img = self.cap.read()
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4')); #高速化（あまり意味ない？
        self.media_img = cv2.flip(self.media_img, 1)
        self.results = hands.process(cv2.cvtColor(self.media_img, cv2.COLOR_BGR2RGB))
        self.text2.set("読み取れませんでした。もう一度やり直してください")
        if self.results.multi_hand_landmarks:
            # 検出した手の数分繰り返し
            for self.h_id, self.hand_landmarks in enumerate(self.results.multi_hand_landmarks):
                def calcDistance(p0,p1):
                    a1 = p1.x - p0.x
                    a2 = p1.y - p0.y
                    return math.sqrt(a1*a1+a2*a2)
                self.index_finger_dis = calcDistance(self.hand_landmarks.landmark[0],self.hand_landmarks.landmark[8])
                self.pinky_finger_dis = calcDistance(self.hand_landmarks.landmark[0],self.hand_landmarks.landmark[20])
                if self.index_finger_dis < 0.35 and self.pinky_finger_dis < 0.3:
                    self.text2.set("あなたはグーを出した")
                    hand_value = 0
                    break
                elif self.index_finger_dis > 0.35 and self.pinky_finger_dis < 0.3:
                    self.text2.set("あなたはチョキを出した")
                    hand_value = 1
                    break
                elif self.index_finger_dis > 0.35 and self.pinky_finger_dis > 0.3:
                    self.text2.set("あなたはパーを出した")
                    hand_value = 2
                    break
            if hand_value == self.index:
                self.text3.set("あいこ")
                self.aiko_flag = 1
                self.playsound()
                self.aiko_state()
            elif hand_value == 0 and self.index == 1:
                self.win_state()
                self.reStart()
            elif hand_value == 0 and self.index == 2:
                self.text3.set("負け")
                self.reStart()
            elif hand_value == 1 and self.index == 0:
                self.text3.set("負け")
                self.reStart()
            elif hand_value == 1 and self.index == 2:
                self.win_state()
                self.reStart()
            elif hand_value == 2 and self.index == 0:
                self.win_state()
                self.reStart()
            else:
                self.text3.set("負け")
                self.reStart()


def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
