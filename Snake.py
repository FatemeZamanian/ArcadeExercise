import random
import arcade
from arcade import check_for_collision

class Apple(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=8
        self.x=random.randint(40,560)
        self.y=random.randint(40,560)
        self.color=arcade.color.RED
    def show(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)
        

class Pear(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.x=random.randint(40,560)
        self.y=random.randint(40,560)
        self.color=arcade.color.YELLOW
    def show(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

class Bomp(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=12
        self.x=random.randint(40,560)
        self.y=random.randint(40,560)
        self.color=arcade.color.BLACK
    def show(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)



class Snake(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.x=300
        self.y=300
        self.color1=arcade.color.GREEN
        self.color2=arcade.color.YELLOW
        self.color=arcade.color.RED
        self.x_change=0
        self.y_change=0
        self.score=0
        self.r=6
        self.body=[]
    
    def show(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.color)
        i=0
        for b in self.body:
            i+=1
            if i%2==0:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color1)
            else:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color2)
        

    def move(self, delta_time: float = 1/60):
        self.body.append({'x':self.x,'y':self.y})
        if len(self.body)>self.score:
            self.body.remove(self.body[0])
        if self.x_change==-1:
            self.x-=self.speed
        elif self.x_change==1:
            self.x+=self.speed
        elif self.y_change==-1:
            self.y-=self.speed
        elif self.y_change==1:
            self.y+=self.speed
    
    

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
        self.snake.show()
        self.apple.show()
        self.pear.show()
        self.bomb.show()
        arcade.draw_text(text=f'Score: {self.snake.score}',start_x=0 ,start_y=250, width=600, font_size=20, align="center", color=arcade.color.WHITE)


    def on_key_release(self, key, modifires):
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif key == arcade.key.ESCAPE:
            self.game_over.exit_game()

    def on_update(self,delta_time: float):
        self.apple.on_update()
        self.pear.on_update()
        self.bomb.on_update()
        self.snake.move(delta_time)
        
        if check_for_collision(self.snake,self.apple):
            self.apple=Apple()
            self.score+=1

        if check_for_collision(self.snake,self.pear):
            self.pear=Pear()
            self.score+=2

        if check_for_collision(self.snake,self.bomb):
            self.bomb=Bomp()
            self.score -=1
            
        if self.lose()==True:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text('Game Over', 300, 300, arcade.color.WHITE, 20, 20)
        arcade.start_render()


    def lose(self):
        if self.x>=590 or self.x<=10 or self.y>=590 or self.y<=10 or self.score<0:
            return True
        else:
            return False
        



if __name__ == "__main__":
    window = Game()
    arcade.run()