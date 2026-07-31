# EFT.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.EFT.SETTLEMENT` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EFT.SETT.PO.PRODUCT` | `EftSettlement_PoProduct` |  |  |  |
| 2 | `EFT.SETT.RESERVED.8` | `EftSettlement_Reserved8` | TField |  |  |
| 3 | `EFT.SETT.RESERVED.9` | `EftSettlement_Reserved9` | TField |  |  |
| 4 | `EFT.SETT.RESERVED.10` | `EftSettlement_Reserved10` | TField |  |  |
| 5 | `EFT.SETT.RESERVED.11` | `EftSettlement_Reserved11` | TField |  |  |
| 6 | `EFT.SETT.RESERVED.12` | `EftSettlement_Reserved12` | TField |  |  |
| 7 | `EFT.SETT.RECORD.STATUS` | `EftSettlement_RecordStatus` | String |  |  |
| 8 | `EFT.SETT.CURR.NO` | `EftSettlement_CurrNo` | String |  |  |
| 9 | `EFT.SETT.INPUTTER` | `EftSettlement_Inputter` |  |  |  |
| 10 | `EFT.SETT.DATE.TIME` | `EftSettlement_DateTime` |  |  |  |
| 11 | `EFT.SETT.AUTHORISER` | `EftSettlement_Authoriser` | String |  |  |
| 12 | `EFT.SETT.CO.CODE` | `EftSettlement_CoCode` | String |  |  |
| 13 | `EFT.SETT.DEPT.CODE` | `EftSettlement_DeptCode` | String |  |  |
| 14 | `EFT.SETT.AUDITOR.CODE` | `EftSettlement_AuditorCode` | String |  |  |
| 15 | `EFT.SETT.AUDIT.DATE.TIME` | `EftSettlement_AuditDateTime` | String |  |  |
