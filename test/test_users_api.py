# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_assign_user_roles(self) -> None:
        """Test case for assign_user_roles

        Assign roles to user
        """
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create user
        """
        pass

    def test_create_user_identity(self) -> None:
        """Test case for create_user_identity

        Link social identity to user
        """
        pass

    def test_create_user_mfa_verification(self) -> None:
        """Test case for create_user_mfa_verification

        Create an MFA verification for a user
        """
        pass

    def test_create_user_personal_access_token(self) -> None:
        """Test case for create_user_personal_access_token

        Add personal access token
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete user
        """
        pass

    def test_delete_user_identity(self) -> None:
        """Test case for delete_user_identity

        Delete social identity from user
        """
        pass

    def test_delete_user_mfa_verification(self) -> None:
        """Test case for delete_user_mfa_verification

        Delete an MFA verification for a user
        """
        pass

    def test_delete_user_personal_access_token(self) -> None:
        """Test case for delete_user_personal_access_token

        Delete personal access token
        """
        pass

    def test_delete_user_role(self) -> None:
        """Test case for delete_user_role

        Remove role from user
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Get user
        """
        pass

    def test_get_user_has_password(self) -> None:
        """Test case for get_user_has_password

        Check if user has password
        """
        pass

    def test_list_user_custom_data(self) -> None:
        """Test case for list_user_custom_data

        Get user custom data
        """
        pass

    def test_list_user_mfa_verifications(self) -> None:
        """Test case for list_user_mfa_verifications

        Get user's MFA verifications
        """
        pass

    def test_list_user_organizations(self) -> None:
        """Test case for list_user_organizations

        Get organizations for a user
        """
        pass

    def test_list_user_personal_access_tokens(self) -> None:
        """Test case for list_user_personal_access_tokens

        Get personal access tokens
        """
        pass

    def test_list_user_roles(self) -> None:
        """Test case for list_user_roles

        Get roles for user
        """
        pass

    def test_list_users(self) -> None:
        """Test case for list_users

        Get users
        """
        pass

    def test_replace_user_identity(self) -> None:
        """Test case for replace_user_identity

        Update social identity of user
        """
        pass

    def test_replace_user_roles(self) -> None:
        """Test case for replace_user_roles

        Update roles for user
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update user
        """
        pass

    def test_update_user_custom_data(self) -> None:
        """Test case for update_user_custom_data

        Update user custom data
        """
        pass

    def test_update_user_is_suspended(self) -> None:
        """Test case for update_user_is_suspended

        Update user suspension status
        """
        pass

    def test_update_user_password(self) -> None:
        """Test case for update_user_password

        Update user password
        """
        pass

    def test_update_user_personal_access_token(self) -> None:
        """Test case for update_user_personal_access_token

        Update personal access token
        """
        pass

    def test_update_user_profile(self) -> None:
        """Test case for update_user_profile

        Update user profile
        """
        pass

    def test_verify_user_password(self) -> None:
        """Test case for verify_user_password

        Verify user password
        """
        pass


if __name__ == '__main__':
    unittest.main()
