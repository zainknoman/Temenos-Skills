# NACUST.PARAM — Table Schema

> Source: `INSERTS/I_F.NACUST.PARAM` in `NACUST_CustomerMessages.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NACUST.ONLINE.MESSAGE` | `NacustParam_OnlineMessage` |  |  |  |
| 2 | `NACUST.MSG.START.DATE` | `NacustParam_MsgStartDate` |  |  |  |
| 3 | `NACUST.MSG.END.DATE` | `NacustParam_MsgEndDate` |  |  |  |
| 4 | `NACUST.POSTING.RESTRICT` | `NacustParam_PostingRestrict` |  |  |  |
| 5 | `NACUST.PR.START.DATE` | `NacustParam_PrStartDate` |  |  |  |
| 6 | `NACUST.PR.END.DATE` | `NacustParam_PrEndDate` |  |  |  |
| 7 | `NACUST.ACCOUNT.FIELDS` | `NacustParam_AccountFields` |  |  |  |
| 8 | `NACUST.CUSTOMER.FIELDS` | `NacustParam_CustomerFields` |  |  |  |
| 9 | `NACUST.SET.ONLINE.MSG` | `NacustParam_SetOnlineMsg` | TField |  | To specify if the online message check is required or not. Radio button with Yes or No option. Validation Rule: The field is open for input only if the record ID is a valid T24 application. |
| 10 | `NACUST.RELATION.CUSTOMER` | `NacustParam_RelationCustomer` | TField |  | To specify if the relation customer check is required or not. Radio button with Yes or No option. Validation Rule: The field is open for input only if the record ID is given as System |
| 11 | `NACUST.STANDARD.MESSAGE` | `NacustParam_StandardMessage` |  |  |  |
| 12 | `NACUST.STD.MSG.START.DATE` | `NacustParam_StdMsgStartDate` |  |  |  |
| 13 | `NACUST.STD.MSG.END.DATE` | `NacustParam_StdMsgEndDate` |  |  |  |
| 14 | `NACUST.RESERVED.1` | `NacustParam_Reserved1` | TField |  |  |
| 15 | `NACUST.RESERVED.2` | `NacustParam_Reserved2` | TField |  |  |
| 16 | `NACUST.RESERVED.3` | `NacustParam_Reserved3` | TField |  |  |
| 17 | `NACUST.RESERVED.4` | `NacustParam_Reserved4` | TField |  |  |
| 18 | `NACUST.RESERVED.5` | `NacustParam_Reserved5` | TField |  |  |
| 19 | `NACUST.LOCAL.REF` | `NacustParam_LocalRef` |  |  |  |
| 20 | `NACUST.OVERRIDE` | `NacustParam_Override` |  |  |  |
| 21 | `NACUST.RECORD.STATUS` | `NacustParam_RecordStatus` | String |  |  |
| 22 | `NACUST.CURR.NO` | `NacustParam_CurrNo` | String |  |  |
| 23 | `NACUST.INPUTTER` | `NacustParam_Inputter` |  |  |  |
| 24 | `NACUST.DATE.TIME` | `NacustParam_DateTime` |  |  |  |
| 25 | `NACUST.AUTHORISER` | `NacustParam_Authoriser` | String |  |  |
| 26 | `NACUST.CO.CODE` | `NacustParam_CoCode` | String |  |  |
| 27 | `NACUST.DEPT.CODE` | `NacustParam_DeptCode` | String |  |  |
| 28 | `NACUST.AUDITOR.CODE` | `NacustParam_AuditorCode` | String |  |  |
| 29 | `NACUST.AUDIT.DATE.TIME` | `NacustParam_AuditDateTime` | String |  |  |
