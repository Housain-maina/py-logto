# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_verification_webauthn_authentication_post200_response import ApiInteractionVerificationWebauthnAuthenticationPost200Response

class TestApiInteractionVerificationWebauthnAuthenticationPost200Response(unittest.TestCase):
    """ApiInteractionVerificationWebauthnAuthenticationPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionVerificationWebauthnAuthenticationPost200Response:
        """Test ApiInteractionVerificationWebauthnAuthenticationPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionVerificationWebauthnAuthenticationPost200Response`
        """
        model = ApiInteractionVerificationWebauthnAuthenticationPost200Response()
        if include_optional:
            return ApiInteractionVerificationWebauthnAuthenticationPost200Response(
                challenge = '',
                timeout = 1.337,
                rp_id = '',
                allow_credentials = [
                    py_logto.models._api_interaction_verification_webauthn_registration_post_200_response_exclude_credentials_inner._api_interaction_verification_webauthn_registration_post_200_response_excludeCredentials_inner(
                        type = '', 
                        id = '', 
                        transports = [
                            'usb'
                            ], )
                    ],
                user_verification = 'required',
                extensions = py_logto.models._api_interaction_verification_webauthn_registration_post_200_response_extensions._api_interaction_verification_webauthn_registration_post_200_response_extensions(
                    appid = '', 
                    cred_props = True, 
                    hmac_create_secret = True, )
            )
        else:
            return ApiInteractionVerificationWebauthnAuthenticationPost200Response(
                challenge = '',
        )
        """

    def testApiInteractionVerificationWebauthnAuthenticationPost200Response(self):
        """Test ApiInteractionVerificationWebauthnAuthenticationPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
