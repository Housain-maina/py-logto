# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_connectors200_response_inner_metadata import ListConnectors200ResponseInnerMetadata

class TestListConnectors200ResponseInnerMetadata(unittest.TestCase):
    """ListConnectors200ResponseInnerMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConnectors200ResponseInnerMetadata:
        """Test ListConnectors200ResponseInnerMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConnectors200ResponseInnerMetadata`
        """
        model = ListConnectors200ResponseInnerMetadata()
        if include_optional:
            return ListConnectors200ResponseInnerMetadata(
                target = '',
                name = None,
                logo = '',
                logo_dark = ''
            )
        else:
            return ListConnectors200ResponseInnerMetadata(
        )
        """

    def testListConnectors200ResponseInnerMetadata(self):
        """Test ListConnectors200ResponseInnerMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()