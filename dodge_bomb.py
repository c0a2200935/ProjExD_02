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



def check_bound(rct: pg.Rect) -> tuple[bool,bool]:
    """
    オブジェクトが画面内or画面外を判定し真理値タプルを返す関数
    引数　rct:こうかとんor爆弾Surfaceのrect
    戻り値：横方向、縦方向判定結果(画面内：True,画面外：False)
    """
    yoko,tate =True,True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_gameover_img = pg.image.load("ex02/fig/8.png")
    kk_gameover_img = pg.transform.rotozoom(kk_gameover_img, 0, 2.0)
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    clock = pg.time.Clock()
    bb_bomb = pg.Surface((20,20))  #練習１
    pg.draw.circle(bb_bomb,(255,0,0),(10,10),10)  #練習１
    bb_rect = bb_bomb.get_rect()  #練習１
    bb_bomb.set_colorkey((0,0,0)) #練習１
    bb_rect.centerx = random.randint(0,WIDTH)  #練習１
    bb_rect.centery = random.randint(0,HEIGHT)  #練習１
    vx,vy = 5,5 #練習２
    
    tmr = 0

    kk_zoom = {  #演習１
    (0,0):pg.transform.rotozoom(kk_img,0,1),
    (5,0):pg.transform.flip(kk_img,True,False),
    (5,5):pg.transform.rotozoom(pg.transform.flip(kk_img,False,True),135,1),
    (0,5):pg.transform.rotozoom(pg.transform.flip(kk_img,False,True),90,1),
    (-5,5):pg.transform.rotozoom(kk_img,45,1),
    (-5,0):pg.transform.rotozoom(kk_img,0,1),
    (-5,-5):pg.transform.rotozoom(kk_img,-45,1),
    (0,-5):pg.transform.rotozoom(pg.transform.flip(kk_img,False,True),-90,1),
    (5,-5):pg.transform.rotozoom(pg.transform.flip(kk_img,False,True),-135,1),
    }

    kk_root = [0,0]
    speed = 0 #演習２加速
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rect.colliderect(bb_rect):
            screen.blit(bg_img, [0, 0])  #演習３
            screen.blit(kk_gameover_img,kk_rect)  #演習３
            pg.display.update()  #演習３
            print("Game Over")
            return
        
        
        key_lst = pg.key.get_pressed()
        sum_move = [0,0]
        for k,tpl in delta.items():
            if key_lst[k]: 
                sum_move[0] += tpl[0]
                sum_move[1] += tpl[1]
        if sum_move != [0,0]:
            kk_root = sum_move
    
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_move[0],sum_move[1])
        if check_bound(kk_rect) != (True,True):
            kk_rect.move_ip(-sum_move[0],-sum_move[1])
        screen.blit(kk_zoom[tuple(kk_root)], kk_rect)  #演習１
        bb_rect.move_ip(vx,vy) #練習2　爆弾の移動
        yoko,tate = check_bound(bb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bb_rect.move_ip(vx,vy)
        screen.blit(bb_bomb,bb_rect)  #練習１
        
        if tmr % 50 == 0 and speed < 10: #演習２
            vx *= 1.1
            vy *= 1.1
            speed += 1
        pg.display.update()
        tmr += 1
        clock.tick(50)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
