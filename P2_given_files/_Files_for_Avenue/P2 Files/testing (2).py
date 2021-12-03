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

import time # imports the time library
import random # imports the random library

def binLocation(_id): # function to determine location of correct bin based on container's id
    location = [] # list for location created

    # assigns location depending on container id and stores it in list "location"
    if _id == "01":
        location = [-0.57, 0.23, 0.37]
    elif _id == "02":
        location = [0, -0.62, 0.37]
    elif _id == "03":
        location = [0, 0.62, 0.37]
    elif _id == "04":
        location = [-0.35, 0.15, 0.35]
    elif _id == "05":
        location = [0, -0.38, 0.35]
    elif _id == "06":
        location = [0, 0.38, 0.35]

    return location

def control_gripper(_id, close): # function to open or close gripper the appropriate amount depending on size of container
    x = 0
    
    while x == 0: # will keep checking position of arms until they are in the correct position
        if arm.emg_left() > 0.5 and arm.emg_right() > 0.5: # checks if both arms are bent
            
            if _id == "01" or _id == "02" or _id == "03": # if container is small
                if close: # if we want to close gripper
                    arm.control_gripper(39)
                else : # if we want to open gripper
                    arm.control_gripper(-39)
                    time.sleep(2) # adds slight delay
            
            elif _id == "04" or _id == "05" or _id == "06": # if container is large
                if close: # if we want to close gripper
                    arm.control_gripper(25)
                else: # if we want to open gripper
                    arm.control_gripper(-25)
                    time.sleep(2) # adds slight delay
            
            x = 1 # to break out of loop

def move_end_effector(x, y, z): # function to move end effector to coordinates that are passed in
    i = 0
    
    while i == 0: # will keep checking position of arms until they are in the correct position
        if arm.emg_left() < 0.5 and arm.emg_right() > 0.5: # if left arm is extended and right arm is bent
            arm.move_arm(x, y, z)
            
            i = 1 # to break out of loop

def autoclave(boolean, _id): # function to open or close appropriate autoclave drawer depending on container id
    if _id == "04" or _id == "05" or _id == "06": # only if container is large
        x = 0
        
        while x == 0:
            if arm.emg_left() > 0.5 and arm.emg_right() < 0.5: # if left arm is bent and right arm is extended
                # open or close corresponding autoclave drawer based on boolean paramater
                if _id == "04":
                    arm.open_red_autoclave(boolean) # repetition of same command so it fully opens/closes
                    time.sleep(1) # delay repeated as well
                    arm.open_red_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_red_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_red_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_red_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_red_autoclave(boolean)
                elif _id == "05":
                    arm.open_green_autoclave(boolean)# repetition of same command so it fully opens/closes
                    time.sleep(1) # delay repeated as well
                    arm.open_green_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_green_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_green_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_green_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_green_autoclave(boolean)
                elif _id == "06":
                    arm.open_blue_autoclave(boolean) 
                    time.sleep(1) # delay repeated as well
                    arm.open_blue_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_blue_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_blue_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_blue_autoclave(boolean)
                    time.sleep(0.5)
                    arm.open_blue_autoclave(boolean)
                x = 1 # to break out of loop
                
def return_pos(id_): # function to reset arm
    arm.home()
    time.sleep(2) # adds delay so container doesn't hit arm as it moves
    arm.spawn_cage(id_) # spawns new container
    
def flow(): # function to keep track of containers and call other functions in correct order
    container = ["01", "02", "03", "04", "05", "06"] # list of container ids
    
    for container_num in range(6, 0, -1): # does 6 iterations, number of containers goes down by 1 each time
        cont_index = random.randrange(0, container_num) # gets random index between 0 and the number of containers left to move
        id_ = container[cont_index] # gets id from randomized index
        container.remove(id_) # removes that id from the list so it doesn't get spawned again
        
        return_pos(int(id_)) # pass in id (as integer) so correct container gets spawned
        
        move_end_effector(0.5, 0, 0.05) # move to pickup location
        control_gripper(id_, True) # close gripper
        coords = binLocation(id_) # get coordinates of autoclave
        move_end_effector(coords[0], coords[1], coords[2]) # move to autoclave location
        autoclave(True, id_) # open autoclave drawer
        control_gripper(id_, False) # open gripper
        autoclave(False, id_) # close autoclave drawer
        

def main(): # main
    flow()
    arm.home() # return home once everything is done

main()

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
