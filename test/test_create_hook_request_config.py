# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_hook_request_config import CreateHookRequestConfig

class TestCreateHookRequestConfig(unittest.TestCase):
    """CreateHookRequestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateHookRequestConfig:
        """Test CreateHookRequestConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateHookRequestConfig`
        """
        model = CreateHookRequestConfig()
        if include_optional:
            return CreateHookRequestConfig(
                url = '',
                headers = {
                    'key' : ''
                    },
                retries = 1.337
            )
        else:
            return CreateHookRequestConfig(
                url = '',
        )
        """

    def testCreateHookRequestConfig(self):
        """Test CreateHookRequestConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
