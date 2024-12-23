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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.get_application_sign_in_experience200_response_color import GetApplicationSignInExperience200ResponseColor
from py_logto.models.list_application_organizations200_response_inner_branding import ListApplicationOrganizations200ResponseInnerBranding
from typing import Optional, Set
from typing_extensions import Self

class GetApplicationSignInExperience200Response(BaseModel):
    """
    GetApplicationSignInExperience200Response
    """ # noqa: E501
    tenant_id: Annotated[str, Field(strict=True, max_length=21)] = Field(alias="tenantId")
    application_id: Annotated[str, Field(min_length=1, strict=True, max_length=21)] = Field(alias="applicationId")
    color: GetApplicationSignInExperience200ResponseColor
    branding: ListApplicationOrganizations200ResponseInnerBranding
    terms_of_use_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(alias="termsOfUseUrl")
    privacy_policy_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(alias="privacyPolicyUrl")
    display_name: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(alias="displayName")
    __properties: ClassVar[List[str]] = ["tenantId", "applicationId", "color", "branding", "termsOfUseUrl", "privacyPolicyUrl", "displayName"]

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
        """Create an instance of GetApplicationSignInExperience200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of color
        if self.color:
            _dict['color'] = self.color.to_dict()
        # override the default output from pydantic by calling `to_dict()` of branding
        if self.branding:
            _dict['branding'] = self.branding.to_dict()
        # set to None if terms_of_use_url (nullable) is None
        # and model_fields_set contains the field
        if self.terms_of_use_url is None and "terms_of_use_url" in self.model_fields_set:
            _dict['termsOfUseUrl'] = None

        # set to None if privacy_policy_url (nullable) is None
        # and model_fields_set contains the field
        if self.privacy_policy_url is None and "privacy_policy_url" in self.model_fields_set:
            _dict['privacyPolicyUrl'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetApplicationSignInExperience200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "applicationId": obj.get("applicationId"),
            "color": GetApplicationSignInExperience200ResponseColor.from_dict(obj["color"]) if obj.get("color") is not None else None,
            "branding": ListApplicationOrganizations200ResponseInnerBranding.from_dict(obj["branding"]) if obj.get("branding") is not None else None,
            "termsOfUseUrl": obj.get("termsOfUseUrl"),
            "privacyPolicyUrl": obj.get("privacyPolicyUrl"),
            "displayName": obj.get("displayName")
        })
        return _obj


