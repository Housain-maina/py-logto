# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_sign_in_exp200_response_password_policy_length import GetSignInExp200ResponsePasswordPolicyLength

class TestGetSignInExp200ResponsePasswordPolicyLength(unittest.TestCase):
    """GetSignInExp200ResponsePasswordPolicyLength unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSignInExp200ResponsePasswordPolicyLength:
        """Test GetSignInExp200ResponsePasswordPolicyLength
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSignInExp200ResponsePasswordPolicyLength`
        """
        model = GetSignInExp200ResponsePasswordPolicyLength()
        if include_optional:
            return GetSignInExp200ResponsePasswordPolicyLength(
                min = 1.337,
                max = 1.337
            )
        else:
            return GetSignInExp200ResponsePasswordPolicyLength(
                min = 1.337,
                max = 1.337,
        )
        """

    def testGetSignInExp200ResponsePasswordPolicyLength(self):
        """Test GetSignInExp200ResponsePasswordPolicyLength"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
