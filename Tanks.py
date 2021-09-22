import time
import random
import arcade
from arcade.window_commands import set_background_color


class Enemy(arcade.Sprite):
    def __init__(self,w,h,speed):
        self.img=random.choice([":resources:images/topdown_tanks/tank_green.png",
        ":resources:images/topdown_tanks/tank_sand.png",
        ":resources:images/topdown_tanks/tank_dark.png"])
        super().__init__(self.img)
        self.speed=speed
        self.width=70
        self.height=90
        self.center_y=h+self.height
        self.line=random.choice(['1','2','3','4'])
        if self.line=='1':
            self.center_x=self.width//2+self.width//2
        elif self.line=='2':
            self.center_x=w//2+self.width//2
        elif self.line=='3':
            self.center_x=w//4+self.width//2
        elif self.line=='4':
            self.center_x=w-self.width//2
    
    def on_update(self, delta_time: float=1/40):
        self.center_y-=self.speed









class Car(arcade.Sprite):
    def __init__(self,w):
        super().__init__(":resources:images/topdown_tanks/tankBody_blue_outline.png")
        self.speed=2
        self.change_x=0
        self.center_x=w//2
        self.center_y=self.height
        self.width=60
        self.height=80
        self.score=0
    
    def move(self,w):
        self.center_x+=self.change_x*self.speed
        if self.center_x>=w or self.center_x<=0:
            self.change_x*=-1




class Game(arcade.Window):
    def __init__(self):
        self.h=600
        self.w=500
        super().__init__(self.w,self.h,'War')
        arcade.set_background_color(arcade.color.GRAY)
        self.background_image=arcade.load_texture(':resources:images/topdown_tanks/tileGrass_roadNorth.png')
        self.me=Car(self.w)
        # self.enemy=Enemy(self.w,self.h)
        self.enemylist=[]
        self.start_time=time.time()
        self.speed=1

    def on_draw(self):
        arcade.start_render()
        if self.lose():
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text(f"Score:{self.me.score}",start_x=self.w//2,start_y=self.h//2,color=arcade.color.BLACK)
            time.sleep(5)
            return
            
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background_image)
        self.me.draw()
        # self.enemy.draw()
        arcade.draw_text(f"Score:{self.me.score}",start_x=0,start_y=0,color=arcade.color.RED)
        for enemy in self.enemylist:
            enemy.draw()

    def on_update(self, delta_time: float):
        if self.lose():
            time.sleep(3)
            self.resetgame()
        if time.time()-self.start_time>2:
            self.enemylist.append(Enemy(self.w,self.h,self.speed))
            self.start_time=time.time()
        self.me.move(self.w)
        for enemy in self.enemylist:
            enemy.on_update()
        # self.enemy.on_update()
        for enemy in self.enemylist:
            if enemy.center_y<0:
                self.me.score+=1
                self.enemylist.remove(enemy)
                # print(self.me.score)

        self.speed+=0.005

    def on_key_press(self,key,modifiers):
        if key==arcade.key.LEFT:
            self.me.change_x=-1
        elif key==arcade.key.RIGHT:
            self.me.change_x=1

    def on_key_release(self,key,modifiers):
        self.me.change_x=0
        

    def lose(self):
        for enemy in self.enemylist:
            if arcade.check_for_collision(enemy,self.me):
                return True
        else:
            return False


    def resetgame(self):
        self.score=0
        self.speed=1
        self.enemylist=[]
        self.me=Car(self.w)

    


game=Game()
arcade.run()