# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_organization_jit_email_domain_request import CreateOrganizationJitEmailDomainRequest

class TestCreateOrganizationJitEmailDomainRequest(unittest.TestCase):
    """CreateOrganizationJitEmailDomainRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOrganizationJitEmailDomainRequest:
        """Test CreateOrganizationJitEmailDomainRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOrganizationJitEmailDomainRequest`
        """
        model = CreateOrganizationJitEmailDomainRequest()
        if include_optional:
            return CreateOrganizationJitEmailDomainRequest(
                email_domain = '0'
            )
        else:
            return CreateOrganizationJitEmailDomainRequest(
                email_domain = '0',
        )
        """

    def testCreateOrganizationJitEmailDomainRequest(self):
        """Test CreateOrganizationJitEmailDomainRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
