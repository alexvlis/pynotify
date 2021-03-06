#!/usr/bin/env python

import os
import sys
import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

# watched events
mask = pyinotify.IN_MODIFY

class EventHandler(pyinotify.ProcessEvent):
	def process_IN_MODIFY(self, event):
		path = event.pathname.split('/')

		# Check if it is a hidden file
		if not path[-1][0] == '.':
			os.system(cmd)

def main(path, callback):
	global cmd
	cmd = callback

	handler = EventHandler()
	wm.add_watch(path, mask, rec=True)
	notifier = pyinotify.Notifier(wm, handler)

	print "Listening for events..."
	notifier.loop()

if __name__ == '__main__':
	argv = sys.argv
	main(str(argv[1]), str(argv[2]))
