# SC.GENERATE.INST — Table Schema

> Source: `INSERTS/I_F.SC.GENERATE.INST` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.GEN.TRADE.ID` | `ScGenerateInst_TradeId` |  |  |  |
| 2 | `SC.GEN.CU.DELIV.KEY` | `ScGenerateInst_CuDelivKey` |  |  |  |
| 3 | `SC.GEN.BR.DELIV.KEY` | `ScGenerateInst_BrDelivKey` |  |  |  |
| 4 | `SC.GEN.DEP.DELIV.KEY` | `ScGenerateInst_DepDelivKey` |  |  |  |
| 5 | `SC.GEN.CU.ADVICE.REQD` | `ScGenerateInst_CuAdviceReqd` | TField |  | Flag for customer advice, Yes for advice required. |
| 6 | `SC.GEN.BROKER.ADVICE.REQD` | `ScGenerateInst_BrokerAdviceReqd` | TField |  | This field specifies whether a broker advice is to be sent. Validation Rules: YES/NO |
| 7 | `SC.GEN.DEPOT.ADVICE.REQD` | `ScGenerateInst_DepotAdviceReqd` | TField |  | This field specifies whether a depository advice is to be produced. Validation Rules: YES/NO |
| 8 | `SC.GEN.RESERVED.3` | `ScGenerateInst_Reserved3` | TField |  |  |
| 9 | `SC.GEN.RESERVED.2` | `ScGenerateInst_Reserved2` | TField |  |  |
| 10 | `SC.GEN.RESERVED.1` | `ScGenerateInst_Reserved1` | TField |  |  |
| 11 | `SC.GEN.LOCAL.REF` | `ScGenerateInst_LocalRef` |  |  |  |
| 12 | `SC.GEN.OVERRIDE` | `ScGenerateInst_Override` |  |  |  |
| 13 | `SC.GEN.RECORD.STATUS` | `ScGenerateInst_RecordStatus` | String |  |  |
| 14 | `SC.GEN.CURR.NO` | `ScGenerateInst_CurrNo` | String |  |  |
| 15 | `SC.GEN.INPUTTER` | `ScGenerateInst_Inputter` |  |  |  |
| 16 | `SC.GEN.DATE.TIME` | `ScGenerateInst_DateTime` |  |  |  |
| 17 | `SC.GEN.AUTHORISER` | `ScGenerateInst_Authoriser` | String |  |  |
| 18 | `SC.GEN.CO.CODE` | `ScGenerateInst_CoCode` | String |  |  |
| 19 | `SC.GEN.DEPT.CODE` | `ScGenerateInst_DeptCode` | String |  |  |
| 20 | `SC.GEN.AUDITOR.CODE` | `ScGenerateInst_AuditorCode` | String |  |  |
| 21 | `SC.GEN.AUDIT.DATE.TIME` | `ScGenerateInst_AuditDateTime` | String |  |  |
