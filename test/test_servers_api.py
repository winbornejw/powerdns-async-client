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
from powerdns_async_client.api.servers_api import ServersApi  # noqa: E501
from powerdns_async_client.rest import ApiException


class TestServersApi(unittest.TestCase):
    """ServersApi unit test stubs"""

    def setUp(self):
        self.api = ServersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cache_flush_by_name(self):
        """Test case for cache_flush_by_name

        Flush a cache-entry by name  # noqa: E501
        """
        pass

    def test_list_server(self):
        """Test case for list_server

        List a server  # noqa: E501
        """
        pass

    def test_list_servers(self):
        """Test case for list_servers

        List all servers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
