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
from jcapiv2.apis.g_suite_api import GSuiteApi


class TestGSuiteApi(unittest.TestCase):
    """ GSuiteApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.g_suite_api.GSuiteApi()

    def tearDown(self):
        pass

    def test_graph_g_suite_associations_list(self):
        """
        Test case for graph_g_suite_associations_list

        List the associations of a G Suite instance
        """
        pass

    def test_graph_g_suite_associations_post(self):
        """
        Test case for graph_g_suite_associations_post

        Manage the associations of a G Suite instance
        """
        pass

    def test_graph_g_suite_traverse_user(self):
        """
        Test case for graph_g_suite_traverse_user

        List the Users bound to a G Suite instance
        """
        pass

    def test_graph_g_suite_traverse_user_group(self):
        """
        Test case for graph_g_suite_traverse_user_group

        List the User Groups bound to a G Suite instance
        """
        pass


if __name__ == '__main__':
    unittest.main()
