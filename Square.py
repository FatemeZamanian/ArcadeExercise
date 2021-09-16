import arcade

arcade.Window(500,500,':)')
arcade.set_background_color(arcade.color.BLACK)
m=20
r = 10
arcade.start_render()
flag=True
for i in range(20,481,m):
    for j in range(20,481,m):
        if not flag:
            arcade.draw_circle_filled(i,j, r, arcade.color.MAGENTA)
            flag = True
        else:
            arcade.draw_circle_filled(i,j, r,arcade.color.CYAN)
            flag = False
    if flag:
        flag = False
    else:
        flag = True
        

arcade.finish_render()
arcade.run()