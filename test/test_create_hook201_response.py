# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_hook201_response import CreateHook201Response

class TestCreateHook201Response(unittest.TestCase):
    """CreateHook201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateHook201Response:
        """Test CreateHook201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateHook201Response`
        """
        model = CreateHook201Response()
        if include_optional:
            return CreateHook201Response(
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
                created_at = 1.337
            )
        else:
            return CreateHook201Response(
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

    def testCreateHook201Response(self):
        """Test CreateHook201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()