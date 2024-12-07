# UpdateOtherProfileRequestAddress

The new address for the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_other_profile_request_address import UpdateOtherProfileRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOtherProfileRequestAddress from a JSON string
update_other_profile_request_address_instance = UpdateOtherProfileRequestAddress.from_json(json)
# print the JSON string representation of the object
print(UpdateOtherProfileRequestAddress.to_json())

# convert the object into a dict
update_other_profile_request_address_dict = update_other_profile_request_address_instance.to_dict()
# create an instance of UpdateOtherProfileRequestAddress from a dict
update_other_profile_request_address_from_dict = UpdateOtherProfileRequestAddress.from_dict(update_other_profile_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


