# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_hooks200_response_inner import ListHooks200ResponseInner

class TestListHooks200ResponseInner(unittest.TestCase):
    """ListHooks200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListHooks200ResponseInner:
        """Test ListHooks200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListHooks200ResponseInner`
        """
        model = ListHooks200ResponseInner()
        if include_optional:
            return ListHooks200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '',
                event = 'PostRegister',
                events = [
                    'PostRegister'
                    ],
                config = py_logto.models.list_hooks_200_response_inner_config.ListHooks_200_response_inner_config(
                    url = '', 
                    headers = {
                        'key' : ''
                        }, 
                    retries = 1.337, ),
                signing_key = '',
                enabled = True,
                created_at = 1.337,
                execution_stats = py_logto.models.list_hooks_200_response_inner_execution_stats.ListHooks_200_response_inner_executionStats(
                    success_count = 1.337, 
                    request_count = 1.337, )
            )
        else:
            return ListHooks200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '',
                event = 'PostRegister',
                events = [
                    'PostRegister'
                    ],
                config = py_logto.models.list_hooks_200_response_inner_config.ListHooks_200_response_inner_config(
                    url = '', 
                    headers = {
                        'key' : ''
                        }, 
                    retries = 1.337, ),
                signing_key = '',
                enabled = True,
                created_at = 1.337,
        )
        """

    def testListHooks200ResponseInner(self):
        """Test ListHooks200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
