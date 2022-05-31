import pygame
from pygame.locals import *
import buttons
import time
import random


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
color = (160,169,245)
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Memory')
font = pygame.font.SysFont('Times New Roman', 20)
font1 = pygame.font.SysFont('Times New Roman', 45)
chances = 3

def main_menu():
    window.fill(color)
    new_game = buttons.Button('Nowa gra',150, 50, 325, 300)
    quit = buttons.Button('Wyjście', 150, 50, 325, 355)
    
    quit.change_card(color=(180,180,180))
    new_game.change_card(color=(180,180,180))
    end_game('Witaj w grze w memory!', 300,200)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or quit.clicked_button(window):
                pygame.quit()
        if new_game.clicked_button(window):
            level_1()
        pygame.display.update()
         
    

def show_text(surface, text, x, y):
    text = font.render(text,1, pygame.Color('Black'))
    surface.blit(text, (x,y))
    pygame.display.update()

def win_window(winner,x,y): 
    
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color) 
        info3 = font.render('Zgadłeś, przechodzisz do następnego poziomu!', 1, pygame.Color('Black'))
        window.blit(winner, (x,y)) 
        window.blit(info3, (220,400))

        next_level = buttons.Button('Dalej', 150, 50, 325, 540)
        next_level.change_card(color=(180,180,180))
        if next_level.clicked_button(window):
            level_2()
        pygame.display.update()

def win_window_level_2(winner,x,y): 
    
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color) 
        info3 = font.render('Zgadłeś, przechodzisz do następnego poziomu!', 1, pygame.Color('Black'))
        window.blit(winner, (x,y)) 
        window.blit(info3, (220,400))
        next_level = buttons.Button('Dalej', 150, 50, 325, 540)
        next_level.change_card(color=(180,180,180))
        if next_level.clicked_button(window):
            level_3()
            
        pygame.display.update()

def win_window_level_3(winner,x,y): 
   
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color) 
        info3 = font.render('Gratulacje, przeszedłeś wszystkie poziomy!', 1, pygame.Color('Black'))
        window.blit(winner, (x,y)) 
        window.blit(info3, ((window.get_width()-info3.get_width())/2,2))
            
        next_level = buttons.Button('Od nowa', 150, 50, 325, 540)
        next_level.change_card(color=(180,180,180))
        if next_level.clicked_button(window):
            level_1()
        go_back = buttons.Button('Menu', 150, 50, 10, 540)
        go_back.change_card(color = (180,180,180))
        if go_back.clicked_button(window):
            main_menu()

        pygame.display.update()

def end_game(text,x,y):
    end_game = font.render(text, 1, pygame.Color('Black'))
    back = pygame.Rect((x-10,y-10,end_game.get_width()+20, end_game.get_height()+20))
    pygame.draw.rect(window, 'WHITE', back)
    window.blit(end_game, (x,y))
    pygame.display.update()
    
    


def level_1():
    #sekundnik
    countdown = 5
    last_count = pygame.time.get_ticks()

    #losowanie numerka do wylosowania karty
    tab = [0,1]
    number = random.choice(tab)
    #losowanie dwóch randomowych kart z puli
    tail = [i for i in range(1,11)]
    sample = random.sample(tail,2)
    
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color)
        play_width = 150
        play_height = 250
        go_back = buttons.Button('Menu', 150, 50, 10, 540)
        go_back.change_card(color=(180,180,180))
        global chances

        #powrót do poprzedniego menu
        if go_back.clicked_button(window):
            main_menu()

        if countdown > 0:
            info = font.render('Masz 5 sekund i '+str(chances)+' szanse, zapamiętaj poniższe karty', 1, pygame.Color('Black'))
            window.blit(info, (200,5))
            #sekundnik c.d.
            seconds = font1.render(str(countdown), True, pygame.Color('black'))
            seconds_rect = seconds.get_rect(midbottom = window.get_rect().midbottom)
            window.blit(seconds, seconds_rect)
            
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
            
            
            
            k2 = pygame.image.load('Talia/'+str(sample[0])+'.png')
            k2 = pygame.transform.scale(k2, (play_width, play_height))
             
            k3 = pygame.image.load('Talia/'+str(sample[1])+'.png')
            k3 = pygame.transform.scale(k3, (play_width, play_height))
            
            window.blit(k2, (250,50))
            window.blit(k3, (410,50)) 
            
            
        #moment rozpoczęcia gry
        if countdown == 0:
            
            info = font.render('Wskaż położenie widniejącej na miniaturze karty klikając w pole', 1, pygame.Color('Black'))
            window.blit(info, (150,5))
            e_k2 = buttons.Button('', play_width, play_height, 230,50, bg='navy')
            e_k3 = buttons.Button('', play_width, play_height, 390,50, bg='navy')
            
            #hoover effect
            e_k2.change_card()
            e_k3.change_card()
            
            
            if e_k2.clicked_button(window): 
                if tab[number]==k2:
                    win_window(k2,250,50)
                if tab[number]!= k2:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 270,400)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.',220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)    
                    
            if e_k3.clicked_button(window):
                if tab[number] == k3:
                   win_window(k3,410,50)
                if tab[number] != k3:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 270,400) 
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
            tab = [k2,k3]
            #losowanie karty do odgadnięcia
            if tab[number] == k2:
                small_k2 = pygame.transform.scale(k2, (play_width*0.5, play_height*0.5))
                window.blit(small_k2, (650,30))  
            elif tab[number] == k3:
                small_k3 = pygame.transform.scale(k3, (play_width*0.5, play_height*0.5))
                window.blit(small_k3, (650,30))     

        pygame.display.update()
        clock.tick(10)

def level_2():
    #sekundnik
    countdown = 5
    last_count = pygame.time.get_ticks()

    tab = [i for i in range(4)]
    print(tab)
    number = random.choice(tab)
    #losowanie 4 dowolnych kart z puli
    tail = [i for i in range(1,11)]
    sample = random.sample(tail,4)
    global chances
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color)
        play_width = 150
        play_height = 250
        go_back = buttons.Button('Menu', 150, 50, 10, 540)
        go_back.change_card(color=(180,180,180))

        #powrót do poprzedniego menu
        if go_back.clicked_button(window):
            main_menu()

        if countdown > 0:
            info = font.render('Masz 5 sekund i '+str(chances)+' szanse, zapamiętaj poniższe karty', 1, pygame.Color('Black'))
            window.blit(info, (225,5))
            #sekundnik c.d.
            seconds = font1.render(str(countdown), True, pygame.Color('black'))
            seconds_rect = seconds.get_rect(midbottom = window.get_rect().midbottom)
            window.blit(seconds, seconds_rect)
            
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

            k1 = pygame.image.load('Talia/'+str(sample[0])+'.png')
            k1 = pygame.transform.scale(k1, (play_width, play_height))
            window.blit(k1, (90,50))
            k2 = pygame.image.load('Talia/'+str(sample[1])+'.png')
            k2 = pygame.transform.scale(k2, (play_width, play_height))
            window.blit(k2, (250,50)) 
            k3 = pygame.image.load('Talia/'+str(sample[2])+'.png')
            k3 = pygame.transform.scale(k3, (play_width, play_height))
            window.blit(k3, (410,50)) 
            k4 = pygame.image.load('Talia/'+str(sample[3])+'.png')
            k4 = pygame.transform.scale(k4, (play_width, play_height))
            window.blit(k4, (570,50))
            
        #moment rozpoczęcia gry
        if countdown == 0:
            info = font.render('Wskaż położenie widniejącej na miniaturze karty klikając w pole', 1, pygame.Color('Black'))
            window.blit(info, (150,5))
            
            e_k1 = buttons.Button('', play_width, play_height, 70,50, bg='navy')
            e_k2 = buttons.Button('', play_width, play_height, 230,50, bg='navy')
            e_k3 = buttons.Button('', play_width, play_height, 390,50, bg='navy')
            e_k4 = buttons.Button('', play_width, play_height, 550,50, bg='navy')
            
            e_k1.change_card()
            e_k2.change_card()
            e_k3.change_card()
            e_k4.change_card()

            if e_k1.clicked_button(window):
                if tab[number] == k1:
                    win_window_level_2(k1,90,50)
                elif tab[number] != k1:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,400)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            if e_k2.clicked_button(window): 
                if tab[number]==k2:
                    win_window_level_2(k2,250,50)
                elif tab[number]!= k2:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,400)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            if e_k3.clicked_button(window):
                if tab[number] == k3:
                    win_window_level_2(k3,410,50)
                elif tab[number] != k3:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,400)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            if e_k4.clicked_button(window):
                if tab[number] == k4:
                    win_window_level_2(k4,570,50)
                elif tab[number] != k4:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,400)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                   
            

            tab = [k1,k2,k3,k4]

            if tab[number] == k1:
                small_k1 = pygame.transform.scale(k1, (play_width*0.5, play_height*0.5))
                window.blit(small_k1, (720,30)) 
            elif tab[number] == k2:
                small_k2 = pygame.transform.scale(k2, (play_width*0.5, play_height*0.5))
                window.blit(small_k2, (720,30))        
            elif tab[number] == k3:
                small_k3 = pygame.transform.scale(k3, (play_width*0.5, play_height*0.5))
                window.blit(small_k3, (720,30))    
            elif tab[number] == k4:
                small_k4 = pygame.transform.scale(k4, (play_width*0.5, play_height*0.5))
                window.blit(small_k4, (720,30)) 

        pygame.display.update()
        clock.tick(10)

def level_3():
    #sekundnik
    countdown = 5
    last_count = pygame.time.get_ticks()

    tab = [i for i in range(4)]
    number = random.choice(tab)

    #losowanie 6 dowolnych kart z puli
    tail = [i for i in range(1,11)]
    sample = random.sample(tail,6)

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
           
        window.fill(color)
        play_width = 150
        play_height = 250
        go_back = buttons.Button('Menu', 150, 50, 10, 540)
        go_back.change_card(color=(180,180,180))

        #powrót do poprzedniego menu
        if go_back.clicked_button(window):
            main_menu()

        if countdown > 0:
            info = font.render('Masz 5 sekund i '+str(chances)+' szanse, zapamiętaj poniższe karty', 1, pygame.Color('Black'))
            window.blit(info, (225,2))
            #sekundnik c.d.
            seconds = font1.render(str(countdown), True, pygame.Color('black'))
            seconds_rect = seconds.get_rect(midbottom = window.get_rect().midbottom)
            window.blit(seconds, seconds_rect)
            
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

            k1 = pygame.image.load('Talia/'+str(sample[0])+'.png')
            k1 = pygame.transform.scale(k1, (play_width, play_height))
            window.blit(k1, (150,25))
            k2 = pygame.image.load('Talia/'+str(sample[1])+'.png')
            k2 = pygame.transform.scale(k2, (play_width, play_height))
            window.blit(k2, (310,25)) 
            k3 = pygame.image.load('Talia/'+str(sample[2])+'.png')
            k3 = pygame.transform.scale(k3, (play_width, play_height))
            window.blit(k3, (470,25)) 
            k4 = pygame.image.load('Talia/'+str(sample[3])+'.png')
            k4 = pygame.transform.scale(k4, (play_width, play_height))
            window.blit(k4, (150,280))
            k5 = pygame.image.load('Talia/'+str(sample[4])+'.png')
            k5 = pygame.transform.scale(k5, (play_width, play_height))
            window.blit(k5, (310,280))
            k6 = pygame.image.load('Talia/'+str(sample[5])+'.png')
            k6 = pygame.transform.scale(k6, (play_width, play_height))
            window.blit(k6, (470,280))
            
        #moment rozpoczęcia gry
        if countdown == 0:
            info = font.render('Wskaż położenie widniejącej na miniaturze karty klikając w pole', 1, pygame.Color('Black'))
            window.blit(info, (150,2))
            
            e_k1 = buttons.Button('', play_width, play_height, 130,25, bg='navy')
            e_k2 = buttons.Button('', play_width, play_height, 290,25, bg='navy')
            e_k3 = buttons.Button('', play_width, play_height, 450,25, bg='navy')
            e_k4 = buttons.Button('', play_width, play_height, 130,280, bg='navy')
            e_k5 = buttons.Button('', play_width, play_height, 290,280, bg='navy')
            e_k6 = buttons.Button('', play_width, play_height, 450,280, bg='navy')
            
            e_k1.change_card()
            e_k2.change_card()
            e_k3.change_card()
            e_k4.change_card()
            e_k5.change_card()
            e_k6.change_card()

            tab = [k1,k2,k3,k4,k5,k6]

            if tab[number] == k1:
                small_k1 = pygame.transform.scale(k1, (play_width*0.5, play_height*0.5))
                window.blit(small_k1, (720,30)) 
            elif tab[number] == k2:
                small_k2 = pygame.transform.scale(k2, (play_width*0.5, play_height*0.5))
                window.blit(small_k2, (720,30))        
            elif tab[number] == k3:
                small_k3 = pygame.transform.scale(k3, (play_width*0.5, play_height*0.5))
                window.blit(small_k3, (720,30))    
            elif tab[number] == k4:
                small_k4 = pygame.transform.scale(k4, (play_width*0.5, play_height*0.5))
                window.blit(small_k4, (720,30)) 
            elif tab[number] == k5:
                small_k5 = pygame.transform.scale(k5, (play_width*0.5, play_height*0.5))
                window.blit(small_k5, (720,30))
            elif tab[number] == k6:
                small_k6 = pygame.transform.scale(k6, (play_width*0.5, play_height*0.5))
                window.blit(small_k6, (720,30))
            
            if e_k1.clicked_button(window):
                if tab[number] == k1:
                    win_window_level_3(k1,150,25)
                elif tab[number] != k1:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)   
            elif e_k2.clicked_button(window): 
                if tab[number]==k2:
                    win_window_level_3(k2,310,25)
                elif tab[number]!= k2:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            elif e_k3.clicked_button(window):
                if tab[number] == k3:
                    win_window_level_3(k3,470,25)
                elif tab[number] != k3:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            elif e_k4.clicked_button(window):
                if tab[number] == k4:
                    win_window_level_3(k4,150,280)
                elif tab[number] != k4:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            elif e_k5.clicked_button(window):
                if tab[number] == k5:
                    win_window_level_3(k5,310,280)
                elif tab[number] != k5:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
                    
            elif e_k6.clicked_button(window):
                if tab[number] == k6:
                    win_window_level_3(k6,470,280)
                elif tab[number] != k6:
                    end_game('Nie odgadłeś, spróbuj jeszcze raz', 260,560)
                    chances -= 1
                    if chances >0:
                        show_text(window,'Pozostałe szanse ' + str(chances), 320,570)
                    elif chances == 0:
                        show_text(window,'Wykorzystałeś wszystkie szanse! Koniec gry.', 220,570)
                        time.sleep(1.5)
                        chances = 3
                        main_menu()
                    time.sleep(1.5)
            
            
            

        pygame.display.update()
        clock.tick(120)

main_menu()



