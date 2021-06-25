<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# ZIA: URL Lookup

## Function - ZIA: URL Lookup

### API Name
`funct_zia_url_lookup`

### Output Name
`None`

### Message Destination
`zia`

### Pre-Processing Script
```python
inputs.zia_urls = artifact.value
```

### Post-Processing Script
```python
##  ZIA - wf_zia_url_lookup post processing script ##

#  Globals
FN_NAME = "funct_zia_url_lookup"
WF_NAME = "Example: ZIA: URL Lookup"
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]

# Processing
def main():
    note_text = u''
    urls = INPUTS.get("zia_urls")
    if CONTENT:
        note_text = u"ZIA Integration: Workflow <b>{0}</b>: There were <b>{1}</b> Results (s) returned for " \
                        u"URL <b>{2}</b> SOAR function <b>{3}</b>.".format(WF_NAME, len(CONTENT), urls, FN_NAME)
        note_text += u"<br><b>{}</b>".format(CONTENT)

    else:
        note_text += u"ZIA Integration: Workflow <b>{0}</b>: There were <b>no</b> results returned " \
                     u"for SOAR function <b>{1}</b>."\
            .format(WF_NAME, FN_NAME)

    incident.addNote(helper.createRichText(note_text))

main()


```

---
