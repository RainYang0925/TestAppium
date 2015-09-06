#!/usr/bin/python
#  -*- coding: utf-8 -*-
__author__ = 'jandrob1978@gmail.com'

#  Created by Alejandro Barros on 15/08/15.
#  Copyright (c) 2015 Alejandro Barros Cuetos. All rights reserved.

#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  && and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#

import unittest
import string
import random

from appium import webdriver


class BasicTest(unittest.TestCase):
    """
    Basic Test to illustrate using Appium
    The objective is to test a simple form like screen.
    """

    def setUp(self):
        """
        Sets up Appium. In here you setup the app's bundle id, platform, etc..
        Also you configure the simulator if you're using it, or the device data
        in case you're testing on real devices.
        :return:
        """
        bundle_id = "com.filtercode.TestAppium"
        device_name = "<device_name>"
        udid = '<device_udid>'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'bundleId': bundle_id,
                'platformName': 'iOS',
                'deviceName': device_name,
                'udid': udid
            })

    def tearDown(self):
        """
        It quits Appium's Selenium driver.
        :return:
        """
        self.driver.quit()

    def _random_string_length(self, length):
        """
        Generates a random string of the given length.
        :param length: the length of the desired string.
        :return: the generated string.
        """
        return ''.join(random.SystemRandom().choice(string.lowercase) for _ in range(length))

    def _populate_random_textfields(self, string_length, textfields):
        """
        Internal method to populate the given textfields with random strings of the given length.
        :param string_length: the length of the generated string.
        :param textfields: a list of textfield names.
        :return: a dictionary with the generated values
        """
        values = {}

        for textfield_name in textfields:
            textfield = self.driver.find_element_by_name(textfield_name)
            values[textfield_name] = self._random_string_length(string_length)
            textfield.send_keys(values[textfield_name])

        return values

    def test_ui_clearing(self):
        """
        Tests that the clear button works as specified.
        First it populates with random strings two textfields.
        It triggers the clear action by tapping in the button.
        Checks that both textfields text property is equal to empty string.
        :return:
        """
        self._populate_random_textfields(5, ['TextField1', 'TextField2'])
        self.driver.find_element_by_name('ClearButton').click()

        textfield1_value = self.driver.find_element_by_name('TextField1').text
        textfield2_value = self.driver.find_element_by_name('TextField2').text

        self.assertEqual(textfield1_value, "")
        self.assertEqual(textfield2_value, "")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
