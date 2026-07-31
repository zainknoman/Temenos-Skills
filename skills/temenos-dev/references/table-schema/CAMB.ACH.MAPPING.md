# CAMB.ACH.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAMB.ACH.MAPPING` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.MAPP.PO.PRODUCT` | `CambAchMapping_PoProduct` |  |  |  |
| 2 | `ACH.MAPP.CR.DR.TXN` | `CambAchMapping_CrDrTxn` |  |  |  |
| 3 | `ACH.MAPP.CPA.TXN.CODE` | `CambAchMapping_CpaTxnCode` |  |  |  |
| 4 | `ACH.MAPP.FT.TXN.TYPE` | `CambAchMapping_FtTxnType` |  |  |  |
| 5 | `ACH.MAPP.ACH.ACCOUNT` | `CambAchMapping_AchAccount` |  |  |  |
| 6 | `ACH.MAPP.ACH.VERSION` | `CambAchMapping_AchVersion` |  |  |  |
| 7 | `ACH.MAPP.SETTLE.VERSION` | `CambAchMapping_SettleVersion` |  |  |  |
| 8 | `ACH.MAPP.NONSETTLE.VERSION` | `CambAchMapping_NonsettleVersion` |  |  |  |
| 9 | `ACH.MAPP.NOMINEE.TXN.TYPE` | `CambAchMapping_NomineeTxnType` | TField |  | Purpose of the field is to define the FTTC used for the nominee demand payments.Valdation: Record from FT.TXN.TYPE.CONDITION application.eg. AC91 |
| 10 | `ACH.MAPP.RESERVED.8` | `CambAchMapping_Reserved8` | TField |  |  |
| 11 | `ACH.MAPP.RESERVED.7` | `CambAchMapping_Reserved7` | TField |  |  |
| 12 | `ACH.MAPP.RESERVED.6` | `CambAchMapping_Reserved6` | TField |  |  |
| 13 | `ACH.MAPP.RESERVED.5` | `CambAchMapping_Reserved5` | TField |  |  |
| 14 | `ACH.MAPP.RESERVED.4` | `CambAchMapping_Reserved4` | TField |  |  |
| 15 | `ACH.MAPP.RESERVED.3` | `CambAchMapping_Reserved3` | TField |  |  |
| 16 | `ACH.MAPP.RESERVED.2` | `CambAchMapping_Reserved2` | TField |  |  |
| 17 | `ACH.MAPP.RESERVED.1` | `CambAchMapping_Reserved1` | TField |  |  |
| 18 | `ACH.MAPP.LOCAL.REF` | `CambAchMapping_LocalRef` |  |  |  |
| 19 | `ACH.MAPP.RECORD.STATUS` | `CambAchMapping_RecordStatus` | String |  |  |
| 20 | `ACH.MAPP.CURR.NO` | `CambAchMapping_CurrNo` | String |  |  |
| 21 | `ACH.MAPP.INPUTTER` | `CambAchMapping_Inputter` |  |  |  |
| 22 | `ACH.MAPP.DATE.TIME` | `CambAchMapping_DateTime` |  |  |  |
| 23 | `ACH.MAPP.AUTHORISER` | `CambAchMapping_Authoriser` | String |  |  |
| 24 | `ACH.MAPP.CO.CODE` | `CambAchMapping_CoCode` | String |  |  |
| 25 | `ACH.MAPP.DEPT.CODE` | `CambAchMapping_DeptCode` | String |  |  |
| 26 | `ACH.MAPP.AUDITOR.CODE` | `CambAchMapping_AuditorCode` | String |  |  |
| 27 | `ACH.MAPP.AUDIT.DATE.TIME` | `CambAchMapping_AuditDateTime` | String |  |  |
