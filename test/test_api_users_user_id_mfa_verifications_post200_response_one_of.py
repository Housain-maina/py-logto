# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_users_user_id_mfa_verifications_post200_response_one_of import ApiUsersUserIdMfaVerificationsPost200ResponseOneOf

class TestApiUsersUserIdMfaVerificationsPost200ResponseOneOf(unittest.TestCase):
    """ApiUsersUserIdMfaVerificationsPost200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiUsersUserIdMfaVerificationsPost200ResponseOneOf:
        """Test ApiUsersUserIdMfaVerificationsPost200ResponseOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiUsersUserIdMfaVerificationsPost200ResponseOneOf`
        """
        model = ApiUsersUserIdMfaVerificationsPost200ResponseOneOf()
        if include_optional:
            return ApiUsersUserIdMfaVerificationsPost200ResponseOneOf(
                type = '',
                secret = '',
                secret_qr_code = ''
            )
        else:
            return ApiUsersUserIdMfaVerificationsPost200ResponseOneOf(
                type = '',
                secret = '',
                secret_qr_code = '',
        )
        """

    def testApiUsersUserIdMfaVerificationsPost200ResponseOneOf(self):
        """Test ApiUsersUserIdMfaVerificationsPost200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
