# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_sign_in_exp_get200_response_sign_in_methods_inner import ApiSignInExpGet200ResponseSignInMethodsInner

class TestApiSignInExpGet200ResponseSignInMethodsInner(unittest.TestCase):
    """ApiSignInExpGet200ResponseSignInMethodsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSignInExpGet200ResponseSignInMethodsInner:
        """Test ApiSignInExpGet200ResponseSignInMethodsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSignInExpGet200ResponseSignInMethodsInner`
        """
        model = ApiSignInExpGet200ResponseSignInMethodsInner()
        if include_optional:
            return ApiSignInExpGet200ResponseSignInMethodsInner(
                identifier = 'username',
                password = True,
                verification_code = True,
                is_password_primary = True
            )
        else:
            return ApiSignInExpGet200ResponseSignInMethodsInner(
                identifier = 'username',
                password = True,
                verification_code = True,
                is_password_primary = True,
        )
        """

    def testApiSignInExpGet200ResponseSignInMethodsInner(self):
        """Test ApiSignInExpGet200ResponseSignInMethodsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
