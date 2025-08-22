import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Tema da interface
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# Banco
def criar_banco():
    return sqlite3.connect('ESTOQUE_LOJA_DE_ESPORTES.db')

# Produtos de esporte e seus preços
produtos_esporte = {
    'Bola': 50.0,
    'Tênis': 200.0,
    'Camiseta': 80.0,
    'Rede': 150.0,
    'Luvas': 40.0,
    'Raquete': 300.0
}

# Cadastro de cliente
def salvar_dados():
    nome = campo_usuario.get()
    cpf = campo_cpf.get()
    email = campo_email.get()
    senha = campo_senha.get()

    if nome == '' or cpf == '' or email == '' or senha == '':
        messagebox.showerror('Erro', 'Preencha todos os campos!')
        return
    if not cpf.isdigit() or len(cpf) != 11:
        messagebox.showerror('Erro', 'CPF deve ter 11 números!')
        return
    if len(senha) < 3:
        messagebox.showerror('Erro', 'Senha deve ter pelo menos 3 dígitos!')
        return

    banco = criar_banco()
    c = banco.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        cpf TEXT,
        email TEXT,
        senha TEXT
    )''')
    c.execute('INSERT INTO clientes (usuario, cpf, email, senha) VALUES (?, ?, ?, ?)',
              (nome, cpf, email, senha))
    banco.commit()
    banco.close()

    messagebox.showinfo('Sucesso', 'Cliente cadastrado!')
    campo_usuario.delete(0, 'end')
    campo_cpf.delete(0, 'end')
    campo_email.delete(0, 'end')
    campo_senha.delete(0, 'end')

# Cadastro de compra
def cadastrar_compra():
    cliente_id = campo_cliente_id.get()
    produto = campo_produto.get()
    quantidade = campo_quantidade.get()

    if cliente_id == '' or produto == '' or quantidade == '':
        messagebox.showerror('Erro', 'Preencha todos os campos da compra!')
        return
    if produto not in produtos_esporte:
        messagebox.showerror('Erro', f'Produto inválido! Veja a lista: {", ".join(produtos_esporte.keys())}')
        return

    preco = produtos_esporte[produto]  # pega o preço do produto
    total = preco * int(quantidade)

    banco = criar_banco()
    c = banco.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS compras(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto TEXT,
        quantidade INTEGER,
        preco REAL
    )''')
    c.execute('INSERT INTO compras (cliente_id, produto, quantidade, preco) VALUES (?, ?, ?, ?)',
              (cliente_id, produto, int(quantidade), total))
    banco.commit()
    banco.close()

    messagebox.showinfo('Sucesso', f'Compra do produto {produto} cadastrada!\nTotal: R${total:.2f}')
    campo_cliente_id.delete(0, 'end')
    campo_produto.delete(0, 'end')
    campo_quantidade.delete(0, 'end')

# Listar compras
def lista_compras():
    cliente_id = campo_cliente_id.get()
    if cliente_id == '':
        messagebox.showwarning('Aviso', 'Digite o ID do cliente!')
        return

    banco = criar_banco()
    c = banco.cursor()
    c.execute('SELECT produto, quantidade, preco FROM compras WHERE cliente_id=?', (cliente_id,))
    compras = c.fetchall()
    banco.close()

    if len(compras) == 0:
        messagebox.showinfo('Compras', 'Nenhuma compra encontrada!')
        return

    texto = 'Compras do cliente:\n'
    total_geral = 0
    for produto, quantidade, preco in compras:
        texto += f'{produto} - {quantidade} x R${produtos_esporte[produto]:.2f} = R${preco:.2f}\n'
        total_geral += preco
    texto += f'\nTotal Geral: R${total_geral:.2f}'
    messagebox.showinfo('Compras', texto)

# Janela principal
app = ctk.CTk()
app.geometry('400x700')
app.title('Cadastro Clientes e Compras')

# --- Cliente ---
ctk.CTkLabel(app, text='--- CADASTRO DO CLIENTE ---').pack(pady=5)
campo_usuario = ctk.CTkEntry(app, placeholder_text='Usuário', width=250)
campo_usuario.pack(pady=5)
campo_cpf = ctk.CTkEntry(app, placeholder_text='CPF (11 números)', width=250)
campo_cpf.pack(pady=5)
campo_email = ctk.CTkEntry(app, placeholder_text='Email', width=250)
campo_email.pack(pady=5)
campo_senha = ctk.CTkEntry(app, placeholder_text='Senha (min 3 dígitos)', width=250, show='*')
campo_senha.pack(pady=5)
ctk.CTkButton(app, text='Cadastrar Cliente', command=salvar_dados).pack(pady=10)

# --- Compra ---
ctk.CTkLabel(app, text='--- CADASTRO DA COMPRAS ---').pack(pady=5)
campo_cliente_id = ctk.CTkEntry(app, placeholder_text='ID do Cliente', width=250)
campo_cliente_id.pack(pady=5)
# Mostrar produtos e preços
produtos_texto = ', '.join([f'{p} (R${preco:.2f})' for p, preco in produtos_esporte.items()])
ctk.CTkLabel(app, text='Produtos e preços: ' + produtos_texto).pack(pady=5)

campo_produto = ctk.CTkEntry(app, placeholder_text='Produto', width=250)
campo_produto.pack(pady=5)
campo_quantidade = ctk.CTkEntry(app, placeholder_text='Quantidade', width=250)
campo_quantidade.pack(pady=5)
#CRIANDO OS BOTOES 
ctk.CTkButton(app, text='Cadastrar Compra', command=cadastrar_compra).pack(pady=10)
ctk.CTkButton(app, text='Ver Compras do Cliente', command=lista_compras).pack(pady=10)

app.mainloop()
























