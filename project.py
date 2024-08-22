import tkinter as tk
from tkinter import messagebox, simpledialog

# Inicializando a lista de funcionários e o ID global
lista_funcionarios = []
id_global = 4297914  # Altere para o número do seu RU

# Função para cadastrar um funcionário
def cadastrar_funcionario():
    global id_global
    nome = simpledialog.askstring("Cadastro de Funcionário", "Por favor entre com o nome do Funcionário:")
    setor = simpledialog.askstring("Cadastro de Funcionário", "Por favor entre com o setor do Funcionário:")
    salario = simpledialog.askfloat("Cadastro de Funcionário", "Por favor entre com o salário do Funcionário:")
    
    if nome and setor and salario is not None:
        funcionario = {
            'id': id_global,
            'nome': nome,
            'setor': setor,
            'salario': salario
        }
        
        lista_funcionarios.append(funcionario.copy())  # Copiando o dicionário para a lista
        messagebox.showinfo("Cadastro", "Funcionário cadastrado com sucesso!")
        id_global += 1  # Incrementando o ID global após o cadastro

# Função para consultar funcionários
def consultar_funcionarios():
    consulta_opcao = simpledialog.askinteger("Consulta de Funcionários", 
        "Escolha a opção desejada:\n1 - Consultar Todos os Funcionários\n2 - Consultar Funcionário por id\n3 - Consultar Funcionário(s) por setor\n4 - Cancelar", 
        minvalue=1, maxvalue=4)
    
    if consulta_opcao == 1:
        resultado = ""
        for func in lista_funcionarios:
            resultado += f"----------------\nid: {func['id']}\nnome: {func['nome']}\nsetor: {func['setor']}\nsalário: {func['salario']}\n"
        messagebox.showinfo("Consulta", resultado if resultado else "Nenhum funcionário cadastrado.")
    elif consulta_opcao == 2:
        id_func = simpledialog.askinteger("Consulta por ID", "Digite o id do funcionário:")
        resultado = ""
        for func in lista_funcionarios:
            if func['id'] == id_func:
                resultado = (f"----------------\nid: {func['id']}\nnome: {func['nome']}\nsetor: {func['setor']}\nsalário: {func['salario']}\n")
                break
        messagebox.showinfo("Consulta", resultado if resultado else "Id não encontrado.")
    elif consulta_opcao == 3:
        setor = simpledialog.askstring("Consulta por Setor", "Digite o setor do(s) funcionário(s):")
        resultado = ""
        for func in lista_funcionarios:
            if func['setor'].lower() == setor.lower():
                resultado += (f"----------------\nid: {func['id']}\nnome: {func['nome']}\nsetor: {func['setor']}\nsalário: {func['salario']}\n")
        messagebox.showinfo("Consulta", resultado if resultado else "Nenhum funcionário encontrado para o setor informado.")
    elif consulta_opcao == 4:
        return

# Função para remover um funcionário
def remover_funcionario():
    id_func = simpledialog.askinteger("Remover Funcionário", "Digite o id do funcionário a ser removido:")
    
    global lista_funcionarios
    for func in lista_funcionarios:
        if func['id'] == id_func:
            lista_funcionarios.remove(func)
            messagebox.showinfo("Remoção", "Funcionário removido com sucesso!")
            return
    messagebox.showwarning("Remoção", "Id inválido.")

# Função para encerrar o programa
def encerrar_programa():
    root.destroy()

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Funcionários")
root.geometry("300x200")

# Label de boas-vindas
welcome_label = tk.Label(root, text="Bem-vindo à empresa do Anderson Fortes Dias", padx=20, pady=20)
welcome_label.pack()

# Botões do menu principal
btn_cadastrar = tk.Button(root, text="Cadastrar Funcionário", command=cadastrar_funcionario)
btn_cadastrar.pack(pady=5)

btn_consultar = tk.Button(root, text="Consultar Funcionário", command=consultar_funcionarios)
btn_consultar.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Funcionário", command=remover_funcionario)
btn_remover.pack(pady=5)

btn_encerrar = tk.Button(root, text="Encerrar Programa", command=encerrar_programa)
btn_encerrar.pack(pady=5)

# Iniciando a interface gráfica
root.mainloop()
