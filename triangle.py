#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time


def automate():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.init_node('Automatic_Controller')

	move_cmd = Twist()
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = -3.1
	pub.publish(move_cmd)
	time.sleep(1)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)		
	move_cmd.linear.x = 1.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(3)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 9
	pub.publish(move_cmd)
	time.sleep(1.2)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)		
	move_cmd.linear.x = 1.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(3)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 9
	pub.publish(move_cmd)
	time.sleep(1.3)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)		
	move_cmd.linear.x = 1.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(3)
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 0.0
	pub.publish(move_cmd)
	time.sleep(1)

if __name__ == '__main__' :
	try:
		automate()
	except rospy.ROSInterruptException:
		pass