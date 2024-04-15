# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import powerdns_async_client
from powerdns_async_client.api.zonemetadata_api import ZonemetadataApi  # noqa: E501
from powerdns_async_client.rest import ApiException


class TestZonemetadataApi(unittest.TestCase):
    """ZonemetadataApi unit test stubs"""

    def setUp(self):
        self.api = ZonemetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_metadata(self):
        """Test case for create_metadata

        Creates a set of metadata entries  # noqa: E501
        """
        pass

    def test_delete_metadata(self):
        """Test case for delete_metadata

        Delete all items of a single kind of domain metadata.  # noqa: E501
        """
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        Get the content of a single kind of domain metadata as a Metadata object.  # noqa: E501
        """
        pass

    def test_list_metadata(self):
        """Test case for list_metadata

        Get all the Metadata associated with the zone.  # noqa: E501
        """
        pass

    def test_modify_metadata(self):
        """Test case for modify_metadata

        Replace the content of a single kind of domain metadata.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
