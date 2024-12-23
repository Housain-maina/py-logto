# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_roles200_response_inner import ListRoles200ResponseInner

class TestListRoles200ResponseInner(unittest.TestCase):
    """ListRoles200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListRoles200ResponseInner:
        """Test ListRoles200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListRoles200ResponseInner`
        """
        model = ListRoles200ResponseInner()
        if include_optional:
            return ListRoles200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '0',
                type = 'User',
                is_default = True,
                users_count = 1.337,
                featured_users = [
                    py_logto.models.list_roles_200_response_inner_featured_users_inner.ListRoles_200_response_inner_featuredUsers_inner(
                        id = '0', 
                        avatar = '', 
                        name = '', )
                    ],
                applications_count = 1.337,
                featured_applications = [
                    py_logto.models.list_roles_200_response_inner_featured_applications_inner.ListRoles_200_response_inner_featuredApplications_inner(
                        id = '0', 
                        name = '0', 
                        type = 'Native', )
                    ]
            )
        else:
            return ListRoles200ResponseInner(
                tenant_id = '',
                id = '0',
                name = '0',
                description = '0',
                type = 'User',
                is_default = True,
                users_count = 1.337,
                featured_users = [
                    py_logto.models.list_roles_200_response_inner_featured_users_inner.ListRoles_200_response_inner_featuredUsers_inner(
                        id = '0', 
                        avatar = '', 
                        name = '', )
                    ],
                applications_count = 1.337,
                featured_applications = [
                    py_logto.models.list_roles_200_response_inner_featured_applications_inner.ListRoles_200_response_inner_featuredApplications_inner(
                        id = '0', 
                        name = '0', 
                        type = 'Native', )
                    ],
        )
        """

    def testListRoles200ResponseInner(self):
        """Test ListRoles200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
