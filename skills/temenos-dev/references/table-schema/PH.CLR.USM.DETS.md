# PH.CLR.USM.DETS — Table Schema

> Source: `INSERTS/I_F.PH.CLR.USM.DETS` in `PH_LocalClearingGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PHCUD.BIC` | `PhClrUsmDets_Bic` | TField |  | Conditional Field � One of the BIC/Bank Code/Institution Id should be present. Holds the BIC of the respective bank to determine the status |
| 2 | `PHCUD.BankCode` | `PhClrUsmDets_Bankcode` | TField |  |  |
| 3 | `PHCUD.InstitutionID` | `PhClrUsmDets_Institutionid` | TField |  |  |
| 4 | `PHCUD.BankStatus` | `PhClrUsmDets_Bankstatus` | TField |  |  |
| 5 | `PHCUD.EffectiveDate` | `PhClrUsmDets_Effectivedate` | TField |  |  |
| 6 | `PHCUD.MessageContent` | `PhClrUsmDets_Messagecontent` | TField |  | To store the USM received message content |
| 7 | `PHCUD.RESERVED.10` | `PhClrUsmDets_Reserved10` |  |  |  |
| 8 | `PHCUD.RESERVED.9` | `PhClrUsmDets_Reserved9` |  |  |  |
| 9 | `PHCUD.RESERVED.8` | `PhClrUsmDets_Reserved8` | TField |  | Reserverd field for future use. Not Applicable. |
| 10 | `PHCUD.RESERVED.7` | `PhClrUsmDets_Reserved7` | TField |  | Reserverd field for future use. Not Applicable. |
| 11 | `PHCUD.RESERVED.6` | `PhClrUsmDets_Reserved6` | TField |  | Reserverd field for future use. Not Applicable. |
| 12 | `PHCUD.RESERVED.5` | `PhClrUsmDets_Reserved5` | TField |  | Reserverd field for future use. Not Applicable. |
| 13 | `PHCUD.RESERVED.4` | `PhClrUsmDets_Reserved4` | TField |  | Reserverd field for future use. Not Applicable. |
| 14 | `PHCUD.RESERVED.3` | `PhClrUsmDets_Reserved3` | TField |  | Reserverd field for future use. Not Applicable. |
| 15 | `PHCUD.RESERVED.2` | `PhClrUsmDets_Reserved2` | TField |  | Reserverd field for future use. Not Applicable. |
| 16 | `PHCUD.RESERVED.1` | `PhClrUsmDets_Reserved1` | TField |  | Reserverd field for future use. Not Applicable. |
| 17 | `PHCUD.OVERRIDE` | `PhClrUsmDets_Override` |  |  |  |
| 18 | `PHCUD.RECORD.STATUS` | `PhClrUsmDets_RecordStatus` | String |  |  |
| 19 | `PHCUD.CURR.NO` | `PhClrUsmDets_CurrNo` | String |  |  |
| 20 | `PHCUD.INPUTTER` | `PhClrUsmDets_Inputter` |  |  |  |
| 21 | `PHCUD.DATE.TIME` | `PhClrUsmDets_DateTime` |  |  |  |
| 22 | `PHCUD.AUTHORISER` | `PhClrUsmDets_Authoriser` | String |  |  |
| 23 | `PHCUD.CO.CODE` | `PhClrUsmDets_CoCode` | String |  |  |
| 24 | `PHCUD.DEPT.CODE` | `PhClrUsmDets_DeptCode` | String |  |  |
| 25 | `PHCUD.AUDITOR.CODE` | `PhClrUsmDets_AuditorCode` | String |  |  |
| 26 | `PHCUD.AUDIT.DATE.TIME` | `PhClrUsmDets_AuditDateTime` | String |  |  |
