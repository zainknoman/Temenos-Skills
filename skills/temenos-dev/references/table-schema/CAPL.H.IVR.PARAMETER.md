# CAPL.H.IVR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.H.IVR.PARAMETER` in `CATELS_TelephoneBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.IVR.PM.DFLT.TXN.TYPE` | `CaplHIvrParameter_DfltTxnType` | TField |  | This field value will be used as a default transaction type while performing FUNDS.TRANSFER through IVR interface.Validation: The value in this field should be a valid record from the table FT.TXN.TYPE.CONDITIONEg: AC |
| 2 | `CP.IVR.PM.AA.DISB.TXN.TYPE` | `CaplHIvrParameter_AaDisbTxnType` | TField |  | This field value will be used as a transaction type while performing loan disbursement through IVR channel.Validation: The value in this field should be a valid record from the table FT.TXN.TYPE.CONDITION.Eg: ACMT |
| 3 | `CP.IVR.PM.AA.RPY.TXN.TYPE` | `CaplHIvrParameter_AaRpyTxnType` | TField |  | This field value will be used as a transaction type while performing loan repayment through IVR channel.Validation: The value in this field should be a valid record from the table FT.TXN.TYPE.CONDITION.Eg: ACRT |
| 4 | `CP.IVR.PM.AUT.CON.RTNS` | `CaplHIvrParameter_AutConRtns` |  |  |  |
| 5 | `CP.IVR.PM.INP.RTNS` | `CaplHIvrParameter_InpRtns` |  |  |  |
| 6 | `CP.IVR.PM.AUTH.RTNS` | `CaplHIvrParameter_AuthRtns` |  |  |  |
| 7 | `CP.IVR.PM.CARD.ACT.VERSION` | `CaplHIvrParameter_CardActVersion` | TField |  | Field is used to store the version to be considered for updating the activated date field in CARD.ACCESS while activating the card.Eg. CARD.ACCESS,CAMBWhile activating card through IVR, field ACTIVATED.DATE gets updated in CARD.ACCESS |
| 8 | `CP.IVR.PM.RESERVED.8` | `CaplHIvrParameter_Reserved8` | TField |  |  |
| 9 | `CP.IVR.PM.RESERVED.7` | `CaplHIvrParameter_Reserved7` | TField |  |  |
| 10 | `CP.IVR.PM.RESERVED.6` | `CaplHIvrParameter_Reserved6` | TField |  |  |
| 11 | `CP.IVR.PM.RESERVED.5` | `CaplHIvrParameter_Reserved5` | TField |  |  |
| 12 | `CP.IVR.PM.RESERVED.4` | `CaplHIvrParameter_Reserved4` | TField |  |  |
| 13 | `CP.IVR.PM.RESERVED.3` | `CaplHIvrParameter_Reserved3` | TField |  |  |
| 14 | `CP.IVR.PM.RESERVED.2` | `CaplHIvrParameter_Reserved2` | TField |  |  |
| 15 | `CP.IVR.PM.RESERVED.1` | `CaplHIvrParameter_Reserved1` | TField |  |  |
| 16 | `CP.IVR.PM.LOCAL.REF` | `CaplHIvrParameter_LocalRef` |  |  |  |
| 17 | `CP.IVR.PM.OVERRIDE` | `CaplHIvrParameter_Override` |  |  |  |
| 18 | `CP.IVR.PM.RECORD.STATUS` | `CaplHIvrParameter_RecordStatus` | String |  |  |
| 19 | `CP.IVR.PM.CURR.NO` | `CaplHIvrParameter_CurrNo` | String |  |  |
| 20 | `CP.IVR.PM.INPUTTER` | `CaplHIvrParameter_Inputter` |  |  |  |
| 21 | `CP.IVR.PM.DATE.TIME` | `CaplHIvrParameter_DateTime` |  |  |  |
| 22 | `CP.IVR.PM.AUTHORISER` | `CaplHIvrParameter_Authoriser` | String |  |  |
| 23 | `CP.IVR.PM.CO.CODE` | `CaplHIvrParameter_CoCode` | String |  |  |
| 24 | `CP.IVR.PM.DEPT.CODE` | `CaplHIvrParameter_DeptCode` | String |  |  |
| 25 | `CP.IVR.PM.AUDITOR.CODE` | `CaplHIvrParameter_AuditorCode` | String |  |  |
| 26 | `CP.IVR.PM.AUDIT.DATE.TIME` | `CaplHIvrParameter_AuditDateTime` | String |  |  |
