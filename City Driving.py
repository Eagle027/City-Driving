import pygame as pg
from sys import exit
import random
pg.init()


#----------------Display Setting----------------

icon = pg.image.load("E:\p_thon\City Driving\icon.png")
pg.display.set_icon(icon)

screen_width = 700 
screen_height = 950
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("City Driving")

#---------------------------------------------------------



#------------Main-menu(font selection + rendering)------------

main_menu_img = pg.image.load("E:\p_thon\City Driving\menu.png").convert_alpha()
font = pg.font.Font("E:\p_thon\City Driving\FONTS\BlackOpsOne-Regular.ttf", 50)
font_2 = pg.font.Font("E:\p_thon\City Driving\FONTS\BlackOpsOne-Regular.ttf", 60)
font_small = pg.font.Font("E:\p_thon\City Driving\FONTS\BlackOpsOne-Regular.ttf", 30)

sub_font = pg.font.Font("E:\p_thon\City Driving\FONTS\Orbitron-VariableFont_wght.ttf", 25)
text_clr = (80, 0, 0)

#-------------Score Board-------------------

score = 0
def draw_score(text, font, txt_clr, x, y, bck_clr = None):
    score = sub_font.render(text, font, txt_clr, bck_clr)
    screen.blit(score, (x, y))
    
#------------------------------------------

def draw_text(text, font, txt_clr, x, y):
    img = font.render(text, True, txt_clr)
    screen.blit(img, (x, y))

def draw_sub_text(text, sub_font, txt_clr, x, y):
    img = sub_font.render(text, True, text_clr)
    screen.blit(img, (x, y))

def draw_menu_text(text, sub_font, txt_clr, x, y):
    img = sub_font.render(text, True, txt_clr)
    screen.blit(img, (x, y))

clock = pg.time.Clock()

#-------------------------------------------------------





 #--------------------Setting Surfaces--------------------

car = pg.image.load("E:\p_thon\City Driving\car.png").convert_alpha()
car_rect = car.get_rect()
car_width = 105
car_height = 450

road1 = pg.image.load("E:\p_thon\City Driving\Road.png")
road2 = pg.image.load("E:\p_thon\City Driving\Road.png")
road_width = 0

road1_height = 0
road2_height = -950

#-----------MENU IMAGES----------
city = pg.image.load("E:\p_thon\City Driving\city.png")
dialogue = pg.image.load("E:\p_thon\City Driving\dialog.png").convert_alpha()
cross = pg.image.load("E:\p_thon\City Driving\cross.png").convert_alpha()
key = pg.image.load("E:\p_thon\City Driving\key.png").convert_alpha()
sound2 = pg.image.load("E:\p_thon\City Driving\sound2.png") 

scroll_Y = 0

#------------------Obstacle Surface------------------

obs_car = pg.image.load("E:\p_thon\City Driving\obstacle_car.png").convert_alpha()
obs_car_rect = obs_car.get_rect()
obs_car_width = 125
obs_car_height = 10

obs_car2 = pg.image.load("E:\p_thon\City Driving\obs_car_2.png").convert_alpha()
obs_car2_rect = obs_car2.get_rect()
obs_car2_width = 400
obs_car2_height = -100

obs_car3 = pg.image.load("E:\p_thon\City Driving\obs_car_3.png").convert_alpha()
obs_car3_rect = obs_car3.get_rect()
obs_car3_width = 260
obs_car3_height = 10
obs_car3_scaled = pg.transform.rotate(obs_car3, 270)

#-------------------Sound mixer---------------------------

sound = pg.mixer.Sound(r"E:\p_thon\City Driving\neon-overdrive-cyberpunk-gaming-edm-415723.mp3")
sound.play(-1)
sound.set_volume(0.2)



start_menu = True #Trigger Variable
menu = False


color_lst = ["green", 
             "red", 
             "orange", 
             "dodgerblue", 
             "white", 
             "magenta"]


color_indx = 0
threshold = None
#-----------------------Helper functions------------------

def game_blit():
    screen.blit(road1, (road_width, road1_height + scroll_Y))
    screen.blit(road2, (road_width, road2_height + scroll_Y))
    screen.blit(car, (car_width, car_height))
    screen.blit(obs_car, (obs_car_width, obs_car_height))
    screen.blit(obs_car2, (obs_car2_width, obs_car2_height))
    screen.blit(obs_car3_scaled, (obs_car3_width, obs_car3_height))
    
    threshold = score // 1000
    
    if threshold < len(color_lst):
        color_indx = threshold
    
    else:
        color_indx = threshold % len(color_lst)
    
    current_clr = color_lst[color_indx]

    draw_score(f"SCORE: {score}", font, current_clr, 10, 10)

def redraw_window():
    global road_height, start_menu, scroll_Y, score
    keys = pg.key.get_pressed()
     
    if start_menu:
        screen.fill("azure3")
        screen.blit(main_menu_img, (190, 80))
        draw_text("City Driving", font, "#380404CC", 190, 500)
        draw_sub_text("(__Press space(_) to start__)", font_small, "#FFFFFFFF", 105, 690)
        
        if keys[pg.K_SPACE]:
            start_menu = False
        
    
    else:
        game_blit()
    
        scroll_Y += 3

        if scroll_Y > 950:
            scroll_Y = 0
    
        score += 1
        



# mid_menu = False

#------------------Loop-loop-----------------------

executing = True

while executing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            exit()
    
    
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT] and car_width < 460:
        car_width += 2

    if keys[pg.K_LEFT] and car_width > 78:
        car_width -= 2
    
    if keys[pg.K_UP] and car_height > 0:
        car_height -= 2


    if keys[pg.K_DOWN] and car_height < 700:
        car_height += 2

    #------Game Menu------

    if keys[pg.K_ESCAPE] and not start_menu: 
        menu = True
        
        
    if keys[pg.K_RETURN]:
        menu =  False



    #-----------------Obstacle car drawing----------------------

    obs_car_height -= 2.5
    if obs_car_height < -500:
        obs_car_height = random.randrange(1100, 1500, 100)

    obs_car2_height += 3.1
    if obs_car2_height > 950:
        obs_car2_height = random.randrange(-300, -800, -50) 

    obs_car3_height +=3.5
    if obs_car3_height > 950:
        obs_car3_height = random.randrange(-300, -800, -50)

    #--------------------------------------------------------


    if menu:
        screen.fill("azure3")
        screen.blit(city, (0, 500))
        screen.blit(dialogue, (0, 230))
        screen.blit(cross, (25, 255))
        screen.blit(sound2, (553, 414))
        screen.blit(key, (40, 548))

        draw_menu_text("MAIN MENU", font_2, "#270101", 170, 100)
        draw_menu_text("Press (e) to EXIT", sub_font, "#A40707D6", 225, 295)
        draw_menu_text("Press (shift/ m) to MUTE", sub_font, "#EE5007FF", 185, 445)
        draw_menu_text("Press (Enter) to RESUME", sub_font, "#031494B6", 180, 583)
        
        if keys[pg.K_e]:
            executing = False
        
        if keys[pg.K_m]:
            sound.set_volume(0)
            
            if keys[pg.K_LSHIFT] and keys[pg.K_m]:
                sound.set_volume(0.2)

    
    else:
        redraw_window()
        

    #------------------Collision-------------------------
    
    #-----------------------------------------------------------
    
    pg.display.flip()
clock.tick(60)
