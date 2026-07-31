# ST.CUSTOMER.EXIT.STATUS — Table Schema

> Source: `INSERTS/I_F.ST.CUSTOMER.EXIT.STATUS` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CES.DESCRIPTION` | `StCustomerExitStatus_Description` | TField | Yes | This will represent the description of the customer exit status. Validation Rules: This field is mandatory |
| 2 | `ST.CES.CUSTOMER.TYPE` | `StCustomerExitStatus_CustomerType` | TField | Yes | Indicates the customer type for which a specific exit status is available Allowed values are: Prospect and Active Validation Rules: This field is mandatory |
| 3 | `ST.CES.ALLOWED.EXIT.REASON` | `StCustomerExitStatus_AllowedExitReason` |  |  |  |
| 4 | `ST.CES.ALLOW.REMOVE.EXIT.STATUS` | `StCustomerExitStatus_AllowRemoveExitStatus` | TField |  | Specifies if the bank user will be allowed to re-open a professional relationship with the respective prospect or customer by removing its exit status Allowed values are Yes and No |
| 5 | `ST.CES.RESERVED.16` | `StCustomerExitStatus_Reserved16` |  |  |  |
| 6 | `ST.CES.RESERVED.15` | `StCustomerExitStatus_Reserved15` | TField |  |  |
| 7 | `ST.CES.RESERVED.14` | `StCustomerExitStatus_Reserved14` | TField |  |  |
| 8 | `ST.CES.RESERVED.13` | `StCustomerExitStatus_Reserved13` | TField |  |  |
| 9 | `ST.CES.RESERVED.12` | `StCustomerExitStatus_Reserved12` | TField |  |  |
| 10 | `ST.CES.RESERVED.11` | `StCustomerExitStatus_Reserved11` | TField |  |  |
| 11 | `ST.CES.RESERVED.10` | `StCustomerExitStatus_Reserved10` | TField |  |  |
| 12 | `ST.CES.RESERVED.9` | `StCustomerExitStatus_Reserved9` | TField |  |  |
| 13 | `ST.CES.RESERVED.8` | `StCustomerExitStatus_Reserved8` | TField |  |  |
| 14 | `ST.CES.RESERVED.7` | `StCustomerExitStatus_Reserved7` | TField |  |  |
| 15 | `ST.CES.RESERVED.6` | `StCustomerExitStatus_Reserved6` | TField |  |  |
| 16 | `ST.CES.RESERVED.5` | `StCustomerExitStatus_Reserved5` | TField |  |  |
| 17 | `ST.CES.RESERVED.4` | `StCustomerExitStatus_Reserved4` | TField |  |  |
| 18 | `ST.CES.RESERVED.3` | `StCustomerExitStatus_Reserved3` | TField |  |  |
| 19 | `ST.CES.RESERVED.2` | `StCustomerExitStatus_Reserved2` | TField |  |  |
| 20 | `ST.CES.RESERVED.1` | `StCustomerExitStatus_Reserved1` | TField |  |  |
| 21 | `ST.CES.LOCAL.REF` | `StCustomerExitStatus_LocalRef` |  |  |  |
| 22 | `ST.CES.OVERRIDE` | `StCustomerExitStatus_Override` |  |  |  |
| 23 | `ST.CES.RECORD.STATUS` | `StCustomerExitStatus_RecordStatus` | String |  |  |
| 24 | `ST.CES.CURR.NO` | `StCustomerExitStatus_CurrNo` | String |  |  |
| 25 | `ST.CES.INPUTTER` | `StCustomerExitStatus_Inputter` |  |  |  |
| 26 | `ST.CES.DATE.TIME` | `StCustomerExitStatus_DateTime` |  |  |  |
| 27 | `ST.CES.AUTHORISER` | `StCustomerExitStatus_Authoriser` | String |  |  |
| 28 | `ST.CES.CO.CODE` | `StCustomerExitStatus_CoCode` | String |  |  |
| 29 | `ST.CES.DEPT.CODE` | `StCustomerExitStatus_DeptCode` | String |  |  |
| 30 | `ST.CES.AUDITOR.CODE` | `StCustomerExitStatus_AuditorCode` | String |  |  |
| 31 | `ST.CES.AUDIT.DATE.TIME` | `StCustomerExitStatus_AuditDateTime` | String |  |  |
