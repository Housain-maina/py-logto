# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_consent_get200_response_application import ApiInteractionConsentGet200ResponseApplication

class TestApiInteractionConsentGet200ResponseApplication(unittest.TestCase):
    """ApiInteractionConsentGet200ResponseApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionConsentGet200ResponseApplication:
        """Test ApiInteractionConsentGet200ResponseApplication
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionConsentGet200ResponseApplication`
        """
        model = ApiInteractionConsentGet200ResponseApplication()
        if include_optional:
            return ApiInteractionConsentGet200ResponseApplication(
                id = '0',
                name = '0',
                branding = py_logto.models._api_interaction_consent_get_200_response_application_branding._api_interaction_consent_get_200_response_application_branding(
                    logo_url = '', 
                    dark_logo_url = '', 
                    favicon = '', ),
                display_name = '',
                privacy_policy_url = '',
                terms_of_use_url = ''
            )
        else:
            return ApiInteractionConsentGet200ResponseApplication(
                id = '0',
                name = '0',
        )
        """

    def testApiInteractionConsentGet200ResponseApplication(self):
        """Test ApiInteractionConsentGet200ResponseApplication"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
