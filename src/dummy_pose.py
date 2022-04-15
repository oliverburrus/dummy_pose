#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from random import randint


def talker():
	pub = rospy.Publisher('pose_msg', PoseStamped, queue_size = 1)
	rospy.init_node('dummy_pose', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		msg = PoseStamped()
		point_x = randint(1, 5)
		point_y = randint(1, 5)
		msg.pose.position.x = point_x
		msg.pose.position.y = point_y
		msg.pose.orientation.x = 0
		msg.header.stamp = rospy.Time.now()
		pub.publish(msg)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


