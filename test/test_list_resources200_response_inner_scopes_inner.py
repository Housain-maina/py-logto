# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner

class TestListResources200ResponseInnerScopesInner(unittest.TestCase):
    """ListResources200ResponseInnerScopesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListResources200ResponseInnerScopesInner:
        """Test ListResources200ResponseInnerScopesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListResources200ResponseInnerScopesInner`
        """
        model = ListResources200ResponseInnerScopesInner()
        if include_optional:
            return ListResources200ResponseInnerScopesInner(
                tenant_id = '',
                id = '0',
                resource_id = '0',
                name = '0',
                description = '',
                created_at = 1.337
            )
        else:
            return ListResources200ResponseInnerScopesInner(
                tenant_id = '',
                id = '0',
                resource_id = '0',
                name = '0',
                description = '',
                created_at = 1.337,
        )
        """

    def testListResources200ResponseInnerScopesInner(self):
        """Test ListResources200ResponseInnerScopesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
