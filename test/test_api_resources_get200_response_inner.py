# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_resources_get200_response_inner import ApiResourcesGet200ResponseInner

class TestApiResourcesGet200ResponseInner(unittest.TestCase):
    """ApiResourcesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResourcesGet200ResponseInner:
        """Test ApiResourcesGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResourcesGet200ResponseInner`
        """
        model = ApiResourcesGet200ResponseInner()
        if include_optional:
            return ApiResourcesGet200ResponseInner(
                id = '0',
                name = '0',
                indicator = '0',
                is_default = True,
                access_token_ttl = 1.337,
                scopes = [
                    py_logto.models._api_resources_get_200_response_inner_scopes_inner._api_resources_get_200_response_inner_scopes_inner(
                        id = '0', 
                        resource_id = '0', 
                        name = '0', 
                        description = '', 
                        created_at = 1.337, )
                    ]
            )
        else:
            return ApiResourcesGet200ResponseInner(
                id = '0',
                name = '0',
                indicator = '0',
                is_default = True,
                access_token_ttl = 1.337,
        )
        """

    def testApiResourcesGet200ResponseInner(self):
        """Test ApiResourcesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
