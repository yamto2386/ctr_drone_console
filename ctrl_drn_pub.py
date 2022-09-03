#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def go(self):
	w = 'go' 
	self.pub.publish(w) #publish x and y
	rospy.loginfo(w) #print x and y ,current time
	print("foward")

def back(self):
	s = 'back'
	self.pub.publish(s)
	rospy.loginfo(s)
	print("back")

def right(self):
	r = 'right'
	self.pub.publish(r)
	rospy.loginfo(r)
	print("right")

def left(self):
	l = 'left'
	self.pub.publish(l)
	rospy.loginfo(l)
	print("left")

def up(self):
	u = 'up'
	self.pub.publish(u)
	rospy.loginfo(u)
	print("up")

def down(self):
	d = 'down'
	self.pub.publish(d)
	rospy.loginfo(d)
	print("down")

def halt(self):
	p = 'halt'
	self.pub.publish(p)
	rospy.loginfo(p)
	print("halt")

def tour(self):
	t = 'tour'
	self.pub.publish(t)
	rospy.loginfo(t)
	print("tour")

def walk(self):
	w = 'walk'
	self.pub.publish(w)
	rospy.loginfo(w)
	print("walk")

def tour_call(self):
	c = 'tour_call'
	self.pub.publish(c)
	rospy.loginfo(c)
	print("tour_call")

def fry(self):
	f = 'fry'
	self.pub.publish(f)
	rospy.loginfo(f)
	print("fry")

def restart(self):
	r = 'restart'
	self.pub.publish(r)
	rospy.loginfo(r)
	print("restart")

class Test:
	def __init__(self):
		self.pub = rospy.Publisher('cmd', String, queue_size=10)
		self.node = rospy.init_node('talker', anonymous=True) #genarate node
		self.rate = rospy.Rate(100)
		self.ctrl_key = ''
    	
		
	def controll_drone(self):
		while not rospy.is_shutdown():
#        hello_str = "hello world %s" % rospy.get_time()
#        rospy.loginfo(hello_str)
#        pub.publish(hello_str)
			self.ctrl_key = raw_input()
			key = self.ctrl_key
	
			if key == 'w':	#press w to go forward
				go(self)
			elif key == 's':	#press s to go back
				back(self)
			elif key == 'a':	#press a to go left
				left(self)
			elif key == 'd':	#press d to go right
				right(self)
			elif key == 'Up':	#press up_arrow to up
				up(self)
			elif key == 'Down':	#press down_arrow to down
				down(self)
			elif key == 'h':	#press down_arrow to down
				halt(self)
			elif key == 't':	#press down_arrow to down
				tour(self)
			elif key == 'e':	#press down_arrow to down
				walk(self)
			elif key == 'c':	#press down_arrow to down
				tour_call(self)
			elif key == 'f':	#press down_arrow to down
				fry(self)
			elif key == 'r':	#press down_arrow to down
				restart(self)
			else:
				print("input key")
			self.rate.sleep()

if __name__ == '__main__':
	try:
		ctr = Test()
		ctr.controll_drone()
	except rospy.ROSInterruptException: pass
