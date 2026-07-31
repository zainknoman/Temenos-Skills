# ARACCT.ONLINE.SWEEP.PARAM — Table Schema

> Source: `INSERTS/I_F.ARACCT.ONLINE.SWEEP.PARAM` in `ARACCT_BalanceCheck.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.SWEEP.AUTO.REV.SWEEP.CREATION` | `AracctOnlineSweepParam_AutoRevSweepCreation` | TField |  | This is a Yes/No field which is used to identify if the auto reverse sweep creation has to be enabled or not. |
| 2 | `ARACCT.SWEEP.REVERSE.SWEEP.TYPE` | `AracctOnlineSweepParam_ReverseSweepType` | TField |  | This is a text field, where used is allowed to enter a sweep type which will be used for the creation of reverse sweep. |
| 3 | `ARACCT.SWEEP.RESERVED.10` | `AracctOnlineSweepParam_Reserved10` | TField |  | Reserved for furture use. |
| 4 | `ARACCT.SWEEP.RESERVED.9` | `AracctOnlineSweepParam_Reserved9` | TField |  | Reserved for furture use. |
| 5 | `ARACCT.SWEEP.RESERVED.8` | `AracctOnlineSweepParam_Reserved8` | TField |  | Reserved for furture use. |
| 6 | `ARACCT.SWEEP.RESERVED.7` | `AracctOnlineSweepParam_Reserved7` | TField |  | Reserved for furture use. |
| 7 | `ARACCT.SWEEP.RESERVED.6` | `AracctOnlineSweepParam_Reserved6` | TField |  | Reserved for furture use. |
| 8 | `ARACCT.SWEEP.RESERVED.5` | `AracctOnlineSweepParam_Reserved5` | TField |  | Reserved for furture use. |
| 9 | `ARACCT.SWEEP.RESERVED.4` | `AracctOnlineSweepParam_Reserved4` | TField |  | Reserved for furture use. |
| 10 | `ARACCT.SWEEP.RESERVED.3` | `AracctOnlineSweepParam_Reserved3` | TField |  | Reserved for furture use. |
| 11 | `ARACCT.SWEEP.RESERVED.2` | `AracctOnlineSweepParam_Reserved2` | TField |  | Reserved for furture use. |
| 12 | `ARACCT.SWEEP.RESERVED.1` | `AracctOnlineSweepParam_Reserved1` | TField |  | Reserved for furture use. |
| 13 | `ARACCT.SWEEP.RECORD.STATUS` | `AracctOnlineSweepParam_RecordStatus` | String |  |  |
| 14 | `ARACCT.SWEEP.CURR.NO` | `AracctOnlineSweepParam_CurrNo` | String |  |  |
| 15 | `ARACCT.SWEEP.INPUTTER` | `AracctOnlineSweepParam_Inputter` |  |  |  |
| 16 | `ARACCT.SWEEP.DATE.TIME` | `AracctOnlineSweepParam_DateTime` |  |  |  |
| 17 | `ARACCT.SWEEP.AUTHORISER` | `AracctOnlineSweepParam_Authoriser` | String |  |  |
| 18 | `ARACCT.SWEEP.CO.CODE` | `AracctOnlineSweepParam_CoCode` | String |  |  |
| 19 | `ARACCT.SWEEP.DEPT.CODE` | `AracctOnlineSweepParam_DeptCode` | String |  |  |
| 20 | `ARACCT.SWEEP.AUDITOR.CODE` | `AracctOnlineSweepParam_AuditorCode` | String |  |  |
| 21 | `ARACCT.SWEEP.AUDIT.DATE.TIME` | `AracctOnlineSweepParam_AuditDateTime` | String |  |  |
