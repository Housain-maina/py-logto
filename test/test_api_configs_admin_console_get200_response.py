# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_admin_console_get200_response import ApiConfigsAdminConsoleGet200Response

class TestApiConfigsAdminConsoleGet200Response(unittest.TestCase):
    """ApiConfigsAdminConsoleGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsAdminConsoleGet200Response:
        """Test ApiConfigsAdminConsoleGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsAdminConsoleGet200Response`
        """
        model = ApiConfigsAdminConsoleGet200Response()
        if include_optional:
            return ApiConfigsAdminConsoleGet200Response(
                sign_in_experience_customized = True,
                organization_created = True,
                development_tenant_migration_notification = py_logto.models._api_configs_admin_console_get_200_response_development_tenant_migration_notification._api_configs_admin_console_get_200_response_developmentTenantMigrationNotification(
                    is_paid_tenant = True, 
                    tag = '', 
                    read_at = 1.337, ),
                checked_charge_notification = py_logto.models._api_configs_admin_console_get_200_response_checked_charge_notification._api_configs_admin_console_get_200_response_checkedChargeNotification(
                    token = True, 
                    api_resource = True, 
                    machine_to_machine_app = True, 
                    tenant_member = True, )
            )
        else:
            return ApiConfigsAdminConsoleGet200Response(
                sign_in_experience_customized = True,
                organization_created = True,
        )
        """

    def testApiConfigsAdminConsoleGet200Response(self):
        """Test ApiConfigsAdminConsoleGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
