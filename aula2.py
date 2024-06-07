def adicionar_usuario(dados):
    return f"Usuário {dados['nome']} adicionado."

def remover_usuario(dados):
    return f"Usuário {dados['nome']} removido."

def executar_comando(comando, nome_usuario):
    dados = {"nome": nome_usuario}
    comandos = {
        "adicionar": adicionar_usuario,
        "remover": remover_usuario
    }
    funcao = comandos.get(comando)
    if funcao:
        return funcao(dados)
    else:
        return "Comando inválido."

# Entrada do usuário
resposta = input("adicionar/remover: \n")
usuariores = input("Usuário: \n")

# Executa o comando e exibe o resultado
resultado = executar_comando(resposta, usuariores)
print(resultado)
# test de mudança