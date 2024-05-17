# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_user import ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser

class TestApiInteractionVerificationWebauthnRegistrationPost200ResponseUser(unittest.TestCase):
    """ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser:
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser`
        """
        model = ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser()
        if include_optional:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser(
                id = '',
                name = '',
                display_name = ''
            )
        else:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser(
                id = '',
                name = '',
                display_name = '',
        )
        """

    def testApiInteractionVerificationWebauthnRegistrationPost200ResponseUser(self):
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()