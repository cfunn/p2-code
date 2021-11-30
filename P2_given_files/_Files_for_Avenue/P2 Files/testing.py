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

def binLocation(_id):

    location = []

    # assigns location depending on container id
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

def main(): # still testing
    arm.spawn_cage(1) # spawn container
    time.sleep(2)
    i=arm.emg_left()
    while arm.emg_left()<0.5: #while left arm is not bent
        if arm.emg_left()>0.5: # if left arm is bent then do the following
            arm.move_arm(0.5, 0, 0.05) # move to pickup location
            time.sleep(2)
            control_gripper("01", True) # pick up container
        else:
            i=arm.emg_left()
        i=arm.emg_left()
    coords = binLocation("01") # get coordinates of autoclave
    time.sleep(2)
    while (arm.emg_left()>0.5 or arm.emg_left()<0.5) and arm.emg_right()<0.5: #do the following loop while right arm is not greater than 0.5 and left arm is greater than or less than 0.5
        if arm.emg_left()>0.5 and arm.emg_right()>0.5: # if both arms are bent then the following code
            arm.move_arm(coords[0], coords[1], coords[2]) # move to autoclave location
    time.sleep(2)
    while arm.emg_left()>0.5 and arm.emg_right()>0.5: #while left arm and right arm is bent fully
        if arm.emg_left()>0.5 and arm.emg_right()<0.5: # if left arm is bent fully only then do the following
            control_gripper("01", False) #open gripper
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
