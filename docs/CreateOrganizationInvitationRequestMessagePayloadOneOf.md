# CreateOrganizationInvitationRequestMessagePayloadOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_organization_invitation_request_message_payload_one_of import CreateOrganizationInvitationRequestMessagePayloadOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationInvitationRequestMessagePayloadOneOf from a JSON string
create_organization_invitation_request_message_payload_one_of_instance = CreateOrganizationInvitationRequestMessagePayloadOneOf.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationInvitationRequestMessagePayloadOneOf.to_json())

# convert the object into a dict
create_organization_invitation_request_message_payload_one_of_dict = create_organization_invitation_request_message_payload_one_of_instance.to_dict()
# create an instance of CreateOrganizationInvitationRequestMessagePayloadOneOf from a dict
create_organization_invitation_request_message_payload_one_of_from_dict = CreateOrganizationInvitationRequestMessagePayloadOneOf.from_dict(create_organization_invitation_request_message_payload_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


