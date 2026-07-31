# USREGS.FDIC.DEPOSIT.CLASS.CODE — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.DEPOSIT.CLASS.CODE` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.CODE.DESCRIPTION` | `UsregsFdicDepositClassCode_Description` |  |  |  |
| 2 | `FDIC.CODE.DEPOSIT.CLASS.TYPE` | `UsregsFdicDepositClassCode_DepositClassType` | TField |  | The Deposit Class Type (Parent) of the Deposit Class Codes. A Virtual table name FDIC.CLASS.TYPE has been defined in EB.LOOKUP table to define the set of values which required as drop down to this field. |
| 3 | `FDIC.CODE.RESERVED.10` | `UsregsFdicDepositClassCode_Reserved10` | TField |  |  |
| 4 | `FDIC.CODE.RESERVED.9` | `UsregsFdicDepositClassCode_Reserved9` | TField |  |  |
| 5 | `FDIC.CODE.RESERVED.8` | `UsregsFdicDepositClassCode_Reserved8` | TField |  |  |
| 6 | `FDIC.CODE.RESERVED.7` | `UsregsFdicDepositClassCode_Reserved7` | TField |  |  |
| 7 | `FDIC.CODE.RESERVED.6` | `UsregsFdicDepositClassCode_Reserved6` | TField |  |  |
| 8 | `FDIC.CODE.RESERVED.5` | `UsregsFdicDepositClassCode_Reserved5` | TField |  |  |
| 9 | `FDIC.CODE.RESERVED.4` | `UsregsFdicDepositClassCode_Reserved4` | TField |  |  |
| 10 | `FDIC.CODE.RESERVED.3` | `UsregsFdicDepositClassCode_Reserved3` | TField |  |  |
| 11 | `FDIC.CODE.RESERVED.2` | `UsregsFdicDepositClassCode_Reserved2` | TField |  |  |
| 12 | `FDIC.CODE.RESERVED.1` | `UsregsFdicDepositClassCode_Reserved1` | TField |  |  |
| 13 | `FDIC.CODE.LOCAL.REF` | `UsregsFdicDepositClassCode_LocalRef` |  |  |  |
| 14 | `FDIC.CODE.OVERRIDE` | `UsregsFdicDepositClassCode_Override` |  |  |  |
| 15 | `FDIC.CODE.RECORD.STATUS` | `UsregsFdicDepositClassCode_RecordStatus` | String |  |  |
| 16 | `FDIC.CODE.CURR.NO` | `UsregsFdicDepositClassCode_CurrNo` | String |  |  |
| 17 | `FDIC.CODE.INPUTTER` | `UsregsFdicDepositClassCode_Inputter` |  |  |  |
| 18 | `FDIC.CODE.DATE.TIME` | `UsregsFdicDepositClassCode_DateTime` |  |  |  |
| 19 | `FDIC.CODE.AUTHORISER` | `UsregsFdicDepositClassCode_Authoriser` | String |  |  |
| 20 | `FDIC.CODE.CO.CODE` | `UsregsFdicDepositClassCode_CoCode` | String |  |  |
| 21 | `FDIC.CODE.DEPT.CODE` | `UsregsFdicDepositClassCode_DeptCode` | String |  |  |
| 22 | `FDIC.CODE.AUDITOR.CODE` | `UsregsFdicDepositClassCode_AuditorCode` | String |  |  |
| 23 | `FDIC.CODE.AUDIT.DATE.TIME` | `UsregsFdicDepositClassCode_AuditDateTime` | String |  |  |
