import cv2
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master.geometry("700x700")
        self.master.title("一文字タイピング")

        self.create_widgets()


    def create_widgets(self):
        """
        self.frame_cam = tk.LabelFrame(self.master, text = 'Camera')
        self.frame_cam.place(x = 10, y = 10)#位置
        self.frame_cam.configure(width = 500, height = 500)#サイズ
        self.frame_cam.grid_propagate(0)
        """

        self.q_label = tk.LabelFrame(self.master, text="問題：")
        self.q_label.place(x=10, y=10)
        self.q_label.configure(width = 500, height = 500)#サイズ
        self.q_label.grid_propagate(0)

        self.q_label2 = tk.Label(self, text="tkinter", width=5, anchor="w", font=("",20))

        self.ans_label = tk.Label(self, text="解答：", font=("",20))

        self.canvas1 = tk.Canvas(self.q_label)
        self.canvas1.configure(width = 10, height = 10)
        self.canvas1.grid(column = 0, row = 0, padx = 10, pady = 10)


def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
