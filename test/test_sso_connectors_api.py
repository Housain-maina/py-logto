# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.sso_connectors_api import SSOConnectorsApi


class TestSSOConnectorsApi(unittest.TestCase):
    """SSOConnectorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SSOConnectorsApi()

    def tearDown(self) -> None:
        pass

    def test_api_sso_connectors_get(self) -> None:
        """Test case for api_sso_connectors_get

        List SSO connectors
        """
        pass

    def test_api_sso_connectors_id_delete(self) -> None:
        """Test case for api_sso_connectors_id_delete

        Delete SSO connector
        """
        pass

    def test_api_sso_connectors_id_get(self) -> None:
        """Test case for api_sso_connectors_id_get

        Get SSO connector
        """
        pass

    def test_api_sso_connectors_id_patch(self) -> None:
        """Test case for api_sso_connectors_id_patch

        Update SSO connector
        """
        pass

    def test_api_sso_connectors_post(self) -> None:
        """Test case for api_sso_connectors_post

        Create SSO connector
        """
        pass


if __name__ == '__main__':
    unittest.main()