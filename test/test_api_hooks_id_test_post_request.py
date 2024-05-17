# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_hooks_id_test_post_request import ApiHooksIdTestPostRequest

class TestApiHooksIdTestPostRequest(unittest.TestCase):
    """ApiHooksIdTestPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiHooksIdTestPostRequest:
        """Test ApiHooksIdTestPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiHooksIdTestPostRequest`
        """
        model = ApiHooksIdTestPostRequest()
        if include_optional:
            return ApiHooksIdTestPostRequest(
                events = [
                    'PostRegister'
                    ],
                config = py_logto.models._api_hooks__id__test_post_request_config._api_hooks__id__test_post_request_config(
                    url = '', 
                    headers = {
                        'key' : ''
                        }, 
                    retries = 1.337, ),
                event = None
            )
        else:
            return ApiHooksIdTestPostRequest(
                events = [
                    'PostRegister'
                    ],
                config = py_logto.models._api_hooks__id__test_post_request_config._api_hooks__id__test_post_request_config(
                    url = '', 
                    headers = {
                        'key' : ''
                        }, 
                    retries = 1.337, ),
        )
        """

    def testApiHooksIdTestPostRequest(self):
        """Test ApiHooksIdTestPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()