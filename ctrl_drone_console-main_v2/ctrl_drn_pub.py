#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def go():
	w = 'go' #get_time() 現在時間を取得　秒単位
	pub.publish(w) #publish x and y
	rospy.loginfo(w) #print x and y ,current time
	print("foward")

def back():
	s = 'back'
	pub.publish(s)
	rospy.loginfo(s)
	print("back")

def right():
	d = 'right'
	pub.publish(r)
	rospy.loginfo(r)
	print("right")

def left():
	a = 'left'
	pub.publish(l)
	rospy.loginfo(l)
	print("left")

def up():
	u = 'up'
	pub.publish(u)
	rospy.loginfo(u)
	print("up")

def down():
	d = 'down'
	pub.publish(d)
	rospy.loginfo(d)
	print("down")

def halt():
	p = 'halt'
	pub.publish(p)
	rospy.loginfo(p)
	print("halt")

def tour():
	t = 'tour'
	pub.publish(t)
	rospy.loginfo(t)
	print("tour")

def walk():
	w = 'walk'
	pub.publish(w)
	rospy.loginfo(w)
	print("walk")

def tour_call():
	c = 'tour_call'
	pub.publish(c)
	rospy.loginfo(c)
	print("tour_call")

def fry():
	f = 'fry'
	pub.publish(f)
	rospy.loginfo(f)
	print("fry")

def restart():
	r = 'restart'
	pub.publish(r)
	rospy.loginfo(r)
	print("restart")

def controll_drone():
    pub = rospy.Publisher('cmd', String, queue_size=10)
	#topicに、'cmd'という名前を与え、Stringというそのtopicを介して送るメッセージ型を指定している。
	#queue_size=10という引数は、rospyがバッファリングする配信メッセージの数指定である。続き↓
	#メッセージを送信する側のノードが受信する側のノードが受け取れる頻度より高い頻度でメッセージを送信した場合には、rospyはqueue_sizeを超えるメッセージを切り捨てる。

    rospy.init_node('talker', anonymous=True) #genarate node
	#anonymousをTrueにしておく理由
	#ROSネットワークでは同じ名前のノードが接続してきた場合、古いノードは接続を強制的に切られる。anonymousをTrueにしておくと、ノード名を自動で変更して複数接続可能になる。
	#そのため、このファイルは複数立ち上げてもつながる。

    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
#        hello_str = "hello world %s" % rospy.get_time()
#        rospy.loginfo(hello_str)
#        pub.publish(hello_str)
	
	ctrl_key = input()
	
	if ctrl_key == 'w':	#press w to go forward
		go()
	elif ctrl_key == 's':	#press s to go back
		back()
	elif ctrl_key == 'a':	#press a to go left
		left()
	elif ctrl_key == 'd':	#press d to go right
		right()
	elif ctrl_key == 'Up':	#press up_arrow to up
		up()
	elif ctrl_key == 'Down':	#press down_arrow to down
		down()
	elif ctrl_key == 'h':	#press down_arrow to down
		halt()
	elif ctrl_key == 't':	#press down_arrow to down
		tour()
	elif ctrl_key == 'e':	#press down_arrow to down
		walk()
	elif ctrl_key == 'c':	#press down_arrow to down
		tour_call()
	elif ctrl_key == 'f':	#press down_arrow to down
		fry()
	elif ctrl_key == 'r':	#press down_arrow to down
		restart()
	else:
		print("input key")
        rate.sleep()
	

if __name__ == '__main__':
    try:
        controll_drone()	#call "controll drone"
    except rospy.ROSInterruptException:
        pass
