<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Defender Set Indicator

## Function - Defender Set Indicator

### API Name
`defender_set_indicator`

### Output Name
`None`

### Message Destination
`fn_microsoft_defender`

### Pre-Processing Script
```python
inputs.defender_indicator_type = artifact.type
inputs.defender_indicator_value = artifact.value
inputs.defender_description = rule.properties.indicator_description
inputs.defender_expiration_time = rule.properties.indicator_expiration
inputs.defender_title = rule.properties.indicator_title
inputs.defender_severity = str(rule.properties.indicator_severity)
inputs.defender_indicator_action = str(rule.properties.indicator_action)
```

### Post-Processing Script
```python
import java.util.Date as Date

msg = u"Defender Action {}.\nAction: {}\nArtifact: {}\nTitle: {}\nComment: {}\nSeverity: {}\nExpiration: {}"\
   .format("successful" if results.success else "unsuccessful",
           str(rule.properties.indicator_action),
           artifact.value,
           rule.properties.indicator_title,
           rule.properties.indicator_description,
           str(rule.properties.indicator_severity),
           rule.properties.indicator_expiration)
           
if not results.success:
    msg = u"{}\nReason: {}".format(msg, results.reason)

incident.addNote(msg)

if results.success:
    row = incident.addRow("defender_indicators")
    row['report_date'] = Date().getTime()
    row['ind_id'] = results.content['id']
    row['ind_value'] = results.content['indicatorValue']
    row['ind_type'] = results.content['indicatorType']
    row['ind_title'] = results.content['title']
    row['ind_description'] = results.content['description']
    row['ind_action'] = results.content['action']
    row['ind_severity'] = results.content['severity']
    row['ind_created_by'] = results.content['createdByDisplayName']
    row['ind_creation_date'] = results.content['creationTimeDateTimeUtc_ts']
    row['ind_expiration_date'] = results.content['expirationTime_ts']
    row['status'] = 'Active'

```

---
