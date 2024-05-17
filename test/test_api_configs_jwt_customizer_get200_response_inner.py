# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_jwt_customizer_get200_response_inner import ApiConfigsJwtCustomizerGet200ResponseInner

class TestApiConfigsJwtCustomizerGet200ResponseInner(unittest.TestCase):
    """ApiConfigsJwtCustomizerGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsJwtCustomizerGet200ResponseInner:
        """Test ApiConfigsJwtCustomizerGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsJwtCustomizerGet200ResponseInner`
        """
        model = ApiConfigsJwtCustomizerGet200ResponseInner()
        if include_optional:
            return ApiConfigsJwtCustomizerGet200ResponseInner(
                key = '',
                value = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_1._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_1(
                    script = '', 
                    environment_variables = {
                        'key' : ''
                        }, 
                    context_sample = py_logto.models.context_sample.contextSample(), 
                    token_sample = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_1_token_sample._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_1_tokenSample(
                        jti = '', 
                        aud = null, 
                        scope = '', 
                        client_id = '', 
                        kind = '', ), )
            )
        else:
            return ApiConfigsJwtCustomizerGet200ResponseInner(
                key = '',
                value = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_1._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_1(
                    script = '', 
                    environment_variables = {
                        'key' : ''
                        }, 
                    context_sample = py_logto.models.context_sample.contextSample(), 
                    token_sample = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_1_token_sample._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_1_tokenSample(
                        jti = '', 
                        aud = null, 
                        scope = '', 
                        client_id = '', 
                        kind = '', ), ),
        )
        """

    def testApiConfigsJwtCustomizerGet200ResponseInner(self):
        """Test ApiConfigsJwtCustomizerGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()