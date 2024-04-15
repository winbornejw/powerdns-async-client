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
from powerdns_async_client.api.config_api import ConfigApi  # noqa: E501
from powerdns_async_client.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config(self):
        """Test case for get_config

        Returns all ConfigSettings for a single server  # noqa: E501
        """
        pass

    def test_get_config_setting(self):
        """Test case for get_config_setting

        Returns a specific ConfigSetting for a single server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
