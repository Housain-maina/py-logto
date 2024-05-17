# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_users_user_id_patch_request_name import ApiUsersUserIdPatchRequestName

class TestApiUsersUserIdPatchRequestName(unittest.TestCase):
    """ApiUsersUserIdPatchRequestName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiUsersUserIdPatchRequestName:
        """Test ApiUsersUserIdPatchRequestName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiUsersUserIdPatchRequestName`
        """
        model = ApiUsersUserIdPatchRequestName()
        if include_optional:
            return ApiUsersUserIdPatchRequestName(
            )
        else:
            return ApiUsersUserIdPatchRequestName(
        )
        """

    def testApiUsersUserIdPatchRequestName(self):
        """Test ApiUsersUserIdPatchRequestName"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()