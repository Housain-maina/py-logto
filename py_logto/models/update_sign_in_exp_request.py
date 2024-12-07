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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.get_sign_in_exp200_response_custom_ui_assets import GetSignInExp200ResponseCustomUiAssets
from py_logto.models.get_sign_in_exp200_response_mfa import GetSignInExp200ResponseMfa
from py_logto.models.get_sign_in_exp200_response_password_policy import GetSignInExp200ResponsePasswordPolicy
from py_logto.models.get_sign_in_exp200_response_social_sign_in import GetSignInExp200ResponseSocialSignIn
from py_logto.models.list_application_organizations200_response_inner_branding import ListApplicationOrganizations200ResponseInnerBranding
from py_logto.models.update_sign_in_exp_request_color import UpdateSignInExpRequestColor
from py_logto.models.update_sign_in_exp_request_language_info import UpdateSignInExpRequestLanguageInfo
from py_logto.models.update_sign_in_exp_request_sign_in import UpdateSignInExpRequestSignIn
from py_logto.models.update_sign_in_exp_request_sign_up import UpdateSignInExpRequestSignUp
from py_logto.models.update_sign_in_exp_request_support_email import UpdateSignInExpRequestSupportEmail
from py_logto.models.update_sign_in_exp_request_support_website_url import UpdateSignInExpRequestSupportWebsiteUrl
from py_logto.models.update_sign_in_exp_request_terms_of_use_url import UpdateSignInExpRequestTermsOfUseUrl
from py_logto.models.update_sign_in_exp_request_unknown_session_redirect_url import UpdateSignInExpRequestUnknownSessionRedirectUrl
from typing import Optional, Set
from typing_extensions import Self

class UpdateSignInExpRequest(BaseModel):
    """
    UpdateSignInExpRequest
    """ # noqa: E501
    tenant_id: Optional[Annotated[str, Field(strict=True, max_length=21)]] = Field(default=None, alias="tenantId")
    color: Optional[UpdateSignInExpRequestColor] = None
    branding: Optional[ListApplicationOrganizations200ResponseInnerBranding] = None
    language_info: Optional[UpdateSignInExpRequestLanguageInfo] = Field(default=None, alias="languageInfo")
    agree_to_terms_policy: Optional[StrictStr] = Field(default=None, alias="agreeToTermsPolicy")
    sign_in: Optional[UpdateSignInExpRequestSignIn] = Field(default=None, alias="signIn")
    sign_up: Optional[UpdateSignInExpRequestSignUp] = Field(default=None, alias="signUp")
    social_sign_in: Optional[GetSignInExp200ResponseSocialSignIn] = Field(default=None, alias="socialSignIn")
    social_sign_in_connector_targets: Optional[List[StrictStr]] = Field(default=None, description="Specify the social sign-in connectors to display on the sign-in page.", alias="socialSignInConnectorTargets")
    sign_in_mode: Optional[StrictStr] = Field(default=None, alias="signInMode")
    custom_css: Optional[StrictStr] = Field(default=None, alias="customCss")
    custom_content: Optional[Dict[str, StrictStr]] = Field(default=None, description="Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value.", alias="customContent")
    custom_ui_assets: Optional[GetSignInExp200ResponseCustomUiAssets] = Field(default=None, alias="customUiAssets")
    password_policy: Optional[GetSignInExp200ResponsePasswordPolicy] = Field(default=None, alias="passwordPolicy")
    mfa: Optional[GetSignInExp200ResponseMfa] = None
    single_sign_on_enabled: Optional[StrictBool] = Field(default=None, alias="singleSignOnEnabled")
    terms_of_use_url: Optional[UpdateSignInExpRequestTermsOfUseUrl] = Field(default=None, alias="termsOfUseUrl")
    privacy_policy_url: Optional[UpdateSignInExpRequestTermsOfUseUrl] = Field(default=None, alias="privacyPolicyUrl")
    support_email: Optional[UpdateSignInExpRequestSupportEmail] = Field(default=None, alias="supportEmail")
    support_website_url: Optional[UpdateSignInExpRequestSupportWebsiteUrl] = Field(default=None, alias="supportWebsiteUrl")
    unknown_session_redirect_url: Optional[UpdateSignInExpRequestUnknownSessionRedirectUrl] = Field(default=None, alias="unknownSessionRedirectUrl")
    __properties: ClassVar[List[str]] = ["tenantId", "color", "branding", "languageInfo", "agreeToTermsPolicy", "signIn", "signUp", "socialSignIn", "socialSignInConnectorTargets", "signInMode", "customCss", "customContent", "customUiAssets", "passwordPolicy", "mfa", "singleSignOnEnabled", "termsOfUseUrl", "privacyPolicyUrl", "supportEmail", "supportWebsiteUrl", "unknownSessionRedirectUrl"]

    @field_validator('agree_to_terms_policy')
    def agree_to_terms_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Automatic', 'ManualRegistrationOnly', 'Manual']):
            raise ValueError("must be one of enum values ('Automatic', 'ManualRegistrationOnly', 'Manual')")
        return value

    @field_validator('sign_in_mode')
    def sign_in_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SignIn', 'Register', 'SignInAndRegister']):
            raise ValueError("must be one of enum values ('SignIn', 'Register', 'SignInAndRegister')")
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
        """Create an instance of UpdateSignInExpRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of language_info
        if self.language_info:
            _dict['languageInfo'] = self.language_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sign_in
        if self.sign_in:
            _dict['signIn'] = self.sign_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sign_up
        if self.sign_up:
            _dict['signUp'] = self.sign_up.to_dict()
        # override the default output from pydantic by calling `to_dict()` of social_sign_in
        if self.social_sign_in:
            _dict['socialSignIn'] = self.social_sign_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_ui_assets
        if self.custom_ui_assets:
            _dict['customUiAssets'] = self.custom_ui_assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_policy
        if self.password_policy:
            _dict['passwordPolicy'] = self.password_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mfa
        if self.mfa:
            _dict['mfa'] = self.mfa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terms_of_use_url
        if self.terms_of_use_url:
            _dict['termsOfUseUrl'] = self.terms_of_use_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of privacy_policy_url
        if self.privacy_policy_url:
            _dict['privacyPolicyUrl'] = self.privacy_policy_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support_email
        if self.support_email:
            _dict['supportEmail'] = self.support_email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support_website_url
        if self.support_website_url:
            _dict['supportWebsiteUrl'] = self.support_website_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unknown_session_redirect_url
        if self.unknown_session_redirect_url:
            _dict['unknownSessionRedirectUrl'] = self.unknown_session_redirect_url.to_dict()
        # set to None if custom_css (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css is None and "custom_css" in self.model_fields_set:
            _dict['customCss'] = None

        # set to None if custom_ui_assets (nullable) is None
        # and model_fields_set contains the field
        if self.custom_ui_assets is None and "custom_ui_assets" in self.model_fields_set:
            _dict['customUiAssets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateSignInExpRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "color": UpdateSignInExpRequestColor.from_dict(obj["color"]) if obj.get("color") is not None else None,
            "branding": ListApplicationOrganizations200ResponseInnerBranding.from_dict(obj["branding"]) if obj.get("branding") is not None else None,
            "languageInfo": UpdateSignInExpRequestLanguageInfo.from_dict(obj["languageInfo"]) if obj.get("languageInfo") is not None else None,
            "agreeToTermsPolicy": obj.get("agreeToTermsPolicy"),
            "signIn": UpdateSignInExpRequestSignIn.from_dict(obj["signIn"]) if obj.get("signIn") is not None else None,
            "signUp": UpdateSignInExpRequestSignUp.from_dict(obj["signUp"]) if obj.get("signUp") is not None else None,
            "socialSignIn": GetSignInExp200ResponseSocialSignIn.from_dict(obj["socialSignIn"]) if obj.get("socialSignIn") is not None else None,
            "socialSignInConnectorTargets": obj.get("socialSignInConnectorTargets"),
            "signInMode": obj.get("signInMode"),
            "customCss": obj.get("customCss"),
            "customContent": obj.get("customContent"),
            "customUiAssets": GetSignInExp200ResponseCustomUiAssets.from_dict(obj["customUiAssets"]) if obj.get("customUiAssets") is not None else None,
            "passwordPolicy": GetSignInExp200ResponsePasswordPolicy.from_dict(obj["passwordPolicy"]) if obj.get("passwordPolicy") is not None else None,
            "mfa": GetSignInExp200ResponseMfa.from_dict(obj["mfa"]) if obj.get("mfa") is not None else None,
            "singleSignOnEnabled": obj.get("singleSignOnEnabled"),
            "termsOfUseUrl": UpdateSignInExpRequestTermsOfUseUrl.from_dict(obj["termsOfUseUrl"]) if obj.get("termsOfUseUrl") is not None else None,
            "privacyPolicyUrl": UpdateSignInExpRequestTermsOfUseUrl.from_dict(obj["privacyPolicyUrl"]) if obj.get("privacyPolicyUrl") is not None else None,
            "supportEmail": UpdateSignInExpRequestSupportEmail.from_dict(obj["supportEmail"]) if obj.get("supportEmail") is not None else None,
            "supportWebsiteUrl": UpdateSignInExpRequestSupportWebsiteUrl.from_dict(obj["supportWebsiteUrl"]) if obj.get("supportWebsiteUrl") is not None else None,
            "unknownSessionRedirectUrl": UpdateSignInExpRequestUnknownSessionRedirectUrl.from_dict(obj["unknownSessionRedirectUrl"]) if obj.get("unknownSessionRedirectUrl") is not None else None
        })
        return _obj


