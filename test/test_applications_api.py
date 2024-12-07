# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.applications_api import ApplicationsApi


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationsApi()

    def tearDown(self) -> None:
        pass

    def test_assign_application_roles(self) -> None:
        """Test case for assign_application_roles

        Assign API resource roles to application
        """
        pass

    def test_create_application(self) -> None:
        """Test case for create_application

        Create an application
        """
        pass

    def test_create_application_protected_app_metadata_custom_domain(self) -> None:
        """Test case for create_application_protected_app_metadata_custom_domain

        Add a custom domain to the application.
        """
        pass

    def test_create_application_secret(self) -> None:
        """Test case for create_application_secret

        Add application secret
        """
        pass

    def test_create_application_user_consent_organization(self) -> None:
        """Test case for create_application_user_consent_organization

        Grant a list of organization access of a user for a application.
        """
        pass

    def test_create_application_user_consent_scope(self) -> None:
        """Test case for create_application_user_consent_scope

        Assign user consent scopes to application.
        """
        pass

    def test_delete_application(self) -> None:
        """Test case for delete_application

        Delete application
        """
        pass

    def test_delete_application_legacy_secret(self) -> None:
        """Test case for delete_application_legacy_secret

        Delete application legacy secret
        """
        pass

    def test_delete_application_protected_app_metadata_custom_domain(self) -> None:
        """Test case for delete_application_protected_app_metadata_custom_domain

        Remove custom domain.
        """
        pass

    def test_delete_application_role(self) -> None:
        """Test case for delete_application_role

        Remove a API resource role from application
        """
        pass

    def test_delete_application_secret(self) -> None:
        """Test case for delete_application_secret

        Delete application secret
        """
        pass

    def test_delete_application_user_consent_organization(self) -> None:
        """Test case for delete_application_user_consent_organization

        Revoke a user's access to an organization for a application.
        """
        pass

    def test_delete_application_user_consent_scope(self) -> None:
        """Test case for delete_application_user_consent_scope

        Remove user consent scope from application.
        """
        pass

    def test_get_application(self) -> None:
        """Test case for get_application

        Get application
        """
        pass

    def test_get_application_sign_in_experience(self) -> None:
        """Test case for get_application_sign_in_experience

        Get the application level sign-in experience
        """
        pass

    def test_list_application_organizations(self) -> None:
        """Test case for list_application_organizations

        Get application organizations
        """
        pass

    def test_list_application_protected_app_metadata_custom_domains(self) -> None:
        """Test case for list_application_protected_app_metadata_custom_domains

        Get application custom domains.
        """
        pass

    def test_list_application_roles(self) -> None:
        """Test case for list_application_roles

        Get application API resource roles
        """
        pass

    def test_list_application_secrets(self) -> None:
        """Test case for list_application_secrets

        Get application secrets
        """
        pass

    def test_list_application_user_consent_organizations(self) -> None:
        """Test case for list_application_user_consent_organizations

        List all the user consented organizations of a application.
        """
        pass

    def test_list_application_user_consent_scopes(self) -> None:
        """Test case for list_application_user_consent_scopes

        List all the user consent scopes of an application.
        """
        pass

    def test_list_applications(self) -> None:
        """Test case for list_applications

        Get applications
        """
        pass

    def test_replace_application_roles(self) -> None:
        """Test case for replace_application_roles

        Update API resource roles for application
        """
        pass

    def test_replace_application_sign_in_experience(self) -> None:
        """Test case for replace_application_sign_in_experience

        Update application level sign-in experience
        """
        pass

    def test_replace_application_user_consent_organizations(self) -> None:
        """Test case for replace_application_user_consent_organizations

        Grant a list of organization access of a user for a application.
        """
        pass

    def test_update_application(self) -> None:
        """Test case for update_application

        Update application
        """
        pass

    def test_update_application_custom_data(self) -> None:
        """Test case for update_application_custom_data

        Update application custom data
        """
        pass

    def test_update_application_secret(self) -> None:
        """Test case for update_application_secret

        Update application secret
        """
        pass


if __name__ == '__main__':
    unittest.main()
