# CAMB.ATM.POS.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.ATM.POS.PARAM` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ATM.POS.ATM.SWITCH` | `CambAtmPosParam_AtmSwitch` | TField |  | Define type of ATM switch used i.e. EVERLINK/THRESHOLD |
| 2 | `CAMB.ATM.POS.PSN.POSN` | `CambAtmPosParam_PsnPosn` | TField |  | This field used to parameterise the PSN position from the incoming ISO request for Transaction validation.Eg: 35[11,3]The above definition indicates that system should take the Bit Map 35 and the position starts from 11 for 3 chars. |
| 3 | `CAMB.ATM.POS.RECV.INST.ID` | `CambAtmPosParam_RecvInstId` | TField |  | Field to sTore the receiver's institution ID |
| 4 | `CAMB.ATM.POS.PRE.AUT.HLD.DAYS` | `CambAtmPosParam_PreAutHldDays` | TField |  | This Field used to parameterise the number of days to be used for calculating the expiry date when processing the pre-authorization POS messages.Include W or C as suffix to specify calendar or Working days.E.g.: 4C, 5WEg: 3C |
| 5 | `CAMB.ATM.POS.PRE.AUTH.BIT.MAP` | `CambAtmPosParam_PreAuthBitMap` |  |  |  |
| 6 | `CAMB.ATM.POS.RESERVED.7` | `CambAtmPosParam_Reserved7` |  |  |  |
| 7 | `CAMB.ATM.POS.RESERVED.6` | `CambAtmPosParam_Reserved6` |  |  |  |
| 8 | `CAMB.ATM.POS.RESERVED.5` | `CambAtmPosParam_Reserved5` |  |  |  |
| 9 | `CAMB.ATM.POS.RESERVED.4` | `CambAtmPosParam_Reserved4` |  |  |  |
| 10 | `CAMB.ATM.POS.RESERVED.3` | `CambAtmPosParam_Reserved3` |  |  |  |
| 11 | `CAMB.ATM.POS.RESERVED.2` | `CambAtmPosParam_Reserved2` | TField |  |  |
| 12 | `CAMB.ATM.POS.RESERVED.1` | `CambAtmPosParam_Reserved1` | TField |  |  |
| 13 | `CAMB.ATM.POS.RECORD.STATUS` | `CambAtmPosParam_RecordStatus` | String |  |  |
| 14 | `CAMB.ATM.POS.CURR.NO` | `CambAtmPosParam_CurrNo` | String |  |  |
| 15 | `CAMB.ATM.POS.INPUTTER` | `CambAtmPosParam_Inputter` |  |  |  |
| 16 | `CAMB.ATM.POS.DATE.TIME` | `CambAtmPosParam_DateTime` |  |  |  |
| 17 | `CAMB.ATM.POS.AUTHORISER` | `CambAtmPosParam_Authoriser` | String |  |  |
| 18 | `CAMB.ATM.POS.CO.CODE` | `CambAtmPosParam_CoCode` | String |  |  |
| 19 | `CAMB.ATM.POS.DEPT.CODE` | `CambAtmPosParam_DeptCode` | String |  |  |
| 20 | `CAMB.ATM.POS.AUDITOR.CODE` | `CambAtmPosParam_AuditorCode` | String |  |  |
| 21 | `CAMB.ATM.POS.AUDIT.DATE.TIME` | `CambAtmPosParam_AuditDateTime` | String |  |  |
