import time
import random
import arcade
from arcade import check_for_collision

class Apple(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,560)
        self.center_y=random.randint(40,560)
        self.color=arcade.color.RED
        self.width=20
        self.height=20
    def show(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
        

class Pear(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,560)
        self.center_y=random.randint(40,560)
        self.color=arcade.color.YELLOW
        self.height=20
        self.width=20
    def show(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Bomp(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,560)
        self.center_y=random.randint(40,560)
        self.color=arcade.color.WHITE
        self.height=20
        self.width=20
    def show(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)



class Snake(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.center_x=300
        self.center_y=300
        self.color2=arcade.color.BLUE
        self.color3=arcade.color.YELLOW
        self.color1=arcade.color.RED
        self.x_change=0
        self.y_change=0
        self.width=16
        self.height=16
        self.score=0
        self.r=10
        self.speed=1
        self.body=[]
    
    def show(self):
        i=0
        for b in self.body:
            i+=1
            if i%2==0:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color2)
            else:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color3)
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color1)

    def on_update(self, delta_time: float = 1/40):
        self.body.append({'x':self.center_x,'y':self.center_y})
        if len(self.body)>self.score:
            self.body.remove(self.body[0])
        # if self.x_change==-1:
        #     self.center_x-=self.speed
        # elif self.x_change==1:
        #     self.center_x+=self.speed
        # elif self.y_change==-1:
        #     self.center_y-=self.speed
        # elif self.y_change==1:
        #     self.center_y+=self.speed
        self.center_x += self.speed * self.x_change
        self.center_y += self.speed * self.y_change
    
    

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 600, 600, 'Super Snake')
        arcade.set_background_color(arcade.color.BLACK)
        self.snake=Snake()
        self.apple=Apple()
        self.pear=Pear()
        self.bomb=Bomp()

    def on_draw(self):
        arcade.start_render()
        if self.lose():
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text('Game Over', 220, 300, arcade.color.WHITE, 20, 20)
            time.sleep(5)
            return
        self.snake.show()
        self.apple.show()
        self.pear.show()
        self.bomb.show()
        arcade.draw_text(text=f'Score: {self.snake.score}',start_x=0,start_y=560,width=600, font_size=20, align="center", color=arcade.color.WHITE)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.snake.x_change= -1
            self.snake.y_change= 0
    
        elif key == arcade.key.RIGHT:
            self.snake.x_change = 1
            self.snake.y_change = 0

        elif key == arcade.key.UP:
            self.snake.x_change = 0
            self.snake.y_change = 1
    
        elif key == arcade.key.DOWN:
            self.snake.x_change = 0
            self.snake.y_change = -1

    def on_update(self,delta_time: float):
        self.apple.on_update()
        self.pear.on_update()
        self.bomb.on_update()
        self.snake.on_update(delta_time)
        
        if check_for_collision(self.snake,self.apple):
            self.apple=Apple()
            self.snake.score+=1

        if check_for_collision(self.snake,self.pear):
            self.pear=Pear()
            self.snake.score+=2

        if check_for_collision(self.snake,self.bomb):
            self.bomb=Bomp()
            self.snake.score -=1
            
        
    def lose(self):
        if self.snake.center_x>=590 or self.snake.center_x<=10 or self.snake.center_y>=590 or self.snake.center_y<=10 or self.snake.score<0:
            return True
        else:
            return False
        

if __name__ == "__main__":
    window = Game()
    arcade.run()