# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_connectors_get200_response_inner_form_items_inner import ApiConnectorsGet200ResponseInnerFormItemsInner

class TestApiConnectorsGet200ResponseInnerFormItemsInner(unittest.TestCase):
    """ApiConnectorsGet200ResponseInnerFormItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConnectorsGet200ResponseInnerFormItemsInner:
        """Test ApiConnectorsGet200ResponseInnerFormItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConnectorsGet200ResponseInnerFormItemsInner`
        """
        model = ApiConnectorsGet200ResponseInnerFormItemsInner()
        if include_optional:
            return ApiConnectorsGet200ResponseInnerFormItemsInner(
                type = '',
                select_items = [
                    py_logto.models._api_connectors_get_200_response_inner_form_items_inner_one_of_select_items_inner._api_connectors_get_200_response_inner_formItems_inner_oneOf_selectItems_inner(
                        value = '', 
                        title = '', )
                    ],
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
            return ApiConnectorsGet200ResponseInnerFormItemsInner(
                type = '',
                select_items = [
                    py_logto.models._api_connectors_get_200_response_inner_form_items_inner_one_of_select_items_inner._api_connectors_get_200_response_inner_formItems_inner_oneOf_selectItems_inner(
                        value = '', 
                        title = '', )
                    ],
                key = '',
                label = '',
        )
        """

    def testApiConnectorsGet200ResponseInnerFormItemsInner(self):
        """Test ApiConnectorsGet200ResponseInnerFormItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()