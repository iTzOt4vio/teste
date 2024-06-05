def adicionar_usuario(dados):
    return f"Usuário {dados['nome']} adicionado."

def remover_usuario(dados):
    return f"Usuário {dados['nome']} removido."

def usuario(valor, usuario):
    comandos = {
        "adicionar": adicionar_usuario,
        "remover": remover_usuario
    }
    return comandos.get(valor, usuario)


resposta = input("adicionar/remover: \n")
usuariores = input("Usuário: \n")
seletor = usuario(resposta, usuariores)