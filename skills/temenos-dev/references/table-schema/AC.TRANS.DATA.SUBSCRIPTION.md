# AC.TRANS.DATA.SUBSCRIPTION — Table Schema

> Source: `INSERTS/I_F.AC.TRANS.DATA.SUBSCRIPTION` in `AC_TransactionData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.TDS.SUB.DESCRIPTION` | `AcTransDataSubscription_SubDescription` |  |  |  |
| 2 | `AC.TDS.SUB.ACTIVE` | `AcTransDataSubscription_SubActive` | TField |  |  |
| 3 | `AC.TDS.CACHE.BUCKET` | `AcTransDataSubscription_CacheBucket` | TField |  |  |
| 4 | `AC.TDS.SUB.APPLICATION` | `AcTransDataSubscription_SubApplication` |  |  |  |
| 5 | `AC.TDS.SUB.APP.ACTIVE` | `AcTransDataSubscription_SubAppActive` |  |  |  |
| 6 | `AC.TDS.SUB.STAGE` | `AcTransDataSubscription_SubStage` |  |  |  |
| 7 | `AC.TDS.SUB.COMPANY` | `AcTransDataSubscription_SubCompany` |  |  |  |
| 8 | `AC.TDS.OUTPUT.LOCATION` | `AcTransDataSubscription_OutputLocation` | TField |  |  |
| 9 | `AC.TDS.CONSUMER.SERVICE` | `AcTransDataSubscription_ConsumerService` | TField |  |  |
| 10 | `AC.TDS.LOCAL.REF` | `AcTransDataSubscription_LocalRef` |  |  |  |
| 11 | `AC.TDS.OVERRIDE` | `AcTransDataSubscription_Override` |  |  |  |
| 12 | `AC.TDS.RECORD.STATUS` | `AcTransDataSubscription_RecordStatus` | String |  |  |
| 13 | `AC.TDS.CURR.NO` | `AcTransDataSubscription_CurrNo` | String |  |  |
| 14 | `AC.TDS.INPUTTER` | `AcTransDataSubscription_Inputter` |  |  |  |
| 15 | `AC.TDS.DATE.TIME` | `AcTransDataSubscription_DateTime` |  |  |  |
| 16 | `AC.TDS.AUTHORISER` | `AcTransDataSubscription_Authoriser` | String |  |  |
| 17 | `AC.TDS.CO.CODE` | `AcTransDataSubscription_CoCode` | String |  |  |
| 18 | `AC.TDS.DEPT.CODE` | `AcTransDataSubscription_DeptCode` | String |  |  |
| 19 | `AC.TDS.AUDITOR.CODE` | `AcTransDataSubscription_AuditorCode` | String |  |  |
| 20 | `AC.TDS.AUDIT.DATE.TIME` | `AcTransDataSubscription_AuditDateTime` | String |  |  |
