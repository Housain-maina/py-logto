# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.translation_object import TranslationObject

class TestTranslationObject(unittest.TestCase):
    """TranslationObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranslationObject:
        """Test TranslationObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranslationObject`
        """
        model = TranslationObject()
        if include_optional:
            return TranslationObject(
                translation_key = None
            )
        else:
            return TranslationObject(
        )
        """

    def testTranslationObject(self):
        """Test TranslationObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
