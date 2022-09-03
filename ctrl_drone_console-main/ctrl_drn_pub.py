#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def go():
	x = 10 % rospy.get_time() #get_time() 現在時間を取得　秒単位
	y = 10 % rospy.get.time()
	pub.publish(x , y) #publish x and y
	rospy.loginfo(x , y) #print x and y ,current time
	print("foward")

def back():
	x = -10 % rospy.get_time()
	y = -10 % rospy.get.time()
	pub.publish(x , y)
	rospy.loginfo(x)
	print("back")

def right():
	x = 10 % rospy.get_time()
	pub.publish(x)
	rospy.loginfo(x)
	print("right")

def left():
	x = -10 % rospy.get_time()
	pub.publish(x)
	rospy.loginfo(x)
	print("right")

def up():
	z = 10 % rospy.get_time()
	pub.publish(z)
	rospy.loginfo(z)
	print("up")

def down():
	z = -10 % rospy.get_time()
	pub.publish(z)
	rospy.loginfo(z)
	print("down")

def controll_drone():
    pub = rospy.Publisher('chatter', String, queue_size=10)
	#topicに、'chatter'という名前を与え、Stringというそのtopicを介して送るメッセージ型を指定している。
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
	else:
		print("input key")
        rate.sleep()
	

if __name__ == '__main__':
    try:
        controll_drone()	#call "controll drone"
    except rospy.ROSInterruptException:
        pass
