# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_resources_get200_response_inner_scopes_inner import ApiResourcesGet200ResponseInnerScopesInner

class TestApiResourcesGet200ResponseInnerScopesInner(unittest.TestCase):
    """ApiResourcesGet200ResponseInnerScopesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResourcesGet200ResponseInnerScopesInner:
        """Test ApiResourcesGet200ResponseInnerScopesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResourcesGet200ResponseInnerScopesInner`
        """
        model = ApiResourcesGet200ResponseInnerScopesInner()
        if include_optional:
            return ApiResourcesGet200ResponseInnerScopesInner(
                id = '0',
                resource_id = '0',
                name = '0',
                description = '',
                created_at = 1.337
            )
        else:
            return ApiResourcesGet200ResponseInnerScopesInner(
                id = '0',
                resource_id = '0',
                name = '0',
                description = '',
                created_at = 1.337,
        )
        """

    def testApiResourcesGet200ResponseInnerScopesInner(self):
        """Test ApiResourcesGet200ResponseInnerScopesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
