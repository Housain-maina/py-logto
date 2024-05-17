# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_hooks_id_patch_request import ApiHooksIdPatchRequest

class TestApiHooksIdPatchRequest(unittest.TestCase):
    """ApiHooksIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiHooksIdPatchRequest:
        """Test ApiHooksIdPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiHooksIdPatchRequest`
        """
        model = ApiHooksIdPatchRequest()
        if include_optional:
            return ApiHooksIdPatchRequest(
                name = '0',
                event = 'PostRegister',
                events = [
                    'PostRegister'
                    ],
                config = py_logto.models._api_hooks_post_request_config._api_hooks_post_request_config(
                    url = '', 
                    headers = {
                        'key' : ''
                        }, 
                    retries = 1.337, ),
                enabled = True,
                created_at = 1.337
            )
        else:
            return ApiHooksIdPatchRequest(
        )
        """

    def testApiHooksIdPatchRequest(self):
        """Test ApiHooksIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
