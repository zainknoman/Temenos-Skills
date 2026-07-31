# PP.RSCHANNEL.SELECTION — Table Schema

> Source: `INSERTS/I_F.PP.RSCHANNEL.SELECTION` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RSC.TransactionCurrency` | `PpRschannelSelection_Transactioncurrency` |  |  |  |
| 2 | `PP.RSC.DestinationCountry` | `PpRschannelSelection_Destinationcountry` |  |  |  |
| 3 | `PP.RSC.Priority` | `PpRschannelSelection_Priority` |  |  |  |
| 4 | `PP.RSC.Ranking` | `PpRschannelSelection_Ranking` |  |  |  |
| 5 | `PP.RSC.Channel` | `PpRschannelSelection_Channel` |  |  |  |
| 6 | `PP.RSC.LOCAL.REF` | `PpRschannelSelection_LocalRef` |  |  |  |
| 7 | `PP.RSC.RESERVED05` | `PpRschannelSelection_Reserved05` | TField |  |  |
| 8 | `PP.RSC.RESERVED04` | `PpRschannelSelection_Reserved04` | TField |  |  |
| 9 | `PP.RSC.RESERVED03` | `PpRschannelSelection_Reserved03` | TField |  |  |
| 10 | `PP.RSC.RESERVED02` | `PpRschannelSelection_Reserved02` | TField |  |  |
| 11 | `PP.RSC.RESERVED01` | `PpRschannelSelection_Reserved01` | TField |  |  |
| 12 | `PP.RSC.OVERRIDE` | `PpRschannelSelection_Override` |  |  |  |
| 13 | `PP.RSC.RECORD.STATUS` | `PpRschannelSelection_RecordStatus` | String |  |  |
| 14 | `PP.RSC.CURR.NO` | `PpRschannelSelection_CurrNo` | String |  |  |
| 15 | `PP.RSC.INPUTTER` | `PpRschannelSelection_Inputter` |  |  |  |
| 16 | `PP.RSC.DATE.TIME` | `PpRschannelSelection_DateTime` |  |  |  |
| 17 | `PP.RSC.AUTHORISER` | `PpRschannelSelection_Authoriser` | String |  |  |
| 18 | `PP.RSC.CO.CODE` | `PpRschannelSelection_CoCode` | String |  |  |
| 19 | `PP.RSC.DEPT.CODE` | `PpRschannelSelection_DeptCode` | String |  |  |
| 20 | `PP.RSC.AUDITOR.CODE` | `PpRschannelSelection_AuditorCode` | String |  |  |
| 21 | `PP.RSC.AUDIT.DATE.TIME` | `PpRschannelSelection_AuditDateTime` | String |  |  |
