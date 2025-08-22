import sqlite3
import tkinter as tk
from tkinter import messagebox



def criar_banco():
    conn =  sqlite3.connect('dabase.db')
    return conn

def salvar_dados():
    nome  = input_nome.get()
    email = input_email.get()
    
    if nome and email:
        banco =  criar_banco()
        c = banco.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS dados(
                nome TEXT NOT NULL,
                email TEXT NOT NULL                
        ) 
    ''' )
        
        
        banco.commit()
        c.execute('INSERT INTO dados (nome, email)values(?,?)',(nome,email))
        banco.commit()
        banco.close()

        messagebox.showinfo('Sucesso', 'dados salvos com sucesso')
        input_nome.delete(0,tk.END)#DELATAR O INPUT 
        input_email.delete(0,tk.END)
    else:
        messagebox.showerror('Erro', 'Preencha corretamente')    



root  =  tk.Tk()

root.geometry('650x350')

text_label =  tk.Label(root, text='Nome', font = (70))
text_label.pack()

input_nome  =  tk.Entry(root, font = (70))
input_nome.pack()

email_label =  tk.Label(root, text ='E-mail', font = (70))
email_label.pack()

input_email  =  tk.Entry(root, font = (70))
input_email.pack()

btn = tk.Button(root, text = 'salvar', command=salvar_dados, font = (70), width=30 )
btn.pack(pady=30)

root.mainloop()































