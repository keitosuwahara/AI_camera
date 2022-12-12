import tkinter as tk

root = tk.Tk()

# コールバック関数をネストして定義
def callback(i):
    def x():
        print(str(i)+"が押されました")
    return x
    
buttons = []
for i in range(5):
    # コールバック関数にボタン番号の値を引数で渡す
    buttons.append(tk.Button(root,text=i,command=callback(i)))
    buttons[i].pack(fill="x")

root.mainloop()