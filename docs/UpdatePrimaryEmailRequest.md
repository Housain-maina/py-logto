# UpdatePrimaryEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The new email for the user. | 
**new_identifier_verification_record_id** | **str** | The identifier verification record ID for the new email ownership verification. | 

## Example

```python
from py_logto.models.update_primary_email_request import UpdatePrimaryEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePrimaryEmailRequest from a JSON string
update_primary_email_request_instance = UpdatePrimaryEmailRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePrimaryEmailRequest.to_json())

# convert the object into a dict
update_primary_email_request_dict = update_primary_email_request_instance.to_dict()
# create an instance of UpdatePrimaryEmailRequest from a dict
update_primary_email_request_from_dict = UpdatePrimaryEmailRequest.from_dict(update_primary_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


