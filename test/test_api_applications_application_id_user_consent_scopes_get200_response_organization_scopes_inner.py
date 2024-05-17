# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_organization_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner

class TestApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner(unittest.TestCase):
    """ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner:
        """Test ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner`
        """
        model = ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner()
        if include_optional:
            return ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner(
                id = '0',
                name = '0',
                description = ''
            )
        else:
            return ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner(
                id = '0',
                name = '0',
                description = '',
        )
        """

    def testApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner(self):
        """Test ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
