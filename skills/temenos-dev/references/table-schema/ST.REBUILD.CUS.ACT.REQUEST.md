# ST.REBUILD.CUS.ACT.REQUEST — Table Schema

> Source: `INSERTS/I_F.ST.REBUILD.CUS.ACT.REQUEST` in `ST_CustomerActivity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.RCR.ALL.PARTY.ID` | `StRebuildCusActRequest_AllPartyId` | TField |  | If set as YES, then the rebuild will be done for all the parties present. Validations: Only one of the ALL.PARTY.ID,PARTY.APPLN and PARTY.ID fields are allowed to input. |
| 2 | `ST.RCR.PARTY.APPLN` | `StRebuildCusActRequest_PartyAppln` |  |  |  |
| 3 | `ST.RCR.PARTY.ID` | `StRebuildCusActRequest_PartyId` |  |  |  |
| 4 | `ST.RCR.ALL.ACT.APPLN` | `StRebuildCusActRequest_AllActAppln` | TField |  | If set as Yes, then all the contracts which defines the activity of the parties will be taken into consideration while rebuilding. Validations: Only one of the ALL.ACT.APPLN,ALL.LINK.APPLN and APPLICATION fields are allowed to input. |
| 5 | `ST.RCR.ALL.LINK.APPLN` | `StRebuildCusActRequest_AllLinkAppln` | TField |  | If set as Yes, then all the static applications that needs to be listed in ST.CUSTOMER.ACTIVITY will be taken into consideration while rebuilding. Applications whose USE.IN.ACTIVITY is as LINK in ST.CUSTOMER.ACTIVITY.PARAMETER will only be taken into consideration Validations: Only one of the ALL.ACT.APPLN,ALL.LINK.APPLN and APPLICATION fields are allowed to input. |
| 6 | `ST.RCR.APPLICATION` | `StRebuildCusActRequest_Application` |  |  |  |
| 7 | `ST.RCR.CUS.COMPANY` | `StRebuildCusActRequest_CusCompany` | TField | Yes | Valid Customer company needs to be specified, if a branch company is mentioned,then auto populates to the respective customer company Mandatory field Only one request can be done for one customer company at a time If an unprocessed request exists for the current customer company mentioned, then the current request is not allowed to be authorised. |
| 8 | `ST.RCR.REG.EXCLUDE` | `StRebuildCusActRequest_RegExclude` | TField |  | This field, if set as YES represents that the request is initiated to remove the customer activity from ST.CUSTOMER.ACTIVITY and CZ.CUSTOMER.ACTIVITY for the excluded customers based on the ST.REG.EXCLUDE.PARAM criteria Manual input is disabled. Authorising ST.REG.EXCLUDE.PARAM will initiate the rebuild request by setting REG.EXCLUDE field as YES automatically. Reversal of request is not possible if this field is set as YES. |
| 9 | `ST.RCR.RESERVED.19` | `StRebuildCusActRequest_Reserved19` | TField |  |  |
| 10 | `ST.RCR.RESERVED.18` | `StRebuildCusActRequest_Reserved18` | TField |  |  |
| 11 | `ST.RCR.RESERVED.17` | `StRebuildCusActRequest_Reserved17` | TField |  |  |
| 12 | `ST.RCR.RESERVED.16` | `StRebuildCusActRequest_Reserved16` | TField |  |  |
| 13 | `ST.RCR.RESERVED.15` | `StRebuildCusActRequest_Reserved15` | TField |  |  |
| 14 | `ST.RCR.RESERVED.14` | `StRebuildCusActRequest_Reserved14` | TField |  |  |
| 15 | `ST.RCR.RESERVED.13` | `StRebuildCusActRequest_Reserved13` | TField |  |  |
| 16 | `ST.RCR.RESERVED.12` | `StRebuildCusActRequest_Reserved12` | TField |  |  |
| 17 | `ST.RCR.RESERVED.11` | `StRebuildCusActRequest_Reserved11` | TField |  |  |
| 18 | `ST.RCR.RESERVED.10` | `StRebuildCusActRequest_Reserved10` | TField |  |  |
| 19 | `ST.RCR.RESERVED.09` | `StRebuildCusActRequest_Reserved09` | TField |  |  |
| 20 | `ST.RCR.RESERVED.08` | `StRebuildCusActRequest_Reserved08` | TField |  |  |
| 21 | `ST.RCR.RESERVED.07` | `StRebuildCusActRequest_Reserved07` | TField |  |  |
| 22 | `ST.RCR.RESERVED.06` | `StRebuildCusActRequest_Reserved06` | TField |  |  |
| 23 | `ST.RCR.RESERVED.05` | `StRebuildCusActRequest_Reserved05` | TField |  |  |
| 24 | `ST.RCR.RESERVED.04` | `StRebuildCusActRequest_Reserved04` | TField |  |  |
| 25 | `ST.RCR.RESERVED.03` | `StRebuildCusActRequest_Reserved03` | TField |  |  |
| 26 | `ST.RCR.RESERVED.02` | `StRebuildCusActRequest_Reserved02` | TField |  |  |
| 27 | `ST.RCR.RESERVED.01` | `StRebuildCusActRequest_Reserved01` | TField |  |  |
| 28 | `ST.RCR.LOCAL.REF` | `StRebuildCusActRequest_LocalRef` |  |  |  |
| 29 | `ST.RCR.OVERRIDE` | `StRebuildCusActRequest_Override` |  |  |  |
| 30 | `ST.RCR.RECORD.STATUS` | `StRebuildCusActRequest_RecordStatus` | String |  |  |
| 31 | `ST.RCR.CURR.NO` | `StRebuildCusActRequest_CurrNo` | String |  |  |
| 32 | `ST.RCR.INPUTTER` | `StRebuildCusActRequest_Inputter` |  |  |  |
| 33 | `ST.RCR.DATE.TIME` | `StRebuildCusActRequest_DateTime` |  |  |  |
| 34 | `ST.RCR.AUTHORISER` | `StRebuildCusActRequest_Authoriser` | String |  |  |
| 35 | `ST.RCR.CO.CODE` | `StRebuildCusActRequest_CoCode` | String |  |  |
| 36 | `ST.RCR.DEPT.CODE` | `StRebuildCusActRequest_DeptCode` | String |  |  |
| 37 | `ST.RCR.AUDITOR.CODE` | `StRebuildCusActRequest_AuditorCode` | String |  |  |
| 38 | `ST.RCR.AUDIT.DATE.TIME` | `StRebuildCusActRequest_AuditDateTime` | String |  |  |
