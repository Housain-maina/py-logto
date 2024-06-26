# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_api_organization_invitations_get(self) -> None:
        """Test case for api_organization_invitations_get

        Get organization invitations
        """
        pass

    def test_api_organization_invitations_id_delete(self) -> None:
        """Test case for api_organization_invitations_id_delete

        Delete organization invitation
        """
        pass

    def test_api_organization_invitations_id_get(self) -> None:
        """Test case for api_organization_invitations_id_get

        Get organization invitation
        """
        pass

    def test_api_organization_invitations_id_message_post(self) -> None:
        """Test case for api_organization_invitations_id_message_post

        Resend invitation message
        """
        pass

    def test_api_organization_invitations_id_status_put(self) -> None:
        """Test case for api_organization_invitations_id_status_put

        Update organization invitation status
        """
        pass

    def test_api_organization_invitations_post(self) -> None:
        """Test case for api_organization_invitations_post

        Create organization invitation
        """
        pass

    def test_api_organization_roles_id_resource_scopes_get(self) -> None:
        """Test case for api_organization_roles_id_resource_scopes_get

        Get organization role resource scopes
        """
        pass

    def test_api_organization_roles_id_resource_scopes_post(self) -> None:
        """Test case for api_organization_roles_id_resource_scopes_post

        Assign resource scopes to organization role
        """
        pass

    def test_api_organization_roles_id_resource_scopes_put(self) -> None:
        """Test case for api_organization_roles_id_resource_scopes_put

        Replace resource scopes for organization role
        """
        pass

    def test_api_organization_roles_id_resource_scopes_scope_id_delete(self) -> None:
        """Test case for api_organization_roles_id_resource_scopes_scope_id_delete

        Remove resource scope
        """
        pass


if __name__ == '__main__':
    unittest.main()
