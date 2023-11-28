import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 800


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    bb_bomb = pg.Surface((20,20))  #練習１
    pg.draw.circle(bb_bomb,(255,0,0),(10,10),10)  #練習１
    bb_rect = bb_bomb.get_rect()  #練習１
    bb_bomb.set_colorkey((0,0,0)) #練習１
    bb_rect.centerx = random.randint(0,WIDTH)  #練習１
    bb_rect.centery = random.randint(0,HEIGHT)  #練習１
    vx,vy = 5,1 #練習２
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bb_rect.move_ip(vx,vy) #練習2　爆弾の移動
        screen.blit(bb_bomb,bb_rect)  #練習１
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
