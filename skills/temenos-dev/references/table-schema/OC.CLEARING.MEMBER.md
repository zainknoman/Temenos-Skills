# OC.CLEARING.MEMBER — Table Schema

> Source: `INSERTS/I_F.OC.CLEARING.MEMBER` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.CLEAR.MEM.INTERFACE` | `OcClearingMember_Interface` | TField | No | This field explains the means of interface between T24 bank and its Clearing Member. Reserved for future use. Validation Rules: Optional field. Valid Values are Auto and Manual. |
| 2 | `OC.CLEAR.MEM.FILE.TRANSFER.MTH` | `OcClearingMember_FileTransferMth` | TField | No | Denotes how the trade and position data is exchanged with the clearing member. Reserved for future use. Validation Rules: Optional field. Valid Values are Secure File transfer , MQ , SWIFT file act,other and null . |
| 3 | `OC.CLEAR.MEM.CLEARING.MODEL` | `OcClearingMember_ClearingModel` | TField | Yes | Indicates whether the trade cleared is based on Principal or Agent model. If the Model is Principal, the Counterparty to a cleared trade would be the Clearing Member and if the model is Agent, then the Counterparty would be Central Clearing Party/House. Validation Rules: Mandatory field. Valid values are Principal and Agency. |
| 4 | `OC.CLEAR.MEM.CLEARING.HOUSE` | `OcClearingMember_ClearingHouse` |  |  |  |
| 5 | `OC.CLEAR.MEM.RESERVED10` | `OcClearingMember_Reserved10` | TField |  |  |
| 6 | `OC.CLEAR.MEM.RESERVED9` | `OcClearingMember_Reserved9` | TField |  |  |
| 7 | `OC.CLEAR.MEM.RESERVED8` | `OcClearingMember_Reserved8` | TField |  |  |
| 8 | `OC.CLEAR.MEM.RESERVED7` | `OcClearingMember_Reserved7` | TField |  |  |
| 9 | `OC.CLEAR.MEM.RESERVED6` | `OcClearingMember_Reserved6` | TField |  |  |
| 10 | `OC.CLEAR.MEM.RESERVED5` | `OcClearingMember_Reserved5` | TField |  |  |
| 11 | `OC.CLEAR.MEM.RESERVED4` | `OcClearingMember_Reserved4` | TField |  |  |
| 12 | `OC.CLEAR.MEM.RESERVED3` | `OcClearingMember_Reserved3` | TField |  |  |
| 13 | `OC.CLEAR.MEM.RESERVED2` | `OcClearingMember_Reserved2` | TField |  |  |
| 14 | `OC.CLEAR.MEM.RESERVED1` | `OcClearingMember_Reserved1` | TField |  |  |
| 15 | `OC.CLEAR.MEM.LOCAL.REF` | `OcClearingMember_LocalRef` |  |  |  |
| 16 | `OC.CLEAR.MEM.RECORD.STATUS` | `OcClearingMember_RecordStatus` | String |  |  |
| 17 | `OC.CLEAR.MEM.CURR.NO` | `OcClearingMember_CurrNo` | String |  |  |
| 18 | `OC.CLEAR.MEM.INPUTTER` | `OcClearingMember_Inputter` |  |  |  |
| 19 | `OC.CLEAR.MEM.DATE.TIME` | `OcClearingMember_DateTime` |  |  |  |
| 20 | `OC.CLEAR.MEM.AUTHORISER` | `OcClearingMember_Authoriser` | String |  |  |
| 21 | `OC.CLEAR.MEM.CO.CODE` | `OcClearingMember_CoCode` | String |  |  |
| 22 | `OC.CLEAR.MEM.DEPT.CODE` | `OcClearingMember_DeptCode` | String |  |  |
| 23 | `OC.CLEAR.MEM.AUDITOR.CODE` | `OcClearingMember_AuditorCode` | String |  |  |
| 24 | `OC.CLEAR.MEM.AUDIT.DATE.TIME` | `OcClearingMember_AuditDateTime` | String |  |  |
