# EB.DIGITAL.SIGNATURE — Table Schema

> Source: `INSERTS/I_F.EB.DIGITAL.SIGNATURE` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DGL.SGR.TXN.DIGITAL.SIGN.DATE` | `EbDigitalSignature_TxnDigitalSignDate` | TField |  | Field to store the date in which the transaction is digitally signed (i.e record created in this table reference to original transaction record). Validation Rules: System updated date format field. |
| 2 | `DGL.SGR.DIGITAL.SIGNATURE` | `EbDigitalSignature_DigitalSignature` | TField |  | Field used to store the Digital Signature coming via IRIS Validation Rules: Maximum of 80 Alphanumeric characters allowed. |
| 3 | `DGL.SGR.DS.RULE.DATA` | `EbDigitalSignature_DsRuleData` | TField |  | Field used to store the transaction representation used to form digital signature This holds the formatted rule data based on DATA.RULE field defined in EB.DIGITAL.SIGN.PARAM table for an application for which the transaction request is processed. Example: '74504$$100$$18654' This can be used for any future comparison to identify the system (like COB, .VALIDATE etc) updated value of that specific data rule fields. Validation Rules: Maximum of 80 Alphanumeric characters allowed. |
| 4 | `DGL.SGR.TXN.COMPANY` | `EbDigitalSignature_TxnCompany` | TField |  | Field used store the transaction company Validation Rules: Maximum of 11 Alphanumeric characters allowed. |
| 5 | `DGL.SGR.RESERVED.6` | `EbDigitalSignature_Reserved6` | TField |  |  |
| 6 | `DGL.SGR.RESERVED.5` | `EbDigitalSignature_Reserved5` | TField |  |  |
| 7 | `DGL.SGR.RESERVED.4` | `EbDigitalSignature_Reserved4` | TField |  |  |
| 8 | `DGL.SGR.RESERVED.3` | `EbDigitalSignature_Reserved3` | TField |  |  |
| 9 | `DGL.SGR.RESERVED.2` | `EbDigitalSignature_Reserved2` | TField |  |  |
| 10 | `DGL.SGR.RESERVED.1` | `EbDigitalSignature_Reserved1` | TField |  |  |
