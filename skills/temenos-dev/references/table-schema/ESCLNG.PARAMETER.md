# ESCLNG.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESCLNG.PARAMETER` in `ESCLNG_MiscellaneousPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.SNCE.CT.NO.OF.DAYS` | `EsclngParameter_CtNoOfDays` | TField |  | Number of days are calculated for SLA period based on CT NO OF DAYS |
| 2 | `ES.SNCE.DD.NO.OF.DAYS` | `EsclngParameter_DdNoOfDays` | TField |  | Number of days are calculated for SLA period based on DD NO OF DAYS |
| 3 | `ES.SNCE.LOCAL.REF` | `EsclngParameter_LocalRef` |  |  |  |
| 4 | `ES.SNCE.SNCE07.NRBE.GRP.CODE` | `EsclngParameter_Snce07NrbeGrpCode` |  |  |  |
| 5 | `ES.SNCE.GRP.CODE.DESC` | `EsclngParameter_GrpCodeDesc` |  |  |  |
| 6 | `ES.SNCE.SNCE07VAT.TYPE` | `EsclngParameter_Snce07vatType` |  |  |  |
| 7 | `ES.SNCE.SNCE07.VAT.PERCENTAGE` | `EsclngParameter_Snce07VatPercentage` |  |  |  |
| 8 | `ES.SNCE.SNCE07.PRO.RATE.PERCENTAGE` | `EsclngParameter_Snce07ProRatePercentage` |  |  |  |
| 9 | `ES.SNCE.NRPY.CLAIMS.PL` | `EsclngParameter_NrpyClaimsPl` | TField |  | Holds the NRPY CLAIMS PL |
| 10 | `ES.SNCE.INTERNAL.CASH.ACCOUNT` | `EsclngParameter_InternalCashAccount` | TField |  | Holds the Internal Account |
| 11 | `ES.SNCE.TRANSACTION.TYPE` | `EsclngParameter_TransactionType` |  |  |  |
| 12 | `ES.SNCE.INCOMING.SLA` | `EsclngParameter_IncomingSla` |  |  |  |
| 13 | `ES.SNCE.OUTGOING.SLA` | `EsclngParameter_OutgoingSla` |  |  |  |
| 14 | `ES.SNCE.INEM.UNPAID.GENERATION.DAY` | `EsclngParameter_InemUnpaidGenerationDay` | TField |  | Unpaid generation day for INEM |
| 15 | `ES.SNCE.IMSERSO.UNPAID.GENERATION.DAY` | `EsclngParameter_ImsersoUnpaidGenerationDay` | TField |  | Unpaid generation day for IMSERSO |
| 16 | `ES.SNCE.RESERVED.13` | `EsclngParameter_Reserved13` | TField |  |  |
| 17 | `ES.SNCE.RESERVED.14` | `EsclngParameter_Reserved14` | TField |  |  |
| 18 | `ES.SNCE.RESERVED.15` | `EsclngParameter_Reserved15` | TField |  |  |
| 19 | `ES.SNCE.OVERRIDE` | `EsclngParameter_Override` |  |  |  |
| 20 | `ES.SNCE.RECORD.STATUS` | `EsclngParameter_RecordStatus` | String |  |  |
| 21 | `ES.SNCE.CURR.NO` | `EsclngParameter_CurrNo` | String |  |  |
| 22 | `ES.SNCE.INPUTTER` | `EsclngParameter_Inputter` |  |  |  |
| 23 | `ES.SNCE.DATE.TIME` | `EsclngParameter_DateTime` |  |  |  |
| 24 | `ES.SNCE.AUTHORISER` | `EsclngParameter_Authoriser` | String |  |  |
| 25 | `ES.SNCE.CO.CODE` | `EsclngParameter_CoCode` | String |  |  |
| 26 | `ES.SNCE.DEPT.CODE` | `EsclngParameter_DeptCode` | String |  |  |
| 27 | `ES.SNCE.AUDITOR.CODE` | `EsclngParameter_AuditorCode` | String |  |  |
| 28 | `ES.SNCE.AUDIT.DATE.TIME` | `EsclngParameter_AuditDateTime` | String |  |  |
| 29 | `ES.SNCE.RETURN.SLA` | `EsclngParameter_ReturnSla` |  |  |  |
