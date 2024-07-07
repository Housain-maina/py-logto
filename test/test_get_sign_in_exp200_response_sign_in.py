# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_sign_in_exp200_response_sign_in import GetSignInExp200ResponseSignIn

class TestGetSignInExp200ResponseSignIn(unittest.TestCase):
    """GetSignInExp200ResponseSignIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSignInExp200ResponseSignIn:
        """Test GetSignInExp200ResponseSignIn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSignInExp200ResponseSignIn`
        """
        model = GetSignInExp200ResponseSignIn()
        if include_optional:
            return GetSignInExp200ResponseSignIn(
                methods = [
                    py_logto.models.get_sign_in_exp_200_response_sign_in_methods_inner.GetSignInExp_200_response_signIn_methods_inner(
                        identifier = 'username', 
                        password = True, 
                        verification_code = True, 
                        is_password_primary = True, )
                    ]
            )
        else:
            return GetSignInExp200ResponseSignIn(
                methods = [
                    py_logto.models.get_sign_in_exp_200_response_sign_in_methods_inner.GetSignInExp_200_response_signIn_methods_inner(
                        identifier = 'username', 
                        password = True, 
                        verification_code = True, 
                        is_password_primary = True, )
                    ],
        )
        """

    def testGetSignInExp200ResponseSignIn(self):
        """Test GetSignInExp200ResponseSignIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
