## ----------------------------------------------------------------------------------------------------------
## TEMPLATE
## Please DO NOT change the naming convention within this template. Some changes may
## lead to your program not functioning as intended.

import sys
sys.path.append('../')

from Common_Libraries.p2_sim_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        arm.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

arm = qarm()
update_thread = repeating_timer(2, update_sim)

#---------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

# program not complete - still testing, have to add a couple more functions

import time
import random

def binLocation(_id):

    location = []

    # assigns location depending on container id
    if _id == "01":
        location = [-0.57, 0.22, 0.37]
    elif _id == "02":
        location = [0, -0.62, 0.37]
    elif _id == "03":
        location = [0, 0.62, 0.37]
    elif _id == "04":
        location = [-0.35, 0.15, 0.35]
    elif _id == "05":
        location = [0, -0.41, 0.35]
    elif _id == "06":
        location = [0, 0.41, 0.35]

    return location

def control_gripper(_id, close):
    x=0
    while x==0: #while left arm is not bent
        if arm.emg_left()>0.5 and arm.emg_right()>0.5: # if left arm is bent then do the following
            time.sleep(2)
            if _id == "01" or _id == "02" or _id == "03": # if container is small
                if close: # to close gripper
                    arm.control_gripper(39)
                else :
                    arm.control_gripper(-39)
            elif _id == "04" or _id == "05" or _id == "06": # if container is large
                if close: # to close gripper
                    arm.control_gripper(25)
                else:
                    arm.control_gripper(-25)
            x=1

def move_end_effector(x, y, z):
    i=0
    while i==0: #do the following loop while right arm is not greater than 0.5 and left arm is greater than or less than 0.5
        if arm.emg_left()<0.5 and arm.emg_right()>0.5: # if both arms are bent then the following code
            arm.move_arm(x, y, z)
            i=1

def autoclave(boolean,_id):
    if _id == "04" or _id == "05" or _id == "06": # if container is large:
        x=0
        while x==0:
            if arm.emg_left()>0.5 and arm.emg_right()<0.5: # if left arm is bent fully only then do the following
                if _id== "04":
                    arm.open_red_autoclave(boolean)
                    x=1
                elif _id== "05":
                    arm.open_green_autoclave(boolean)
                    x=1

                elif _id== "06":
                    arm.open_blue_autoclave(boolean)
                    x=1

def return_pos(id_):
    arm.home()
    time.sleep(2)
    arm.spawn_cage(id_) # spawn container

def terminate_p():
    arm.terminate_arm()
    
def bmain():
    container = ["01", "02", "03", "04", "05", "06"]
    for container_num in range(6,0,-1):
        current_cont=random.randrange(0, container_num)
        id_ = container[current_cont]
        return_pos(int(id_))
        move_end_effector(0.5, 0, 0.05) 
        control_gripper(id_, True) # pick up container
        coords = binLocation(id_) # get coordinates of autoclave
        move_end_effector(coords[0], coords[1], coords[2]) # move to autoclave location
        autoclave(True,id_)
        control_gripper(id_, False) #open gripper
        autoclave(False, id_)
        container.remove(id_)
    terminate_p()

def main(): # still testing
    bmain()
            #control_gripper(i_d)
        #arm.move_arm(location[0], location[1], location[2])

main()

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
