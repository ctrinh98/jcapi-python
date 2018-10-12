# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.workday_import_api import WorkdayImportApi


class TestWorkdayImportApi(unittest.TestCase):
    """ WorkdayImportApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.workday_import_api.WorkdayImportApi()

    def tearDown(self):
        pass

    def test_workdays_authorize(self):
        """
        Test case for workdays_authorize

        Authorize Workday
        """
        pass

    def test_workdays_deauthorize(self):
        """
        Test case for workdays_deauthorize

        Deauthorize Workday
        """
        pass

    def test_workdays_delete(self):
        """
        Test case for workdays_delete

        Delete Workday
        """
        pass

    def test_workdays_get(self):
        """
        Test case for workdays_get

        Get Workday
        """
        pass

    def test_workdays_import(self):
        """
        Test case for workdays_import

        Workday Import
        """
        pass

    def test_workdays_importresults(self):
        """
        Test case for workdays_importresults

        List Import Results
        """
        pass

    def test_workdays_list(self):
        """
        Test case for workdays_list

        List Workdays
        """
        pass

    def test_workdays_post(self):
        """
        Test case for workdays_post

        Create new Workday
        """
        pass

    def test_workdays_put(self):
        """
        Test case for workdays_put

        Update Workday
        """
        pass

    def test_workdays_settings(self):
        """
        Test case for workdays_settings

        Get Workday Settings (incomplete)
        """
        pass

    def test_workdays_workers(self):
        """
        Test case for workdays_workers

        List Workday Workers
        """
        pass


if __name__ == '__main__':
    unittest.main()
