import tkinter as tk



def display():
    texto = input_.get()
    mostra_text.config(text=texto)




janela  =  tk.Tk()
janela.geometry('700x300')
janela.title('DISPLAY TEXT')
janela.configure(bg = "blue")

# grid() 

mostra_text1 = tk.Label(janela, text=' FKSDLFKÇLSDFK', fg='BLACK', bg='black', font=('arial', 15))
mostra_text1.grid(row=3, column=0, padx=10, pady=10)

texto = tk.Label(janela, text ='Isso é um texto', font=('arial', 20), fg="white", bg='black')
texto.grid(row=0, column=1, padx=10)

input_ = tk.Entry(janela,   fg='white',font=('arial',15), bg='black')
input_.grid(row=1, column=1, padx=10, pady=10)
# input_.bind("<Return>")


btn = tk.Button(janela, text='Mostre o texto', font=('arial',20), fg='yellow', bg='black', command=display)
btn.grid(row=2, column=1, padx=10, pady=10)
janela.bind("<Return>", lambda event: display())




mostra_text = tk.Label(janela, text='', fg='white', bg='black', font=('arial', 15))
mostra_text.grid(row=3, column=1, padx=10)



janela.mainloop()


























