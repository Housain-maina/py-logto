# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_oidc_key_type_get200_response_inner import ApiConfigsOidcKeyTypeGet200ResponseInner

class TestApiConfigsOidcKeyTypeGet200ResponseInner(unittest.TestCase):
    """ApiConfigsOidcKeyTypeGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsOidcKeyTypeGet200ResponseInner:
        """Test ApiConfigsOidcKeyTypeGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsOidcKeyTypeGet200ResponseInner`
        """
        model = ApiConfigsOidcKeyTypeGet200ResponseInner()
        if include_optional:
            return ApiConfigsOidcKeyTypeGet200ResponseInner(
                id = '',
                created_at = 1.337,
                signing_key_algorithm = 'RSA'
            )
        else:
            return ApiConfigsOidcKeyTypeGet200ResponseInner(
                id = '',
                created_at = 1.337,
        )
        """

    def testApiConfigsOidcKeyTypeGet200ResponseInner(self):
        """Test ApiConfigsOidcKeyTypeGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
