# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_sso_connector_providers200_response_inner import ListSsoConnectorProviders200ResponseInner

class TestListSsoConnectorProviders200ResponseInner(unittest.TestCase):
    """ListSsoConnectorProviders200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSsoConnectorProviders200ResponseInner:
        """Test ListSsoConnectorProviders200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSsoConnectorProviders200ResponseInner`
        """
        model = ListSsoConnectorProviders200ResponseInner()
        if include_optional:
            return ListSsoConnectorProviders200ResponseInner(
                provider_name = 'OIDC',
                provider_type = 'oidc',
                logo = '',
                logo_dark = '',
                description = '',
                name = ''
            )
        else:
            return ListSsoConnectorProviders200ResponseInner(
                provider_name = 'OIDC',
                provider_type = 'oidc',
                logo = '',
                logo_dark = '',
                description = '',
                name = '',
        )
        """

    def testListSsoConnectorProviders200ResponseInner(self):
        """Test ListSsoConnectorProviders200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()