# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.verify_web_authn_authentication_verification_request_payload import VerifyWebAuthnAuthenticationVerificationRequestPayload

class TestVerifyWebAuthnAuthenticationVerificationRequestPayload(unittest.TestCase):
    """VerifyWebAuthnAuthenticationVerificationRequestPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifyWebAuthnAuthenticationVerificationRequestPayload:
        """Test VerifyWebAuthnAuthenticationVerificationRequestPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifyWebAuthnAuthenticationVerificationRequestPayload`
        """
        model = VerifyWebAuthnAuthenticationVerificationRequestPayload()
        if include_optional:
            return VerifyWebAuthnAuthenticationVerificationRequestPayload(
                type = '',
                id = '',
                raw_id = '',
                authenticator_attachment = 'cross-platform',
                client_extension_results = py_logto.models.verify_web_authn_registration_verification_request_payload_client_extension_results.VerifyWebAuthnRegistrationVerification_request_payload_clientExtensionResults(
                    appid = True, 
                    crep_props = py_logto.models.verify_web_authn_registration_verification_request_payload_client_extension_results_crep_props.VerifyWebAuthnRegistrationVerification_request_payload_clientExtensionResults_crepProps(
                        rk = True, ), 
                    hmac_create_secret = True, ),
                response = py_logto.models.verify_web_authn_authentication_verification_request_payload_response.VerifyWebAuthnAuthenticationVerification_request_payload_response(
                    client_data_json = '', 
                    authenticator_data = '', 
                    signature = '', 
                    user_handle = '', )
            )
        else:
            return VerifyWebAuthnAuthenticationVerificationRequestPayload(
                type = '',
                id = '',
                raw_id = '',
                client_extension_results = py_logto.models.verify_web_authn_registration_verification_request_payload_client_extension_results.VerifyWebAuthnRegistrationVerification_request_payload_clientExtensionResults(
                    appid = True, 
                    crep_props = py_logto.models.verify_web_authn_registration_verification_request_payload_client_extension_results_crep_props.VerifyWebAuthnRegistrationVerification_request_payload_clientExtensionResults_crepProps(
                        rk = True, ), 
                    hmac_create_secret = True, ),
                response = py_logto.models.verify_web_authn_authentication_verification_request_payload_response.VerifyWebAuthnAuthenticationVerification_request_payload_response(
                    client_data_json = '', 
                    authenticator_data = '', 
                    signature = '', 
                    user_handle = '', ),
        )
        """

    def testVerifyWebAuthnAuthenticationVerificationRequestPayload(self):
        """Test VerifyWebAuthnAuthenticationVerificationRequestPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
