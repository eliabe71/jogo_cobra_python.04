import pygame
from Cobrinha import Cobra
from ajuda import Ajuda
from Recordes import Recordes
class Menu:
    def __init__(self):
        try:
            pygame.init()
        except:
            print("Eliabe")

        tela = pygame.display.set_mode((600,600));
        cor_fundo = (255,255,255)

        pygame.font.init()

        fonte_default = pygame.font.get_default_font()
        fonte = "Cambria"
        try:
            estilo_fonte = pygame.font.SysFont(fonte,40)
        except:
            estilo_fontetilo_fonte = pygame.font.SysFont(fonte_default,40)

        cor = (255,165,0)
        cor2 = (200,165,0)

        iniciar = estilo_fonte.render("JOGAR",True,(255,255,255))
        recordes = estilo_fonte.render("RECORDES",True,(255,255,255))
        ajuda = estilo_fonte.render("AJUDA",True,(255,255,255))
        sair = estilo_fonte.render("SAIR",True,(255,255,255))
        imagem = pygame.image.load("Imagens/fundo.png")
        back = pygame.image.load("Imagens/gramado.jpg")
        ini = True
        while ini:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                     ini = False
                     pygame.quit()
            #pygame.mouse.set_cursor(cursor)
            a = pygame.mouse.get_pressed()
            print(a)
            b= pygame.mouse.get_pos()
            
            tela.blit(back, (0,0,600,600))
            tela.blit(imagem, (0,0,600,600))
            
            
            #tela.fill(cor_fundo)
            tela.fill(cor,(250,280,140,50))
            tela.blit(iniciar,(260,280))
            
            #ajuda
            tela.fill(cor,(50,350,140,50))
            tela.blit(ajuda,(60,350))
            
            #recordes
            tela.fill(cor,(210,350,215,50))
            tela.blit(recordes,(220,350))

            #Sair
            tela.fill(cor,(450,350,105,50))
            tela.blit(sair,(460,350))

            
             ##botaão iniciar.        
            if 250<= b[0]<=390 and 280<=b[1]<=330:
                tela.fill(cor2,(245,275,150,60))
                tela.blit(iniciar,(260,280))
                pygame.display.update()
                
            ##botão do ajuda.
            if 50<= b[0]<=190 and 350<=b[1]<=400:
                tela.fill(cor2,(45,345,150,60))
                tela.blit(ajuda,(60,350))
                pygame.display.update()

            #recordes
            if 210<= b[0]<=425 and 350<=b[1]<=400:
                tela.fill(cor2,(205,345,225,60))
                tela.blit(recordes,(220,350))
                pygame.display.update()


            ##sair
            if 450<= b[0]<=555 and 350<=b[1]<=400:
                tela.fill(cor2,(445,345,115,60))
                tela.blit(sair,(460,350))
                pygame.display.update()   
            #Jogar
            if 250<= b[0]<=390 and 280<=b[1]<=330 and a[0]:
                Cobra()
                
            #Ajuda
            if 50<= b[0]<=190 and 350<=b[1]<=400 and a[0]:
                Ajuda()
            #Recordes
            if(210<= b[0]<=425 and 350<=b[1]<=400) and a[0]:
                Recordes()
             
            #Sair    
            if 450<= b[0]<=555 and 350<=b[1]<=400 and a[0]:
               pygame.quit()
               break
               
         
            pygame.display.update()         
        pygame.quit()

    

    
