# UpdateOtherProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family_name** | **str** | The new family name for the user. | [optional] 
**given_name** | **str** | The new given name for the user. | [optional] 
**middle_name** | **str** | The new middle name for the user. | [optional] 
**nickname** | **str** | The new nickname for the user. | [optional] 
**preferred_username** | **str** | The new preferred username for the user. | [optional] 
**profile** | **str** | The new profile for the user. | [optional] 
**website** | **str** | The new website for the user. | [optional] 
**gender** | **str** | The new gender for the user. | [optional] 
**birthdate** | **str** | The new birthdate for the user. | [optional] 
**zoneinfo** | **str** | The new zoneinfo for the user. | [optional] 
**locale** | **str** | The new locale for the user. | [optional] 
**address** | [**UpdateOtherProfileRequestAddress**](UpdateOtherProfileRequestAddress.md) |  | [optional] 

## Example

```python
from py_logto.models.update_other_profile_request import UpdateOtherProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOtherProfileRequest from a JSON string
update_other_profile_request_instance = UpdateOtherProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOtherProfileRequest.to_json())

# convert the object into a dict
update_other_profile_request_dict = update_other_profile_request_instance.to_dict()
# create an instance of UpdateOtherProfileRequest from a dict
update_other_profile_request_from_dict = UpdateOtherProfileRequest.from_dict(update_other_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


