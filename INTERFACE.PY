import tkinter as tk
from tkinter import messagebox
import random
import pygame

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogos")
        
        self.menu_frame = tk.Frame(self.root, bg="#f9f9f9")
        self.menu_frame.pack(pady=20)
        
        self.title_label = tk.Label(self.menu_frame, text="Bem-vindo(a) aos Jogos!", font=("Arial", 20, "bold"), bg="#f9f9f9")
        self.title_label.pack()
        
        self.description_label = tk.Label(self.menu_frame, text="Escolha um jogo para jogar:", font=("Arial", 14), bg="#f9f9f9")
        self.description_label.pack(pady=10)
        
        self.guess_button = tk.Button(self.menu_frame, text="Adivinhe o Número", font=("Arial", 12), command=self.start_guess_game)
        self.guess_button.pack(pady=5)
        
        self.tic_tac_toe_button = tk.Button(self.menu_frame, text="Jogo da Velha", font=("Arial", 12), command=self.start_tic_tac_toe_game)
        self.tic_tac_toe_button.pack(pady=5)
        
        self.sudoku_button = tk.Button(self.menu_frame, text="Sudoku", font=("Arial", 12), command=self.start_sudoku_game)
        self.sudoku_button.pack(pady=5)
        
        self.snake_button = tk.Button(self.menu_frame, text="Snake", font=("Arial", 12), command=self.start_snake_game)
        self.snake_button.pack(pady=5)
        
    def start_guess_game(self):
        guess_game = GuessGame()
        
    def start_tic_tac_toe_game(self):
        tic_tac_toe_game = TicTacToeGame()
        
    def start_sudoku_game(self):
        sudoku_game = SudokuGame()
        
    def start_snake_game(self):
        snake_game = SnakeGame()

class GuessGame:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Adivinhe o Número")
        
        self.secret_number = random.randint(1, 100)
        self.guesses = 0
        
        self.label = tk.Label(self.root, text="Adivinhe o número entre 1 e 100:")
        self.label.pack()
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(self.root, text="Adivinhar", command=self.check_guess)
        self.button.pack(pady=5)
        
    def check_guess(self):
        guess = int(self.entry.get())
        self.guesses += 1
        
        if guess == self.secret_number:
            messagebox.showinfo("Adivinhe o Número", "Parabéns! Você acertou em {} tentativas.".format(self.guesses))
            self.root.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Adivinhe o Número", "Tente um número maior.")
        else:
            messagebox.showinfo("Adivinhe o Número", "Tente um número menor.")

class TicTacToeGame:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Jogo da Velha")
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", width=10, height=5, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
                
        self.status_label = tk.Label(self.root, text="Vez do jogador X")
        self.status_label.grid(row=3, columnspan=3, pady=5)
        
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win():
                messagebox.showinfo("Jogo da Velha", "Jogador {} venceu!".format(self.current_player))
                self.root.destroy()
            elif self.check_draw():
                messagebox.showinfo("Jogo da Velha", "Empate!")
                self.root.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text="Vez do jogador {}".format(self.current_player))
                
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

class SudokuGame:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Sudoku")
        
       #COLOCAR O SUDOKU AQUI QUANDO ESTIVER PRONTO
        
        pass

class SnakeGame:
    def __init__(self):
        pygame.init()

        COR_FUNDO = (0, 0, 0)
        COR_COBRA = (0, 255, 0)
        COR_COMIDA = (255, 0, 0)

        largura_tela = 640
        altura_tela = 480

        tamanho = 20 #cobra e comida

        tela = pygame.display.set_mode((largura_tela, altura_tela))#tela
        pygame.display.set_caption("Jogo da Cobrinha")

        relogio = pygame.time.Clock()#velocidade

        # Função para desenhar a cobrinha
        def desenhar_cobrinha(cobrinha):
            for parte in cobrinha:
                pygame.draw.rect(tela, COR_COBRA, (parte[0], parte[1], tamanho, tamanho))

        def gerar_comida():
            x = random.randint(0, largura_tela - tamanho) // 20 * 20#aparecer comidinhas hummm
            y = random.randint(0, altura_tela - tamanho) // 20 * 20
            return x, y

        def jogo():
            sair = False
            fim_de_jogo = False #funções reais do jogo
            velocidade = 10

            #posições iniciais da cobrinha e comida
            cobrinha = [(largura_tela // 2, altura_tela // 2)]
            dx = 0
            dy = 0

            comida_x, comida_y = gerar_comida()

            while not sair:
                while fim_de_jogo:
                    tela.fill(COR_FUNDO)
                    fonte = pygame.font.Font(None, 36)
                    texto = fonte.render("Fim de jogo! Pressione R para recomeçar ou Q para sair.", True, COR_COBRA)
                    tela.blit(texto, (largura_tela // 2 - texto.get_width() // 2, altura_tela // 2 - texto.get_height() // 2))
                    pygame.display.update()

                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            sair = True
                            fim_de_jogo = False
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_q:
                                sair = True
                                fim_de_jogo = False
                            elif evento.key == pygame.K_r:
                                jogo()

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        sair = True
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_LEFT and dx != tamanho:
                            dx = -tamanho
                            dy = 0
                        elif evento.key == pygame.K_RIGHT and dx != -tamanho:
                            dx = tamanho
                            dy = 0
                        elif evento.key == pygame.K_UP and dy != tamanho:
                            dx = 0
                            dy = -tamanho
                        elif evento.key == pygame.K_DOWN and dy != -tamanho:
                            dx = 0
                            dy = tamanho

                if not sair:
                    tela.fill(COR_FUNDO)

                    cabeca_x = cobrinha[0][0] + dx
                    cabeca_y = cobrinha[0][1] + dy

                    if cabeca_x < 0 or cabeca_x >= largura_tela or cabeca_y < 0 or cabeca_y >= altura_tela:
                        fim_de_jogo = True

                    
                    if (cabeca_x, cabeca_y) in cobrinha[1:]:#se ela colidir consigo mesma
                        fim_de_jogo = True

                    if cabeca_x == comida_x and cabeca_y == comida_y:
                        comida_x, comida_y = gerar_comida()#ver se ela comeu a comida
                        velocidade += 1
                    else:
                        
                        cobrinha.pop()#remover o segmento

                    cobrinha.insert(0, (cabeca_x, cabeca_y))#posição nova

                    desenhar_cobrinha(cobrinha)
                    pygame.draw.rect(tela, COR_COMIDA, (comida_x, comida_y, tamanho, tamanho))

                    pygame.display.update()

                    relogio.tick(velocidade)

            pygame.quit()

        jogo()

        pass

root = tk.Tk()
app = App(root)
root.mainloop()
