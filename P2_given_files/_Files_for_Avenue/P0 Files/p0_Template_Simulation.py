import sys
sys.path.append('../')
import time
from Common_Libraries.p0_sim_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        my_qbot.ping()
    except Exception as error_update_sim:
        print (error_update_sim)


speed = 0.1 # in m/s
my_qbot = qbot(speed)

#---------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

import time

def binLocation(_id):

    location = []

    if _id == "01":
        location = [-0.65, 0.25, 0.4]
    elif _id == "02":
        location = [0, -0.65, 0.4]
    elif _id == "03":
        location = [0, 0.65, 0.4]
    elif _id == "04":
        location = [-0.45, 0.15, 0.2]
    elif _id == "05":
        location = [0, -0.5, 0.2]
    elif _id == "06":
        location = [0, 0.5, 0.2]

    return location

def control_gripper(_id, close):

    if close: # to close gripper
        if _id == "01" or _id == "02" or _id == "03": # if container is small
            arm.control_gripper(35)
        elif _id == "04" or _id == "05" or _id == "06": # if container is large
            arm.control_gripper(20)
    else: # to open gripper
        arm.control_gripper(-45)

def move_end_effector(x, y, z):
        arm.move_arm(x, y, z)

def main():
    arm.spawn_cage(1)
    arm.move_arm(0.5, 0, 0.05)
    time.sleep(2)
    control_gripper("01", True)
    coords = binLocation("01")
    time.sleep(2)
    arm.move_arm(coords[0], coords[1], coords[2])
    time.sleep(2)
    control_gripper("01", False)
    #while i == 0:
        #arm.home()
        #i_d = "02"
        #if arm.emg_right()>0.5 and arm.emg_left()>0.5:
            #location = binLocation(i_d)
            #control_gripper(i_d)
        #arm.move_arm(location[0], location[1], location[2])

main()

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------

update_thread = repeating_timer(2, update_sim)
