# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_sign_in_exp_patch_request_sign_up import ApiSignInExpPatchRequestSignUp

class TestApiSignInExpPatchRequestSignUp(unittest.TestCase):
    """ApiSignInExpPatchRequestSignUp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSignInExpPatchRequestSignUp:
        """Test ApiSignInExpPatchRequestSignUp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSignInExpPatchRequestSignUp`
        """
        model = ApiSignInExpPatchRequestSignUp()
        if include_optional:
            return ApiSignInExpPatchRequestSignUp(
                identifiers = [
                    'username'
                    ],
                password = True,
                verify = True
            )
        else:
            return ApiSignInExpPatchRequestSignUp(
                identifiers = [
                    'username'
                    ],
                password = True,
                verify = True,
        )
        """

    def testApiSignInExpPatchRequestSignUp(self):
        """Test ApiSignInExpPatchRequestSignUp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
