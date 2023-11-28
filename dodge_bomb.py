import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 800

delta = {
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(5,0)
}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    clock = pg.time.Clock()
    bb_bomb = pg.Surface((20,20))  #練習１
    pg.draw.circle(bb_bomb,(255,0,0),(10,10),10)  #練習１
    bb_rect = bb_bomb.get_rect()  #練習１
    bb_bomb.set_colorkey((0,0,0)) #練習１
    bb_rect.centerx = random.randint(0,WIDTH)  #練習１
    bb_rect.centery = random.randint(0,HEIGHT)  #練習１
    vx,vy = 5,5 #練習２
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        sum_move = [0,0]
        for k,tpl in delta.items():
            if key_lst[k]: 
                sum_move[0] += tpl[0]
                sum_move[1] += tpl[1]

        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_move[0],sum_move[1])
        screen.blit(kk_img, kk_rect)
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
