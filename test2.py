import os, tkinter, tkinter.filedialog, tkinter.messagebox

def func():
    global value
    print("in the function =",EditBox1.get())
    value = EditBox1.get()

# ウインドウ
root = tkinter.Tk()
root.title(u"テストプログラム")
root.geometry("400x300")

# データ数入力
Static1 = tkinter.Label(text=u'データ数')
Static1.place(x=5,y=5)
EditBox1 = tkinter.Entry(width=5)
EditBox1.place(x=100, y=5)

b = tkinter.Button(text='Exec', command=func)
b.pack()

root.mainloop()

print("value=",value) # データが格納されたことを確認