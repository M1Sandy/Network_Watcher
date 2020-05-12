# Author: Abdulrahman Alhoshani

#!/usr/bin/python

import time, psutil

def main():
	curr_down = 0
	curr_up = 0
	while True:
		new_curr_down = psutil.net_io_counters().bytes_recv
		new_curr_up = psutil.net_io_counters().bytes_sent
		
		if curr_down or curr_up:
			printing(new_curr_down - curr_down, new_curr_up-curr_up)
			
		curr_down = new_curr_down
		curr_up = new_curr_up
		time.sleep(1)
	
def printing(download,uplaod):
	print("Downdload: " + str(download) + "Bytes\tUpload: " + str(uplaod) + "Bytes \r", end="")
main()