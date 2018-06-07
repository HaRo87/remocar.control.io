'''
 Copyright (C) 2018 Robert Hansel
 
 This software may be modified and distributed under the terms
 of the MIT license.  See the LICENSE file for details.
'''
import pytest
from error import ControlConfigError
from config import MotorConfig
from config import MotorType

def test_motorconfig_high_pin_violation_lower_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 0, 3, 23)
    assert str(err_info.value) == "(0, 'must be >=2 and <= 26!')"

def test_motorconfig_high_pin_violation_higher_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 27, 3, 23)
    assert str(err_info.value) == "(27, 'must be >=2 and <= 26!')"

def test_motorconfig_low_pin_violation_lower_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 3, 0, 23)
    assert str(err_info.value) == "(0, 'must be >=2 and <= 26!')"

def test_motorconfig_low_pin_violation_higher_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 3, 27, 23)
    assert str(err_info.value) == "(27, 'must be >=2 and <= 26!')"
    
def test_motorconfig_ena_pin_violation_lower_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 3, 23, 0)
    assert str(err_info.value) == "(0, 'must be >=2 and <= 26!')"

def test_motorconfig_ena_pin_violation_higher_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        MotorConfig(MotorType.MOVEMENT, 3, 23, 27)
    assert str(err_info.value) == "(27, 'must be >=2 and <= 26!')"

def test_correct_config_movement():
    motorConfig = MotorConfig(MotorType.MOVEMENT, 2, 4, 3)
    assert motorConfig.motorType == MotorType.MOVEMENT
    assert motorConfig.gpioHighPin == 2
    assert motorConfig.gpioLowPin == 4
    assert motorConfig.gpioEnaPin == 3

def test_correct_config_steering():
    motorConfig = MotorConfig(MotorType.STEERING, 2, 4, 3)
    assert motorConfig.motorType == MotorType.STEERING
    assert motorConfig.gpioHighPin == 2
    assert motorConfig.gpioLowPin == 4
    assert motorConfig.gpioEnaPin == 3
