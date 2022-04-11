


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Base_Work">Base Work</a>
      <ul>
        <li><a href="#BaseProcessorClass">BaseProcessor,Lens and Sensor Classes and Docstrings</a></li>
      </ul>
    </li>
    <li>
      <a href="#SpecificSkills">Specific Skills</a>
      <ul>
        <li><a href="#Documentation">Documentation</a></li>
        <li><a href="#Packaging">Packaging</a></li>
        <li><a href="#Testing">Testing</a></li>
        <li><a href="#Docker">Docker</a></li>
      </ul>
    </li>
    <li>
      <a href="#AdvancedPython">Advanced Python</a>
      <ul>
        <li><a href="#Lensdecorator">Lens decorator</a></li>
        <li><a href="#iterator">Iterator</a></li>
        <li><a href="#mymeanfunction">mymean function</a></li>        
        <li><a href="#concurrent">concurrent</a></li>
      </ul>
    </li>

  </ol>
</details>

<p id="Base_Work">
</p>

<p id="BaseProcessorClass">
</p>

# BaseProcessor,Lens and Sensor Classes and docstrings documentation

The first part of the project can be found in the camera_simulator.py file.




<p id="SpecificSkills">
</p>

# Specific Skills

<p id="Documentation">
</p>

## Documentation

The documentation of the BaseProcessor,Lens and Sensor Classes can be found on the following folder : './docs/_build/html'
please click on the index.html file to see the documentation.

The tutorial about how to use the CameraSimulator package can be found on camera_simulator_usage.ipynb file, it s a detailed description about how to use the package. Note that the tutorial was created on the CameraSimulator package which is the next part of the project.


<p id="Packaging">
</p>

## Packaging

Packaging files can be found on the './build_library' folder, you can find the setup.py file that was used to build the wheels. after that the package was published in pypi, you could find the package here [CameraSimulator](https://pypi.org/project/CameraSimulator/). 

Note that I called the package as CameraSimulator not as camera-simulator.

<p id="Testing">
</p>

## Testing

Unit tests file is called test_camera_simulator and it does 32 different testing for the CameraSimulator Package.

<p id="Docker">
</p>

## Docker

Dockerfile can be found on the main folder of the project as dockerfile. TO use it please use the following commands on the command prompt:


    cd path/to/main/folder
    docker build . -t containername
    docker run containername


-t flag tags our image you can easily change containername with any other name that you desire to.

# Advanced Python

<p id="AdvancedPython">
</p>

## Lens Decorator

<p id="Lensdecorator">
</p>

This is the first part where i had problems. I tried to implement the decorator in the camera_simulator.py in the lines 188 to 211. the lines are commented because they dont behave as expected. i tried two ways to do it, so you will find two functions 'run_lens' and 'run_before' that work as decorators for the process function in the process method of sensor class.
for the run_lens decorator i could run the lens.process function when sensor.process is called, but as you may realize the Lens class is instanciate inside the decorator, so of course everytime we use sensor.processwe will instanciate a Lens object and the result will deppend on that instance, so it doesnt meet the expected behavior. 

I found that a common approach for this problems is like the run_before method, and i think that is the more correct approach, but i couldnt implement it, that is because two things: first, i am not just running any function, i am calling a function that belongs to other class, so to use it inside the decorator i have to instanciate the class and i didnt found the way to do it. second i had problems with the parameters of the decorator, the main problem is to use the same image as the sensor.process method, so i could use something like 'args[1]' but i think that it is not the correct use of 
the parameters inside the decorator.

## Iterator

<p id="Iterator">
</p>

in the sensor class i implemented __iter__ and __next__ to allow Sensor to be iterable and to achieve the objective behavior. to test this you can use the following example:


        x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
        sensor = Sensor()
        sensor.process(x)
        for c in sensor:
            print(c)

you will realize that sensor is an iterable class and achieve the objective.

<p id="mymeanfunction">
</p>

## mymean function

the solution for this part of the project can be found on the folder mean, in the mean.py file you will find a function called my_mean that creates a random image, of random size (1,1000), then that image is processed by sensor and then returns the image mean. 
Using setuptools I created an entry point for the function you can found it in setup.py (inside mean folder)
to use the entry point please type the following command:

    python setup.py develop

and then you will be able to access and use the function typing:

    pysensor

<p id="concurrent">
</p>

## concurrent

on the futures.py file you will find the implementation of concurrent package to create a pool of 5 workers and call mymean function 100 times.




### Final thoughts:

you can find the complete project on the [Github repository](https://pypi.org/project/CameraSimulator/).

Thankyou
