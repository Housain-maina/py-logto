# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from py_logto.models.list_connectors200_response_inner_form_items_inner_one_of import ListConnectors200ResponseInnerFormItemsInnerOneOf
from py_logto.models.list_connectors200_response_inner_form_items_inner_one_of1 import ListConnectors200ResponseInnerFormItemsInnerOneOf1
from py_logto.models.list_connectors200_response_inner_form_items_inner_one_of2 import ListConnectors200ResponseInnerFormItemsInnerOneOf2
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

LISTCONNECTORS200RESPONSEINNERFORMITEMSINNER_ONE_OF_SCHEMAS = ["ListConnectors200ResponseInnerFormItemsInnerOneOf", "ListConnectors200ResponseInnerFormItemsInnerOneOf1", "ListConnectors200ResponseInnerFormItemsInnerOneOf2"]

class ListConnectors200ResponseInnerFormItemsInner(BaseModel):
    """
    ListConnectors200ResponseInnerFormItemsInner
    """
    # data type: ListConnectors200ResponseInnerFormItemsInnerOneOf
    oneof_schema_1_validator: Optional[ListConnectors200ResponseInnerFormItemsInnerOneOf] = None
    # data type: ListConnectors200ResponseInnerFormItemsInnerOneOf1
    oneof_schema_2_validator: Optional[ListConnectors200ResponseInnerFormItemsInnerOneOf1] = None
    # data type: ListConnectors200ResponseInnerFormItemsInnerOneOf2
    oneof_schema_3_validator: Optional[ListConnectors200ResponseInnerFormItemsInnerOneOf2] = None
    actual_instance: Optional[Union[ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2]] = None
    one_of_schemas: Set[str] = { "ListConnectors200ResponseInnerFormItemsInnerOneOf", "ListConnectors200ResponseInnerFormItemsInnerOneOf1", "ListConnectors200ResponseInnerFormItemsInnerOneOf2" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ListConnectors200ResponseInnerFormItemsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: ListConnectors200ResponseInnerFormItemsInnerOneOf
        if not isinstance(v, ListConnectors200ResponseInnerFormItemsInnerOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListConnectors200ResponseInnerFormItemsInnerOneOf`")
        else:
            match += 1
        # validate data type: ListConnectors200ResponseInnerFormItemsInnerOneOf1
        if not isinstance(v, ListConnectors200ResponseInnerFormItemsInnerOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListConnectors200ResponseInnerFormItemsInnerOneOf1`")
        else:
            match += 1
        # validate data type: ListConnectors200ResponseInnerFormItemsInnerOneOf2
        if not isinstance(v, ListConnectors200ResponseInnerFormItemsInnerOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListConnectors200ResponseInnerFormItemsInnerOneOf2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ListConnectors200ResponseInnerFormItemsInner with oneOf schemas: ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ListConnectors200ResponseInnerFormItemsInner with oneOf schemas: ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ListConnectors200ResponseInnerFormItemsInnerOneOf
        try:
            instance.actual_instance = ListConnectors200ResponseInnerFormItemsInnerOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListConnectors200ResponseInnerFormItemsInnerOneOf1
        try:
            instance.actual_instance = ListConnectors200ResponseInnerFormItemsInnerOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListConnectors200ResponseInnerFormItemsInnerOneOf2
        try:
            instance.actual_instance = ListConnectors200ResponseInnerFormItemsInnerOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListConnectors200ResponseInnerFormItemsInner with oneOf schemas: ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListConnectors200ResponseInnerFormItemsInner with oneOf schemas: ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ListConnectors200ResponseInnerFormItemsInnerOneOf, ListConnectors200ResponseInnerFormItemsInnerOneOf1, ListConnectors200ResponseInnerFormItemsInnerOneOf2]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


