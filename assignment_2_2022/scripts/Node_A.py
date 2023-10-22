#! /usr/bin/env python

# import ros stuff
import rospy
import actionlib
import actionlib.msg
import sys, select
import assignment_2_2022.msg
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import custom_msg
from std_srvs.srv import *
from geometry_msgs.msg import Twist, Pose, Point

def action_client():
    # Creation of the action client
    act_client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)

    # Waiting the server
    act_client.wait_for_server()

    while not rospy.is_shutdown():
        # Get input from the user
        while True:
            try:
                target_x = float(input('Coordinate X: '))
                target_y = float(input('Coordinate Y: '))
            except ValueError:
                print('Argh!! Please enter valid numbers \n')
                continue
            else:
                break

        # Creation of the goal for the robot
        goal = assignment_2_2022.msg.PlanningGoal()
        goal.target_pose.pose.position.x = target_x
        goal.target_pose.pose.position.y = target_y

        # Send goal to the server
        act_client.send_goal(goal)

        # The user has 15 seconds to delete the goal by typing the word "cancel"
        print('Now you have 15 seconds to delete the goal')
        print('If you want to delete the goal, just write the word "cancel": ')
        word = select.select([sys.stdin], [], [], 15)[0]            # The select function is interesting
        if word:                                                    # because it allows us to take input
            value = sys.stdin.readline().rstrip()                   # from the user and set a timer within
            if (value == "cancel"):                                 # which the user can decide to cancel
                act_client.cancel_goal()                            # the target

def publish_msg(message):
    global publisher
        
    # Get the position and velocity
    pos_x = message.pose.pose.position.x
    pos_y = message.pose.pose.position.y
    vel_x = message.twist.twist.linear.x
    vel_y = message.twist.twist.linear.y

    # Creation of the custom message
    custom_message = custom_msg()
    
    custom_message.actual_x = pos_x
    custom_message.actual_y = pos_y
    custom_message.actual_vel_x = vel_x
    custom_message.actual_vel_y = vel_y
    
    # Publishing the custom message
    publisher.publish(custom_message)

if __name__ == '__main__':
    # Creation of the node A
    rospy.init_node('Node_A')

    # Creation of the Publisher
    publisher = rospy.Publisher('/position_and_velocity', custom_msg, queue_size = 1)

    # Creation of the Subscriber
    subscriber = rospy.Subscriber('/odom', Odometry, publish_msg)
    
    action_client()