# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.dashboard_api import DashboardApi


class TestDashboardApi(unittest.TestCase):
    """DashboardApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardApi()

    def tearDown(self) -> None:
        pass

    def test_get_active_user_counts(self) -> None:
        """Test case for get_active_user_counts

        Get active user data
        """
        pass

    def test_get_new_user_counts(self) -> None:
        """Test case for get_new_user_counts

        Get new user count
        """
        pass

    def test_get_total_user_count(self) -> None:
        """Test case for get_total_user_count

        Get total user count
        """
        pass


if __name__ == '__main__':
    unittest.main()
