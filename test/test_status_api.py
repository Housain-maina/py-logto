# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.status_api import StatusApi


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatusApi()

    def tearDown(self) -> None:
        pass

    def test_get_status(self) -> None:
        """Test case for get_status

        Health check
        """
        pass


if __name__ == '__main__':
    unittest.main()
