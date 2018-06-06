'''
 Copyright (C) 2018 Robert Hansel
 
 This software may be modified and distributed under the terms
 of the MIT license.  See the LICENSE file for details.
'''
import pytest
from error import ControlConfigError
from config import *

def test_motorconfig_high_pin_violation_lower_boundary_thows_error():
    with pytest.raises(ControlConfigError) as err_info:
        motorconfig = MotorConfig(MotorType.MOVEMENT, 0, 3, 23)
    assert str(err_info.value) == "(0, 'must be >=2 and <= 26!')"