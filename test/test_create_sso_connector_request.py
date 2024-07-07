# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_sso_connector_request import CreateSsoConnectorRequest

class TestCreateSsoConnectorRequest(unittest.TestCase):
    """CreateSsoConnectorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSsoConnectorRequest:
        """Test CreateSsoConnectorRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSsoConnectorRequest`
        """
        model = CreateSsoConnectorRequest()
        if include_optional:
            return CreateSsoConnectorRequest(
                config = None,
                domains = [
                    ''
                    ],
                branding = py_logto.models.list_organization_jit_sso_connectors_200_response_inner_branding.ListOrganizationJitSsoConnectors_200_response_inner_branding(
                    display_name = '', 
                    logo = '', 
                    dark_logo = '', ),
                sync_profile = True,
                provider_name = '0',
                connector_name = '0'
            )
        else:
            return CreateSsoConnectorRequest(
                provider_name = '0',
                connector_name = '0',
        )
        """

    def testCreateSsoConnectorRequest(self):
        """Test CreateSsoConnectorRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()