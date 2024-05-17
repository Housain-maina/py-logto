# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_applications_application_id_sign_in_experience_put_request import ApiApplicationsApplicationIdSignInExperiencePutRequest

class TestApiApplicationsApplicationIdSignInExperiencePutRequest(unittest.TestCase):
    """ApiApplicationsApplicationIdSignInExperiencePutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiApplicationsApplicationIdSignInExperiencePutRequest:
        """Test ApiApplicationsApplicationIdSignInExperiencePutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiApplicationsApplicationIdSignInExperiencePutRequest`
        """
        model = ApiApplicationsApplicationIdSignInExperiencePutRequest()
        if include_optional:
            return ApiApplicationsApplicationIdSignInExperiencePutRequest(
                branding = py_logto.models._api_interaction_consent_get_200_response_application_branding._api_interaction_consent_get_200_response_application_branding(
                    logo_url = '', 
                    dark_logo_url = '', 
                    favicon = '', ),
                display_name = '',
                terms_of_use_url = None,
                privacy_policy_url = None
            )
        else:
            return ApiApplicationsApplicationIdSignInExperiencePutRequest(
                terms_of_use_url = None,
                privacy_policy_url = None,
        )
        """

    def testApiApplicationsApplicationIdSignInExperiencePutRequest(self):
        """Test ApiApplicationsApplicationIdSignInExperiencePutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
