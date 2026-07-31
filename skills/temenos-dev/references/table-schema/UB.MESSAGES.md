# UB.MESSAGES — Table Schema

> Source: `INSERTS/I_F.UB.MESSAGES` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.MSG.PRE.RTN` | `UbMessages_PreRtn` | TField |  | Field is used to store the routine which is used before sendign the request message to the switch provider. |
| 2 | `UB.MSG.RCL.REQ.MSG` | `UbMessages_RclReqMsg` | TField |  | Field is used to store the request Message ID to Convert T24 format to Flat file.Validation:Up to R13 release, record from RAD.CONDUIT.LINEARFrom R17 release, record from DFE.MAPPING |
| 3 | `UB.MSG.REQ.LOG.DIR` | `UbMessages_ReqLogDir` | TField |  | Field to store the valid directory in which the request message is logged in.eg. TEST.IN |
| 4 | `UB.MSG.RESERVED.8` | `UbMessages_Reserved8` | TField |  |  |
| 5 | `UB.MSG.RESERVED.7` | `UbMessages_Reserved7` | TField |  |  |
| 6 | `UB.MSG.RCL.RES.MSG` | `UbMessages_RclResMsg` | TField |  | Field is used to store the Response Message ID to Convert T24 format to Flat file.Validation:Up to R13 release, record from RAD.CONDUIT.LINEARFrom R17 release, record from DFE.MAPPING |
| 7 | `UB.MSG.POST.RTN` | `UbMessages_PostRtn` | TField |  |  |
| 8 | `UB.MSG.RES.LOG.DIR` | `UbMessages_ResLogDir` | TField |  |  |
| 9 | `UB.MSG.RESERVED.6` | `UbMessages_Reserved6` | TField |  |  |
| 10 | `UB.MSG.RESERVED.5` | `UbMessages_Reserved5` | TField |  |  |
| 11 | `UB.MSG.RESERVED.4` | `UbMessages_Reserved4` | TField |  |  |
| 12 | `UB.MSG.TIME.OUT` | `UbMessages_TimeOut` | TField |  | Field to store the seconds to be considered for Timeout for TCP response.Eg. 3 |
| 13 | `UB.MSG.FT.VERSION` | `UbMessages_FtVersion` | TField |  | Field is used to store the FT version that is to be used for the Bill payment.Validation - record from VERSIONeg. FUNDS.TRANSFER,CAMB.BILL.PAY |
| 14 | `UB.MSG.LOCAL.REF` | `UbMessages_LocalRef` |  |  |  |
| 15 | `UB.MSG.RESERVED.3` | `UbMessages_Reserved3` | TField |  |  |
| 16 | `UB.MSG.RESERVED.2` | `UbMessages_Reserved2` | TField |  |  |
| 17 | `UB.MSG.RESERVED.1` | `UbMessages_Reserved1` | TField |  |  |
| 18 | `UB.MSG.OVERRIDE` | `UbMessages_Override` |  |  |  |
| 19 | `UB.MSG.RECORD.STATUS` | `UbMessages_RecordStatus` | String |  |  |
| 20 | `UB.MSG.CURR.NO` | `UbMessages_CurrNo` | String |  |  |
| 21 | `UB.MSG.INPUTTER` | `UbMessages_Inputter` |  |  |  |
| 22 | `UB.MSG.DATE.TIME` | `UbMessages_DateTime` |  |  |  |
| 23 | `UB.MSG.AUTHORISER` | `UbMessages_Authoriser` | String |  |  |
| 24 | `UB.MSG.CO.CODE` | `UbMessages_CoCode` | String |  |  |
| 25 | `UB.MSG.DEPT.CODE` | `UbMessages_DeptCode` | String |  |  |
| 26 | `UB.MSG.AUDITOR.CODE` | `UbMessages_AuditorCode` | String |  |  |
| 27 | `UB.MSG.AUDIT.DATE.TIME` | `UbMessages_AuditDateTime` | String |  |  |
