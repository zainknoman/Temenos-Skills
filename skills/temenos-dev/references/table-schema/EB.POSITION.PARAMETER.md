# EB.POSITION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.POSITION.PARAMETER` in `AC_CurrencyPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.POS.DESCRIPTION` | `EbPositionParameter_Description` |  |  |  |
| 2 | `EB.POS.CCYMKT.POSTYPE` | `EbPositionParameter_CcymktPostype` |  |  |  |
| 3 | `EB.POS.AL.CATEG` | `EbPositionParameter_AlCateg` |  |  |  |
| 4 | `EB.POS.ALFWD.CATEG` | `EbPositionParameter_AlfwdCateg` |  |  |  |
| 5 | `EB.POS.FXSP.CATEG` | `EbPositionParameter_FxspCateg` |  |  |  |
| 6 | `EB.POS.FXFWD.CATEG` | `EbPositionParameter_FxfwdCateg` |  |  |  |
| 7 | `EB.POS.IN.CR.TXN.CODE` | `EbPositionParameter_InCrTxnCode` | TField |  | Credit Transaction code to be used on the Position Account STMT.ENTRY. Validation Rules: : A Valid Transaction Code. |
| 8 | `EB.POS.IN.DR.TXN.CODE` | `EbPositionParameter_InDrTxnCode` | TField |  | Debit Transaction code to be used on the Position Account STMT.ENTRY. Validation Rules: : A Valid Transaction Code. |
| 9 | `EB.POS.MAT.CR.TXN.CODE` | `EbPositionParameter_MatCrTxnCode` | TField |  | Credit Transaction code to be used on the Position Account STMT.ENTRY. Validation Rules: : A Valid Transaction Code. |
| 10 | `EB.POS.MAT.DR.TXN.CODE` | `EbPositionParameter_MatDrTxnCode` | TField |  | Debit Transaction code to be used on the Position Account STMT.ENTRY. Validation Rules: : A Valid Transaction Code. |
| 11 | `EB.POS.ENT.TYPE` | `EbPositionParameter_EntType` |  |  |  |
| 12 | `EB.POS.CHANGE.DD` | `EbPositionParameter_ChangeDd` |  |  |  |
| 13 | `EB.POS.DEALER.DESK` | `EbPositionParameter_DealerDesk` |  |  |  |
| 14 | `EB.POS.JOUR.PRINT.EXC.RVN` | `EbPositionParameter_JourPrintExcRvn` | TField |  | Used to exclude spec entries with txn code as RVN. If set to YES, then the RE section will not be printed in the TXN.JOURNAL report. Validation Rules: : Possible values YES_NO and Null |
| 15 | `EB.POS.POS.MVMT.HIST` | `EbPositionParameter_PosMvmtHist` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `EB.POS.RESERVED08` | `EbPositionParameter_Reserved08` | TField |  |  |
| 17 | `EB.POS.RESERVED07` | `EbPositionParameter_Reserved07` | TField |  |  |
| 18 | `EB.POS.RESERVED06` | `EbPositionParameter_Reserved06` | TField |  |  |
| 19 | `EB.POS.RESERVED05` | `EbPositionParameter_Reserved05` | TField |  |  |
| 20 | `EB.POS.RESERVED04` | `EbPositionParameter_Reserved04` | TField |  |  |
| 21 | `EB.POS.RESERVED03` | `EbPositionParameter_Reserved03` | TField |  |  |
| 22 | `EB.POS.LOCAL.REF` | `EbPositionParameter_LocalRef` |  |  |  |
| 23 | `EB.POS.OVERRIDE` | `EbPositionParameter_Override` |  |  |  |
| 24 | `EB.POS.RECORD.STATUS` | `EbPositionParameter_RecordStatus` | String |  |  |
| 25 | `EB.POS.CURR.NO` | `EbPositionParameter_CurrNo` | String |  |  |
| 26 | `EB.POS.INPUTTER` | `EbPositionParameter_Inputter` |  |  |  |
| 27 | `EB.POS.DATE.TIME` | `EbPositionParameter_DateTime` |  |  |  |
| 28 | `EB.POS.AUTHORISER` | `EbPositionParameter_Authoriser` | String |  |  |
| 29 | `EB.POS.CO.CODE` | `EbPositionParameter_CoCode` | String |  |  |
| 30 | `EB.POS.DEPT.CODE` | `EbPositionParameter_DeptCode` | String |  |  |
| 31 | `EB.POS.AUDITOR.CODE` | `EbPositionParameter_AuditorCode` | String |  |  |
| 32 | `EB.POS.AUDIT.DATE.TIME` | `EbPositionParameter_AuditDateTime` | String |  |  |
