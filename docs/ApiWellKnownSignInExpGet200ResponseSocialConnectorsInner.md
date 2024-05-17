# ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**target** | **str** |  | 
**name** | **object** | Validator function | 
**description** | **object** | Validator function | 
**logo** | **str** |  | 
**logo_dark** | **str** |  | 
**readme** | **str** |  | 
**config_template** | **str** |  | [optional] 
**form_items** | [**List[ApiConnectorsGet200ResponseInnerFormItemsInner]**](ApiConnectorsGet200ResponseInnerFormItemsInner.md) |  | [optional] 
**platform** | **str** |  | 
**is_standard** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.api_well_known_sign_in_exp_get200_response_social_connectors_inner import ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner from a JSON string
api_well_known_sign_in_exp_get200_response_social_connectors_inner_instance = ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner.from_json(json)
# print the JSON string representation of the object
print(ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner.to_json())

# convert the object into a dict
api_well_known_sign_in_exp_get200_response_social_connectors_inner_dict = api_well_known_sign_in_exp_get200_response_social_connectors_inner_instance.to_dict()
# create an instance of ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner from a dict
api_well_known_sign_in_exp_get200_response_social_connectors_inner_from_dict = ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner.from_dict(api_well_known_sign_in_exp_get200_response_social_connectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


