# CBCRRT.CRR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CBCRRT.CRR.PARAMETER` in `CBCRRT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBCRRT.CURRENCY` | `CbcrrtCrrParameter_Currency` |  |  |  |
| 2 | `CBCRRT.NON.TERM.DEPOSIT.RATE` | `CbcrrtCrrParameter_NonTermDepositRate` |  |  |  |
| 3 | `CBCRRT.TERM.DEPOSIT.RATE` | `CbcrrtCrrParameter_TermDepositRate` |  |  |  |
| 4 | `CBCRRT.OVERSEAS.DEPOSIT.RATE` | `CbcrrtCrrParameter_OverseasDepositRate` |  |  |  |
| 5 | `CBCRRT.CRR.PRODUCT.GROUP` | `CbcrrtCrrParameter_CrrProductGroup` |  |  |  |
| 6 | `CBCRRT.CRR.PRODUCT` | `CbcrrtCrrParameter_CrrProduct` |  |  |  |
| 7 | `CBCRRT.CRR.INTEREST.PROPERTY` | `CbcrrtCrrParameter_CrrInterestProperty` |  |  |  |
| 8 | `CBCRRT.RESERVED.1` | `CbcrrtCrrParameter_Reserved1` | TField |  | This field is reserved for future use |
| 9 | `CBCRRT.RESERVED.2` | `CbcrrtCrrParameter_Reserved2` | TField |  | This field is reserved for future use |
| 10 | `CBCRRT.RESERVED.3` | `CbcrrtCrrParameter_Reserved3` | TField |  | This field is reserved for future use |
| 11 | `CBCRRT.RESERVED.4` | `CbcrrtCrrParameter_Reserved4` | TField |  | This field is reserved for future use |
| 12 | `CBCRRT.RESERVED.5` | `CbcrrtCrrParameter_Reserved5` | TField |  | This field is reserved for future use |
| 13 | `CBCRRT.LOCAL.REF` | `CbcrrtCrrParameter_LocalRef` |  |  |  |
| 14 | `CBCRRT.OVERRIDE` | `CbcrrtCrrParameter_Override` |  |  |  |
| 15 | `CBCRRT.RECORD.STATUS` | `CbcrrtCrrParameter_RecordStatus` | String |  |  |
| 16 | `CBCRRT.CURR.NO` | `CbcrrtCrrParameter_CurrNo` | String |  |  |
| 17 | `CBCRRT.INPUTTER` | `CbcrrtCrrParameter_Inputter` |  |  |  |
| 18 | `CBCRRT.DATE.TIME` | `CbcrrtCrrParameter_DateTime` |  |  |  |
| 19 | `CBCRRT.AUTHORISER` | `CbcrrtCrrParameter_Authoriser` | String |  |  |
| 20 | `CBCRRT.CO.CODE` | `CbcrrtCrrParameter_CoCode` | String |  |  |
| 21 | `CBCRRT.DEPT.CODE` | `CbcrrtCrrParameter_DeptCode` | String |  |  |
| 22 | `CBCRRT.AUDITOR.CODE` | `CbcrrtCrrParameter_AuditorCode` | String |  |  |
| 23 | `CBCRRT.AUDIT.DATE.TIME` | `CbcrrtCrrParameter_AuditDateTime` | String |  |  |
