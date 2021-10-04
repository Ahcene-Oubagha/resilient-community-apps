<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: Send SMS: Incident

## Function - Utilities: Get Contact Info

### API Name
`utilities_get_contact_info`

### Output Name
`incident_members`

### Message Destination
`fn_utilities`

### Pre-Processing Script
```python
inputs.incident_id = incident.id
```

### Post-Processing Script
```python
None
```

---

## Function - Send SMS using AWS SNS

### API Name
`fn_send_sms_via_sns`

### Output Name
``

### Message Destination
`fn_aws_utilities`

### Pre-Processing Script
```python
numbers = []
if workflow.properties.incident_members is not None:
  owner = workflow.properties.incident_members.owner
  members = workflow.properties.incident_members.members
  
  if owner is not None:
    if owner['phone'] is not None and owner['phone'] != '':
      numbers.append(owner['phone'])
      
  for member in members:
    number = member['phone']
    if number is not None and number != '':
      numbers.append(number)
    
inputs.phone_numbers = ','.join(numbers)
inputs.msg_body = "[Example Workflow, Send SMS: Incident] New incident, " + incident.name + ", which you are a member of, has been created."
```

### Post-Processing Script
```python
None
```

---
