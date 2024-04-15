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
from powerdns_async_client.api.tsigkey_api import TsigkeyApi  # noqa: E501
from powerdns_async_client.rest import ApiException


class TestTsigkeyApi(unittest.TestCase):
    """TsigkeyApi unit test stubs"""

    def setUp(self):
        self.api = TsigkeyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tsig_key(self):
        """Test case for create_tsig_key

        Add a TSIG key  # noqa: E501
        """
        pass

    def test_delete_tsig_key(self):
        """Test case for delete_tsig_key

        Delete the TSIGKey with tsigkey_id  # noqa: E501
        """
        pass

    def test_get_tsig_key(self):
        """Test case for get_tsig_key

        Get a specific TSIGKeys on the server, including the actual key  # noqa: E501
        """
        pass

    def test_list_tsig_keys(self):
        """Test case for list_tsig_keys

        Get all TSIGKeys on the server, except the actual key  # noqa: E501
        """
        pass

    def test_put_tsig_key(self):
        """Test case for put_tsig_key

        """
        pass


if __name__ == '__main__':
    unittest.main()
