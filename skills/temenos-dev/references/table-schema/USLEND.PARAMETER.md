# USLEND.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USLEND.PARAMETER` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLEND.PARAM.CURRENCY` | `UslendParameter_Currency` |  |  |  |
| 2 | `USLEND.PARAM.SURP.THRESHOLD.AMT` | `UslendParameter_SurpThresholdAmt` |  |  |  |
| 3 | `USLEND.PARAM.SURPLUS.OPTION` | `UslendParameter_SurplusOption` |  |  |  |
| 4 | `USLEND.PARAM.SHORTAGE.OPTION` | `UslendParameter_ShortageOption` |  |  |  |
| 5 | `USLEND.PARAM.TEST.ANALYSIS.PERIOD` | `UslendParameter_TestAnalysisPeriod` |  |  |  |
| 6 | `USLEND.PARAM.PAYMENT.EFF.PERIOD` | `UslendParameter_PaymentEffPeriod` |  |  |  |
| 7 | `USLEND.PARAM.SHORT.THRESHOLD.AMT` | `UslendParameter_ShortThresholdAmt` |  |  |  |
| 8 | `USLEND.PARAM.SHORT.BEYOND.THRES` | `UslendParameter_ShortBeyondThres` |  |  |  |
| 9 | `USLEND.PARAM.RESERVED.23` | `UslendParameter_Reserved23` |  |  |  |
| 10 | `USLEND.PARAM.OUTPUT.FORMAT` | `UslendParameter_OutputFormat` | TField |  |  |
| 11 | `USLEND.PARAM.DISBURSE.PROPERTIES` | `UslendParameter_DisburseProperties` |  |  |  |
| 12 | `USLEND.PARAM.ESCROW.BILL.TYPE` | `UslendParameter_EscrowBillType` |  |  |  |
| 13 | `USLEND.PARAM.ADHOC.ESCROW.PROP` | `UslendParameter_AdhocEscrowProp` |  |  |  |
| 14 | `USLEND.PARAM.OVERDRAW` | `UslendParameter_Overdraw` | TField |  |  |
| 15 | `USLEND.PARAM.ESCROW.SHORT.PROP` | `UslendParameter_EscrowShortProp` | TField |  |  |
| 16 | `USLEND.PARAM.ESCROW.OVER.PROP` | `UslendParameter_EscrowOverProp` | TField |  |  |
| 17 | `USLEND.PARAM.RESERVED.15` | `UslendParameter_Reserved15` | TField |  | Reserve Fields |
| 18 | `USLEND.PARAM.RESERVED.14` | `UslendParameter_Reserved14` | TField |  | Reserve Fields |
| 19 | `USLEND.PARAM.RESERVED.13` | `UslendParameter_Reserved13` | TField |  | Reserve Fields |
| 20 | `USLEND.PARAM.RESERVED.12` | `UslendParameter_Reserved12` | TField |  | Reserve Fields |
| 21 | `USLEND.PARAM.RESERVED.11` | `UslendParameter_Reserved11` | TField |  | Reserve Fields |
| 22 | `USLEND.PARAM.RESERVED.10` | `UslendParameter_Reserved10` | TField |  | Reserve Fields |
| 23 | `USLEND.PARAM.RESERVED.9` | `UslendParameter_Reserved9` | TField |  | Reserve Fields |
| 24 | `USLEND.PARAM.RESERVED.8` | `UslendParameter_Reserved8` | TField |  | Reserve Fields |
| 25 | `USLEND.PARAM.RESERVED.7` | `UslendParameter_Reserved7` | TField |  | Reserve Fields |
| 26 | `USLEND.PARAM.RESERVED.6` | `UslendParameter_Reserved6` | TField |  | Reserve Fields |
| 27 | `USLEND.PARAM.RESERVED.5` | `UslendParameter_Reserved5` | TField |  | Reserve Fields |
| 28 | `USLEND.PARAM.RESERVED.4` | `UslendParameter_Reserved4` | TField |  | Reserve Fields |
| 29 | `USLEND.PARAM.RESERVED.3` | `UslendParameter_Reserved3` | TField |  | Reserve Fields |
| 30 | `USLEND.PARAM.RESERVED.2` | `UslendParameter_Reserved2` | TField |  | Reserve Fields |
| 31 | `USLEND.PARAM.DESCRIPTION` | `UslendParameter_Description` |  |  |  |
| 32 | `USLEND.PARAM.LOCAL.REF` | `UslendParameter_LocalRef` |  |  |  |
| 33 | `USLEND.PARAM.RECORD.STATUS` | `UslendParameter_RecordStatus` | String |  |  |
| 34 | `USLEND.PARAM.CURR.NO` | `UslendParameter_CurrNo` | String |  |  |
| 35 | `USLEND.PARAM.INPUTTER` | `UslendParameter_Inputter` |  |  |  |
| 36 | `USLEND.PARAM.DATE.TIME` | `UslendParameter_DateTime` |  |  |  |
| 37 | `USLEND.PARAM.AUTHORISER` | `UslendParameter_Authoriser` | String |  |  |
| 38 | `USLEND.PARAM.CO.CODE` | `UslendParameter_CoCode` | String |  |  |
| 39 | `USLEND.PARAM.DEPT.CODE` | `UslendParameter_DeptCode` | String |  |  |
| 40 | `USLEND.PARAM.AUDITOR.CODE` | `UslendParameter_AuditorCode` | String |  |  |
| 41 | `USLEND.PARAM.AUDIT.DATE.TIME` | `UslendParameter_AuditDateTime` | String |  |  |
