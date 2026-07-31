# USCORE.DELIVERY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USCORE.DELIVERY.PARAMETER` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.DEL.PAR.DESCRIPTION` | `UscoreDeliveryParameter_Description` | TField |  | This field allow the user to enter description. |
| 2 | `USCORE.DEL.PAR.BANK.ADDRESS` | `UscoreDeliveryParameter_BankAddress` | TField |  | This field is used to define whether pre-printed paper is used or Lead Company or Branch Company address is used to display the bank address in advices/notices sent out from T24. |
| 3 | `USCORE.DEL.PAR.RESERVED.10` | `UscoreDeliveryParameter_Reserved10` | TField |  |  |
| 4 | `USCORE.DEL.PAR.RESERVED.9` | `UscoreDeliveryParameter_Reserved9` | TField |  |  |
| 5 | `USCORE.DEL.PAR.RESERVED.8` | `UscoreDeliveryParameter_Reserved8` | TField |  |  |
| 6 | `USCORE.DEL.PAR.RESERVED.7` | `UscoreDeliveryParameter_Reserved7` | TField |  |  |
| 7 | `USCORE.DEL.PAR.RESERVED.6` | `UscoreDeliveryParameter_Reserved6` | TField |  |  |
| 8 | `USCORE.DEL.PAR.RESERVED.5` | `UscoreDeliveryParameter_Reserved5` | TField |  |  |
| 9 | `USCORE.DEL.PAR.RESERVED.4` | `UscoreDeliveryParameter_Reserved4` | TField |  |  |
| 10 | `USCORE.DEL.PAR.RESERVED.3` | `UscoreDeliveryParameter_Reserved3` | TField |  |  |
| 11 | `USCORE.DEL.PAR.RESERVED.2` | `UscoreDeliveryParameter_Reserved2` | TField |  |  |
| 12 | `USCORE.DEL.PAR.RESERVED.1` | `UscoreDeliveryParameter_Reserved1` | TField |  |  |
| 13 | `USCORE.DEL.PAR.RECORD.STATUS` | `UscoreDeliveryParameter_RecordStatus` | String |  |  |
| 14 | `USCORE.DEL.PAR.CURR.NO` | `UscoreDeliveryParameter_CurrNo` | String |  |  |
| 15 | `USCORE.DEL.PAR.INPUTTER` | `UscoreDeliveryParameter_Inputter` |  |  |  |
| 16 | `USCORE.DEL.PAR.DATE.TIME` | `UscoreDeliveryParameter_DateTime` |  |  |  |
| 17 | `USCORE.DEL.PAR.AUTHORISER` | `UscoreDeliveryParameter_Authoriser` | String |  |  |
| 18 | `USCORE.DEL.PAR.CO.CODE` | `UscoreDeliveryParameter_CoCode` | String |  |  |
| 19 | `USCORE.DEL.PAR.DEPT.CODE` | `UscoreDeliveryParameter_DeptCode` | String |  |  |
| 20 | `USCORE.DEL.PAR.AUDITOR.CODE` | `UscoreDeliveryParameter_AuditorCode` | String |  |  |
| 21 | `USCORE.DEL.PAR.AUDIT.DATE.TIME` | `UscoreDeliveryParameter_AuditDateTime` | String |  |  |
