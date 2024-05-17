# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.roles_api import RolesApi


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RolesApi()

    def tearDown(self) -> None:
        pass

    def test_api_roles_get(self) -> None:
        """Test case for api_roles_get

        Get roles
        """
        pass

    def test_api_roles_id_applications_application_id_delete(self) -> None:
        """Test case for api_roles_id_applications_application_id_delete

        Remove role from application
        """
        pass

    def test_api_roles_id_applications_get(self) -> None:
        """Test case for api_roles_id_applications_get

        Get role applications
        """
        pass

    def test_api_roles_id_applications_post(self) -> None:
        """Test case for api_roles_id_applications_post

        Assign role to applications
        """
        pass

    def test_api_roles_id_delete(self) -> None:
        """Test case for api_roles_id_delete

        Delete role
        """
        pass

    def test_api_roles_id_get(self) -> None:
        """Test case for api_roles_id_get

        Get role
        """
        pass

    def test_api_roles_id_patch(self) -> None:
        """Test case for api_roles_id_patch

        Update role
        """
        pass

    def test_api_roles_id_scopes_get(self) -> None:
        """Test case for api_roles_id_scopes_get

        Get role scopes
        """
        pass

    def test_api_roles_id_scopes_post(self) -> None:
        """Test case for api_roles_id_scopes_post

        Link scopes to role
        """
        pass

    def test_api_roles_id_scopes_scope_id_delete(self) -> None:
        """Test case for api_roles_id_scopes_scope_id_delete

        Unlink scope from role
        """
        pass

    def test_api_roles_id_users_get(self) -> None:
        """Test case for api_roles_id_users_get

        Get role users
        """
        pass

    def test_api_roles_id_users_post(self) -> None:
        """Test case for api_roles_id_users_post

        Assign role to users
        """
        pass

    def test_api_roles_id_users_user_id_delete(self) -> None:
        """Test case for api_roles_id_users_user_id_delete

        Remove role from user
        """
        pass

    def test_api_roles_post(self) -> None:
        """Test case for api_roles_post

        Create a role
        """
        pass


if __name__ == '__main__':
    unittest.main()