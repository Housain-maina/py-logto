# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_sign_in_exp_patch200_response_password_policy import ApiSignInExpPatch200ResponsePasswordPolicy

class TestApiSignInExpPatch200ResponsePasswordPolicy(unittest.TestCase):
    """ApiSignInExpPatch200ResponsePasswordPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSignInExpPatch200ResponsePasswordPolicy:
        """Test ApiSignInExpPatch200ResponsePasswordPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSignInExpPatch200ResponsePasswordPolicy`
        """
        model = ApiSignInExpPatch200ResponsePasswordPolicy()
        if include_optional:
            return ApiSignInExpPatch200ResponsePasswordPolicy(
                length = py_logto.models._api_sign_in_exp_get_200_response_password_policy_length._api_sign_in_exp_get_200_response_passwordPolicy_length(
                    min = 1.337, 
                    max = 1.337, ),
                character_types = py_logto.models._api_sign_in_exp_get_200_response_password_policy_character_types._api_sign_in_exp_get_200_response_passwordPolicy_characterTypes(
                    min = 1.337, ),
                rejects = py_logto.models._api_sign_in_exp_get_200_response_password_policy_rejects._api_sign_in_exp_get_200_response_passwordPolicy_rejects(
                    pwned = True, 
                    repetition_and_sequence = True, 
                    user_info = True, 
                    words = [
                        ''
                        ], )
            )
        else:
            return ApiSignInExpPatch200ResponsePasswordPolicy(
        )
        """

    def testApiSignInExpPatch200ResponsePasswordPolicy(self):
        """Test ApiSignInExpPatch200ResponsePasswordPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
