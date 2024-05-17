# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_users_user_id_patch200_response import ApiUsersUserIdPatch200Response

class TestApiUsersUserIdPatch200Response(unittest.TestCase):
    """ApiUsersUserIdPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiUsersUserIdPatch200Response:
        """Test ApiUsersUserIdPatch200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiUsersUserIdPatch200Response`
        """
        model = ApiUsersUserIdPatch200Response()
        if include_optional:
            return ApiUsersUserIdPatch200Response(
                id = '0',
                username = '',
                primary_email = '',
                primary_phone = '',
                name = '',
                avatar = '',
                custom_data = None,
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
                    profile = '', 
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
                has_password = True,
                sso_identities = [
                    py_logto.models._api_users__user_id__get_200_response_sso_identities_inner._api_users__userId__get_200_response_ssoIdentities_inner(
                        id = '0', 
                        user_id = '0', 
                        issuer = '0', 
                        identity_id = '0', 
                        detail = py_logto.models.detail.detail(), 
                        created_at = 1.337, 
                        sso_connector_id = '0', )
                    ]
            )
        else:
            return ApiUsersUserIdPatch200Response(
                id = '0',
                username = '',
                primary_email = '',
                primary_phone = '',
                name = '',
                avatar = '',
                custom_data = None,
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
                    profile = '', 
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
        )
        """

    def testApiUsersUserIdPatch200Response(self):
        """Test ApiUsersUserIdPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
