# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_connectors_get200_response_inner_form_items_inner_one_of1 import ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1

class TestApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1(unittest.TestCase):
    """ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1:
        """Test ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1`
        """
        model = ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1()
        if include_optional:
            return ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1(
                type = 'Text',
                key = '',
                label = '',
                placeholder = '',
                required = True,
                default_value = {},
                show_conditions = [
                    py_logto.models._api_connectors_get_200_response_inner_form_items_inner_one_of_show_conditions_inner._api_connectors_get_200_response_inner_formItems_inner_oneOf_showConditions_inner(
                        target_key = '', 
                        expect_value = {}, )
                    ],
                description = '',
                tooltip = '',
                is_confidential = True
            )
        else:
            return ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1(
                type = 'Text',
                key = '',
                label = '',
        )
        """

    def testApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1(self):
        """Test ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()