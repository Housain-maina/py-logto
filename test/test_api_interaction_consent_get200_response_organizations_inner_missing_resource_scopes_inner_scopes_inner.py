# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_consent_get200_response_organizations_inner_missing_resource_scopes_inner_scopes_inner import ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner

class TestApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner(unittest.TestCase):
    """ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner:
        """Test ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner`
        """
        model = ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner()
        if include_optional:
            return ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner(
                id = '0',
                name = '0',
                description = ''
            )
        else:
            return ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner(
                id = '0',
                name = '0',
                description = '',
        )
        """

    def testApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner(self):
        """Test ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInnerScopesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
