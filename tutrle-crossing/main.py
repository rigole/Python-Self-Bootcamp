import time
from turtle import Screen
from car_manager import CarManager
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars() 
    
    #Detect collision with car
    
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            
    
    #Detect a crossing 
    if player.finished_lined_crossed():
        player.go_to_start()
        car_manager.increasing_level()
            
            
screen.exitonclick()
    