# INTRF.HOLD.PARAM — Table Schema

> Source: `INSERTS/I_F.INTRF.HOLD.PARAM` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HOLD.PARAM.INTRF.POS` | `IntrfHoldParam_IntrfPos` |  |  |  |
| 2 | `HOLD.PARAM.INTRF.POS.VAL` | `IntrfHoldParam_IntrfPosVal` |  |  |  |
| 3 | `HOLD.PARAM.HOLD.PERIOD` | `IntrfHoldParam_HoldPeriod` |  |  |  |
| 4 | `HOLD.PARAM.DESC.INTRF.POS` | `IntrfHoldParam_DescIntrfPos` |  |  |  |
| 5 | `HOLD.PARAM.HOLD.TYPE` | `IntrfHoldParam_HoldType` | TField |  | This field is to configure the hold type that needs to be updated in the AC.LOCKED.EVENTS > CDIC.HOLD.TYPE field. In order to determine the type of hold being placed.Valid record from EB.LOOKUP table.Ex. CAREGS.CDIC.DEPOSIT.HOLD * Cheque |
| 6 | `HOLD.PARAM.HOLD.BIT.MAP` | `IntrfHoldParam_HoldBitMap` | TField |  | The purpose of this field is used to define the bit map position for the ISO message, where the ATM hold time interval code will be available.If this field is configured and the incoming value in the message is BLANK , then system will not refer the HOLD.PERIOD to place the hold.Allowed values are 35 alphanumeric charactersThe value in this field to be configured as:Ex. 126 [4] where,126 - Bit Map Value[4] - Represents the time interval (Minutes, Hours, Days) |
| 7 | `HOLD.PARAM.HOLD.BIT.MAP.CODE` | `IntrfHoldParam_HoldBitMapCode` |  |  |  |
| 8 | `HOLD.PARAM.HLD.BIT.MAP.CD.VAL` | `IntrfHoldParam_HldBitMapCdVal` |  |  |  |
| 9 | `HOLD.PARAM.HOLD.BIT.MAP.TIME` | `IntrfHoldParam_HoldBitMapTime` | TField |  | This field is used to define the bit map position where the time interval is available in the ISO message.Allowed values are 10 alphanumeric characters.Ex. 126[5,2], where126 = Bit Map[5,2] = from 5th position 2 characters.Note: If the value in the bit map is "00" then system will capture current system date and time in AC.LOCKED.EVENTS. |
| 10 | `HOLD.PARAM.OVERRIDE` | `IntrfHoldParam_Override` |  |  |  |
| 11 | `HOLD.PARAM.RECORD.STATUS` | `IntrfHoldParam_RecordStatus` | String |  |  |
| 12 | `HOLD.PARAM.CURR.NO` | `IntrfHoldParam_CurrNo` | String |  |  |
| 13 | `HOLD.PARAM.INPUTTER` | `IntrfHoldParam_Inputter` |  |  |  |
| 14 | `HOLD.PARAM.DATE.TIME` | `IntrfHoldParam_DateTime` |  |  |  |
| 15 | `HOLD.PARAM.AUTHORISER` | `IntrfHoldParam_Authoriser` | String |  |  |
| 16 | `HOLD.PARAM.CO.CODE` | `IntrfHoldParam_CoCode` | String |  |  |
| 17 | `HOLD.PARAM.DEPT.CODE` | `IntrfHoldParam_DeptCode` | String |  |  |
| 18 | `HOLD.PARAM.AUDITOR.CODE` | `IntrfHoldParam_AuditorCode` | String |  |  |
| 19 | `HOLD.PARAM.AUDIT.DATE.TIME` | `IntrfHoldParam_AuditDateTime` | String |  |  |
