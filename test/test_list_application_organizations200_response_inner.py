# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_application_organizations200_response_inner import ListApplicationOrganizations200ResponseInner

class TestListApplicationOrganizations200ResponseInner(unittest.TestCase):
    """ListApplicationOrganizations200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplicationOrganizations200ResponseInner:
        """Test ListApplicationOrganizations200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplicationOrganizations200ResponseInner`
        """
        model = ListApplicationOrganizations200ResponseInner()
        if include_optional:
            return ListApplicationOrganizations200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '',
                custom_data = None,
                is_mfa_required = True,
                branding = py_logto.models.list_application_organizations_200_response_inner_branding.ListApplicationOrganizations_200_response_inner_branding(
                    logo_url = '', 
                    dark_logo_url = '', 
                    favicon = '', 
                    dark_favicon = '', ),
                created_at = 1.337,
                organization_roles = [
                    py_logto.models.list_application_organizations_200_response_inner_organization_roles_inner.ListApplicationOrganizations_200_response_inner_organizationRoles_inner(
                        id = '', 
                        name = '', )
                    ]
            )
        else:
            return ListApplicationOrganizations200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '',
                custom_data = None,
                is_mfa_required = True,
                branding = py_logto.models.list_application_organizations_200_response_inner_branding.ListApplicationOrganizations_200_response_inner_branding(
                    logo_url = '', 
                    dark_logo_url = '', 
                    favicon = '', 
                    dark_favicon = '', ),
                created_at = 1.337,
                organization_roles = [
                    py_logto.models.list_application_organizations_200_response_inner_organization_roles_inner.ListApplicationOrganizations_200_response_inner_organizationRoles_inner(
                        id = '', 
                        name = '', )
                    ],
        )
        """

    def testListApplicationOrganizations200ResponseInner(self):
        """Test ListApplicationOrganizations200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
