# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_sign_in_exp200_response_password_policy_rejects import GetSignInExp200ResponsePasswordPolicyRejects

class TestGetSignInExp200ResponsePasswordPolicyRejects(unittest.TestCase):
    """GetSignInExp200ResponsePasswordPolicyRejects unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSignInExp200ResponsePasswordPolicyRejects:
        """Test GetSignInExp200ResponsePasswordPolicyRejects
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSignInExp200ResponsePasswordPolicyRejects`
        """
        model = GetSignInExp200ResponsePasswordPolicyRejects()
        if include_optional:
            return GetSignInExp200ResponsePasswordPolicyRejects(
                pwned = True,
                repetition_and_sequence = True,
                user_info = True,
                words = [
                    ''
                    ]
            )
        else:
            return GetSignInExp200ResponsePasswordPolicyRejects(
                pwned = True,
                repetition_and_sequence = True,
                user_info = True,
                words = [
                    ''
                    ],
        )
        """

    def testGetSignInExp200ResponsePasswordPolicyRejects(self):
        """Test GetSignInExp200ResponsePasswordPolicyRejects"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
