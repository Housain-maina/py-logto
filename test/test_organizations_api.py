# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_api_organizations_get(self) -> None:
        """Test case for api_organizations_get

        Get organizations
        """
        pass

    def test_api_organizations_id_delete(self) -> None:
        """Test case for api_organizations_id_delete

        Delete organization
        """
        pass

    def test_api_organizations_id_get(self) -> None:
        """Test case for api_organizations_id_get

        Get organization
        """
        pass

    def test_api_organizations_id_patch(self) -> None:
        """Test case for api_organizations_id_patch

        Update organization
        """
        pass

    def test_api_organizations_id_users_get(self) -> None:
        """Test case for api_organizations_id_users_get

        Get organization user members
        """
        pass

    def test_api_organizations_id_users_post(self) -> None:
        """Test case for api_organizations_id_users_post

        Add user members to organization
        """
        pass

    def test_api_organizations_id_users_put(self) -> None:
        """Test case for api_organizations_id_users_put

        Replace organization user members
        """
        pass

    def test_api_organizations_id_users_roles_post(self) -> None:
        """Test case for api_organizations_id_users_roles_post

        Assign roles to organization user members
        """
        pass

    def test_api_organizations_id_users_user_id_delete(self) -> None:
        """Test case for api_organizations_id_users_user_id_delete

        Remove user member from organization
        """
        pass

    def test_api_organizations_id_users_user_id_roles_get(self) -> None:
        """Test case for api_organizations_id_users_user_id_roles_get

        Get roles for a user in an organization
        """
        pass

    def test_api_organizations_id_users_user_id_roles_post(self) -> None:
        """Test case for api_organizations_id_users_user_id_roles_post

        Assign roles to a user in an organization
        """
        pass

    def test_api_organizations_id_users_user_id_roles_put(self) -> None:
        """Test case for api_organizations_id_users_user_id_roles_put

        Update roles for a user in an organization
        """
        pass

    def test_api_organizations_id_users_user_id_roles_role_id_delete(self) -> None:
        """Test case for api_organizations_id_users_user_id_roles_role_id_delete

        Remove a role from a user in an organization
        """
        pass

    def test_api_organizations_post(self) -> None:
        """Test case for api_organizations_post

        Create an organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
