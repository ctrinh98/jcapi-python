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
from jcapiv2.apis.active_directory_api import ActiveDirectoryApi


class TestActiveDirectoryApi(unittest.TestCase):
    """ ActiveDirectoryApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.active_directory_api.ActiveDirectoryApi()

    def tearDown(self):
        pass

    def test_activedirectories_delete(self):
        """
        Test case for activedirectories_delete

        Delete an Active Directory
        """
        pass

    def test_activedirectories_get(self):
        """
        Test case for activedirectories_get

        Get an Active Directory
        """
        pass

    def test_activedirectories_list(self):
        """
        Test case for activedirectories_list

        List Active Directories
        """
        pass

    def test_activedirectories_post(self):
        """
        Test case for activedirectories_post

        Create a new Active Directory
        """
        pass

    def test_graph_active_directory_associations_list(self):
        """
        Test case for graph_active_directory_associations_list

        List the associations of an Active Directory instance
        """
        pass

    def test_graph_active_directory_associations_post(self):
        """
        Test case for graph_active_directory_associations_post

        Manage the associations of an Active Directory instance
        """
        pass

    def test_graph_active_directory_traverse_user_group(self):
        """
        Test case for graph_active_directory_traverse_user_group

        List the User Groups bound to an Active Directory instance
        """
        pass


if __name__ == '__main__':
    unittest.main()
