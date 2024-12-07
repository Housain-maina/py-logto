# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.test_jwt_customizer_request_one_of import TestJwtCustomizerRequestOneOf

class TestTestJwtCustomizerRequestOneOf(unittest.TestCase):
    """TestJwtCustomizerRequestOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestJwtCustomizerRequestOneOf:
        """Test TestJwtCustomizerRequestOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestJwtCustomizerRequestOneOf`
        """
        model = TestJwtCustomizerRequestOneOf()
        if include_optional:
            return TestJwtCustomizerRequestOneOf(
                token_type = '',
                environment_variables = {
                    'key' : ''
                    },
                script = '',
                token = py_logto.models.get_jwt_customizer_200_response_one_of_token_sample.GetJwtCustomizer_200_response_oneOf_tokenSample(
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
                    kind = '', ),
                context = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample.GetJwtCustomizer_200_response_oneOf_contextSample(
                    user = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user.GetJwtCustomizer_200_response_oneOf_contextSample_user(
                        id = '0', 
                        username = '', 
                        primary_email = '', 
                        primary_phone = '', 
                        name = '', 
                        avatar = '', 
                        custom_data = py_logto.models.custom_data.customData(), 
                        identities = {
                            'key' : py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_identities_value.GetJwtCustomizer_200_response_oneOf_contextSample_user_identities_value(
                                user_id = '', 
                                details = py_logto.models.details.details(), )
                            }, 
                        last_sign_in_at = 1.337, 
                        created_at = 1.337, 
                        updated_at = 1.337, 
                        profile = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile(
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
                            address = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile_address.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile_address(
                                formatted = '', 
                                street_address = '', 
                                locality = '', 
                                region = '', 
                                postal_code = '', 
                                country = '', ), ), 
                        application_id = '', 
                        is_suspended = True, 
                        has_password = True, 
                        sso_identities = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_sso_identities_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_ssoIdentities_inner(
                                issuer = '0', 
                                identity_id = '0', 
                                detail = py_logto.models.detail.detail(), )
                            ], 
                        mfa_verification_factors = [
                            'Totp'
                            ], 
                        roles = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner(
                                id = '0', 
                                name = '0', 
                                description = '0', 
                                scopes = [
                                    py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner(
                                        id = '0', 
                                        name = '0', 
                                        description = '', 
                                        resource_id = '0', 
                                        resource = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                                            tenant_id = '', 
                                            id = '0', 
                                            name = '0', 
                                            indicator = '0', 
                                            is_default = True, 
                                            access_token_ttl = 1.337, ), )
                                    ], )
                            ], 
                        organizations = [
                            py_logto.models.list_application_user_consent_scopes_200_response_organization_scopes_inner.ListApplicationUserConsentScopes_200_response_organizationScopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], 
                        organization_roles = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_organization_roles_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_organizationRoles_inner(
                                organization_id = '', 
                                role_id = '', 
                                role_name = '', )
                            ], ), 
                    grant = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_grant.GetJwtCustomizer_200_response_oneOf_contextSample_grant(
                        type = '', 
                        subject_token_context = py_logto.models.subject_token_context.subjectTokenContext(), ), )
            )
        else:
            return TestJwtCustomizerRequestOneOf(
                token_type = '',
                script = '',
                token = py_logto.models.get_jwt_customizer_200_response_one_of_token_sample.GetJwtCustomizer_200_response_oneOf_tokenSample(
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
                    kind = '', ),
                context = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample.GetJwtCustomizer_200_response_oneOf_contextSample(
                    user = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user.GetJwtCustomizer_200_response_oneOf_contextSample_user(
                        id = '0', 
                        username = '', 
                        primary_email = '', 
                        primary_phone = '', 
                        name = '', 
                        avatar = '', 
                        custom_data = py_logto.models.custom_data.customData(), 
                        identities = {
                            'key' : py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_identities_value.GetJwtCustomizer_200_response_oneOf_contextSample_user_identities_value(
                                user_id = '', 
                                details = py_logto.models.details.details(), )
                            }, 
                        last_sign_in_at = 1.337, 
                        created_at = 1.337, 
                        updated_at = 1.337, 
                        profile = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile(
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
                            address = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile_address.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile_address(
                                formatted = '', 
                                street_address = '', 
                                locality = '', 
                                region = '', 
                                postal_code = '', 
                                country = '', ), ), 
                        application_id = '', 
                        is_suspended = True, 
                        has_password = True, 
                        sso_identities = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_sso_identities_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_ssoIdentities_inner(
                                issuer = '0', 
                                identity_id = '0', 
                                detail = py_logto.models.detail.detail(), )
                            ], 
                        mfa_verification_factors = [
                            'Totp'
                            ], 
                        roles = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner(
                                id = '0', 
                                name = '0', 
                                description = '0', 
                                scopes = [
                                    py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner(
                                        id = '0', 
                                        name = '0', 
                                        description = '', 
                                        resource_id = '0', 
                                        resource = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                                            tenant_id = '', 
                                            id = '0', 
                                            name = '0', 
                                            indicator = '0', 
                                            is_default = True, 
                                            access_token_ttl = 1.337, ), )
                                    ], )
                            ], 
                        organizations = [
                            py_logto.models.list_application_user_consent_scopes_200_response_organization_scopes_inner.ListApplicationUserConsentScopes_200_response_organizationScopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], 
                        organization_roles = [
                            py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_organization_roles_inner.GetJwtCustomizer_200_response_oneOf_contextSample_user_organizationRoles_inner(
                                organization_id = '', 
                                role_id = '', 
                                role_name = '', )
                            ], ), 
                    grant = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_grant.GetJwtCustomizer_200_response_oneOf_contextSample_grant(
                        type = '', 
                        subject_token_context = py_logto.models.subject_token_context.subjectTokenContext(), ), ),
        )
        """

    def testTestJwtCustomizerRequestOneOf(self):
        """Test TestJwtCustomizerRequestOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
