# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_applications_id_patch_request_protected_app_metadata import ApiApplicationsIdPatchRequestProtectedAppMetadata

class TestApiApplicationsIdPatchRequestProtectedAppMetadata(unittest.TestCase):
    """ApiApplicationsIdPatchRequestProtectedAppMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiApplicationsIdPatchRequestProtectedAppMetadata:
        """Test ApiApplicationsIdPatchRequestProtectedAppMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiApplicationsIdPatchRequestProtectedAppMetadata`
        """
        model = ApiApplicationsIdPatchRequestProtectedAppMetadata()
        if include_optional:
            return ApiApplicationsIdPatchRequestProtectedAppMetadata(
                origin = '',
                session_duration = 1.337,
                page_rules = [
                    py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_page_rules_inner._api_applications_get_200_response_inner_protectedAppMetadata_pageRules_inner(
                        path = '', )
                    ]
            )
        else:
            return ApiApplicationsIdPatchRequestProtectedAppMetadata(
        )
        """

    def testApiApplicationsIdPatchRequestProtectedAppMetadata(self):
        """Test ApiApplicationsIdPatchRequestProtectedAppMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
