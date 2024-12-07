# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_web_authn_registration_verification200_response_registration_options_exclude_credentials_inner import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner

class TestCreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner(unittest.TestCase):
    """CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner:
        """Test CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner`
        """
        model = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner()
        if include_optional:
            return CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner(
                type = '',
                id = '',
                transports = [
                    'usb'
                    ]
            )
        else:
            return CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner(
                type = '',
                id = '',
        )
        """

    def testCreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner(self):
        """Test CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()