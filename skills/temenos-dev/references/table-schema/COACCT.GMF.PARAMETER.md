# COACCT.GMF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.COACCT.GMF.PARAMETER` in `COACCT_GmfTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COACCT.GMF.UVT.LIMIT` | `CoacctGmfParameter_UvtLimit` | TField |  | Limit in UVT above which the 4x1000 tax has to be collected. E.g 350 |
| 2 | `COACCT.GMF.TAX.ID.ACCOUNTS` | `CoacctGmfParameter_TaxIdAccounts` | TField |  | Id of the Tax record that is used for account transactions. E.g 6001 |
| 3 | `COACCT.GMF.TAX.ID.DEPOSITS` | `CoacctGmfParameter_TaxIdDeposits` | TField |  | Id of the Tax record that is used for deposits transactions. E.g 6001 |
| 4 | `COACCT.GMF.REFUND.PL.CATEGORY` | `CoacctGmfParameter_RefundPlCategory` | TField |  | Id of PL expense category that is used for the tax refunds of deposit pay-out. E.g 52000 |
| 5 | `COACCT.GMF.REFUND.ENTRY.PARAM` | `CoacctGmfParameter_RefundEntryParam` | TField |  | AC.ENTRY.PARAM record that is used for generating the tax refund accounting entries. E.g GMF.REFUND |
| 6 | `COACCT.GMF.RESERVED.10` | `CoacctGmfParameter_Reserved10` | TField |  |  |
| 7 | `COACCT.GMF.RESERVED.9` | `CoacctGmfParameter_Reserved9` | TField |  |  |
| 8 | `COACCT.GMF.RESERVED.8` | `CoacctGmfParameter_Reserved8` | TField |  |  |
| 9 | `COACCT.GMF.RESERVED.7` | `CoacctGmfParameter_Reserved7` | TField |  |  |
| 10 | `COACCT.GMF.RESERVED.6` | `CoacctGmfParameter_Reserved6` | TField |  |  |
| 11 | `COACCT.GMF.RESERVED.5` | `CoacctGmfParameter_Reserved5` | TField |  |  |
| 12 | `COACCT.GMF.RESERVED.4` | `CoacctGmfParameter_Reserved4` | TField |  |  |
| 13 | `COACCT.GMF.RESERVED.3` | `CoacctGmfParameter_Reserved3` | TField |  |  |
| 14 | `COACCT.GMF.RESERVED.2` | `CoacctGmfParameter_Reserved2` | TField |  |  |
| 15 | `COACCT.GMF.RESERVED.1` | `CoacctGmfParameter_Reserved1` | TField |  |  |
| 16 | `COACCT.GMF.LOCAL.REF` | `CoacctGmfParameter_LocalRef` |  |  |  |
| 17 | `COACCT.GMF.OVERRIDE` | `CoacctGmfParameter_Override` |  |  |  |
| 18 | `COACCT.GMF.RECORD.STATUS` | `CoacctGmfParameter_RecordStatus` | String |  |  |
| 19 | `COACCT.GMF.CURR.NO` | `CoacctGmfParameter_CurrNo` | String |  |  |
| 20 | `COACCT.GMF.INPUTTER` | `CoacctGmfParameter_Inputter` |  |  |  |
| 21 | `COACCT.GMF.DATE.TIME` | `CoacctGmfParameter_DateTime` |  |  |  |
| 22 | `COACCT.GMF.AUTHORISER` | `CoacctGmfParameter_Authoriser` | String |  |  |
| 23 | `COACCT.GMF.CO.CODE` | `CoacctGmfParameter_CoCode` | String |  |  |
| 24 | `COACCT.GMF.DEPT.CODE` | `CoacctGmfParameter_DeptCode` | String |  |  |
| 25 | `COACCT.GMF.AUDITOR.CODE` | `CoacctGmfParameter_AuditorCode` | String |  |  |
| 26 | `COACCT.GMF.AUDIT.DATE.TIME` | `CoacctGmfParameter_AuditDateTime` | String |  |  |
