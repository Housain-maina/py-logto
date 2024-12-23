# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from py_logto.models.list_applications200_response_inner_protected_app_metadata_custom_domains_inner import ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner
from py_logto.models.list_applications200_response_inner_protected_app_metadata_page_rules_inner import ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner
from typing import Optional, Set
from typing_extensions import Self

class ListApplications200ResponseInnerProtectedAppMetadata(BaseModel):
    """
    ListApplications200ResponseInnerProtectedAppMetadata
    """ # noqa: E501
    host: StrictStr
    origin: StrictStr
    session_duration: Union[StrictFloat, StrictInt] = Field(alias="sessionDuration")
    page_rules: List[ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner] = Field(alias="pageRules")
    custom_domains: Optional[List[ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner]] = Field(default=None, alias="customDomains")
    __properties: ClassVar[List[str]] = ["host", "origin", "sessionDuration", "pageRules", "customDomains"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListApplications200ResponseInnerProtectedAppMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in page_rules (list)
        _items = []
        if self.page_rules:
            for _item_page_rules in self.page_rules:
                if _item_page_rules:
                    _items.append(_item_page_rules.to_dict())
            _dict['pageRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_domains (list)
        _items = []
        if self.custom_domains:
            for _item_custom_domains in self.custom_domains:
                if _item_custom_domains:
                    _items.append(_item_custom_domains.to_dict())
            _dict['customDomains'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListApplications200ResponseInnerProtectedAppMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "origin": obj.get("origin"),
            "sessionDuration": obj.get("sessionDuration"),
            "pageRules": [ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner.from_dict(_item) for _item in obj["pageRules"]] if obj.get("pageRules") is not None else None,
            "customDomains": [ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.from_dict(_item) for _item in obj["customDomains"]] if obj.get("customDomains") is not None else None
        })
        return _obj


