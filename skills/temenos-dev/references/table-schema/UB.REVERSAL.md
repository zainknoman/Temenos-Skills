# UB.REVERSAL — Table Schema

> Source: `INSERTS/I_F.UB.REVERSAL` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.REV.PAYER` | `UbReversal_Payer` |  |  |  |
| 2 | `UB.REV.ORIG.BP.FT.ID` | `UbReversal_OrigBpFtId` |  |  |  |
| 3 | `UB.REV.PAYEE.ID` | `UbReversal_PayeeId` |  |  |  |
| 4 | `UB.REV.PAYER.BP.AC.NO` | `UbReversal_PayerBpAcNo` |  |  |  |
| 5 | `UB.REV.EFFECTIVE.DATE` | `UbReversal_EffectiveDate` |  |  |  |
| 6 | `UB.REV.AMOUNT` | `UbReversal_Amount` |  |  |  |
| 7 | `UB.REV.ORIG.TRACE.NO` | `UbReversal_OrigTraceNo` |  |  |  |
| 8 | `UB.REV.ADDITIONAL.FLD` | `UbReversal_AdditionalFld` |  |  |  |
| 9 | `UB.REV.ADDITIONAL.VAL` | `UbReversal_AdditionalVal` |  |  |  |
| 10 | `UB.REV.INT.OFS.MSG.ID` | `UbReversal_IntOfsMsgId` |  |  |  |
| 11 | `UB.REV.INT.TXN.STATUS` | `UbReversal_IntTxnStatus` |  |  |  |
| 12 | `UB.REV.INT.TXN.ID` | `UbReversal_IntTxnId` |  |  |  |
| 13 | `UB.REV.INT.OVR.DETAILS` | `UbReversal_IntOvrDetails` |  |  |  |
| 14 | `UB.REV.INT.ERR.DETAILS` | `UbReversal_IntErrDetails` |  |  |  |
| 15 | `UB.REV.INT.DATE.TIME` | `UbReversal_IntDateTime` |  |  |  |
| 16 | `UB.REV.EXT.TXN.STATUS` | `UbReversal_ExtTxnStatus` |  |  |  |
| 17 | `UB.REV.EXT.TXN.ID` | `UbReversal_ExtTxnId` |  |  |  |
| 18 | `UB.REV.EXT.ERR.DETAILS` | `UbReversal_ExtErrDetails` |  |  |  |
| 19 | `UB.REV.EXT.DATE.TIME` | `UbReversal_ExtDateTime` |  |  |  |
| 20 | `UB.REV.LOCAL.REF` | `UbReversal_LocalRef` |  |  |  |
| 21 | `UB.REV.RESERVED.10` | `UbReversal_Reserved10` |  |  |  |
| 22 | `UB.REV.RESERVED.9` | `UbReversal_Reserved9` |  |  |  |
| 23 | `UB.REV.RESERVED.8` | `UbReversal_Reserved8` |  |  |  |
| 24 | `UB.REV.RESERVED.7` | `UbReversal_Reserved7` |  |  |  |
| 25 | `UB.REV.RESERVED.6` | `UbReversal_Reserved6` |  |  |  |
| 26 | `UB.REV.RESERVED.5` | `UbReversal_Reserved5` |  |  |  |
| 27 | `UB.REV.RESERVED.4` | `UbReversal_Reserved4` |  |  |  |
| 28 | `UB.REV.RESERVED.3` | `UbReversal_Reserved3` |  |  |  |
| 29 | `UB.REV.RESERVED.2` | `UbReversal_Reserved2` |  |  |  |
| 30 | `UB.REV.RESERVED.1` | `UbReversal_Reserved1` |  |  |  |
| 31 | `UB.REV.OVERRIDE` | `UbReversal_Override` |  |  |  |
| 32 | `UB.REV.RECORD.STATUS` | `UbReversal_RecordStatus` |  |  |  |
| 33 | `UB.REV.CURR.NO` | `UbReversal_CurrNo` |  |  |  |
| 34 | `UB.REV.INPUTTER` | `UbReversal_Inputter` |  |  |  |
| 35 | `UB.REV.DATE.TIME` | `UbReversal_DateTime` |  |  |  |
| 36 | `UB.REV.AUTHORISER` | `UbReversal_Authoriser` |  |  |  |
| 37 | `UB.REV.CO.CODE` | `UbReversal_CoCode` |  |  |  |
| 38 | `UB.REV.DEPT.CODE` | `UbReversal_DeptCode` |  |  |  |
| 39 | `UB.REV.AUDITOR.CODE` | `UbReversal_AuditorCode` |  |  |  |
| 40 | `UB.REV.AUDIT.DATE.TIME` | `UbReversal_AuditDateTime` |  |  |  |
