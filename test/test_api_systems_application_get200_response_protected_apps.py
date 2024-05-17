# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_systems_application_get200_response_protected_apps import ApiSystemsApplicationGet200ResponseProtectedApps

class TestApiSystemsApplicationGet200ResponseProtectedApps(unittest.TestCase):
    """ApiSystemsApplicationGet200ResponseProtectedApps unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSystemsApplicationGet200ResponseProtectedApps:
        """Test ApiSystemsApplicationGet200ResponseProtectedApps
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSystemsApplicationGet200ResponseProtectedApps`
        """
        model = ApiSystemsApplicationGet200ResponseProtectedApps()
        if include_optional:
            return ApiSystemsApplicationGet200ResponseProtectedApps(
                default_domain = ''
            )
        else:
            return ApiSystemsApplicationGet200ResponseProtectedApps(
                default_domain = '',
        )
        """

    def testApiSystemsApplicationGet200ResponseProtectedApps(self):
        """Test ApiSystemsApplicationGet200ResponseProtectedApps"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()