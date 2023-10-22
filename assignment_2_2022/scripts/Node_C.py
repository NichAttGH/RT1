#! /usr/bin/env python

# import ros stuff
import rospy
import math, time
from assignment_2_2022.msg import custom_msg

# Initialization of the variable ' last_time_info_printed '
last_time_info_printed = 0      # The last time when informations were printed

# Callback for the subscriber
def cb_pos_vel(message):
    global frequency_info, last_time_info_printed

    # Is necessary to calculate the time in miliseconds
    time_milsec = (1/frequency_info) * 1000

    # Get the actual time
    c_time = time.time() * 1000         # 'Time' give us the time in seconds so we need to convert
                                        # the value in milliseconds as above
    
    if (c_time - last_time_info_printed) > time_milsec:
        # Get current position
        curr_x = message.actual_x
        curr_y = message.actual_y

        # Get target position
        target_x = rospy.get_param("des_pos_x")
        target_y = rospy.get_param("des_pos_y")

        # Calculation of distance and average speed
        dist = math.sqrt(((target_x - curr_x)**2) + ((target_y - curr_y)**2))
        avg_speed = math.sqrt(message.actual_vel_x**2 + message.actual_vel_y**2)

        # Print the obtained values
        print(" Distance from the choosed position: ", round(dist,4))
        print("\n Average speed: ", round(avg_speed,4))

        # Update the last time when informations were printed
        last_time_info_printed = time_milsec

if __name__ == '__main__':
    
    # Creation of the node C
    rospy.init_node('Node_C')

    # Get the value of frequency_info from the param
    frequency_info = rospy.get_param("freq")

    # Creation of the subscriber
    subscriber_pos_and_vel = rospy.Subscriber('/position_and_velocity', custom_msg, cb_pos_vel)
    rospy.spin()
