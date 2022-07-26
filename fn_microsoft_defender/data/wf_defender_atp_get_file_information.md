<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Defender Get File Information

## Function - Defender Get File Information

### API Name
`defender_get_file_information`

### Output Name
`None`

### Message Destination
`fn_microsoft_defender`

### Pre-Processing Script
```python
inputs.defender_file_hash = artifact.value
```

### Post-Processing Script
```python
if not results.success:
    msg = u"Defender Get File Information failed: {}".format(results.reason)
else:
    info = [u"{}: {}".format(k, v) for k, v in results.content.items()]
    msg = u"Defender Get File Information:\n\n{}".format("\n".join(info))

if artifact.description:
    artifact.description = u"{}\n\n{}".format(artifact.description.content, msg)
else:
    artifact.description = msg
    
    
"""
{
    "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Files/$entity",
    "sha1": "4388963aaa83afe2042a46a3c017ad50bdcdafb3",
    "sha256": "413c58c8267d2c8648d8f6384bacc2ae9c929b2b96578b6860b5087cd1bd6462",
    "globalPrevalence": 180022,
    "globalFirstObserved": "2017-09-19T03:51:27.6785431Z",
    "globalLastObserved": "2020-01-06T03:59:21.3229314Z",
    "size": 22139496,
    "fileType": "APP",
    "isPeFile": true,
    "filePublisher": "CHENGDU YIWO Tech Development Co., Ltd.",
    "fileProductName": "EaseUS MobiSaver for Android",
    "signer": "CHENGDU YIWO Tech Development Co., Ltd.",
    "issuer": "VeriSign Class 3 Code Signing 2010 CA",
    "signerHash": "6c3245d4a9bc0244d99dff27af259cbbae2e2d16",
    "isValidCertificate": false,
    "determinationType": "Pua",
    "determinationValue": "PUA:Win32/FusionCore"
}
"""
```

---
