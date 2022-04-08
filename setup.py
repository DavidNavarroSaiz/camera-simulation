from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.1'
DESCRIPTION = 'Basic Camera Emulator'
LONG_DESCRIPTION = 'Camera emulator'

# Setting up
setup(
    name="camera-simulator",
    version=VERSION,
    author="David Navarro ",
    author_email="<dcnavarros@unal.edu.co>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy',],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)