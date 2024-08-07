# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_hooks200_response_inner_config import ListHooks200ResponseInnerConfig

class TestListHooks200ResponseInnerConfig(unittest.TestCase):
    """ListHooks200ResponseInnerConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListHooks200ResponseInnerConfig:
        """Test ListHooks200ResponseInnerConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListHooks200ResponseInnerConfig`
        """
        model = ListHooks200ResponseInnerConfig()
        if include_optional:
            return ListHooks200ResponseInnerConfig(
                url = '',
                headers = {
                    'key' : ''
                    },
                retries = 1.337
            )
        else:
            return ListHooks200ResponseInnerConfig(
                url = '',
        )
        """

    def testListHooks200ResponseInnerConfig(self):
        """Test ListHooks200ResponseInnerConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
