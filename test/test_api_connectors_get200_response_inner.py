# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner

class TestApiConnectorsGet200ResponseInner(unittest.TestCase):
    """ApiConnectorsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConnectorsGet200ResponseInner:
        """Test ApiConnectorsGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConnectorsGet200ResponseInner`
        """
        model = ApiConnectorsGet200ResponseInner()
        if include_optional:
            return ApiConnectorsGet200ResponseInner(
                id = '',
                sync_profile = True,
                config = None,
                metadata = py_logto.models._api_connectors_get_200_response_inner_metadata._api_connectors_get_200_response_inner_metadata(
                    target = '', 
                    name = py_logto.models.name.name(), 
                    logo = '', 
                    logo_dark = '', ),
                connector_id = '0',
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
                is_standard = True,
                type = 'Email',
                is_demo = True,
                extra_info = {
                    'key' : {}
                    },
                usage = 1.337
            )
        else:
            return ApiConnectorsGet200ResponseInner(
                id = '',
                sync_profile = True,
                config = None,
                metadata = py_logto.models._api_connectors_get_200_response_inner_metadata._api_connectors_get_200_response_inner_metadata(
                    target = '', 
                    name = py_logto.models.name.name(), 
                    logo = '', 
                    logo_dark = '', ),
                connector_id = '0',
                target = '',
                name = None,
                description = None,
                logo = '',
                logo_dark = '',
                readme = '',
                platform = 'Native',
                type = 'Email',
        )
        """

    def testApiConnectorsGet200ResponseInner(self):
        """Test ApiConnectorsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()