# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.systems_api import SystemsApi


class TestSystemsApi(unittest.TestCase):
    """SystemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemsApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_application_config(self) -> None:
        """Test case for get_system_application_config

        Get the application constants.
        """
        pass


if __name__ == '__main__':
    unittest.main()
