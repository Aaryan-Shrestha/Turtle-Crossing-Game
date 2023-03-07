import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating 'player' object
player = Player()

# Creating 'car_manager' object
car_manager = CarManager()

# Creating 'scoreboard' object
scoreboard = Scoreboard()
# Add Event Listeners
screen.listen()
screen.onkey(fun=player.go_up, key='Up')

# Game On
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision With Cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing The Road
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
