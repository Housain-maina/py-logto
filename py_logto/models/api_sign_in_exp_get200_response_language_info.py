# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class ApiSignInExpGet200ResponseLanguageInfo(BaseModel):
    """
    The language detection policy for the sign-in page.
    """ # noqa: E501
    auto_detect: StrictBool = Field(alias="autoDetect")
    fallback_language: StrictStr = Field(alias="fallbackLanguage")
    __properties: ClassVar[List[str]] = ["autoDetect", "fallbackLanguage"]

    @field_validator('fallback_language')
    def fallback_language_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['af-ZA', 'am-ET', 'ar-AR', 'as-IN', 'az-AZ', 'be-BY', 'bg-BG', 'bn-IN', 'br-FR', 'bs-BA', 'ca-ES', 'cb-IQ', 'co-FR', 'cs-CZ', 'cx-PH', 'cy-GB', 'da-DK', 'de', 'de-DE', 'el-GR', 'en', 'en-GB', 'en-US', 'eo-EO', 'es', 'es-ES', 'es-419', 'et-EE', 'eu-ES', 'fa-IR', 'ff-NG', 'fi-FI', 'fo-FO', 'fr', 'fr-CA', 'fr-FR', 'fy-NL', 'ga-IE', 'gl-ES', 'gn-PY', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'ht-HT', 'hu-HU', 'hy-AM', 'id-ID', 'ik-US', 'is-IS', 'it', 'it-IT', 'iu-CA', 'ja', 'ja-JP', 'ja-KS', 'jv-ID', 'ka-GE', 'kk-KZ', 'km-KH', 'kn-IN', 'ko', 'ko-KR', 'ku-TR', 'ky-KG', 'lo-LA', 'lt-LT', 'lv-LV', 'mg-MG', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'my-MM', 'nb-NO', 'ne-NP', 'nl-BE', 'nl-NL', 'nn-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt', 'pt-BR', 'pt-PT', 'ro-RO', 'ru', 'ru-RU', 'rw-RW', 'sc-IT', 'si-LK', 'sk-SK', 'sl-SI', 'sn-ZW', 'sq-AL', 'sr-RS', 'sv-SE', 'sw-KE', 'sy-SY', 'sz-PL', 'ta-IN', 'te-IN', 'tg-TJ', 'th-TH', 'tl-PH', 'tr', 'tr-TR', 'tt-RU', 'tz-MA', 'uk-UA', 'ur-PK', 'uz-UZ', 'vi-VN', 'zh', 'zh-CN', 'zh-HK', 'zh-MO', 'zh-TW', 'zz-TR']):
            raise ValueError("must be one of enum values ('af-ZA', 'am-ET', 'ar-AR', 'as-IN', 'az-AZ', 'be-BY', 'bg-BG', 'bn-IN', 'br-FR', 'bs-BA', 'ca-ES', 'cb-IQ', 'co-FR', 'cs-CZ', 'cx-PH', 'cy-GB', 'da-DK', 'de', 'de-DE', 'el-GR', 'en', 'en-GB', 'en-US', 'eo-EO', 'es', 'es-ES', 'es-419', 'et-EE', 'eu-ES', 'fa-IR', 'ff-NG', 'fi-FI', 'fo-FO', 'fr', 'fr-CA', 'fr-FR', 'fy-NL', 'ga-IE', 'gl-ES', 'gn-PY', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'ht-HT', 'hu-HU', 'hy-AM', 'id-ID', 'ik-US', 'is-IS', 'it', 'it-IT', 'iu-CA', 'ja', 'ja-JP', 'ja-KS', 'jv-ID', 'ka-GE', 'kk-KZ', 'km-KH', 'kn-IN', 'ko', 'ko-KR', 'ku-TR', 'ky-KG', 'lo-LA', 'lt-LT', 'lv-LV', 'mg-MG', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'my-MM', 'nb-NO', 'ne-NP', 'nl-BE', 'nl-NL', 'nn-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt', 'pt-BR', 'pt-PT', 'ro-RO', 'ru', 'ru-RU', 'rw-RW', 'sc-IT', 'si-LK', 'sk-SK', 'sl-SI', 'sn-ZW', 'sq-AL', 'sr-RS', 'sv-SE', 'sw-KE', 'sy-SY', 'sz-PL', 'ta-IN', 'te-IN', 'tg-TJ', 'th-TH', 'tl-PH', 'tr', 'tr-TR', 'tt-RU', 'tz-MA', 'uk-UA', 'ur-PK', 'uz-UZ', 'vi-VN', 'zh', 'zh-CN', 'zh-HK', 'zh-MO', 'zh-TW', 'zz-TR')")
        return value

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
        """Create an instance of ApiSignInExpGet200ResponseLanguageInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiSignInExpGet200ResponseLanguageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoDetect": obj.get("autoDetect"),
            "fallbackLanguage": obj.get("fallbackLanguage")
        })
        return _obj


