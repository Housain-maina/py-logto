# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.audit_logs_api import AuditLogsApi


class TestAuditLogsApi(unittest.TestCase):
    """AuditLogsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuditLogsApi()

    def tearDown(self) -> None:
        pass

    def test_get_log(self) -> None:
        """Test case for get_log

        Get log
        """
        pass

    def test_list_logs(self) -> None:
        """Test case for list_logs

        Get logs
        """
        pass


if __name__ == '__main__':
    unittest.main()
