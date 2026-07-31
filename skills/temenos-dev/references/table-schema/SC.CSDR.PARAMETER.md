# SC.CSDR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SC.CSDR.PARAMETER` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CSDR.DEPOSITORY` | `ScCsdrParameter_Depository` |  |  |  |
| 2 | `SC.CSDR.TOL.TRAN.AMT` | `ScCsdrParameter_TolTranAmt` |  |  |  |
| 3 | `SC.CSDR.TOL.AMT` | `ScCsdrParameter_TolAmt` |  |  |  |
| 4 | `SC.CSDR.BILATERAL.CANC` | `ScCsdrParameter_BilateralCanc` |  |  |  |
| 5 | `SC.CSDR.SETT.PEN.MSG` | `ScCsdrParameter_SettPenMsg` | TField |  | This field holds value to set up whether the daily penalty details will be received in MT548 or MT537 message. Allowed values: MT548 or MT537 If value MT548 is set, SC.SETT.PENALTY.DAILY record will be updated upon receiving the penalty details via incoming MT548 swift message If value MT537 is set, SC.SETT.PEANLTY.DAILY record will be updated upon receiving the penalty details via incoming MT537 swift message |
| 6 | `SC.CSDR.SETT.PEN.PL.SUSP` | `ScCsdrParameter_SettPenPlSusp` | TField |  | This field holds value to specify whether bank's PL or a suspense account would be credited or debited when the net penalty amount is posted Allowed values: Either valid Internal suspense category account or PL Category can be defined If the value inputted is internal suspense account, then penalty will be posted to internal suspense accout If the value inputted is PL category, then penalty will be posted to PL category |
| 7 | `SC.CSDR.PEN.DR.TRANS.CODE` | `ScCsdrParameter_PenDrTransCode` | TField |  | This field holds the Debit Transaction code used for Debit accounting entry posted for penalty amount Should be a valid record id from TRANSACTION table |
| 8 | `SC.CSDR.PEN.CR.TRANS.CODE` | `ScCsdrParameter_PenCrTransCode` | TField |  | This field holds the Credit Transaction code used for Credit accounting entry posted for penalty amount Should be a valid record id from TRANSACTION table |
| 9 | `SC.CSDR.RESERVED.5` | `ScCsdrParameter_Reserved5` | TField |  |  |
| 10 | `SC.CSDR.RESERVED.4` | `ScCsdrParameter_Reserved4` | TField |  |  |
| 11 | `SC.CSDR.RESERVED.3` | `ScCsdrParameter_Reserved3` | TField |  |  |
| 12 | `SC.CSDR.RESERVED.2` | `ScCsdrParameter_Reserved2` | TField |  |  |
| 13 | `SC.CSDR.RESERVED.1` | `ScCsdrParameter_Reserved1` | TField |  |  |
| 14 | `SC.CSDR.LOCAL.REF` | `ScCsdrParameter_LocalRef` |  |  |  |
| 15 | `SC.CSDR.OVERRIDE` | `ScCsdrParameter_Override` |  |  |  |
| 16 | `SC.CSDR.RECORD.STATUS` | `ScCsdrParameter_RecordStatus` | String |  |  |
| 17 | `SC.CSDR.CURR.NO` | `ScCsdrParameter_CurrNo` | String |  |  |
| 18 | `SC.CSDR.INPUTTER` | `ScCsdrParameter_Inputter` |  |  |  |
| 19 | `SC.CSDR.DATE.TIME` | `ScCsdrParameter_DateTime` |  |  |  |
| 20 | `SC.CSDR.AUTHORISER` | `ScCsdrParameter_Authoriser` | String |  |  |
| 21 | `SC.CSDR.CO.CODE` | `ScCsdrParameter_CoCode` | String |  |  |
| 22 | `SC.CSDR.DEPT.CODE` | `ScCsdrParameter_DeptCode` | String |  |  |
| 23 | `SC.CSDR.AUDITOR.CODE` | `ScCsdrParameter_AuditorCode` | String |  |  |
| 24 | `SC.CSDR.AUDIT.DATE.TIME` | `ScCsdrParameter_AuditDateTime` | String |  |  |
