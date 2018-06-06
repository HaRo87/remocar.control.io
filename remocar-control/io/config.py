'''
 Copyright (C) 2018 Robert Hansel
 
 This software may be modified and distributed under the terms
 of the MIT license.  See the LICENSE file for details.
'''
from enum import Enum
from error import ControlConfigError

class MotorType(Enum):
    """
    Possible DC motor types. 
    MOVEMENT is for moving the car forward or backwards.
    STEERING is for controlling the direction.
    """
    MOVEMENT = 1
    STEERING = 2

class MotorConfig:
    """
    Motor configuration defining type, high/low and enable GPIO pin.

    Parameters
    ----------
    motorType: MotorType
        Defines the type of the motor to be configured.
    gpioHighPin: int
        Defines the pin number of the pin which in state **high** either 
        defines forward or left. Possible values are >=2 and <=26. Have a
        look at the official Raspberry Pi GPIO reference
        `page <http://packages.python.org/an_example_pypi_project/>`_ 
        to learn more about it.
    gpioLowPin: int
        Defines the pin number of the pin which in state **low** either 
        defines forward or left.
    gpioEnaPin: int
        Defines the pin number of the pin which is used to change the speed
        of the motor.
    
    """
    motorType = MotorType.MOVEMENT
    gpioHighPin = 0
    gpioLowPin = 0
    gpioEnaPin = 0

    def __init__(self, motorType, gpioHighPin, gpioLowPin, gpioEnaPin):
        self.motorType = motorType
        if 2 <= gpioHighPin <= 26:
            self.gpioHighPin = gpioHighPin
        else:
            raise ControlConfigError(gpioHighPin, 'must be >=2 and <= 26!')
        if 2 <= gpioLowPin <= 26:
            self.gpioLowPin = gpioLowPin
        else:
            raise ControlConfigError(gpioLowPin, 'must be >=2 and <= 26!')
        if 2 <= gpioEnaPin <= 26:
            self.gpioEnaPin = gpioEnaPin
        else:
            raise ControlConfigError(gpioEnaPin, 'must be >=2 and <= 26!')

        

