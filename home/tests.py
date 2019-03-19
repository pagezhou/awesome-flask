# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .utils import add_sample, sub_sample

# Create your tests here.


class UtilsTest(TestCase):
    def setUp(self):
        self.x = 5
        self.y = 2

    def test_add(self):
        self.assertEquals(add_sample(self.x, self.y), 7)
        self.assertNotEquals(add_sample(self.x, self.y), 8)

    def test_sub(self):
        self.assertEquals(sub_sample(self.x, self.y), 3)
        self.assertNotEquals(sub_sample(self.x, self.y), 8)
