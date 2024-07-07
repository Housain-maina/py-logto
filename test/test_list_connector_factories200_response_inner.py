# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_connector_factories200_response_inner import ListConnectorFactories200ResponseInner

class TestListConnectorFactories200ResponseInner(unittest.TestCase):
    """ListConnectorFactories200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConnectorFactories200ResponseInner:
        """Test ListConnectorFactories200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConnectorFactories200ResponseInner`
        """
        model = ListConnectorFactories200ResponseInner()
        if include_optional:
            return ListConnectorFactories200ResponseInner(
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
                custom_data = {
                    'key' : {}
                    },
                from_email = '',
                platform = 'Native',
                is_standard = True
            )
        else:
            return ListConnectorFactories200ResponseInner(
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

    def testListConnectorFactories200ResponseInner(self):
        """Test ListConnectorFactories200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()