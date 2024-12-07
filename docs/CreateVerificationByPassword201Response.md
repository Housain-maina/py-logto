# CreateVerificationByPassword201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_record_id** | **str** |  | 
**expires_at** | **str** |  | 

## Example

```python
from py_logto.models.create_verification_by_password201_response import CreateVerificationByPassword201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationByPassword201Response from a JSON string
create_verification_by_password201_response_instance = CreateVerificationByPassword201Response.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationByPassword201Response.to_json())

# convert the object into a dict
create_verification_by_password201_response_dict = create_verification_by_password201_response_instance.to_dict()
# create an instance of CreateVerificationByPassword201Response from a dict
create_verification_by_password201_response_from_dict = CreateVerificationByPassword201Response.from_dict(create_verification_by_password201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


