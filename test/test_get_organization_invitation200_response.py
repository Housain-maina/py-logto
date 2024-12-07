# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response

class TestGetOrganizationInvitation200Response(unittest.TestCase):
    """GetOrganizationInvitation200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOrganizationInvitation200Response:
        """Test GetOrganizationInvitation200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrganizationInvitation200Response`
        """
        model = GetOrganizationInvitation200Response()
        if include_optional:
            return GetOrganizationInvitation200Response(
                tenant_id = '',
                id = '0',
                inviter_id = '',
                invitee = '0',
                accepted_user_id = '',
                organization_id = '0',
                status = 'Pending',
                created_at = 1.337,
                updated_at = 1.337,
                expires_at = 1.337,
                organization_roles = [
                    py_logto.models.list_application_organizations_200_response_inner_organization_roles_inner.ListApplicationOrganizations_200_response_inner_organizationRoles_inner(
                        id = '', 
                        name = '', )
                    ]
            )
        else:
            return GetOrganizationInvitation200Response(
                tenant_id = '',
                id = '0',
                inviter_id = '',
                invitee = '0',
                accepted_user_id = '',
                organization_id = '0',
                status = 'Pending',
                created_at = 1.337,
                updated_at = 1.337,
                expires_at = 1.337,
                organization_roles = [
                    py_logto.models.list_application_organizations_200_response_inner_organization_roles_inner.ListApplicationOrganizations_200_response_inner_organizationRoles_inner(
                        id = '', 
                        name = '', )
                    ],
        )
        """

    def testGetOrganizationInvitation200Response(self):
        """Test GetOrganizationInvitation200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
