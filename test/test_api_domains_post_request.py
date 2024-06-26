# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_domains_post_request import ApiDomainsPostRequest

class TestApiDomainsPostRequest(unittest.TestCase):
    """ApiDomainsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDomainsPostRequest:
        """Test ApiDomainsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDomainsPostRequest`
        """
        model = ApiDomainsPostRequest()
        if include_optional:
            return ApiDomainsPostRequest(
                domain = '0'
            )
        else:
            return ApiDomainsPostRequest(
                domain = '0',
        )
        """

    def testApiDomainsPostRequest(self):
        """Test ApiDomainsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
