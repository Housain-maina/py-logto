# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.organization_invitations_api import OrganizationInvitationsApi


class TestOrganizationInvitationsApi(unittest.TestCase):
    """OrganizationInvitationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationInvitationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization_invitation(self) -> None:
        """Test case for create_organization_invitation

        Create organization invitation
        """
        pass

    def test_create_organization_invitation_message(self) -> None:
        """Test case for create_organization_invitation_message

        Resend invitation message
        """
        pass

    def test_delete_organization_invitation(self) -> None:
        """Test case for delete_organization_invitation

        Delete organization invitation
        """
        pass

    def test_get_organization_invitation(self) -> None:
        """Test case for get_organization_invitation

        Get organization invitation
        """
        pass

    def test_list_organization_invitations(self) -> None:
        """Test case for list_organization_invitations

        Get organization invitations
        """
        pass

    def test_replace_organization_invitation_status(self) -> None:
        """Test case for replace_organization_invitation_status

        Update organization invitation status
        """
        pass


if __name__ == '__main__':
    unittest.main()