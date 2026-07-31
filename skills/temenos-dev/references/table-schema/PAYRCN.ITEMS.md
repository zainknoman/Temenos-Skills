# PAYRCN.ITEMS — Table Schema

> Source: `INSERTS/I_F.PAYRCN.ITEMS` in `FINEXT_ATMRECON.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAYRCN.ITEM.REFERENCE.NUMBER` | `PayrcnItems_ReferenceNumber` | TField |  |  |
| 2 | `PAYRCN.ITEM.ADD.INFO` | `PayrcnItems_AddInfo` | TField |  |  |
| 3 | `PAYRCN.ITEM.OUR.THEIR.FLAG` | `PayrcnItems_OurTheirFlag` | TField |  |  |
| 4 | `PAYRCN.ITEM.CURRENCY` | `PayrcnItems_Currency` | TField |  |  |
| 5 | `PAYRCN.ITEM.TXN.AMT` | `PayrcnItems_TxnAmt` | TField |  |  |
| 6 | `PAYRCN.ITEM.TXN.AMT.LCY` | `PayrcnItems_TxnAmtLcy` | TField |  |  |
| 7 | `PAYRCN.ITEM.TRANSACTION.DATE` | `PayrcnItems_TransactionDate` | TField |  |  |
| 8 | `PAYRCN.ITEM.TRANSACTION.TIME` | `PayrcnItems_TransactionTime` | TField |  |  |
| 9 | `PAYRCN.ITEM.VALUE.DATE` | `PayrcnItems_ValueDate` | TField |  |  |
| 10 | `PAYRCN.ITEM.MATCHED.ID` | `PayrcnItems_MatchedId` |  |  |  |
| 11 | `PAYRCN.ITEM.STATUS` | `PayrcnItems_Status` | TField |  |  |
| 12 | `PAYRCN.ITEM.STATUS.DESC` | `PayrcnItems_StatusDesc` | TField |  |  |
| 13 | `PAYRCN.ITEM.DATE.MATCHED` | `PayrcnItems_DateMatched` | TField |  |  |
| 14 | `PAYRCN.ITEM.CR.DR.INDICATOR` | `PayrcnItems_CrDrIndicator` | TField |  |  |
| 15 | `PAYRCN.ITEM.RECORD.TYPE` | `PayrcnItems_RecordType` | TField |  |  |
| 16 | `PAYRCN.ITEM.RESERVED.31` | `PayrcnItems_Reserved31` | TField |  |  |
| 17 | `PAYRCN.ITEM.RESERVED.30` | `PayrcnItems_Reserved30` | TField |  |  |
| 18 | `PAYRCN.ITEM.RESERVED.29` | `PayrcnItems_Reserved29` | TField |  |  |
| 19 | `PAYRCN.ITEM.RESERVED.28` | `PayrcnItems_Reserved28` | TField |  |  |
| 20 | `PAYRCN.ITEM.RESERVED.27` | `PayrcnItems_Reserved27` | TField |  |  |
| 21 | `PAYRCN.ITEM.RESERVED.26` | `PayrcnItems_Reserved26` | TField |  |  |
| 22 | `PAYRCN.ITEM.RESERVED.25` | `PayrcnItems_Reserved25` | TField |  |  |
| 23 | `PAYRCN.ITEM.RESERVED.24` | `PayrcnItems_Reserved24` | TField |  |  |
| 24 | `PAYRCN.ITEM.RESERVED.23` | `PayrcnItems_Reserved23` | TField |  |  |
| 25 | `PAYRCN.ITEM.RESERVED.22` | `PayrcnItems_Reserved22` | TField |  |  |
| 26 | `PAYRCN.ITEM.RESERVED.21` | `PayrcnItems_Reserved21` | TField |  |  |
| 27 | `PAYRCN.ITEM.VARIABLE.1` | `PayrcnItems_Variable1` | TField |  |  |
| 28 | `PAYRCN.ITEM.VARIABLE.2` | `PayrcnItems_Variable2` | TField |  |  |
| 29 | `PAYRCN.ITEM.VARIABLE.3` | `PayrcnItems_Variable3` | TField |  |  |
| 30 | `PAYRCN.ITEM.VARIABLE.4` | `PayrcnItems_Variable4` | TField |  |  |
| 31 | `PAYRCN.ITEM.VARIABLE.5` | `PayrcnItems_Variable5` | TField |  |  |
| 32 | `PAYRCN.ITEM.VARIABLE.6` | `PayrcnItems_Variable6` | TField |  |  |
| 33 | `PAYRCN.ITEM.VARIABLE.7` | `PayrcnItems_Variable7` | TField |  |  |
| 34 | `PAYRCN.ITEM.VARIABLE.8` | `PayrcnItems_Variable8` | TField |  |  |
| 35 | `PAYRCN.ITEM.VARIABLE.9` | `PayrcnItems_Variable9` | TField |  |  |
| 36 | `PAYRCN.ITEM.VARIABLE.10` | `PayrcnItems_Variable10` | TField |  |  |
| 37 | `PAYRCN.ITEM.VARIABLE.11` | `PayrcnItems_Variable11` | TField |  |  |
| 38 | `PAYRCN.ITEM.VARIABLE.12` | `PayrcnItems_Variable12` | TField |  |  |
| 39 | `PAYRCN.ITEM.VARIABLE.13` | `PayrcnItems_Variable13` | TField |  |  |
| 40 | `PAYRCN.ITEM.VARIABLE.14` | `PayrcnItems_Variable14` | TField |  |  |
| 41 | `PAYRCN.ITEM.VARIABLE.15` | `PayrcnItems_Variable15` | TField |  |  |
| 42 | `PAYRCN.ITEM.VARIABLE.16` | `PayrcnItems_Variable16` | TField |  |  |
| 43 | `PAYRCN.ITEM.VARIABLE.17` | `PayrcnItems_Variable17` | TField |  |  |
| 44 | `PAYRCN.ITEM.VARIABLE.18` | `PayrcnItems_Variable18` | TField |  |  |
| 45 | `PAYRCN.ITEM.VARIABLE.19` | `PayrcnItems_Variable19` | TField |  |  |
| 46 | `PAYRCN.ITEM.VARIABLE.20` | `PayrcnItems_Variable20` | TField |  |  |
| 47 | `PAYRCN.ITEM.VARIABLE.21` | `PayrcnItems_Variable21` | TField |  |  |
| 48 | `PAYRCN.ITEM.VARIABLE.22` | `PayrcnItems_Variable22` | TField |  |  |
| 49 | `PAYRCN.ITEM.VARIABLE.23` | `PayrcnItems_Variable23` | TField |  |  |
| 50 | `PAYRCN.ITEM.VARIABLE.24` | `PayrcnItems_Variable24` | TField |  |  |
| 51 | `PAYRCN.ITEM.VARIABLE.25` | `PayrcnItems_Variable25` | TField |  |  |
| 52 | `PAYRCN.ITEM.VARIABLE.26` | `PayrcnItems_Variable26` | TField |  |  |
| 53 | `PAYRCN.ITEM.VARIABLE.27` | `PayrcnItems_Variable27` | TField |  |  |
| 54 | `PAYRCN.ITEM.VARIABLE.28` | `PayrcnItems_Variable28` | TField |  |  |
| 55 | `PAYRCN.ITEM.VARIABLE.29` | `PayrcnItems_Variable29` | TField |  |  |
| 56 | `PAYRCN.ITEM.VARIABLE.30` | `PayrcnItems_Variable30` | TField |  |  |
| 57 | `PAYRCN.ITEM.RESERVED.20` | `PayrcnItems_Reserved20` | TField |  |  |
| 58 | `PAYRCN.ITEM.RESERVED.19` | `PayrcnItems_Reserved19` | TField |  |  |
| 59 | `PAYRCN.ITEM.RESERVED.18` | `PayrcnItems_Reserved18` | TField |  |  |
| 60 | `PAYRCN.ITEM.RESERVED.17` | `PayrcnItems_Reserved17` | TField |  |  |
| 61 | `PAYRCN.ITEM.RESERVED.16` | `PayrcnItems_Reserved16` | TField |  |  |
| 62 | `PAYRCN.ITEM.RESERVED.15` | `PayrcnItems_Reserved15` | TField |  |  |
| 63 | `PAYRCN.ITEM.RESERVED.14` | `PayrcnItems_Reserved14` | TField |  |  |
| 64 | `PAYRCN.ITEM.RESERVED.13` | `PayrcnItems_Reserved13` | TField |  |  |
| 65 | `PAYRCN.ITEM.RESERVED.12` | `PayrcnItems_Reserved12` | TField |  |  |
| 66 | `PAYRCN.ITEM.RESERVED.11` | `PayrcnItems_Reserved11` | TField |  |  |
| 67 | `PAYRCN.ITEM.RESERVED.10` | `PayrcnItems_Reserved10` | TField |  |  |
| 68 | `PAYRCN.ITEM.RESERVED.9` | `PayrcnItems_Reserved9` | TField |  |  |
| 69 | `PAYRCN.ITEM.RESERVED.8` | `PayrcnItems_Reserved8` | TField |  |  |
| 70 | `PAYRCN.ITEM.RESERVED.7` | `PayrcnItems_Reserved7` | TField |  |  |
| 71 | `PAYRCN.ITEM.RESERVED.6` | `PayrcnItems_Reserved6` | TField |  |  |
| 72 | `PAYRCN.ITEM.RESERVED.5` | `PayrcnItems_Reserved5` | TField |  |  |
| 73 | `PAYRCN.ITEM.RESERVED.4` | `PayrcnItems_Reserved4` | TField |  |  |
| 74 | `PAYRCN.ITEM.RESERVED.3` | `PayrcnItems_Reserved3` | TField |  |  |
| 75 | `PAYRCN.ITEM.RESERVED.2` | `PayrcnItems_Reserved2` | TField |  |  |
| 76 | `PAYRCN.ITEM.RESERVED.1` | `PayrcnItems_Reserved1` | TField |  |  |
| 77 | `PAYRCN.ITEM.OVERRIDE` | `PayrcnItems_Override` |  |  |  |
| 78 | `PAYRCN.ITEM.RECORD.STATUS` | `PayrcnItems_RecordStatus` | String |  |  |
| 79 | `PAYRCN.ITEM.CURR.NO` | `PayrcnItems_CurrNo` | String |  |  |
| 80 | `PAYRCN.ITEM.INPUTTER` | `PayrcnItems_Inputter` |  |  |  |
| 81 | `PAYRCN.ITEM.DATE.TIME` | `PayrcnItems_DateTime` |  |  |  |
| 82 | `PAYRCN.ITEM.AUTHORISER` | `PayrcnItems_Authoriser` | String |  |  |
| 83 | `PAYRCN.ITEM.CO.CODE` | `PayrcnItems_CoCode` | String |  |  |
| 84 | `PAYRCN.ITEM.DEPT.CODE` | `PayrcnItems_DeptCode` | String |  |  |
| 85 | `PAYRCN.ITEM.AUDITOR.CODE` | `PayrcnItems_AuditorCode` | String |  |  |
| 86 | `PAYRCN.ITEM.AUDIT.DATE.TIME` | `PayrcnItems_AuditDateTime` | String |  |  |
