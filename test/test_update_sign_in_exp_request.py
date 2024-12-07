# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_sign_in_exp_request import UpdateSignInExpRequest

class TestUpdateSignInExpRequest(unittest.TestCase):
    """UpdateSignInExpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSignInExpRequest:
        """Test UpdateSignInExpRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSignInExpRequest`
        """
        model = UpdateSignInExpRequest()
        if include_optional:
            return UpdateSignInExpRequest(
                tenant_id = '',
                color = py_logto.models.update_sign_in_exp_request_color.UpdateSignInExp_request_color(
                    primary_color = '#bf3', 
                    is_dark_mode_enabled = True, 
                    dark_primary_color = '#bf3', ),
                branding = py_logto.models.list_application_organizations_200_response_inner_branding.ListApplicationOrganizations_200_response_inner_branding(
                    logo_url = '', 
                    dark_logo_url = '', 
                    favicon = '', 
                    dark_favicon = '', ),
                language_info = py_logto.models.update_sign_in_exp_request_language_info.UpdateSignInExp_request_languageInfo(
                    auto_detect = True, 
                    fallback_language = 'af-ZA', ),
                agree_to_terms_policy = 'Automatic',
                sign_in = py_logto.models.update_sign_in_exp_request_sign_in.UpdateSignInExp_request_signIn(
                    methods = [
                        py_logto.models.get_sign_in_exp_200_response_sign_in_methods_inner.GetSignInExp_200_response_signIn_methods_inner(
                            identifier = 'username', 
                            password = True, 
                            verification_code = True, 
                            is_password_primary = True, )
                        ], ),
                sign_up = py_logto.models.update_sign_in_exp_request_sign_up.UpdateSignInExp_request_signUp(
                    identifiers = [
                        'username'
                        ], 
                    password = True, 
                    verify = True, ),
                social_sign_in = py_logto.models.get_sign_in_exp_200_response_social_sign_in.GetSignInExp_200_response_socialSignIn(
                    automatic_account_linking = True, ),
                social_sign_in_connector_targets = [
                    ''
                    ],
                sign_in_mode = 'SignIn',
                custom_css = '',
                custom_content = {
                    'key' : ''
                    },
                custom_ui_assets = py_logto.models.get_sign_in_exp_200_response_custom_ui_assets.GetSignInExp_200_response_customUiAssets(
                    id = '', 
                    created_at = 1.337, ),
                password_policy = py_logto.models.get_sign_in_exp_200_response_password_policy.GetSignInExp_200_response_passwordPolicy(
                    length = py_logto.models.get_sign_in_exp_200_response_password_policy_length.GetSignInExp_200_response_passwordPolicy_length(
                        min = 1.337, 
                        max = 1.337, ), 
                    character_types = py_logto.models.get_sign_in_exp_200_response_password_policy_character_types.GetSignInExp_200_response_passwordPolicy_characterTypes(
                        min = 1.337, ), 
                    rejects = py_logto.models.get_sign_in_exp_200_response_password_policy_rejects.GetSignInExp_200_response_passwordPolicy_rejects(
                        pwned = True, 
                        repetition_and_sequence = True, 
                        user_info = True, 
                        words = [
                            ''
                            ], ), ),
                mfa = py_logto.models.get_sign_in_exp_200_response_mfa.GetSignInExp_200_response_mfa(
                    factors = [
                        'Totp'
                        ], 
                    policy = 'UserControlled', ),
                single_sign_on_enabled = True,
                terms_of_use_url = None,
                privacy_policy_url = None,
                support_email = None,
                support_website_url = None,
                unknown_session_redirect_url = None
            )
        else:
            return UpdateSignInExpRequest(
        )
        """

    def testUpdateSignInExpRequest(self):
        """Test UpdateSignInExpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
