# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.interaction_api import InteractionApi


class TestInteractionApi(unittest.TestCase):
    """InteractionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InteractionApi()

    def tearDown(self) -> None:
        pass

    def test_api_interaction_bind_mfa_post(self) -> None:
        """Test case for api_interaction_bind_mfa_post

        """
        pass

    def test_api_interaction_consent_get(self) -> None:
        """Test case for api_interaction_consent_get

        """
        pass

    def test_api_interaction_consent_post(self) -> None:
        """Test case for api_interaction_consent_post

        """
        pass

    def test_api_interaction_delete(self) -> None:
        """Test case for api_interaction_delete

        """
        pass

    def test_api_interaction_event_put(self) -> None:
        """Test case for api_interaction_event_put

        """
        pass

    def test_api_interaction_identifiers_patch(self) -> None:
        """Test case for api_interaction_identifiers_patch

        """
        pass

    def test_api_interaction_mfa_put(self) -> None:
        """Test case for api_interaction_mfa_put

        """
        pass

    def test_api_interaction_mfa_skipped_put(self) -> None:
        """Test case for api_interaction_mfa_skipped_put

        """
        pass

    def test_api_interaction_profile_delete(self) -> None:
        """Test case for api_interaction_profile_delete

        """
        pass

    def test_api_interaction_profile_patch(self) -> None:
        """Test case for api_interaction_profile_patch

        """
        pass

    def test_api_interaction_profile_put(self) -> None:
        """Test case for api_interaction_profile_put

        """
        pass

    def test_api_interaction_put(self) -> None:
        """Test case for api_interaction_put

        """
        pass

    def test_api_interaction_single_sign_on_connector_id_authentication_post(self) -> None:
        """Test case for api_interaction_single_sign_on_connector_id_authentication_post

        """
        pass

    def test_api_interaction_single_sign_on_connector_id_authorization_url_post(self) -> None:
        """Test case for api_interaction_single_sign_on_connector_id_authorization_url_post

        """
        pass

    def test_api_interaction_single_sign_on_connector_id_registration_post(self) -> None:
        """Test case for api_interaction_single_sign_on_connector_id_registration_post

        """
        pass

    def test_api_interaction_single_sign_on_connectors_get(self) -> None:
        """Test case for api_interaction_single_sign_on_connectors_get

        """
        pass

    def test_api_interaction_submit_post(self) -> None:
        """Test case for api_interaction_submit_post

        """
        pass

    def test_api_interaction_verification_social_authorization_uri_post(self) -> None:
        """Test case for api_interaction_verification_social_authorization_uri_post

        """
        pass

    def test_api_interaction_verification_totp_post(self) -> None:
        """Test case for api_interaction_verification_totp_post

        """
        pass

    def test_api_interaction_verification_verification_code_post(self) -> None:
        """Test case for api_interaction_verification_verification_code_post

        """
        pass

    def test_api_interaction_verification_webauthn_authentication_post(self) -> None:
        """Test case for api_interaction_verification_webauthn_authentication_post

        """
        pass

    def test_api_interaction_verification_webauthn_registration_post(self) -> None:
        """Test case for api_interaction_verification_webauthn_registration_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
