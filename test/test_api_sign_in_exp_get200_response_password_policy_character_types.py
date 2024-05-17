# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_sign_in_exp_get200_response_password_policy_character_types import ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes

class TestApiSignInExpGet200ResponsePasswordPolicyCharacterTypes(unittest.TestCase):
    """ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes:
        """Test ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes`
        """
        model = ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes()
        if include_optional:
            return ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes(
                min = 1.337
            )
        else:
            return ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes(
                min = 1.337,
        )
        """

    def testApiSignInExpGet200ResponsePasswordPolicyCharacterTypes(self):
        """Test ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
