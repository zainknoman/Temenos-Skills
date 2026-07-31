# SC.MIFID.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.MIFID.PARAM` in `SC_Mifid.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MIFIDPRM.SUITABILITY.CHK` | `ScMifidParam_SuitabilityChk` | TField |  | This Field Specifies whether suitability check to capture fields is set or not The values allowed are :YES/NO If this field is set to Yes Below fields in SC.MIFID.CLIENT.INFO will be no input: BONDS MONEY.MARKET.INSTRUMENTS FIXED.DEPOSITS SHARES MUTUAL.FUNDS HEDGE.FUNDS PVT.EQUITY STRUCTURED.PRDS WARRANTS DERIVATIVES METALS.COMMO Below fields will be available for input ASSET.TYPE SUB.ASSET.TYPE If this field is set to No Below fields in SC.MIFID.CLIENT.INFO will be input: BONDS MONEY.MARKET.INSTRUMENTS FIXED.DEPOSITS SHARES MUTUAL.FUNDS HEDGE.FUNDS PVT.EQUITY STRUCTURED.PRDS WARRANTS DERIVATIVES METALS.COMMO Below fields will be no input: ASSET.TYPE SUB.ASSET.TYPE |
| 2 | `SC.MIFIDPRM.ASSET.TYPE` | `ScMifidParam_AssetType` |  |  |  |
| 3 | `SC.MIFIDPRM.SUB.ASSET.TYPE` | `ScMifidParam_SubAssetType` |  |  |  |
| 4 | `SC.MIFIDPRM.QUESTION.ID` | `ScMifidParam_QuestionId` |  |  |  |
| 5 | `SC.MIFIDPRM.QUESTION` | `ScMifidParam_Question` |  |  |  |
| 6 | `SC.MIFIDPRM.MANDATORY` | `ScMifidParam_Mandatory` |  |  |  |
| 7 | `SC.MIFIDPRM.DROP.PERCENT.VAL` | `ScMifidParam_DropPercentVal` | TField |  |  |
| 8 | `SC.MIFIDPRM.REPORTING.FREQ` | `ScMifidParam_ReportingFreq` | TField |  |  |
| 9 | `SC.MIFIDPRM.REPORTING.FREQ.ST.DATE` | `ScMifidParam_ReportingFreqStDate` | TField |  |  |
| 10 | `SC.MIFIDPRM.KNOWLEDGE.INDICATOR` | `ScMifidParam_KnowledgeIndicator` |  |  |  |
| 11 | `SC.MIFIDPRM.LEI.NCI.CHK.REQ` | `ScMifidParam_LeiNciChkReq` | TField |  |  |
| 12 | `SC.MIFIDPRM.NCI.OVERRIDE.ERR` | `ScMifidParam_NciOverrideErr` | TField |  |  |
| 13 | `SC.MIFIDPRM.RESERVED7` | `ScMifidParam_Reserved7` | TField |  |  |
| 14 | `SC.MIFIDPRM.RESERVED8` | `ScMifidParam_Reserved8` | TField |  |  |
| 15 | `SC.MIFIDPRM.RESERVED9` | `ScMifidParam_Reserved9` | TField |  |  |
| 16 | `SC.MIFIDPRM.RESERVED10` | `ScMifidParam_Reserved10` | TField |  |  |
| 17 | `SC.MIFIDPRM.RESERVED11` | `ScMifidParam_Reserved11` | TField |  |  |
| 18 | `SC.MIFIDPRM.RESERVED12` | `ScMifidParam_Reserved12` | TField |  |  |
| 19 | `SC.MIFIDPRM.RESERVED13` | `ScMifidParam_Reserved13` | TField |  |  |
| 20 | `SC.MIFIDPRM.RESERVED14` | `ScMifidParam_Reserved14` | TField |  |  |
| 21 | `SC.MIFIDPRM.RESERVED15` | `ScMifidParam_Reserved15` | TField |  |  |
| 22 | `SC.MIFIDPRM.RESERVED16` | `ScMifidParam_Reserved16` | TField |  |  |
| 23 | `SC.MIFIDPRM.RESERVED17` | `ScMifidParam_Reserved17` | TField |  |  |
| 24 | `SC.MIFIDPRM.RESERVED18` | `ScMifidParam_Reserved18` | TField |  |  |
| 25 | `SC.MIFIDPRM.RESERVED19` | `ScMifidParam_Reserved19` | TField |  |  |
| 26 | `SC.MIFIDPRM.RESERVED20` | `ScMifidParam_Reserved20` | TField |  |  |
| 27 | `SC.MIFIDPRM.LOCAL.REF` | `ScMifidParam_LocalRef` |  |  |  |
| 28 | `SC.MIFIDPRM.OVERRIDE` | `ScMifidParam_Override` |  |  |  |
| 29 | `SC.MIFIDPRM.RECORD.STATUS` | `ScMifidParam_RecordStatus` | String |  |  |
| 30 | `SC.MIFIDPRM.CURR.NO` | `ScMifidParam_CurrNo` | String |  |  |
| 31 | `SC.MIFIDPRM.INPUTTER` | `ScMifidParam_Inputter` |  |  |  |
| 32 | `SC.MIFIDPRM.DATE.TIME` | `ScMifidParam_DateTime` |  |  |  |
| 33 | `SC.MIFIDPRM.AUTHORISER` | `ScMifidParam_Authoriser` | String |  |  |
| 34 | `SC.MIFIDPRM.CO.CODE` | `ScMifidParam_CoCode` | String |  |  |
| 35 | `SC.MIFIDPRM.DEPT.CODE` | `ScMifidParam_DeptCode` | String |  |  |
| 36 | `SC.MIFIDPRM.AUDITOR.CODE` | `ScMifidParam_AuditorCode` | String |  |  |
| 37 | `SC.MIFIDPRM.AUDIT.DATE.TIME` | `ScMifidParam_AuditDateTime` | String |  |  |
