'''
QR kódgenerátor

pip install qrcode  - szükséges a  modul telepítéshez
pip install pyqrcode- szükséges a  modul telepítéshez


'''


import pyqrcode
import tkinter as tk

def generate_qr():
    qr = pyqrcode.create(entry.get())
    qr.png('qr.png', scale=8)
    img = tk.PhotoImage(file="qr.png")
    label.config(image=img)
    label.image = img

root = tk.Tk()
root.title("QKód generátor")
root.geometry("410x500")          # Az ablak mérete
root.configure(bg='Goldenrod')

leiras = tk.Label(root, text="             ", bg='Goldenrod', font=('Arial', 19)) #felirat
leiras.grid(row=0, column=0, columnspan=2, padx=10, pady=5)


entry = tk.Entry(root)
entry.grid(row=1, column=2,columnspan=2,)

button = tk.Button(root, text="   Kód generálása   ", command=generate_qr)
button.grid(row=2, column=2, padx=20, pady=10,columnspan=2)

label_szoveg= tk.Label(text='  Add meg a szöveget:  ',bg='Goldenrod',font=('Arial', 13))
label_szoveg.grid(row=1, column=0,columnspan=2,)

label = tk.Label(root,bg='Goldenrod')
label.grid(row=4, column=1, padx=10, pady=10, columnspan=3, sticky="nsew")

root.mainloop()
