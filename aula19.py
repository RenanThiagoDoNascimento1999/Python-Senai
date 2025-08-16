import tkinter as tk




def display():
    texto = input_.get()
    mostra_text.config(text=texto)





janela  =  tk.Tk()
janela.geometry("300x300")
janela.title('DISPLAY TEXT')


# pack() # grid() # place()


texto = tk.Label(janela, text ='Isso é um texto', background='black', font=('Lao UI', 30), fg="white")
texto.pack(pady=10)


input_ = tk.Entry(janela,  font=(30), fg='purple')
input_.pack(pady=30)



btn = tk.Button(janela, text='Mostre o texto', font=(25), fg='white', bg='black', command=display)
btn.pack(pady=20)



mostra_text = tk.Label(janela, text='')
mostra_text.pack(pady=20)




janela.mainloop()




























