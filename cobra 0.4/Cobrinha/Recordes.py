import pygame

class Recordes:
    def __init__(self):
        try:
            pygame.init()
        except:
            print("pygame não pode ser iniciado")
        tela = pygame.display.set_mode((660,500))
        pygame.font.init()
        
        cambria = "Cambria"
        f_deault = pygame.font.get_default_font()
        try:
            tit_fonte = pygame.font.SysFont(cambria,25)
            texto_fonte = pygame.font.SysFont(cambria,19)
        except:
            tit_fonte = pygame.font.SysFont(f_default,25)
            texto_fonte = pygame.font.SysFont(f_default,19)

        tit_recordes = tit_fonte.render("Recordes",True,(255,255,255))
        texto_sair = texto_fonte.render("Sair",True,(255,255,255))
        texto_volta = texto_fonte.render("Voltar Ao Menu",True,(255,255,255))
        texto_nome = texto_fonte.render("Nome do jogador",True,(255,255,255))
        texto_pontos = texto_fonte.render("Pontução",True,(255,255,255))
        lista_recordes = [[]]
        entra = True
        while entra:
            try:
                arq_recordes = open("textos/Recordes.txt","r")
            except:
                print("ad")
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    entra = False
                      
            #eventos do mouse
            pos_mouse = pygame.mouse.get_pos()
            botao_mouse = pygame.mouse.get_pressed()
            
            #titulo
            tela.fill((25,200,135))
            tela.blit(tit_recordes,(290,20))
            #botão de sair:
            tela.fill((181,181,181),(10,445,55,38))
            tela.blit(texto_sair,(20,450))
            #botão de voltar  ao menu:
            tela.fill((181,181,181),(490,445,160,38))
            tela.blit(texto_volta,(500,450))

            tela.blit(texto_nome,(30,70))
            tela.blit(texto_pontos,(500,70))
            
            lista_recordes = []
            
            while True:
                lista_aux = [0,0]
                arq = arq_recordes.readline()
                if arq.strip() == "":
                    break
                lista_aux[0] = int(arq.strip())
                arq = arq_recordes.readline()
                lista_aux[1] = arq.strip()
                lista_recordes.append(lista_aux)
            lista_ordenada = sorted(lista_recordes,reverse=True)
            h = 100
            colocacao = 1
            for li in lista_ordenada:
                pont = texto_fonte.render(str(li[0]),True,(255,255,255))
                nome = texto_fonte.render(str(colocacao)+". "+li[1],True,(255,255,255))
                tela.blit(pont,(500,h))
                tela.blit(nome,(30,h))
                h+= 20
                colocacao += 1
                if h >= 400:
                    break
            if 10 <=pos_mouse[0] <= 65 and 445 <=pos_mouse[1] <= 483:
                tela.fill((210,210,210),(10,445,55,38))
                tela.blit(texto_sair,(30,460))
            if 10 <=pos_mouse[0] <= 65 and 445 <=pos_mouse[1] <= 483 and botao_mouse[0]:
                pygame.quit()
                break
            if 490<=pos_mouse[0] <= 650 and 445<= pos_mouse[1]<= 483:
                tela.fill((210,210,210),(490,445,160,38))
                tela.blit(texto_volta,(515,460))
            if 490<=pos_mouse[0] <= 650 and 445<= pos_mouse[1]<= 483 and botao_mouse[0]:
                from menu import Menu
                Menu()
                break
            pygame.display.update()

