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
from py_logto.models.get_sign_in_exp200_response_color import GetSignInExp200ResponseColor
from py_logto.models.get_sign_in_exp200_response_custom_ui_assets import GetSignInExp200ResponseCustomUiAssets
from py_logto.models.get_sign_in_exp200_response_language_info import GetSignInExp200ResponseLanguageInfo
from py_logto.models.get_sign_in_exp200_response_mfa import GetSignInExp200ResponseMfa
from py_logto.models.get_sign_in_exp200_response_password_policy import GetSignInExp200ResponsePasswordPolicy
from py_logto.models.get_sign_in_exp200_response_sign_in import GetSignInExp200ResponseSignIn
from py_logto.models.get_sign_in_exp200_response_sign_up import GetSignInExp200ResponseSignUp
from py_logto.models.get_sign_in_exp200_response_social_sign_in import GetSignInExp200ResponseSocialSignIn
from py_logto.models.list_application_organizations200_response_inner_branding import ListApplicationOrganizations200ResponseInnerBranding
from typing import Optional, Set
from typing_extensions import Self

class GetSignInExp200Response(BaseModel):
    """
    GetSignInExp200Response
    """ # noqa: E501
    tenant_id: Annotated[str, Field(strict=True, max_length=21)] = Field(alias="tenantId")
    id: Annotated[str, Field(min_length=1, strict=True, max_length=21)]
    color: GetSignInExp200ResponseColor
    branding: ListApplicationOrganizations200ResponseInnerBranding
    language_info: GetSignInExp200ResponseLanguageInfo = Field(alias="languageInfo")
    terms_of_use_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(alias="termsOfUseUrl")
    privacy_policy_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(alias="privacyPolicyUrl")
    agree_to_terms_policy: StrictStr = Field(alias="agreeToTermsPolicy")
    sign_in: GetSignInExp200ResponseSignIn = Field(alias="signIn")
    sign_up: GetSignInExp200ResponseSignUp = Field(alias="signUp")
    social_sign_in: GetSignInExp200ResponseSocialSignIn = Field(alias="socialSignIn")
    social_sign_in_connector_targets: List[StrictStr] = Field(description="Enabled social sign-in connectors, will displayed on the sign-in page.", alias="socialSignInConnectorTargets")
    sign_in_mode: StrictStr = Field(alias="signInMode")
    custom_css: Optional[StrictStr] = Field(alias="customCss")
    custom_content: Dict[str, StrictStr] = Field(description="Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value.", alias="customContent")
    custom_ui_assets: Optional[GetSignInExp200ResponseCustomUiAssets] = Field(alias="customUiAssets")
    password_policy: GetSignInExp200ResponsePasswordPolicy = Field(alias="passwordPolicy")
    mfa: GetSignInExp200ResponseMfa
    single_sign_on_enabled: StrictBool = Field(alias="singleSignOnEnabled")
    support_email: Optional[StrictStr] = Field(description="The support email address to display on the error pages.", alias="supportEmail")
    support_website_url: Optional[StrictStr] = Field(description="The support website URL to display on the error pages.", alias="supportWebsiteUrl")
    unknown_session_redirect_url: Optional[StrictStr] = Field(description="The fallback URL to redirect users when the sign-in session does not exist or unknown. Client should initiates a new authentication flow after the redirection.", alias="unknownSessionRedirectUrl")
    __properties: ClassVar[List[str]] = ["tenantId", "id", "color", "branding", "languageInfo", "termsOfUseUrl", "privacyPolicyUrl", "agreeToTermsPolicy", "signIn", "signUp", "socialSignIn", "socialSignInConnectorTargets", "signInMode", "customCss", "customContent", "customUiAssets", "passwordPolicy", "mfa", "singleSignOnEnabled", "supportEmail", "supportWebsiteUrl", "unknownSessionRedirectUrl"]

    @field_validator('agree_to_terms_policy')
    def agree_to_terms_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Automatic', 'ManualRegistrationOnly', 'Manual']):
            raise ValueError("must be one of enum values ('Automatic', 'ManualRegistrationOnly', 'Manual')")
        return value

    @field_validator('sign_in_mode')
    def sign_in_mode_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of GetSignInExp200Response from a JSON string"""
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
        # set to None if terms_of_use_url (nullable) is None
        # and model_fields_set contains the field
        if self.terms_of_use_url is None and "terms_of_use_url" in self.model_fields_set:
            _dict['termsOfUseUrl'] = None

        # set to None if privacy_policy_url (nullable) is None
        # and model_fields_set contains the field
        if self.privacy_policy_url is None and "privacy_policy_url" in self.model_fields_set:
            _dict['privacyPolicyUrl'] = None

        # set to None if custom_css (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css is None and "custom_css" in self.model_fields_set:
            _dict['customCss'] = None

        # set to None if custom_ui_assets (nullable) is None
        # and model_fields_set contains the field
        if self.custom_ui_assets is None and "custom_ui_assets" in self.model_fields_set:
            _dict['customUiAssets'] = None

        # set to None if support_email (nullable) is None
        # and model_fields_set contains the field
        if self.support_email is None and "support_email" in self.model_fields_set:
            _dict['supportEmail'] = None

        # set to None if support_website_url (nullable) is None
        # and model_fields_set contains the field
        if self.support_website_url is None and "support_website_url" in self.model_fields_set:
            _dict['supportWebsiteUrl'] = None

        # set to None if unknown_session_redirect_url (nullable) is None
        # and model_fields_set contains the field
        if self.unknown_session_redirect_url is None and "unknown_session_redirect_url" in self.model_fields_set:
            _dict['unknownSessionRedirectUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSignInExp200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "id": obj.get("id"),
            "color": GetSignInExp200ResponseColor.from_dict(obj["color"]) if obj.get("color") is not None else None,
            "branding": ListApplicationOrganizations200ResponseInnerBranding.from_dict(obj["branding"]) if obj.get("branding") is not None else None,
            "languageInfo": GetSignInExp200ResponseLanguageInfo.from_dict(obj["languageInfo"]) if obj.get("languageInfo") is not None else None,
            "termsOfUseUrl": obj.get("termsOfUseUrl"),
            "privacyPolicyUrl": obj.get("privacyPolicyUrl"),
            "agreeToTermsPolicy": obj.get("agreeToTermsPolicy"),
            "signIn": GetSignInExp200ResponseSignIn.from_dict(obj["signIn"]) if obj.get("signIn") is not None else None,
            "signUp": GetSignInExp200ResponseSignUp.from_dict(obj["signUp"]) if obj.get("signUp") is not None else None,
            "socialSignIn": GetSignInExp200ResponseSocialSignIn.from_dict(obj["socialSignIn"]) if obj.get("socialSignIn") is not None else None,
            "socialSignInConnectorTargets": obj.get("socialSignInConnectorTargets"),
            "signInMode": obj.get("signInMode"),
            "customCss": obj.get("customCss"),
            "customContent": obj.get("customContent"),
            "customUiAssets": GetSignInExp200ResponseCustomUiAssets.from_dict(obj["customUiAssets"]) if obj.get("customUiAssets") is not None else None,
            "passwordPolicy": GetSignInExp200ResponsePasswordPolicy.from_dict(obj["passwordPolicy"]) if obj.get("passwordPolicy") is not None else None,
            "mfa": GetSignInExp200ResponseMfa.from_dict(obj["mfa"]) if obj.get("mfa") is not None else None,
            "singleSignOnEnabled": obj.get("singleSignOnEnabled"),
            "supportEmail": obj.get("supportEmail"),
            "supportWebsiteUrl": obj.get("supportWebsiteUrl"),
            "unknownSessionRedirectUrl": obj.get("unknownSessionRedirectUrl")
        })
        return _obj


