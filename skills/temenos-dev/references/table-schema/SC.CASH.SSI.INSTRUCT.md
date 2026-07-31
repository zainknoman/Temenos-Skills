# SC.CASH.SSI.INSTRUCT — Table Schema

> Source: `INSERTS/I_F.SC.CASH.SSI.INSTRUCT` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CSI.SSI.ID` | `ScCashSsiInstruct_SsiId` |  |  |  |
| 2 | `SC.CSI.CURRENCY` | `ScCashSsiInstruct_Currency` |  |  |  |
| 3 | `SC.CSI.ASSET.SUB` | `ScCashSsiInstruct_AssetSub` |  |  |  |
| 4 | `SC.CSI.ISSUER` | `ScCashSsiInstruct_Issuer` |  |  |  |
| 5 | `SC.CSI.BR.SETT.ACC` | `ScCashSsiInstruct_BrSettAcc` |  |  |  |
| 6 | `SC.CSI.INT.BANK` | `ScCashSsiInstruct_IntBank` |  |  |  |
| 7 | `SC.CSI.BEN.BANK` | `ScCashSsiInstruct_BenBank` |  |  |  |
| 8 | `SC.CSI.BEN.BANK.ADDR` | `ScCashSsiInstruct_BenBankAddr` |  |  |  |
| 9 | `SC.CSI.BEN.BANK.ACC.NO` | `ScCashSsiInstruct_BenBankAccNo` |  |  |  |
| 10 | `SC.CSI.BEN.BANK.CTRY.CODE` | `ScCashSsiInstruct_BenBankCtryCode` |  |  |  |
| 11 | `SC.CSI.END.BENEFICIARY` | `ScCashSsiInstruct_EndBeneficiary` |  |  |  |
| 12 | `SC.CSI.END.BEN.ACC` | `ScCashSsiInstruct_EndBenAcc` |  |  |  |
| 13 | `SC.CSI.VALID.FROM` | `ScCashSsiInstruct_ValidFrom` |  |  |  |
| 14 | `SC.CSI.VALID.TO` | `ScCashSsiInstruct_ValidTo` |  |  |  |
| 15 | `SC.CSI.LAST.REVIEW.DATE` | `ScCashSsiInstruct_LastReviewDate` |  |  |  |
| 16 | `SC.CSI.STATUS` | `ScCashSsiInstruct_Status` |  |  |  |
| 17 | `SC.CSI.SSI.STP` | `ScCashSsiInstruct_SsiStp` |  |  |  |
| 18 | `SC.CSI.MV.RESERVED01` | `ScCashSsiInstruct_MvReserved01` |  |  |  |
| 19 | `SC.CSI.MV.RESERVED02` | `ScCashSsiInstruct_MvReserved02` |  |  |  |
| 20 | `SC.CSI.MV.RESERVED03` | `ScCashSsiInstruct_MvReserved03` |  |  |  |
| 21 | `SC.CSI.MV.RESERVED04` | `ScCashSsiInstruct_MvReserved04` |  |  |  |
| 22 | `SC.CSI.MV.RESERVED05` | `ScCashSsiInstruct_MvReserved05` |  |  |  |
| 23 | `SC.CSI.ROLE` | `ScCashSsiInstruct_Role` | TField |  | This field will show the role played by the counterparty The Role will be defaulted CUSTOMER.TYPE of CUSTOMER.SECURITY part of SSI.ID Multi-Value set |
| 24 | `SC.CSI.RESERVED01` | `ScCashSsiInstruct_Reserved01` | TField |  |  |
| 25 | `SC.CSI.RESERVED02` | `ScCashSsiInstruct_Reserved02` | TField |  |  |
| 26 | `SC.CSI.RESERVED03` | `ScCashSsiInstruct_Reserved03` | TField |  |  |
| 27 | `SC.CSI.RESERVED04` | `ScCashSsiInstruct_Reserved04` | TField |  |  |
| 28 | `SC.CSI.RESERVED05` | `ScCashSsiInstruct_Reserved05` | TField |  |  |
| 29 | `SC.CSI.LOCAL.REF` | `ScCashSsiInstruct_LocalRef` |  |  |  |
| 30 | `SC.CSI.OVERRIDE` | `ScCashSsiInstruct_Override` |  |  |  |
| 31 | `SC.CSI.RECORD.STATUS` | `ScCashSsiInstruct_RecordStatus` | String |  |  |
| 32 | `SC.CSI.CURR.NO` | `ScCashSsiInstruct_CurrNo` | String |  |  |
| 33 | `SC.CSI.INPUTTER` | `ScCashSsiInstruct_Inputter` |  |  |  |
| 34 | `SC.CSI.DATE.TIME` | `ScCashSsiInstruct_DateTime` |  |  |  |
| 35 | `SC.CSI.AUTHORISER` | `ScCashSsiInstruct_Authoriser` | String |  |  |
| 36 | `SC.CSI.CO.CODE` | `ScCashSsiInstruct_CoCode` | String |  |  |
| 37 | `SC.CSI.DEPT.CODE` | `ScCashSsiInstruct_DeptCode` | String |  |  |
| 38 | `SC.CSI.AUDITOR.CODE` | `ScCashSsiInstruct_AuditorCode` | String |  |  |
| 39 | `SC.CSI.AUDIT.DATE.TIME` | `ScCashSsiInstruct_AuditDateTime` | String |  |  |
