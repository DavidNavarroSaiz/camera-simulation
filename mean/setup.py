from setuptools import setup

setup(
    name='pysensor',
    entry_points={
        'console_scripts': [
            'pysensor = mean:my_mean',
        ],
    }
)