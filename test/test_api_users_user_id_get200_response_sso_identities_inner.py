# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_users_user_id_get200_response_sso_identities_inner import ApiUsersUserIdGet200ResponseSsoIdentitiesInner

class TestApiUsersUserIdGet200ResponseSsoIdentitiesInner(unittest.TestCase):
    """ApiUsersUserIdGet200ResponseSsoIdentitiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiUsersUserIdGet200ResponseSsoIdentitiesInner:
        """Test ApiUsersUserIdGet200ResponseSsoIdentitiesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiUsersUserIdGet200ResponseSsoIdentitiesInner`
        """
        model = ApiUsersUserIdGet200ResponseSsoIdentitiesInner()
        if include_optional:
            return ApiUsersUserIdGet200ResponseSsoIdentitiesInner(
                id = '0',
                user_id = '0',
                issuer = '0',
                identity_id = '0',
                detail = None,
                created_at = 1.337,
                sso_connector_id = '0'
            )
        else:
            return ApiUsersUserIdGet200ResponseSsoIdentitiesInner(
                id = '0',
                user_id = '0',
                issuer = '0',
                identity_id = '0',
                detail = None,
                created_at = 1.337,
                sso_connector_id = '0',
        )
        """

    def testApiUsersUserIdGet200ResponseSsoIdentitiesInner(self):
        """Test ApiUsersUserIdGet200ResponseSsoIdentitiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()