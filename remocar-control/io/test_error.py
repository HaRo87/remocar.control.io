'''
 Copyright (C) 2018 Robert Hansel
 
 This software may be modified and distributed under the terms
 of the MIT license.  See the LICENSE file for details.
'''
import pytest
from error import *

def test_control_error_thrown():
    with pytest.raises(ControlError) as err_info:
        raise(ControlError)

def test_control_config_error_thrown():
    with pytest.raises(ControlConfigError) as err_info:
        raise(ControlConfigError('test', 'was not correct'))
    assert str(err_info.value) == "('test', 'was not correct')"

