# UpdatePrimaryPhoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | The new phone for the user. | 
**new_identifier_verification_record_id** | **str** | The identifier verification record ID for the new phone ownership verification. | 

## Example

```python
from py_logto.models.update_primary_phone_request import UpdatePrimaryPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePrimaryPhoneRequest from a JSON string
update_primary_phone_request_instance = UpdatePrimaryPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePrimaryPhoneRequest.to_json())

# convert the object into a dict
update_primary_phone_request_dict = update_primary_phone_request_instance.to_dict()
# create an instance of UpdatePrimaryPhoneRequest from a dict
update_primary_phone_request_from_dict = UpdatePrimaryPhoneRequest.from_dict(update_primary_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


