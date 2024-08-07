# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.sign_in_experience_api import SignInExperienceApi


class TestSignInExperienceApi(unittest.TestCase):
    """SignInExperienceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SignInExperienceApi()

    def tearDown(self) -> None:
        pass

    def test_get_sign_in_exp(self) -> None:
        """Test case for get_sign_in_exp

        Get default sign-in experience settings
        """
        pass

    def test_update_sign_in_exp(self) -> None:
        """Test case for update_sign_in_exp

        Update default sign-in experience settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
