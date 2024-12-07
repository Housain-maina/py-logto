# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_sign_in_exp200_response_social_sign_in import GetSignInExp200ResponseSocialSignIn

class TestGetSignInExp200ResponseSocialSignIn(unittest.TestCase):
    """GetSignInExp200ResponseSocialSignIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSignInExp200ResponseSocialSignIn:
        """Test GetSignInExp200ResponseSocialSignIn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSignInExp200ResponseSocialSignIn`
        """
        model = GetSignInExp200ResponseSocialSignIn()
        if include_optional:
            return GetSignInExp200ResponseSocialSignIn(
                automatic_account_linking = True
            )
        else:
            return GetSignInExp200ResponseSocialSignIn(
        )
        """

    def testGetSignInExp200ResponseSocialSignIn(self):
        """Test GetSignInExp200ResponseSocialSignIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
