import pygame
import wx
from random import randint

class Cobra:
    def __init__(self):
        arq_recordes = open("textos/Recordes.txt", "a")
        # Variáveis para dimensionar a tela
        largura = 630
        tamanho = altura = largura
        dimensao = (largura + 200, altura)
        nome_jogador = ""
        # pontuação
        pontos = 0

        # Direções
        cima = 1
        direita = 2
        baixo = 3
        esquerda = 4

        # Direção inicial
        direcao = cima

        try:
            pygame.init()
        except:
            print("O pygame não pode ser iniciado")
        # A cobra
        cobra = [(300, 300), (315, 300), (330, 300), (345, 300)]

        # Fontes
        pygame.font.init()
        fonte_padrao = pygame.font.get_default_font()
        try:
            t_fonte = pygame.font.SysFont("Impact", 20)
        except:
            t_fonte = pygame.font.SysFont(fonte_padrao, 20)

        # Criando a tela
        tela = pygame.display.set_mode(dimensao)

        # Definindo o estilo da cobra
        cor_cobra = pygame.Surface((15, 15))
        cor_cabeca_cobra = pygame.Surface((15, 15))
        cor_cobra.fill((255, 255, 0), (0, 0, 13, 13))
        cor_cabeca_cobra.fill((255, 255, 200), (0, 0, 13, 13))
        ##poaMaça.
        while True:
            posX = randint(30, largura - 30)
            posY = randint(30, largura - 30)
            pos_maca = (posX // 15 * 15, posY // 15 * 15)

            if pos_maca not in cobra:
                break
            else:
                continue
          
        maca = pygame.image.load("Imagens/maca.png")
        apple = pygame.image.load("Imagens/apple.png")

        
        def musica():
            pygame.mixer.init()
            pygame.mixer.music.load("Sons/musica.mp3")
            pygame.mixer.music.play(loops = -1)
        def mus_gameover1():
            pygame.mixer.init()
            pygame.mixer.music.load("Sons/gameover1.wav")
            pygame.mixer.music.play(loops = 1)
        def mus_gameover2():
            pygame.mixer.init()
            pygame.mixer.music.load("Sons/gameover2.wav")
            pygame.mixer.music.play(loops = 1)
        
        # Tela de inicio em fica aguardando confirmação do jogador
        texto_inicio = t_fonte.render("Pressione Enter para iniciar", True, (255, 255, 255))

        def inicio():
            tela.blit(texto_inicio, (250, 250))

        # funcção que pinta a cobra
        def pinta(lista):
            tela.blit(cor_cabeca_cobra, lista[0])
            for i in range(1, len(lista)):
                tela.blit(cor_cobra, lista[i])

        # Função que pinta a maçã
        def pinta_maca():
            tela.blit(maca, pos_maca)

        # Defina a borda que é uma lista de posições
        borda = []
        # Estilo da borda
        cor_borda = pygame.Surface((15, 15))
        cor_borda.fill((30, 30, 110))

        # Preenche a borda
        for i in range(0, tamanho, 15):
            borda.append((0, i))
            borda.append((tamanho - 15, i))
            borda.append((i, 0))
            borda.append((i, tamanho - 15))

        # Pinta a pequeno retângulos que juntos formam a borda
        def pinta_borda():
            for p in range(0, altura, 15):
                tela.blit(cor_borda, (p, 0))
                tela.blit(cor_borda, (p, altura - 15))
                tela.blit(cor_borda, (0, p))
                tela.blit(cor_borda, (altura - 15, p))

        # Função que é responsável pelo movimento da cobra
        def anda(dir):
            tamanho = len(cobra)
            for i in range(tamanho - 1, 0, -1):
                cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])
            if (dir == cima):
                cobra[0] = (cobra[0][0], cobra[0][1] - 15)
            if (dir == direita):
                cobra[0] = (cobra[0][0] + 15, cobra[0][1])
            if (dir == baixo):
                cobra[0] = (cobra[0][0], cobra[0][1] + 15)
            if (dir == esquerda):
                cobra[0] = (cobra[0][0] - 15, cobra[0][1])
              
        timer = pygame.time.Clock()

        fim = pygame.image.load("Imagens/gameover.jpg")
        texto_reiniciar = t_fonte.render("Reiniciar", True, (255, 255, 255))
        texto_menu = t_fonte.render("Voltar Ao Menu", True, (255, 255, 255))
        texto_sair = t_fonte.render("Sair", True, (255, 255, 255))
        sair = True
        ini = True
        while ini:
            pos_mouse = pygame.mouse.get_pos()
            pos_botao = pygame.mouse.get_pressed()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ini = False
                    pygame.quit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        sair = False
                        ini = False

            if ini == False:
                break

            tela.fill((40, 100, 0), (15, 15, 615, 615))
            tela.fill((130, 150, 240), (630, 0, 850, 650))
            pinta_borda()
            # botão reiniciar
            tela.blit(texto_reiniciar, (650, 200))
            tela.blit(texto_menu, (650, 300))
            tela.blit(texto_sair, (650, 400))
            texto_potuacao = t_fonte.render("P O N T U A Ç Ã O :  {}".format(pontos), True, (255, 255, 255))
            tela.blit(texto_potuacao, (650, 60))
            inicio()
            # pinta botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230:
                tela.fill((255, 102, 0), (640, 190, 150, 40))
                tela.blit(texto_reiniciar, (640, 200))
            # pinta botao menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330:
                tela.fill((255, 102, 0), (640, 290, 150, 40))
                tela.blit(texto_menu, (640, 300))
            # pintabotao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430:
                tela.fill((255, 102, 0), (640, 390, 150, 40))
                tela.blit(texto_sair, (640, 400))
            pygame.display.update()

            # clique do botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230 and pos_botao[0]:
                Cobra()
                break
            # clique do botao de menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330 and pos_botao[0]:
                from menu import Menu
                Menu()
                break

            # clique do botao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430 and pos_botao[0]:
                pygame.quit()
                break

        evento = False
        continua = False
        velocidade = 6
        intervalo_min = 150
        intervalo_max = 180
        apl = True
        m = intervalo_max
        aux = None
        tempo = 0
        min = 20
        musica()
        while not sair:
            
            timer.tick(velocidade)
            
            pos_mouse = pygame.mouse.get_pos()
            pos_botao = pygame.mouse.get_pressed()
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    pygame.quit()
                # Eventos de comando para cobrinha
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if direcao == baixo:
                            direcao = baixo
                        else:
                            direcao = cima
                            evento = True
                            anda(direcao)
                    elif event.key == pygame.K_DOWN:
                        if direcao == cima:
                            direcao = cima
                        else:
                            direcao = baixo
                            evento = True
                            anda(direcao)
                    elif event.key == pygame.K_RIGHT:
                        if direcao == esquerda:
                            direcao = esquerda
                        else:
                            direcao = direita
                            evento = True
                            anda(direcao)
                    elif event.key == pygame.K_LEFT:
                        if direcao == direita:
                            direcao = direita
                        else:
                            direcao = esquerda
                            evento = True
                            anda(direcao)

            # Uma maneira de corrigir um bug que estava acontecendo
            if evento == False:
                anda(direcao)

            # Testa se a cobra colidiu com ela mesma
            for c in range(4, len(cobra)):
                if cobra[0] == cobra[c]:
                    sair = True
                    continua = True

            for i in range(0, len(borda)):
                if cobra[0] == borda[i]:
                    sair = True
                    continua = True
            if sair == True:
                pygame.mixer.music.stop()
                break

            # Testa se a cobra comeu a maçã
            if cobra[0] == pos_maca:
                pontos += 10
                cobra.append((0, 0))
                # Cria uma nova posicção aleatória para a maçã
                while True:
                    posX = randint(30, largura - 30)
                    posY = randint(30, largura - 30)
                    pos_maca = (posX // 15 * 15, posY // 15 * 15)

                    if pos_maca not in cobra:
                        break
                    else:
                        continue
            tela.fill((40, 100, 0), (15, 15, 615, 615))
            tela.fill((130, 150, 240), (630, 0, 850, 650))
            texto_potuacao = t_fonte.render("P O N T U A Ç Ã O :  {}".format(pontos), True, (255, 255, 255))
            tela.blit(texto_potuacao, (650, 60))
            tela.blit(texto_reiniciar, (650, 200))
            tela.blit(texto_menu, (650, 300))
            tela.blit(texto_sair, (650, 400))
            pinta(cobra)
            pinta_borda()
            pinta_maca()
            
            if apl:
                if pontos == intervalo_min:
                    m = randint(intervalo_min,intervalo_max)
                    m = m//10*10
                    print("GHghgJH")
                    apl = False
            if pontos == m:
                print("dasfasfasffsa")
                while True:
                    posA = randint(30, largura - 30)
                    posB = randint(30, largura - 30)
                    pos_apple = (posA// 15 * 15, posB // 15 * 15)

                    if pos_apple not in cobra and pos_apple not in pos_maca:
                        intervalo_min += 150
                        intervalo_max = intervalo_min+30
                        aux = m
                        m = intervalo_max
                        tempo =0
                        break
                    else:
                        continue
            if pontos == aux and tempo<65 and pos_apple != None:       
                tela.blit(apple,pos_apple)
                tempo += 1
            else:
                pos_apple = None

            #Testa se a cobra comeu a "apple"
            if cobra[0] == pos_apple:
                ult = len(cobra) - 1
                for i in range(ult,ult-5,-1):
                    cobra.remove(cobra[i])
                    pos_apple = None
                
            incremento = 0.5
            if pontos >= min:
                velocidade += incremento
                min += 20
            # pinta botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230:
                tela.fill((255, 102, 0), (640, 190, 150, 40))
                tela.blit(texto_reiniciar, (640, 200))
            # pinta botao menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330:
                tela.fill((255, 102, 0), (640, 290, 150, 40))
                tela.blit(texto_menu, (640, 300))
            # pintabotao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430:
                tela.fill((255, 102, 0), (640, 390, 150, 40))
                tela.blit(texto_sair, (640, 400))
            pygame.display.update()

            # clique do botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230 and pos_botao[0]:
                Cobra()
                break
            # clique do botao de menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330 and pos_botao[0]:
                from menu import Menu
                pygame.mixer.music.stop()
                Menu()
                break

            # clique do botao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430 and pos_botao[0]:
                pygame.quit()
                break

            pygame.display.update()
            evento = False

        # Game Over
        timer.tick(4)
        mus_gameover2()
        while continua:
            pos_mouse = pygame.mouse.get_pos()
            pos_botao = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continua = False
            tela.blit(fim, (110, 200))
            tela.fill((130, 150, 240), (630, 0, 850, 650))
            texto_potuacao = t_fonte.render("P O N T U A Ç Ã O :  {}".format(pontos), True, (255, 255, 255))
            tela.blit(texto_potuacao, (650, 60))
            tela.blit(texto_reiniciar, (650, 200))
            tela.blit(texto_menu, (650, 300))
            tela.blit(texto_sair, (650, 400))
            # pinta botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230:
                tela.fill((255, 102, 0), (640, 190, 150, 40))
                tela.blit(texto_reiniciar, (640, 200))
            # pinta botao menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330:
                tela.fill((255, 102, 0), (640, 290, 150, 40))
                tela.blit(texto_menu, (640, 300))
            # pintabotao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430:
                tela.fill((255, 102, 0), (640, 390, 150, 40))
                tela.blit(texto_sair, (640, 400))
                
            pygame.display.update()

            # clique do botao de reiniciar
            if 640 <= pos_mouse[0] <= 850 and 190 <= pos_mouse[1] <= 230 and pos_botao[0]:
                Cobra()
                
                break
            # clique do botao de menu
            if 640 <= pos_mouse[0] <= 850 and 290 <= pos_mouse[1] <= 330 and pos_botao[0]:
                from menu import Menu
                Menu()
                break

            # clique do botao sair
            if 640 <= pos_mouse[0] <= 850 and 390 <= pos_mouse[1] <= 430 and pos_botao[0]:
                pygame.quit()
                break
            app = wx.App()
            caixa = wx.Frame(None, -1)
            caixa.SetDimensions(0,0,200,50)

            
            di = wx.TextEntryDialog(caixa, "Digite seu nome","Registro da pontuação")
            
            if di.ShowModal() == wx.ID_OK:
                nome_jogador = di.GetValue()
                print(nome_jogador)
                if nome_jogador == "":
                    nome_jogador = "Anônimo"
                di.Destroy()
                arq_recordes.write("{}\n".format(pontos))
                arq_recordes.write(nome_jogador+"\n")
                arq_recordes.close()
                Cobra()
                break
            if di.ShowModal() == wx.ID_CANCEL:
                nome_jogador = "Anônimo"
                print(nome_jogador)
                di.Destroy()
                arq_recordes.write("{}\n".format(pontos))
                arq_recordes.write(nome_jogador+"\n")
                arq_recordes.close()
                Cobra()
                break
            pygame.display.update();
        
        pygame.quit()

