import pygame
try:
    pygame.init()
except:
    print("pygame não pode ser iniciado")
class Ajuda:
    def __init__(self):
        print("Ajuda")
        #arq_ajuda = open("textos/ajuda.txt","r")
           
        tela = pygame.display.set_mode((660,500))
        pygame.font.init()
        fonte_default = pygame.font.get_default_font()
        cambria = "Cambria"
        try:
            t_fonte = pygame.font.SysFont(cambria,17)
        except:
            t_fonte = pyagme.font.SysFont(fonte_default,17)
        try:
            aju_fonte = pygame.font.SysFont(cambria,25)
        except:
            aju_fonte = pyagme.font.SysFont(fonte_default,25)
        texto_voltamenu = t_fonte.render("Volta Ao Menu", True,(0,0,0))
        texto_sair = t_fonte.render("Sair", True,(0,0,0))
        texto_ajuda = aju_fonte.render("AJUDA",True,(0,0,0))
      
        entra = True     
        while entra:
            
            arq_ajuda = open("textos/ajuda.txt")
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    entra = False
            ##eventos do mouse.
            pos_mouse = pygame.mouse.get_pos()
            botao_mouse = pygame.mouse.get_pressed()

            ###ajuda
            tela.fill((255,255,255))
            tela.blit(texto_ajuda,(290,10))
            ##botão de sair:
            tela.fill((181,181,181),(10,445,55,38))
            tela.blit(texto_sair,(20,450))
            ##botão de voltar  ao menu:
            tela.fill((181,181,181),(510,445,140,38))
            tela.blit(texto_voltamenu,(520,450))
            a = arq_ajuda.readline()
            h =60
            while True:
                if a.strip() == "-Acabou-":
                    break
                if a.strip()[0:3] == "1. " or a.strip()[0:3] == "2. " or a.strip()[0:3] == "3. ":
                    texto  = t_fonte.render(a.strip(),True,(0,0,0))
                    tela.blit(texto,(10,h))
                else:
                    texto  = t_fonte.render(a.strip(),True,(0,0,0))
                    tela.blit(texto,(30,h))
                a = arq_ajuda.readline()    
                h+=18
            ## eventos para o (sair)
            if 10 <=pos_mouse[0] <= 65 and 445 <=pos_mouse[1] <= 483:
                tela.fill((210,210,210),(10,445,55,38))
                tela.blit(texto_sair,(30,460))
            if 10 <=pos_mouse[0] <= 65 and 445 <=pos_mouse[1] <= 483 and botao_mouse[0]:
                pygame.quit()
                break
            ## eventos para o (voltar ao menu)
            if 510<=pos_mouse[0] <= 650 and 445<= pos_mouse[1]<= 483:
                tela.fill((210,210,210),(510,445,140,38))
                tela.blit(texto_voltamenu,(530,460))
            if 510<=pos_mouse[0] <= 650 and 445<= pos_mouse[1]<= 483 and botao_mouse[0]:
                from menu import Menu
                Menu()
                break
            
            pygame.display.update()
            arq_ajuda.close()              

