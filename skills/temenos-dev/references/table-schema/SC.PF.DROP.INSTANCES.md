# SC.PF.DROP.INSTANCES — Table Schema

> Source: `INSERTS/I_F.SC.PF.DROP.INSTANCES` in `SC_Mifid.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PFDROP.PORTFOLIO.NO` | `ScPfDropInstances_PortfolioNo` | TField |  |  |
| 2 | `SC.PFDROP.CURRENCY` | `ScPfDropInstances_Currency` | TField |  |  |
| 3 | `SC.PFDROP.REPORTING.PRD.ST.DATE` | `ScPfDropInstances_ReportingPrdStDate` |  |  |  |
| 4 | `SC.PFDROP.REPORTING.PRD.END.DATE` | `ScPfDropInstances_ReportingPrdEndDate` |  |  |  |
| 5 | `SC.PFDROP.DROP.DATE` | `ScPfDropInstances_DropDate` |  |  |  |
| 6 | `SC.PFDROP.DROP.PCT.RECORDED` | `ScPfDropInstances_DropPctRecorded` |  |  |  |
| 7 | `SC.PFDROP.PF.VALUE` | `ScPfDropInstances_PfValue` |  |  |  |
| 8 | `SC.PFDROP.REJECT` | `ScPfDropInstances_Reject` |  |  |  |
| 9 | `SC.PFDROP.RESERVED1` | `ScPfDropInstances_Reserved1` | TField |  |  |
| 10 | `SC.PFDROP.RESERVED2` | `ScPfDropInstances_Reserved2` | TField |  |  |
| 11 | `SC.PFDROP.RESERVED3` | `ScPfDropInstances_Reserved3` | TField |  |  |
| 12 | `SC.PFDROP.RESERVED4` | `ScPfDropInstances_Reserved4` | TField |  |  |
| 13 | `SC.PFDROP.RESERVED5` | `ScPfDropInstances_Reserved5` | TField |  |  |
| 14 | `SC.PFDROP.RESERVED6` | `ScPfDropInstances_Reserved6` | TField |  |  |
| 15 | `SC.PFDROP.RESERVED7` | `ScPfDropInstances_Reserved7` | TField |  |  |
| 16 | `SC.PFDROP.RESERVED8` | `ScPfDropInstances_Reserved8` | TField |  |  |
| 17 | `SC.PFDROP.RESERVED9` | `ScPfDropInstances_Reserved9` | TField |  |  |
| 18 | `SC.PFDROP.RESERVED10` | `ScPfDropInstances_Reserved10` | TField |  |  |
| 19 | `SC.PFDROP.RESERVED11` | `ScPfDropInstances_Reserved11` | TField |  |  |
| 20 | `SC.PFDROP.RESERVED12` | `ScPfDropInstances_Reserved12` | TField |  |  |
| 21 | `SC.PFDROP.RESERVED13` | `ScPfDropInstances_Reserved13` | TField |  |  |
| 22 | `SC.PFDROP.RESERVED14` | `ScPfDropInstances_Reserved14` | TField |  |  |
| 23 | `SC.PFDROP.RESERVED15` | `ScPfDropInstances_Reserved15` | TField |  |  |
| 24 | `SC.PFDROP.RESERVED16` | `ScPfDropInstances_Reserved16` | TField |  |  |
| 25 | `SC.PFDROP.RESERVED17` | `ScPfDropInstances_Reserved17` | TField |  |  |
| 26 | `SC.PFDROP.RESERVED18` | `ScPfDropInstances_Reserved18` | TField |  |  |
| 27 | `SC.PFDROP.RESERVED19` | `ScPfDropInstances_Reserved19` | TField |  |  |
| 28 | `SC.PFDROP.RESERVED20` | `ScPfDropInstances_Reserved20` | TField |  |  |
| 29 | `SC.PFDROP.LOCAL.REF` | `ScPfDropInstances_LocalRef` |  |  |  |
| 30 | `SC.PFDROP.OVERRIDE` | `ScPfDropInstances_Override` |  |  |  |
| 31 | `SC.PFDROP.RECORD.STATUS` | `ScPfDropInstances_RecordStatus` | String |  |  |
| 32 | `SC.PFDROP.CURR.NO` | `ScPfDropInstances_CurrNo` | String |  |  |
| 33 | `SC.PFDROP.INPUTTER` | `ScPfDropInstances_Inputter` |  |  |  |
| 34 | `SC.PFDROP.DATE.TIME` | `ScPfDropInstances_DateTime` |  |  |  |
| 35 | `SC.PFDROP.AUTHORISER` | `ScPfDropInstances_Authoriser` | String |  |  |
| 36 | `SC.PFDROP.CO.CODE` | `ScPfDropInstances_CoCode` | String |  |  |
| 37 | `SC.PFDROP.DEPT.CODE` | `ScPfDropInstances_DeptCode` | String |  |  |
| 38 | `SC.PFDROP.AUDITOR.CODE` | `ScPfDropInstances_AuditorCode` | String |  |  |
| 39 | `SC.PFDROP.AUDIT.DATE.TIME` | `ScPfDropInstances_AuditDateTime` | String |  |  |
