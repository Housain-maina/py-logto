# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_connectors200_response_inner_form_items_inner_one_of import ListConnectors200ResponseInnerFormItemsInnerOneOf

class TestListConnectors200ResponseInnerFormItemsInnerOneOf(unittest.TestCase):
    """ListConnectors200ResponseInnerFormItemsInnerOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConnectors200ResponseInnerFormItemsInnerOneOf:
        """Test ListConnectors200ResponseInnerFormItemsInnerOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConnectors200ResponseInnerFormItemsInnerOneOf`
        """
        model = ListConnectors200ResponseInnerFormItemsInnerOneOf()
        if include_optional:
            return ListConnectors200ResponseInnerFormItemsInnerOneOf(
                type = '',
                select_items = [
                    py_logto.models.list_connectors_200_response_inner_form_items_inner_one_of_select_items_inner.ListConnectors_200_response_inner_formItems_inner_oneOf_selectItems_inner(
                        value = '', 
                        title = '', )
                    ],
                key = '',
                label = '',
                placeholder = '',
                required = True,
                default_value = {},
                show_conditions = [
                    py_logto.models.list_connectors_200_response_inner_form_items_inner_one_of_show_conditions_inner.ListConnectors_200_response_inner_formItems_inner_oneOf_showConditions_inner(
                        target_key = '', 
                        expect_value = {}, )
                    ],
                description = '',
                tooltip = '',
                is_confidential = True
            )
        else:
            return ListConnectors200ResponseInnerFormItemsInnerOneOf(
                type = '',
                select_items = [
                    py_logto.models.list_connectors_200_response_inner_form_items_inner_one_of_select_items_inner.ListConnectors_200_response_inner_formItems_inner_oneOf_selectItems_inner(
                        value = '', 
                        title = '', )
                    ],
                key = '',
                label = '',
        )
        """

    def testListConnectors200ResponseInnerFormItemsInnerOneOf(self):
        """Test ListConnectors200ResponseInnerFormItemsInnerOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
