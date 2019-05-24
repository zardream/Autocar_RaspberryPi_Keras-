from picamera import PiCamera
import time

with picamera.PiCamera() as camera

#actual autocar
camera.framerate = 15
camera.start_preview()
camera.start_recording('Video.h264')
time.sleep(5)
camera.stop_recording()

	
camera.stop_preview()