# CreateVerificationBySocial201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_record_id** | **str** | The ID of the verification record. | 
**authorization_uri** | **str** | The authorization URI to navigate to for authentication and authorization in the connected social identity provider. | 
**expires_at** | **str** | The expiration date and time of the verification record. | 

## Example

```python
from py_logto.models.create_verification_by_social201_response import CreateVerificationBySocial201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationBySocial201Response from a JSON string
create_verification_by_social201_response_instance = CreateVerificationBySocial201Response.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationBySocial201Response.to_json())

# convert the object into a dict
create_verification_by_social201_response_dict = create_verification_by_social201_response_instance.to_dict()
# create an instance of CreateVerificationBySocial201Response from a dict
create_verification_by_social201_response_from_dict = CreateVerificationBySocial201Response.from_dict(create_verification_by_social201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


