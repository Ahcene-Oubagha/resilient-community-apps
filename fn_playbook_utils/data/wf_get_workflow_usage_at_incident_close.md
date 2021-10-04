<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# PB: Get workflow/playbook usage at incident close

## Function - PB: Get workflow data

### API Name
`pb_get_workflow_data`

### Output Name
`workflow_data`

### Message Destination
`fn_playbook_utils`

### Pre-Processing Script
```python
inputs.pb_max_incident_id = incident.id
inputs.pb_min_incident_id = incident.id

inputs.pb_min_incident_date = None
inputs.pb_max_incident_date = None
```

### Post-Processing Script
```python
None
```

---

## Function - PB: Get playbook data

### API Name
`pb_get_playbook_data`

### Output Name
`playbook_data`

### Message Destination
`fn_playbook_utils`

### Pre-Processing Script
```python
inputs.pb_max_incident_id = incident.id
inputs.pb_min_incident_id = incident.id

inputs.pb_min_incident_date = None
inputs.pb_max_incident_date = None
```

### Post-Processing Script
```python
None
```

---
