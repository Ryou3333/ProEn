import cv2
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master.geometry("600x400")
        self.master.title("一文字タイピング")

        #self.create_widgets()

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.master.geometry("700x700")
        self.master.title("Tkinter with Video Streaming and Capture")

def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
