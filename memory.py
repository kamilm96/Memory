import tkinter as tk


gui = tk.Tk()
gui.geometry('800x600')
gui.title('Memory')
color = (99,241,188)
gui['background']='#63f1bd'
gui.iconbitmap(r'C:\Users\Lenovo\Desktop\Kurs Python\Projekt\logo.ico')
new_game_button = tk.Button(gui,text="Nowa gra").pack()
rating_button = tk.Button(gui,text="Tablica wyników").pack()
gui.mainloop()
