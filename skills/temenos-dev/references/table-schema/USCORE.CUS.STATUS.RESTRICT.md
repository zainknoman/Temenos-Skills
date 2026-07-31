# USCORE.CUS.STATUS.RESTRICT — Table Schema

> Source: `INSERTS/I_F.USCORE.CUS.STATUS.RESTRICT` in `USCORE_CustomerRestriction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CSR.DESCRIPTION` | `UscoreCusStatusRestrict_Description` |  |  |  |
| 2 | `CSR.APPLICATION` | `UscoreCusStatusRestrict_Application` |  |  |  |
| 3 | `CSR.CUSTOMER.FIELD` | `UscoreCusStatusRestrict_CustomerField` |  |  |  |
| 4 | `CSR.RESERVED.30` | `UscoreCusStatusRestrict_Reserved30` |  |  |  |
| 5 | `CSR.RESERVED.29` | `UscoreCusStatusRestrict_Reserved29` |  |  |  |
| 6 | `CSR.RESERVED.28` | `UscoreCusStatusRestrict_Reserved28` |  |  |  |
| 7 | `CSR.RESERVED.27` | `UscoreCusStatusRestrict_Reserved27` |  |  |  |
| 8 | `CSR.RESERVED.26` | `UscoreCusStatusRestrict_Reserved26` |  |  |  |
| 9 | `CSR.CHG.DESC` | `UscoreCusStatusRestrict_ChgDesc` |  |  |  |
| 10 | `CSR.CHG.FLD` | `UscoreCusStatusRestrict_ChgFld` |  |  |  |
| 11 | `CSR.RESERVED.25` | `UscoreCusStatusRestrict_Reserved25` |  |  |  |
| 12 | `CSR.RESERVED.24` | `UscoreCusStatusRestrict_Reserved24` |  |  |  |
| 13 | `CSR.RESERVED.23` | `UscoreCusStatusRestrict_Reserved23` |  |  |  |
| 14 | `CSR.RESERVED.22` | `UscoreCusStatusRestrict_Reserved22` |  |  |  |
| 15 | `CSR.RESERVED.21` | `UscoreCusStatusRestrict_Reserved21` |  |  |  |
| 16 | `CSR.ACT.DESC` | `UscoreCusStatusRestrict_ActDesc` |  |  |  |
| 17 | `CSR.ACTIVITY.CLASS` | `UscoreCusStatusRestrict_ActivityClass` |  |  |  |
| 18 | `CSR.ACTIVITY` | `UscoreCusStatusRestrict_Activity` |  |  |  |
| 19 | `CSR.RESERVED.20` | `UscoreCusStatusRestrict_Reserved20` |  |  |  |
| 20 | `CSR.RESERVED.19` | `UscoreCusStatusRestrict_Reserved19` |  |  |  |
| 21 | `CSR.RESERVED.18` | `UscoreCusStatusRestrict_Reserved18` |  |  |  |
| 22 | `CSR.RESERVED.17` | `UscoreCusStatusRestrict_Reserved17` |  |  |  |
| 23 | `CSR.RESERVED.16` | `UscoreCusStatusRestrict_Reserved16` |  |  |  |
| 24 | `CSR.STATUS` | `UscoreCusStatusRestrict_Status` |  |  |  |
| 25 | `CSR.MOD.DESC` | `UscoreCusStatusRestrict_ModDesc` |  |  |  |
| 26 | `CSR.VALIDATION.TYPE` | `UscoreCusStatusRestrict_ValidationType` |  |  |  |
| 27 | `CSR.MESSAGE.ID` | `UscoreCusStatusRestrict_MessageId` |  |  |  |
| 28 | `CSR.RESERVED.15` | `UscoreCusStatusRestrict_Reserved15` |  |  |  |
| 29 | `CSR.RESERVED.14` | `UscoreCusStatusRestrict_Reserved14` |  |  |  |
| 30 | `CSR.RESERVED.13` | `UscoreCusStatusRestrict_Reserved13` |  |  |  |
| 31 | `CSR.RESERVED.12` | `UscoreCusStatusRestrict_Reserved12` |  |  |  |
| 32 | `CSR.RESERVED.11` | `UscoreCusStatusRestrict_Reserved11` |  |  |  |
| 33 | `CSR.RESERVED.10` | `UscoreCusStatusRestrict_Reserved10` |  |  |  |
| 34 | `CSR.RESERVED.9` | `UscoreCusStatusRestrict_Reserved9` |  |  |  |
| 35 | `CSR.RESERVED.8` | `UscoreCusStatusRestrict_Reserved8` |  |  |  |
| 36 | `CSR.RESERVED.7` | `UscoreCusStatusRestrict_Reserved7` |  |  |  |
| 37 | `CSR.RESERVED.6` | `UscoreCusStatusRestrict_Reserved6` |  |  |  |
| 38 | `CSR.RESERVED.5` | `UscoreCusStatusRestrict_Reserved5` | TField |  |  |
| 39 | `CSR.RESERVED.4` | `UscoreCusStatusRestrict_Reserved4` | TField |  |  |
| 40 | `CSR.RESERVED.3` | `UscoreCusStatusRestrict_Reserved3` | TField |  |  |
| 41 | `CSR.RESERVED.2` | `UscoreCusStatusRestrict_Reserved2` | TField |  |  |
| 42 | `CSR.RESERVED.1` | `UscoreCusStatusRestrict_Reserved1` | TField |  |  |
| 43 | `CSR.LOCAL.REF` | `UscoreCusStatusRestrict_LocalRef` |  |  |  |
| 44 | `CSR.OVERRIDE` | `UscoreCusStatusRestrict_Override` |  |  |  |
| 45 | `CSR.RECORD.STATUS` | `UscoreCusStatusRestrict_RecordStatus` | String |  |  |
| 46 | `CSR.CURR.NO` | `UscoreCusStatusRestrict_CurrNo` | String |  |  |
| 47 | `CSR.INPUTTER` | `UscoreCusStatusRestrict_Inputter` |  |  |  |
| 48 | `CSR.DATE.TIME` | `UscoreCusStatusRestrict_DateTime` |  |  |  |
| 49 | `CSR.AUTHORISER` | `UscoreCusStatusRestrict_Authoriser` | String |  |  |
| 50 | `CSR.CO.CODE` | `UscoreCusStatusRestrict_CoCode` | String |  |  |
| 51 | `CSR.DEPT.CODE` | `UscoreCusStatusRestrict_DeptCode` | String |  |  |
| 52 | `CSR.AUDITOR.CODE` | `UscoreCusStatusRestrict_AuditorCode` | String |  |  |
| 53 | `CSR.AUDIT.DATE.TIME` | `UscoreCusStatusRestrict_AuditDateTime` | String |  |  |
