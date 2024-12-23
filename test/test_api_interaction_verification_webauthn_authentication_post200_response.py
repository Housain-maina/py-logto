# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
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
            include_optional is a boolean, when False only required
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
                    py_logto.models.create_web_authn_registration_verification_200_response_registration_options_exclude_credentials_inner.CreateWebAuthnRegistrationVerification_200_response_registrationOptions_excludeCredentials_inner(
                        type = '', 
                        id = '', 
                        transports = [
                            'usb'
                            ], )
                    ],
                user_verification = 'required',
                extensions = py_logto.models.create_web_authn_registration_verification_200_response_registration_options_extensions.CreateWebAuthnRegistrationVerification_200_response_registrationOptions_extensions(
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
