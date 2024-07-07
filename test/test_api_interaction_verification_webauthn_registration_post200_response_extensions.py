# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_extensions import ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions

class TestApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions(unittest.TestCase):
    """ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions:
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions`
        """
        model = ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions()
        if include_optional:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions(
                appid = '',
                cred_props = True,
                hmac_create_secret = True
            )
        else:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions(
        )
        """

    def testApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions(self):
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
