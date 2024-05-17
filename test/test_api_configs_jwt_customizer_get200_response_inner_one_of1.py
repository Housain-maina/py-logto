# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_jwt_customizer_get200_response_inner_one_of1 import ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1

class TestApiConfigsJwtCustomizerGet200ResponseInnerOneOf1(unittest.TestCase):
    """ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1:
        """Test ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1`
        """
        model = ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1()
        if include_optional:
            return ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1(
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
            return ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1(
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

    def testApiConfigsJwtCustomizerGet200ResponseInnerOneOf1(self):
        """Test ApiConfigsJwtCustomizerGet200ResponseInnerOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
