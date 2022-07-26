<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: MaaS360 Delete App

## Function - MaaS360 Delete App

### API Name
`maas360_delete_app`

### Output Name
`None`

### Message Destination
`fn_maas360`

### Pre-Processing Script
```python
inputs.maas360_app_type = rule.properties.maas360_rule_app_type if rule.properties.maas360_rule_app_type is not None else inputs.maas360_app_type
inputs.maas360_app_id = artifact.value
```

### Post-Processing Script
```python
# Print empty string instead of None
def string_value(value):
  return value if value is not None else ""
  
def add_results_note(inputs, response_desc):
  noteText = u"""Delete App - {} for input params: 
    - appId: '{}' 
    - appType: '{}'""".format(
      response_desc,
      inputs.get("maas360_app_id"), 
      inputs.get("maas360_app_type").name
      )
  incident.addNote(noteText)
  
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    # Write results to a Note
    inputs = results.get("inputs")
    add_results_note(inputs, content.get("description"))
```

---
