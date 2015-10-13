__author__ = 'yingminzhou'

from random import  random

time = 5
car_positions = [1,1,1]
#############################################################################
while time:
    #decrese time
    time -= 1

    #print(' ')
    for i in range(len(car_positions)):
        # move car
        if random()> 0.3:
            car_positions [i] += 1
        # draw car
        #print('-'*car_positions[i])

################################unfunctional one#################################
time = 5
car_positions = [1,1,1]
def move_cars():
    for i,_ in enumerate(car_positions):
        if random()>0.3:
            car_positions[i] +=1

def draw_cars(car_position):
    print('-'*car_position)

def run_step_of_race():
    global time
    time -= 1
    move_cars()

def draw():
    print(' ')
    for car_position in car_positions:
        draw_cars(car_position)

while time:
    run_step_of_race()
    #draw()

################################functional one#################################
def move_cars_func(car_positions):
    return list(map(lambda x: x + 1 if random()> 0.3 else x,car_positions))

def draw_cars_func(car_position):
    return '-'*car_position

def run_step_of_race_func(state):
    return {'time':state['time']-1,'car_positions': move_cars_func(state['car_positions'])}

def draw_func(state):
    print(' ')
    print('\n'.join(map(draw_cars_func,state['car_positions'])))

def race_func(state):
    draw_func(state)
    if state['time']:
        race_func(run_step_of_race_func(state))

race_func({'time':5,'car_positions':[1,1,1]})


