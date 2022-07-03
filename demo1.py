import cv2
import tkinter as tk

class Application(tk.Frame):
    def _init_(self, master = None):
        super()._init_(master)
        #self.pack()

        self.master.title("一文字タイピング")
        self.master.geometry("600x400")

        self.create_widgets()



def main():
    root = tk.Tk()
    app = Application(master = root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
