# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf

class TestApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf(unittest.TestCase):
    """ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf:
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf`
        """
        model = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf()
        if include_optional:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf(
                script = '',
                environment_variables = {
                    'key' : ''
                    },
                context_sample = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample(
                    user = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user(
                        id = '0', 
                        username = '', 
                        primary_email = '', 
                        primary_phone = '', 
                        name = '', 
                        avatar = '', 
                        custom_data = py_logto.models.custom_data.customData(), 
                        identities = {
                            'key' : py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_identities_value._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_identities_value(
                                user_id = '', 
                                details = py_logto.models.details.details(), )
                            }, 
                        last_sign_in_at = 1.337, 
                        created_at = 1.337, 
                        updated_at = 1.337, 
                        profile = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_profile._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_profile(
                            family_name = '', 
                            given_name = '', 
                            middle_name = '', 
                            nickname = '', 
                            preferred_username = '', 
                            website = '', 
                            gender = '', 
                            birthdate = '', 
                            zoneinfo = '', 
                            locale = '', 
                            address = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_profile_address._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_profile_address(
                                formatted = '', 
                                street_address = '', 
                                locality = '', 
                                region = '', 
                                postal_code = '', 
                                country = '', ), ), 
                        application_id = '', 
                        is_suspended = True, 
                        sso_identities = [
                            py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_sso_identities_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_ssoIdentities_inner(
                                issuer = '0', 
                                identity_id = '0', 
                                detail = py_logto.models.detail.detail(), )
                            ], 
                        mfa_verification_factors = [
                            'Totp'
                            ], 
                        roles = [
                            py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner(
                                id = '0', 
                                name = '0', 
                                description = '0', 
                                scopes = [
                                    py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner(
                                        id = '0', 
                                        name = '0', 
                                        description = '', 
                                        resource_id = '0', 
                                        resource = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                                            id = '0', 
                                            name = '0', 
                                            indicator = '0', 
                                            is_default = True, 
                                            access_token_ttl = 1.337, ), )
                                    ], )
                            ], 
                        organizations = [
                            py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_organization_scopes_inner._api_applications__applicationId__user_consent_scopes_get_200_response_organizationScopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], 
                        organization_roles = [
                            py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_organization_roles_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_organizationRoles_inner(
                                organization_id = '', 
                                role_id = '', 
                                role_name = '', )
                            ], ), ),
                token_sample = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_token_sample._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_tokenSample(
                    jti = '', 
                    aud = null, 
                    scope = '', 
                    client_id = '', 
                    account_id = '', 
                    expires_with_session = True, 
                    grant_id = '', 
                    gty = '', 
                    session_uid = '', 
                    sid = '', 
                    kind = '', )
            )
        else:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf(
        )
        """

    def testApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf(self):
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
