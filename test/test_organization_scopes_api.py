# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.organization_scopes_api import OrganizationScopesApi


class TestOrganizationScopesApi(unittest.TestCase):
    """OrganizationScopesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationScopesApi()

    def tearDown(self) -> None:
        pass

    def test_api_organization_scopes_get(self) -> None:
        """Test case for api_organization_scopes_get

        Get organization scopes
        """
        pass

    def test_api_organization_scopes_id_delete(self) -> None:
        """Test case for api_organization_scopes_id_delete

        Delete organization scope
        """
        pass

    def test_api_organization_scopes_id_get(self) -> None:
        """Test case for api_organization_scopes_id_get

        Get organization scope
        """
        pass

    def test_api_organization_scopes_id_patch(self) -> None:
        """Test case for api_organization_scopes_id_patch

        Update organization scope
        """
        pass

    def test_api_organization_scopes_post(self) -> None:
        """Test case for api_organization_scopes_post

        Create an organization scope
        """
        pass


if __name__ == '__main__':
    unittest.main()
