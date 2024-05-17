# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_connector_factories_get200_response_inner import ApiConnectorFactoriesGet200ResponseInner

class TestApiConnectorFactoriesGet200ResponseInner(unittest.TestCase):
    """ApiConnectorFactoriesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConnectorFactoriesGet200ResponseInner:
        """Test ApiConnectorFactoriesGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConnectorFactoriesGet200ResponseInner`
        """
        model = ApiConnectorFactoriesGet200ResponseInner()
        if include_optional:
            return ApiConnectorFactoriesGet200ResponseInner(
                type = 'Email',
                is_demo = True,
                id = '',
                target = '',
                name = None,
                description = None,
                logo = '',
                logo_dark = '',
                readme = '',
                config_template = '',
                form_items = [
                    null
                    ],
                platform = 'Native',
                is_standard = True
            )
        else:
            return ApiConnectorFactoriesGet200ResponseInner(
                type = 'Email',
                id = '',
                target = '',
                name = None,
                description = None,
                logo = '',
                logo_dark = '',
                readme = '',
                platform = 'Native',
        )
        """

    def testApiConnectorFactoriesGet200ResponseInner(self):
        """Test ApiConnectorFactoriesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
