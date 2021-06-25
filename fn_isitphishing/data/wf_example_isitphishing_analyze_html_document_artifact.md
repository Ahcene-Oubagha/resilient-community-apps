<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: IsItPhishing Analyze HTML Document: Artifact

## Function - IsItPhishing HTML document

### API Name
`isitphishing_html_document`

### Output Name
`None`

### Message Destination
`fn_isitphishing`

### Pre-Processing Script
```python
# Required inputs are: incident id and artifact id.
inputs.incident_id = incident.id
inputs.artifact_id = artifact.id
```

### Post-Processing Script
```python
# Plaintext 
content = u"IsItPhishing analysis of artifact document {0} : {1}".format(results["inputs"]["filename"],results['content']['result'])

# Create a note
note = helper.createPlainText(content)

# Add note to the incident
incident.addNote(note)
```

---
