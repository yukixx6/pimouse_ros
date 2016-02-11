#!/usr/bin/env python
import sys, rospy
from pimouse_ros.msg import MotorFreqs
from geometry_msgs.msg import Twist

class Switch():

	def switch_vel(self):
		devfile = "/dev/rtswitch0"
                try:
                       	with open(devfile,'r') as f:
                               	f = [ int(e) for e in f ]
                               	
				if f == [1]:

                                       	freq.left_hz = 0
                                       	freq.right_hz = 0

                               	if f == [0]:
                                       	freq.left_hz = 400
                                    	freq.right_hz = 400
					

                       	pub.publish(freq)
               	except IOError:
                       	rospy.logerr("cannot write to " + devfile)


				
	def callback_switch_vel(self):
		self.switch_vel()


if __name__ == "__main__":
	rospy.init_node('switch')
	pub = rospy.Publisher('motor_raw', MotorFreqs, queue_size=10)
	freq = MotorFreqs()
	s = Switch()
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		s.callback_switch_vel()
		rate.sleep()


