# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_sign_in_exp_request_unknown_session_redirect_url import UpdateSignInExpRequestUnknownSessionRedirectUrl

class TestUpdateSignInExpRequestUnknownSessionRedirectUrl(unittest.TestCase):
    """UpdateSignInExpRequestUnknownSessionRedirectUrl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSignInExpRequestUnknownSessionRedirectUrl:
        """Test UpdateSignInExpRequestUnknownSessionRedirectUrl
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSignInExpRequestUnknownSessionRedirectUrl`
        """
        model = UpdateSignInExpRequestUnknownSessionRedirectUrl()
        if include_optional:
            return UpdateSignInExpRequestUnknownSessionRedirectUrl(
            )
        else:
            return UpdateSignInExpRequestUnknownSessionRedirectUrl(
        )
        """

    def testUpdateSignInExpRequestUnknownSessionRedirectUrl(self):
        """Test UpdateSignInExpRequestUnknownSessionRedirectUrl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
