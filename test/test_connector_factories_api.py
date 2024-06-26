# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.connector_factories_api import ConnectorFactoriesApi


class TestConnectorFactoriesApi(unittest.TestCase):
    """ConnectorFactoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorFactoriesApi()

    def tearDown(self) -> None:
        pass

    def test_api_connector_factories_get(self) -> None:
        """Test case for api_connector_factories_get

        Get connector factories
        """
        pass

    def test_api_connector_factories_id_get(self) -> None:
        """Test case for api_connector_factories_id_get

        Get connector factory
        """
        pass


if __name__ == '__main__':
    unittest.main()
