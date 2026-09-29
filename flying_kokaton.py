import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８：左右反転した画像surface
    kk_img = pg.image.load("fig/3.png")#練習3：こうかとん画像Surface生成
    kk_img = pg.transform.flip(kk_img, True, False)#練習３：こうかとん画像左右反転
    kk_rct = kk_img.get_rect()#練習10－1：こうかとんRectの取得
    kk_rct.center = 300, 200#練習10－2：こうかとんの初期座標を設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#練習10－3：キーの押下状態取得
        
        u = +1
        t = -1
        r = 0
        m =-1
        n = 0

        

        if key_lst[pg.K_UP]:
            m = r
            n = t
            move
            #kk_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]:
            m = r
            n = u
            move
            #kk_rct.move_ip(0, +1)
        if key_lst[pg.K_LEFT]:
            m = t
            n = r
            move
            #kk_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:
            m = u*2
            n = r
            move
           #kk_rct.move_ip(+2, 0)
        move = kk_rct.move_ip(m,n)

       
        
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習５：背景画像を右から左に
        screen.blit(bg_img2, [-x+1600, 0]) #練習７：2枚目の背景画像
        screen.blit(bg_img, [-x+3200, 0]) #練習8：3枚目の背景画像
        screen.blit(kk_img, kk_rct)#練習4：こうかとんSurfaceをblit
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習６：FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()