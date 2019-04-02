from picamera.array import PiRGBArray
from picamera import PiCamera
import time
def initialize_camera():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.rotation = 270
    camera.resolution = (480, 640)
    camera.framerate = 32
    camera.exposure_mode='sports'
    rawCapture = PiRGBArray(camera, size=(480, 640))
    # allow the camera to warmup
    time.sleep(0.1)
    return camera,rawCapture