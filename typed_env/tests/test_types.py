# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals, division

from unittest import TestCase

import typed_env
from typed_env.environ import VariableTypeError
from typed_env.tests.test_read_dot_env import existing_file


class TestEnvironDictCasts(TestCase):
    def setUp(self):
        contents = """
DEBUG=True
SECRET=rthtrh43t56hf
SECONDS=5
HEIGHT=0.12
PORTS=122,124,12
URL=http://google.com/
INVALID_URL=123
IP=10.0.0.1
IP_V6=abcd:ef::42:1
INVALID_IP=.0.0
        """
        with existing_file('1.txt', contents) as fname:
            self.env = typed_env.initialize_env(env_file=fname)

    def test_plain_string(self):
        self.assertEqual(self.env.get('DEBUG'), 'True')
        self.assertEqual(self.env.get('SECRET'), 'rthtrh43t56hf')

    def test_bool(self):
        self.assertEqual(self.env.get_bool('DEBUG'), True)

    def test_int(self):
        self.assertEqual(self.env.get_int('SECONDS'), 5)

    def test_float(self):
        self.assertEqual(self.env.get_float('HEIGHT'), 0.12)

    def test_list(self):
        self.assertEqual(self.env.get_list('PORTS'), ['122', '124', '12'])

    def test_default_value(self):
        self.assertEqual(self.env.get_bool('AVAVAV', default=True), True)
        
    def test_url(self):
        self.assertEqual(self.env.get_public_url('URL'), 'http://google.com/')
        with self.assertRaises(VariableTypeError):
            self.env.get_public_url('INVALID_URL')
            
    def test_ip(self):
        self.assertEqual(self.env.get_ip('IP'), '10.0.0.1')
        self.assertEqual(self.env.get_ip('IP_V6'), 'abcd:ef::42:1')
        with self.assertRaises(VariableTypeError):
            self.env.get_ip('INVALID_IP')
            
    
    
    
    
    
    
    
    
    
