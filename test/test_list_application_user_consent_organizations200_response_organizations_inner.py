# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_application_user_consent_organizations200_response_organizations_inner import ListApplicationUserConsentOrganizations200ResponseOrganizationsInner

class TestListApplicationUserConsentOrganizations200ResponseOrganizationsInner(unittest.TestCase):
    """ListApplicationUserConsentOrganizations200ResponseOrganizationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplicationUserConsentOrganizations200ResponseOrganizationsInner:
        """Test ListApplicationUserConsentOrganizations200ResponseOrganizationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplicationUserConsentOrganizations200ResponseOrganizationsInner`
        """
        model = ListApplicationUserConsentOrganizations200ResponseOrganizationsInner()
        if include_optional:
            return ListApplicationUserConsentOrganizations200ResponseOrganizationsInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '',
                custom_data = None,
                is_mfa_required = True,
                created_at = 1.337
            )
        else:
            return ListApplicationUserConsentOrganizations200ResponseOrganizationsInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '',
                custom_data = None,
                is_mfa_required = True,
                created_at = 1.337,
        )
        """

    def testListApplicationUserConsentOrganizations200ResponseOrganizationsInner(self):
        """Test ListApplicationUserConsentOrganizations200ResponseOrganizationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
