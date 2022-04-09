from camera_simulator import Lens,Sensor
import numpy as np
import pytest

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (2,4,2),
        (4,2,4),
        (640,480,640)

    ]

)
def test_lens_height(input_a,input_b,expected):
    lens= Lens(input_a,input_b)
    assert lens.height==expected
    
@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (2,4,4),
        (4,2,2),
        (640,480,480)

    ]

)
def test_lens_width(input_a,input_b,expected):
    lens= Lens(input_a,input_b)
    assert lens.width==expected

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (2,"4",TypeError),
        ("4",2,TypeError),
        (True,480,TypeError)

    ]

)
def test_Lens_int_input_init(input_a,input_b,expected):
    with pytest.raises(expected):
        Lens(input_a,input_b)


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (2,"4",TypeError),
        ("4",2,TypeError),
        (True,480,TypeError)

    ]

)
def test_Lens_int_input(input_a,input_b,expected):
    with pytest.raises(expected):
        lens=Lens()
        lens.height = input_a
        lens.width = input_b


@pytest.mark.parametrize(
    "array,input_a,input_b,expected",
    [
        # (np.array([[1, 2, 3], [4, 5, 6]]),2,3,np.array([[1, 2, 3], [4, 5, 6]])),
        (np.array([[1, 2, 3], [4, 5, 6]]),2,4,ValueError),

    ]

)
def test_lens_process_raise(array,input_a,input_b,expected):
    with pytest.raises(expected):
        lens=Lens()
        lens.height = input_a
        lens.width = input_b
        lens.process(array)

@pytest.mark.parametrize(
    "array,input_a,input_b",
    [
        (np.array([[1, 2, 3], [4, 5, 6]], np.int32),2,3),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11]]),3,6),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11],[33, 33, 333,44,44,11],[33, 33, 333,44,44,11]]),5,6)
    ]

)
def test_lens_process(array,input_a,input_b):
        lens=Lens()
        lens.height = input_a
        lens.width = input_b
        assert (lens.process(array) == array).all()


@pytest.mark.parametrize(
    "array,input_a,input_b",
    [
        (np.array([[1, 2, 3], [4, 5, 6]], np.int32),2,3),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11]]),3,6),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11],[33, 33, 333,44,44,11],[33, 33, 333,44,44,11]]),5,6)
    ]

)
def test_lens__enable_process(array,input_a,input_b):
    with pytest.raises(ValueError):
        lens=Lens()
        lens.height = input_a
        lens.width = input_b
        lens.enable = False
        lens.process(array)

    
@pytest.mark.parametrize(
    "input,expected",
    [
        (2,2),
        (4,4),
        (640,640)
    ]

)
def test_Sensor_Gain(input,expected):
    sensor = Sensor(input)
    assert sensor.gain == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        ("2",TypeError),
        ("4,4",TypeError),
        (True,TypeError)

    ]

)
def test_Sensor_Gain_int_input_init(input,expected):
    with pytest.raises(expected):
        sensor = Sensor(input)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("2",TypeError),
        ("4,4",TypeError),
        (True,TypeError)

    ]

)
def test_Sensor_Gain_int_input(input,expected):
    with pytest.raises(expected):
        sensor = Sensor()
        sensor.gain = input

@pytest.mark.parametrize(
    "array,input,expected",
    [
        (np.array([[1, 2, 3], [4, 5, 6]]),2,np.array([[2, 4, 6], [8, 10, 12]])),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11]]),3,np.array([[1395, 1398, 1401,15,102,69], [99, 99, 999,165,132,99],[99, 99, 999,132,132,33]])),
    ]

)
def test_gain_process(array,input,expected):
        sensor = Sensor(input)
        assert (sensor.process(array)==expected).all()


@pytest.mark.parametrize(
    "array,input,expected",
    [
        (np.array([[5, 2, 3], [4, 5, 6]]),2,ValueError),
        (np.array([[465, 466, 467,5,34,23], [33, 33, 333,55,44,33],[33, 33, 333,44,44,11]]),2,ValueError),

    ]

)
def test_Sensor_Gain_enable(array,input,expected):
    with pytest.raises(expected):
        sensor = Sensor(input)
        sensor.enable= False
        sensor.process(array)
