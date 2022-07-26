<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# SentinelOne: Resolve Threat in SentinelOne

## Function - SentinelOne: Resolve Threat in SentinelOne

### API Name
`sentinelone_resolve_threat_in_sentinelone`

### Output Name
`None`

### Message Destination
`fn_sentinelone`

### Pre-Processing Script
```python
inputs.incident_id = incident.id
```

### Post-Processing Script
```python
content = results.get("content")
success = content.get("success", False)
threat_id = content.get("threat_id", None)
if success:
  noteText = u'<b>SentinelOne: Resolve Threat in SentinelOne</b><br> threatId {0} resolved.'.format(threat_id)
else:
  noteText = u'<b>SentinelOne: Resolve Threat in SentinelOne</b><br> threatId {0}: check analystVerdict and incidentStatus in SentinelOne.'.format(threat_id)

incident.addNote(noteText)
```

---
