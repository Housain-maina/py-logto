# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of1_token_sample import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample

class TestApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample(unittest.TestCase):
    """ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample:
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample`
        """
        model = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample()
        if include_optional:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample(
                jti = '',
                aud = None,
                scope = '',
                client_id = '',
                kind = ''
            )
        else:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample(
        )
        """

    def testApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample(self):
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
