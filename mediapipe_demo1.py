import cv2
from mediapipe import *
#import mediapipe as mp
import math
"""
#from scipy.spatial import distance(いらない)
#-----------------#
#MediaPipeをコマンドプロンプトでpip installしていないとエラー出る
#リンク↓↓
#https://qiita.com/akira2768922/items/c660129cc45cce384e90
#-----------------#
"""
# landmarkの繋がり表示用
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

def calcDistance(p0,p1):#2点間の距離
    a1 = p1.x - p0.x
    a2 = p1.y - p0.y
    return math.sqrt(a1*a1+a2*a2)

cap = cv2.VideoCapture(0)   # カメラのID指定
if cap.isOpened():
    while True:
        # カメラから画像取得
        success, img = cap.read()
        if not success:
            continue
        img = cv2.flip(img, 1)          # 画像を左右反転
        img_h, img_w, _ = img.shape     # サイズ取得

        # 検出処理の実行
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            # 検出した手の数分繰り返し
            for h_id, hand_landmarks in enumerate(results.multi_hand_landmarks):

                # landmarkの繋がりをlineで表示
                for line_id in landmark_line_ids:#line_idが(0,1)的な表示、landmark_line_idsが
                    # 1点目座標取得
                    lm = hand_landmarks.landmark[line_id[0]]
                    lm_pos1 = (int(lm.x * img_w), int(lm.y * img_h))
                    # 2点目座標取得
                    lm = hand_landmarks.landmark[line_id[1]]
                    lm_pos2 = (int(lm.x * img_w), int(lm.y * img_h))
                    # line描画
                    cv2.line(img, lm_pos1, lm_pos2, (128, 0, 0), 1)
                    #デバッグ用のprint
                    #print(line_id)
                    #print(landmark_line_ids)

                # landmarkをcircleで表示
                z_list = [lm.z for lm in hand_landmarks.landmark]
                z_min = min(z_list)
                z_max = max(z_list)
                for lm in hand_landmarks.landmark:
                    lm_pos = (int(lm.x * img_w), int(lm.y * img_h))
                    lm_z = int((lm.z - z_min) / (z_max - z_min) * 255)
                    cv2.circle(img, lm_pos, 3, (255, lm_z, lm_z), -1)

                # 検出情報をテキスト出力
                # - テキスト情報を作成
                hand_texts = []
                for c_id, hand_class in enumerate(results.multi_handedness[h_id].classification):
                    hand_texts.append("#%d-%d" % (h_id, c_id))
                    hand_texts.append("- Index:%d" % (hand_class.index))
                    hand_texts.append("- Label:%s" % (hand_class.label))
                    hand_texts.append("- Score:%3.2f" % (hand_class.score * 100))
                # - テキスト表示に必要な座標など準備
                lm = hand_landmarks.landmark[0]
                lm_x = int(lm.x * img_w) - 50
                lm_y = int(lm.y * img_h) - 10
                lm_c = (64, 0, 0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                # - テキスト出力
                for cnt, text in enumerate(hand_texts):
                    cv2.putText(img, text, (lm_x, lm_y + 10 * cnt), font, 0.3, lm_c, 1)
                #テキスト表示
                #dis = distance(hand_landmarks.landmark)

                #cv2.putText(img,"Sleepy eyes. Wake up!",
                #    (10,180), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)
                """
                cv2.putText(img,"hands:{}".format(dis),
                (10,180), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)

                thumb=0#親指
                index_finger=0#人差し指
                middleFinger=0#中指
                third_finger=0#薬指
                pinky_finger=0#小指
                """
                index_finger_dis = calcDistance(hand_landmarks.landmark[0],hand_landmarks.landmark[8])
                pinky_finger_dis = calcDistance(hand_landmarks.landmark[0],hand_landmarks.landmark[20])

                #確認用（format()の中に上↑のdisを代入すると確認できます）
                cv2.putText(img,"hands:{}".format(index_finger_dis),
                    (10,180), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)
                """
                確認したところ、
                (index_finger_dis < 0.35 and pinky_finger_dis < 0.3)でグー
                (index_finger_dis > 0.35 and pinky_finger_dis < 0.3)でチョキ
                (index_finger_dis > 0.35 and pinky_finger_dis > 0.3)でパー
                """

                #画面にグーチョキパーを表示（日本語は？？？になるのでローマ字）
                if(index_finger_dis < 0.35 and pinky_finger_dis < 0.3):
                    cv2.putText(img,"hands:gu",
                        (30,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)
                elif(index_finger_dis > 0.35 and pinky_finger_dis < 0.3):
                    cv2.putText(img,"hands:tyoki",
                        (30,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)
                elif(index_finger_dis > 0.35 and pinky_finger_dis > 0.3):
                    cv2.putText(img,"hands:paa",
                        (30,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)

        # 画像の表示
        cv2.imshow("MediaPipe Hands", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q') or key == 0x1b:
            break

cap.release()
