#!/usr/bin/env python
import time
import rospy
from race.msg import drive_param
import curses
#import signal
#TIMEOUT = 0.1 # number of seconds your want for timeout
forward = 0;
left = 0;
# def interrupted(signum, frame):
#     "called when read times out"
#     global forward
#     forward = 0
#     global left
#     left = 0
#     stdscr.addstr(2, 20, "Stop")
#     stdscr.addstr(2, 25, '%.2f' % forward)
#     stdscr.addstr(3, 20, "Stop")
#     stdscr.addstr(3, 25, '%.2f' % left)
# signal.signal(signal.SIGALRM, interrupted)

# def input():
#     try:
#             foo = stdscr.getch()
#             return foo
#     except:
#             # timeout
#             return



#stdscr = curses.initscr()
#curses.cbreak()
#stdscr.keypad(1)
rospy.init_node('keyboard_talker', anonymous=True)
pub = rospy.Publisher('drive_parameters', drive_param, queue_size=10)

# set alarm
#signal.alarm(TIMEOUT)
#s = input()
# disable the alarm after success
#signal.alarm(0)
#print 'You typed', s

#stdscr.refresh()
cmd = raw_input('Enter command: ')
lst = cmd.split(" ")

while lst[0] != 'q':
#	signal.setitimer(signal.ITIMER_REAL,0.05)
	if lst[0] == 's': 
                forward = int(lst[1])
        elif lst[0] == 't':
		left = int(lst[1])
	elif lst[0] == 'c':
                left = 100;
                forward = 8;
	elif lst[0] == 'x':
		left = 0;
		forward = 0;
		msg = drive_param()
       		msg.velocity = forward
       		msg.angle = left
       	 	pub.publish(msg)
 		break 
	msg = drive_param()
	msg.velocity = forward
	msg.angle = left
	pub.publish(msg)
        cmd = raw_input('Enter command: ')
        lst = cmd.split(" ")
forward = 0;
left = 0;
msg = drive_param()
msg.velocity = forward
msg.angle = left
pub.publish(msg)
