import numpy as np
from random import randint
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from CameraSimulator import Lens,Sensor


def my_mean():
    height = randint(1,1000)
    width = randint(1,1000)
    arr = np.random.randint(low = 0, high = 255, size = (width, height, 3))
    sensor = Sensor()
    res = sensor.process(arr)
    image_mean = np.mean(res)
    return image_mean

if __name__ == '__main__':
    my_mean()