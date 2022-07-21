import cv2
import tkinter as tk
import random
import time
import sys
import mediapipe as mp
import math
import threading
import winsound

janken = [0,1,2]#いらない


landmark_line_ids = [
    (0, 1), (1, 5), (5, 9), (9, 13), (13, 17), (17, 0),  # 掌
    (1, 2), (2, 3), (3, 4),         # 親指
    (5, 6), (6, 7), (7, 8),         # 人差し指
    (9, 10), (10, 11), (11, 12),    # 中指
    (13, 14), (14, 15), (15, 16),   # 薬指
    (17, 18), (18, 19), (19, 20),   # 小指
]

mp_hands = mp.solutions.hands
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
        self.master.title("一文字タイピング")
        self.count = 0
        self.index = 0
        self.hand_value = 0

        self.create_widgets()
        #self.capread()

        self.cap = cv2.VideoCapture(0)



    def end():
        root.destroy()



    def create_widgets(self):
        global canvas1,img,img_gu,img_pa,img_choki,tx
        self.canvas1 = tk.Canvas(self.master, bg = "#deb887", height = 300, width = 300)
        self.canvas1.place(x=0,y=0)

        self.img_gu = tk.PhotoImage(file = "gu.png", width = 500, height = 500)
        self.img_choki = tk.PhotoImage(file = "choki.png", width = 500, height = 500)
        self.img_pa = tk.PhotoImage(file = "pa.png", width = 500, height = 500)
        self.hand_img = ''#空のimg

        self.canvas1.create_image(30,30,image=self.hand_img, anchor = tk.NW,tag ='im')

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

    def start_timer(self,event):
        winsound.PlaySound("jankenpon_01.wav", winsound.SND_FILENAME)
        self.after(1700,self.janken)
    def aiko_timer(self):
        winsound.PlaySound("aikodesho_01.wav", winsound.SND_FILENAME)
        self.after(1600,self.janken)



    def janken(self):
        self.index = random.randint(0,2)
        if self.index == 0:
            self.img = self.img_gu
        elif self.index == 1:
            self.img = self.img_choki
        else:
            self.img = self.img_pa
        self.canvas1.delete('im')#一旦削除してimgを上書き
        self.canvas1.create_image(30,30,image=self.img, anchor = tk.NW,tag = 'im')
        #mediapipe
        #self.count += 1
        self.success, self.media_img = self.cap.read()
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4')); #
        self.media_img = cv2.flip(self.media_img, 1)
        self.media_img_h, self.media_img_w, _ = self.media_img.shape
        self.results = hands.process(cv2.cvtColor(self.media_img, cv2.COLOR_BGR2RGB))
        if self.results.multi_hand_landmarks:
            # 検出した手の数分繰り返し
            for self.h_id, self.hand_landmarks in enumerate(self.results.multi_hand_landmarks):
                def calcDistance(p0,p1):
                    a1 = p1.x - p0.x
                    a2 = p1.y - p0.y
                    return math.sqrt(a1*a1+a2*a2)
                self.index_finger_dis = calcDistance(self.hand_landmarks.landmark[0],self.hand_landmarks.landmark[8])
                self.pinky_finger_dis = calcDistance(self.hand_landmarks.landmark[0],self.hand_landmarks.landmark[20])
                if(self.index_finger_dis < 0.35 and self.pinky_finger_dis < 0.3):
                    self.text2.set("あなたはグーを出した")
                    hand_value = 0
                    break
                elif(self.index_finger_dis > 0.35 and self.pinky_finger_dis < 0.3):
                    self.text2.set("あなたはチョキを出した")
                    hand_value = 1
                    break
                elif(self.index_finger_dis > 0.35 and self.pinky_finger_dis > 0.3):
                    self.text2.set("あなたはパーを出した")
                    hand_value = 2
                    break
            if hand_value == 0 and self.index == 0:
                self.text3.set("あいこ")
                self.aiko_timer()
            elif hand_value == 0 and self.index == 1:
                self.text3.set("勝ち")
            elif hand_value == 0 and self.index == 2:
                self.text3.set("負け")
            elif hand_value == 1 and self.index == 0:
                self.text3.set("負け")
            elif hand_value == 1 and self.index == 1:
                self.text3.set("あいこ")
                self.aiko_timer()
            elif hand_value == 1 and self.index == 2:
                self.text3.set("勝ち")
            elif hand_value == 2 and self.index == 0:
                self.text3.set("勝ち")
            elif hand_value == 2 and self.index == 1:
                self.text3.set("負け")
            else:
                self.text3.set("あいこ")
                self.aiko_timer()


    def end_button(self,event):
        sys.exit()




def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit

    app.mainloop()

if __name__ == "__main__":
    main()
