# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.configs_api import ConfigsApi


class TestConfigsApi(unittest.TestCase):
    """ConfigsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConfigsApi()

    def tearDown(self) -> None:
        pass

    def test_api_configs_admin_console_get(self) -> None:
        """Test case for api_configs_admin_console_get

        Get admin console config
        """
        pass

    def test_api_configs_admin_console_patch(self) -> None:
        """Test case for api_configs_admin_console_patch

        Update admin console config
        """
        pass

    def test_api_configs_jwt_customizer_get(self) -> None:
        """Test case for api_configs_jwt_customizer_get

        Get all JWT customizers
        """
        pass

    def test_api_configs_jwt_customizer_token_type_path_delete(self) -> None:
        """Test case for api_configs_jwt_customizer_token_type_path_delete

        Delete JWT customizer
        """
        pass

    def test_api_configs_jwt_customizer_token_type_path_get(self) -> None:
        """Test case for api_configs_jwt_customizer_token_type_path_get

        Get JWT customizer
        """
        pass

    def test_api_configs_jwt_customizer_token_type_path_patch(self) -> None:
        """Test case for api_configs_jwt_customizer_token_type_path_patch

        Update JWT customizer
        """
        pass

    def test_api_configs_jwt_customizer_token_type_path_put(self) -> None:
        """Test case for api_configs_jwt_customizer_token_type_path_put

        Create or update JWT customizer
        """
        pass

    def test_api_configs_oidc_key_type_get(self) -> None:
        """Test case for api_configs_oidc_key_type_get

        Get OIDC keys
        """
        pass

    def test_api_configs_oidc_key_type_key_id_delete(self) -> None:
        """Test case for api_configs_oidc_key_type_key_id_delete

        Delete OIDC key
        """
        pass

    def test_api_configs_oidc_key_type_rotate_post(self) -> None:
        """Test case for api_configs_oidc_key_type_rotate_post

        Rotate OIDC keys
        """
        pass


if __name__ == '__main__':
    unittest.main()