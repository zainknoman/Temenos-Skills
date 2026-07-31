# SC.FACILITY.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.FACILITY.PARAM` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.FAP.FACILITY.QUESTION` | `ScFacilityParam_FacilityQuestion` |  |  |  |
| 2 | `SC.FAP.ALLOWED.RESPONSE` | `ScFacilityParam_AllowedResponse` |  |  |  |
| 3 | `SC.FAP.DOCUMENT.TYPE` | `ScFacilityParam_DocumentType` |  |  |  |
| 4 | `SC.FAP.DOCUMENT.DESCRIPTION` | `ScFacilityParam_DocumentDescription` |  |  |  |
| 5 | `SC.FAP.MANDATORY.FLAG` | `ScFacilityParam_MandatoryFlag` |  |  |  |
| 6 | `SC.FAP.LIMIT.REFERENCE` | `ScFacilityParam_LimitReference` | TField |  |  |
| 7 | `SC.FAP.AA.PRODUCT.GROUP` | `ScFacilityParam_AaProductGroup` | TField |  |  |
| 8 | `SC.FAP.DR.TXN.CODE` | `ScFacilityParam_DrTxnCode` | TField |  |  |
| 9 | `SC.FAP.CR.TXN.CODE` | `ScFacilityParam_CrTxnCode` | TField |  |  |
| 10 | `SC.FAP.RESERVED.06` | `ScFacilityParam_Reserved06` | TField |  |  |
| 11 | `SC.FAP.RESERVED.05` | `ScFacilityParam_Reserved05` | TField |  |  |
| 12 | `SC.FAP.RESERVED.04` | `ScFacilityParam_Reserved04` | TField |  |  |
| 13 | `SC.FAP.RESERVED.03` | `ScFacilityParam_Reserved03` | TField |  |  |
| 14 | `SC.FAP.RESERVED.02` | `ScFacilityParam_Reserved02` | TField |  |  |
| 15 | `SC.FAP.RESERVED.01` | `ScFacilityParam_Reserved01` | TField |  |  |
| 16 | `SC.FAP.LOCAL.REF` | `ScFacilityParam_LocalRef` |  |  |  |
| 17 | `SC.FAP.OVERRIDE` | `ScFacilityParam_Override` |  |  |  |
| 18 | `SC.FAP.RECORD.STATUS` | `ScFacilityParam_RecordStatus` | String |  |  |
| 19 | `SC.FAP.CURR.NO` | `ScFacilityParam_CurrNo` | String |  |  |
| 20 | `SC.FAP.INPUTTER` | `ScFacilityParam_Inputter` |  |  |  |
| 21 | `SC.FAP.DATE.TIME` | `ScFacilityParam_DateTime` |  |  |  |
| 22 | `SC.FAP.AUTHORISER` | `ScFacilityParam_Authoriser` | String |  |  |
| 23 | `SC.FAP.CO.CODE` | `ScFacilityParam_CoCode` | String |  |  |
| 24 | `SC.FAP.DEPT.CODE` | `ScFacilityParam_DeptCode` | String |  |  |
| 25 | `SC.FAP.AUDITOR.CODE` | `ScFacilityParam_AuditorCode` | String |  |  |
| 26 | `SC.FAP.AUDIT.DATE.TIME` | `ScFacilityParam_AuditDateTime` | String |  |  |
