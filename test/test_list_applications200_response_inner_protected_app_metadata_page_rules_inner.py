# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_applications200_response_inner_protected_app_metadata_page_rules_inner import ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner

class TestListApplications200ResponseInnerProtectedAppMetadataPageRulesInner(unittest.TestCase):
    """ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner:
        """Test ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner`
        """
        model = ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner()
        if include_optional:
            return ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner(
                path = ''
            )
        else:
            return ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner(
                path = '',
        )
        """

    def testListApplications200ResponseInnerProtectedAppMetadataPageRulesInner(self):
        """Test ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
