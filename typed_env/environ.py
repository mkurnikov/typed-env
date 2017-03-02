# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals, division

import warnings
from typing import Any, Dict, List, Union


class ImproperlyConfiguredError(Exception):
    pass


# Cannot rely on None since it may be desired as a return value.
class NotSetType(object):
    pass


NOTSET = NotSetType()

# Boolean true strings
TRUE_VALUES = ('true', 'on', 'ok', 'y', 'yes', '1')


class BaseEnvironment(object):
    def __init__(self, env_dict=None):
        # type: (Dict[str, str]) -> None
        self.env_dict = env_dict
    
    def __contains__(self, item):
        # type: (str) -> bool
        return item in self.env_dict
    
    def get(self, var, default=NOTSET):
        # type: (str, Union[str, NotSetType]) -> Any
        
        value = self.env_dict.get(var)
        if value is None:
            if default is NOTSET:
                error_msg = "Environment variable '{}' not set.".format(var)
                raise ImproperlyConfiguredError(error_msg)
            else:
                value = default
        
        # no casts in plain get(), always string
        return value


class Environment(BaseEnvironment):
    def getbool(self, var, default=NOTSET):
        # type: (str, Union[bool, NotSetType]) -> bool
        # will fail, if default=Notset, and no such variable in env.
        value = super(Environment, self).get(var, default=default)
        
        # return immediately, if default
        if value == default:
            return value
        
        return value.lower() in TRUE_VALUES
    
    def getint(self, var, default=NOTSET):
        # type: (str, Union[int, NotSetType]) -> int
        value = super(Environment, self).get(var, default=default)
        
        if value == default:
            return value
        
        if str(int(value)) != value:
            # float number
            warnings.warn('Environment variable {var} specified as int, but is of float type.')
        
        return int(value)
    
    def getfloat(self, var, default=NOTSET):
        # type: (str, Union[float, NotSetType]) -> float
        value = self.get(var, default=default)
        
        if value == default:
            return value
        
        return float(value)
    
    def getlist(self, var, default=NOTSET):
        # type: (str, Union[List[Any], NotSetType]) -> List[Any]
        value = self.get(var, default=default)
        
        if value == default:
            return value
        
        return list(value.split(','))
