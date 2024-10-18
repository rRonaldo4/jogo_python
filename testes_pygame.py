 def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
def receber_movimento(jogador):
    linha = int(input(f"Jogador {jogador}, insira a linha (0, 1 ou 2): "))
    coluna = int(input(f"Jogador {jogador}, insira a coluna (0, 1 ou 2): "))
    return linha, coluna
def atualizar_tabuleiro(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador
def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False
