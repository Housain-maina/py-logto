# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_rp import ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp

class TestApiInteractionVerificationWebauthnRegistrationPost200ResponseRp(unittest.TestCase):
    """ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp:
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp`
        """
        model = ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp()
        if include_optional:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp(
                name = '',
                id = ''
            )
        else:
            return ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp(
                name = '',
        )
        """

    def testApiInteractionVerificationWebauthnRegistrationPost200ResponseRp(self):
        """Test ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
