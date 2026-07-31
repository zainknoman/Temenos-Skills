# AC.ALLOCATION.RULE — Table Schema

> Source: `INSERTS/I_F.AC.ALLOCATION.RULE` in `AC_SoftAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.AR.DESCRIPTION` | `AcAllocationRule_Description` | TField |  | Used to describe the type of allocation ruleds being set up. |
| 2 | `AC.AR.EVENT.TYPE` | `AcAllocationRule_EventType` |  |  |  |
| 3 | `AC.AR.ENTRY.PRINT.MASK` | `AcAllocationRule_EntryPrintMask` |  |  |  |
| 4 | `AC.AR.RESERVED16` | `AcAllocationRule_Reserved16` |  |  |  |
| 5 | `AC.AR.RESERVED15` | `AcAllocationRule_Reserved15` |  |  |  |
| 6 | `AC.AR.MVMT.TARGET` | `AcAllocationRule_MvmtTarget` |  |  |  |
| 7 | `AC.AR.MVMT.CR.TXN` | `AcAllocationRule_MvmtCrTxn` |  |  |  |
| 8 | `AC.AR.MVMT.DR.TXN` | `AcAllocationRule_MvmtDrTxn` |  |  |  |
| 9 | `AC.AR.MVMT.CR.RE.T` | `AcAllocationRule_MvmtCrReT` |  |  |  |
| 10 | `AC.AR.MVMT.DR.RE.T` | `AcAllocationRule_MvmtDrReT` |  |  |  |
| 11 | `AC.AR.MVMT.STMT` | `AcAllocationRule_MvmtStmt` |  |  |  |
| 12 | `AC.AR.MVMT.CATEG` | `AcAllocationRule_MvmtCateg` |  |  |  |
| 13 | `AC.AR.MVMT.SPEC` | `AcAllocationRule_MvmtSpec` |  |  |  |
| 14 | `AC.AR.RESERVED14` | `AcAllocationRule_Reserved14` |  |  |  |
| 15 | `AC.AR.OPP.TARGET` | `AcAllocationRule_OppTarget` |  |  |  |
| 16 | `AC.AR.OPP.CR.TXN` | `AcAllocationRule_OppCrTxn` |  |  |  |
| 17 | `AC.AR.OPP.DR.TXN` | `AcAllocationRule_OppDrTxn` |  |  |  |
| 18 | `AC.AR.OPP.CR.RE.T` | `AcAllocationRule_OppCrReT` |  |  |  |
| 19 | `AC.AR.OPP.DR.RE.T` | `AcAllocationRule_OppDrReT` |  |  |  |
| 20 | `AC.AR.OPP.STMT` | `AcAllocationRule_OppStmt` |  |  |  |
| 21 | `AC.AR.OPP.CATEG` | `AcAllocationRule_OppCateg` |  |  |  |
| 22 | `AC.AR.OPP.SPEC` | `AcAllocationRule_OppSpec` |  |  |  |
| 23 | `AC.AR.RESERVED13` | `AcAllocationRule_Reserved13` |  |  |  |
| 24 | `AC.AR.RESERVED12` | `AcAllocationRule_Reserved12` |  |  |  |
| 25 | `AC.AR.RESERVED11` | `AcAllocationRule_Reserved11` |  |  |  |
| 26 | `AC.AR.DEF.CR.TXN` | `AcAllocationRule_DefCrTxn` | TField |  | The default TRANSACTION to be used when creating credit STMT.ENTRY or CATEG.ENTRY entries. This will only be used when the MVMT.CR.TXN or OPP.CR.TXN field is left blank. |
| 27 | `AC.AR.DEF.DR.TXN` | `AcAllocationRule_DefDrTxn` | TField |  | The default TRANSACTION to be used when creating debit STMT.ENTRY or CATEG.ENTRY entries. This will only be used when the MVMT.DR.TXN or OPP.DR.TXN field is left blank. |
| 28 | `AC.AR.DEF.CR.RE.T` | `AcAllocationRule_DefCrReT` | TField |  | The default RE.TXN.CODE to be used when creating credit RE.CONSOL.SPEC entries. This will only be used when the MVMT.CR.RE.T or OPP.CR.RE.T field is left blank. |
| 29 | `AC.AR.DEF.DR.RE.T` | `AcAllocationRule_DefDrReT` | TField |  | The default RE.TXN.CODE to be used when creating debit RE.CONSOL.SPEC entries. This will only be used when the MVMT.DR.RE.T or OPP.DR.RE.T field is left blank. |
| 30 | `AC.AR.RESERVED10` | `AcAllocationRule_Reserved10` | TField |  |  |
| 31 | `AC.AR.RESERVED09` | `AcAllocationRule_Reserved09` | TField |  |  |
| 32 | `AC.AR.RESERVED08` | `AcAllocationRule_Reserved08` | TField |  |  |
| 33 | `AC.AR.RESERVED07` | `AcAllocationRule_Reserved07` | TField |  |  |
| 34 | `AC.AR.RESERVED06` | `AcAllocationRule_Reserved06` | TField |  |  |
| 35 | `AC.AR.RESERVED05` | `AcAllocationRule_Reserved05` | TField |  |  |
| 36 | `AC.AR.RESERVED04` | `AcAllocationRule_Reserved04` | TField |  |  |
| 37 | `AC.AR.RESERVED03` | `AcAllocationRule_Reserved03` | TField |  |  |
| 38 | `AC.AR.RESERVED02` | `AcAllocationRule_Reserved02` | TField |  |  |
| 39 | `AC.AR.LOCAL.REF` | `AcAllocationRule_LocalRef` |  |  |  |
| 40 | `AC.AR.OVERRIDE` | `AcAllocationRule_Override` |  |  |  |
| 41 | `AC.AR.RECORD.STATUS` | `AcAllocationRule_RecordStatus` | String |  |  |
| 42 | `AC.AR.CURR.NO` | `AcAllocationRule_CurrNo` | String |  |  |
| 43 | `AC.AR.INPUTTER` | `AcAllocationRule_Inputter` |  |  |  |
| 44 | `AC.AR.DATE.TIME` | `AcAllocationRule_DateTime` |  |  |  |
| 45 | `AC.AR.AUTHORISER` | `AcAllocationRule_Authoriser` | String |  |  |
| 46 | `AC.AR.CO.CODE` | `AcAllocationRule_CoCode` | String |  |  |
| 47 | `AC.AR.DEPT.CODE` | `AcAllocationRule_DeptCode` | String |  |  |
| 48 | `AC.AR.AUDITOR.CODE` | `AcAllocationRule_AuditorCode` | String |  |  |
| 49 | `AC.AR.AUDIT.DATE.TIME` | `AcAllocationRule_AuditDateTime` | String |  |  |
