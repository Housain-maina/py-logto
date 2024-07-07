# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_sign_in_exp_request_sign_in import UpdateSignInExpRequestSignIn

class TestUpdateSignInExpRequestSignIn(unittest.TestCase):
    """UpdateSignInExpRequestSignIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSignInExpRequestSignIn:
        """Test UpdateSignInExpRequestSignIn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSignInExpRequestSignIn`
        """
        model = UpdateSignInExpRequestSignIn()
        if include_optional:
            return UpdateSignInExpRequestSignIn(
                methods = [
                    py_logto.models.get_sign_in_exp_200_response_sign_in_methods_inner.GetSignInExp_200_response_signIn_methods_inner(
                        identifier = 'username', 
                        password = True, 
                        verification_code = True, 
                        is_password_primary = True, )
                    ]
            )
        else:
            return UpdateSignInExpRequestSignIn(
                methods = [
                    py_logto.models.get_sign_in_exp_200_response_sign_in_methods_inner.GetSignInExp_200_response_signIn_methods_inner(
                        identifier = 'username', 
                        password = True, 
                        verification_code = True, 
                        is_password_primary = True, )
                    ],
        )
        """

    def testUpdateSignInExpRequestSignIn(self):
        """Test UpdateSignInExpRequestSignIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
