import pygame
import time
from plane_sprites import *

#初始化方法(导入并初始化所有pygame模块)
pygame.init()

#初始化游戏显示窗口
screen=pygame.display.set_mode((480,700))

#绘制背景图像
#1.加载图像数据
bg=pygame.image.load("./images/background.png")
#2.blit绘制图像
screen.blit(bg,(0,0))

#绘制英雄的飞机
hero=pygame.image.load("./images/me1.png")
#blit绘制图像
screen.blit(hero,(180,300))

#3.update更新图像数据
pygame.display.update()

#创建游戏时钟对象
clock=pygame.time.Clock()

#1.定义rect记录飞机的位置
hero_rect=pygame.Rect(180,300,102,126)

#创建敌机的精灵
enemy=GameSprite("./images/enemy1.png")#默认速度为1
enemy1=GameSprite("./images/enemy1.png",2)#速度修改为2

#创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)

#游戏循环
while True:
    #游戏刷新帧率
    clock.tick(60)

    #监听事件
    for event in pygame.event.get():
        #判断事件类型是否为退出事件
        if event.type==pygame.QUIT:
            print("退出游戏")
            time.sleep(0.5)
            pygame.quit()
            #直接退出系统
            exit()

    #2修改飞机位置
    hero_rect.y-=1

    #判断飞机的位置
    if hero_rect.y<=-70:
        hero_rect.y=525
    
    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    #让精灵组调用两个方法
    #update-让组中的所有精灵更新位置
    enemy_group.update()
    #draw-在screen上绘制所有的精灵
    enemy_group.draw(screen)

    #4.调用update方法更新显示
    pygame.display.update()

#游戏结束前调用(卸载所有pygame模块)
pygame.quit()
