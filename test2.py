import tkinter as tk

class MainWindow():
    counter = 0
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Test")
        self.window.geometry("800x500")


        #新規DBの名前を入力するテキストボックスの処理
        dbname_label = tk.Label(self.window, text = "新規作成するデータベースの名前を入力してください", font = ("Helvetica", 10))
        dbname_label.place(x=80, y=10)
        dbname_value = tk.Entry(width=20)
        dbname_value.place(x=175, y=30)

        #新規主キーの名前を入力するテキストボックスの処理
        prikey_label = tk.Label(self.window, text = "主キーを入力してください", font = ("Helvetica", 10))
        prikey_label.place(x=80, y=60)

        prikey_value = tk.Entry(width=20)
        prikey_value.place(x=175, y=80)


                #新規サブキー1
        subkey1_label = tk.Label(self.window, text = "サブキー1を入力してください", font = ("Helvetica", 10))
        subkey1_label.place(x=80, y=110)
        subkey1_value = tk.Entry(width=20)
        subkey1_value.place(x=175, y=130)


            
        #新規サブキー2
        subkey2_label = tk.Label(self.window, text = "サブキー2を入力してください", font = ("Helvetica", 10))
        subkey2_label.place(x=80, y=160)
        subkey2_value = tk.Entry(width=20)
        subkey2_value.place(x=175, y=180)


            #新規サブキー3
        subkey3_label = tk.Label(self.window, text = "サブキー3を入力してください", font = ("Helvetica", 10))
        subkey3_label.place(x=80, y=210)
        subkey3_value = tk.Entry(width=20)
        subkey3_value.place(x=175, y=230)


            #新規サブキー4
        subkey4_label = tk.Label(self.window, text = "サブキー4を入力してください", font = ("Helvetica", 10))
        subkey4_label.place(x=80, y=260)
        subkey4_value = tk.Entry(width=20)
        subkey4_value.place(x=175, y=280)


        
        button = tk.Button(self.window,text = "次へ", command=self.btn_click_to_confirm)
        button.pack(side="top")

        self.window.mainloop()
        
    def btn_click_to_confirm(self):
        self.counter += 1
        
        t = tk.Toplevel(self.window)
        t.wm_title("Create Window")
        
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

if __name__ == "__main__":
        MainWindow()