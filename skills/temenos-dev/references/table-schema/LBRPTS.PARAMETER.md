# LBRPTS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LBRPTS.PARAMETER` in `LBRPTS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBRPTS.PARAM.TAX.TYPE` | `LbrptsParameter_TaxType` |  |  |  |
| 2 | `LBRPTS.PARAM.TAX.DEBIT.CATEGORY` | `LbrptsParameter_TaxDebitCategory` |  |  |  |
| 3 | `LBRPTS.PARAM.TAX.CREDIT.CATEGORY` | `LbrptsParameter_TaxCreditCategory` |  |  |  |
| 4 | `LBRPTS.PARAM.TAX.PAY.TYPE` | `LbrptsParameter_TaxPayType` |  |  |  |
| 5 | `LBRPTS.PARAM.TAX.TELLER.TRAN.CO` | `LbrptsParameter_TaxTellerTranCo` |  |  |  |
| 6 | `LBRPTS.PARAM.TAX.LIMIT.AMT` | `LbrptsParameter_TaxLimitAmt` |  |  |  |
| 7 | `LBRPTS.PARAM.STAMP.CATEG.CODE` | `LbrptsParameter_StampCategCode` |  |  |  |
| 8 | `LBRPTS.PARAM.STAMP.PL.CATEG.CODE` | `LbrptsParameter_StampPlCategCode` | TField |  | PL Category code which corresponds to the account which is used in the stamps transaction |
| 9 | `LBRPTS.PARAM.RESERVED10` | `LbrptsParameter_Reserved10` | TField |  |  |
| 10 | `LBRPTS.PARAM.RESERVED9` | `LbrptsParameter_Reserved9` | TField |  |  |
| 11 | `LBRPTS.PARAM.RESERVED8` | `LbrptsParameter_Reserved8` | TField |  |  |
| 12 | `LBRPTS.PARAM.RESERVED7` | `LbrptsParameter_Reserved7` | TField |  |  |
| 13 | `LBRPTS.PARAM.RESERVED6` | `LbrptsParameter_Reserved6` | TField |  |  |
| 14 | `LBRPTS.PARAM.RESERVED5` | `LbrptsParameter_Reserved5` | TField |  |  |
| 15 | `LBRPTS.PARAM.RESERVED4` | `LbrptsParameter_Reserved4` | TField |  |  |
| 16 | `LBRPTS.PARAM.RESERVED3` | `LbrptsParameter_Reserved3` | TField |  |  |
| 17 | `LBRPTS.PARAM.RESERVED2` | `LbrptsParameter_Reserved2` | TField |  |  |
| 18 | `LBRPTS.PARAM.RESERVED1` | `LbrptsParameter_Reserved1` | TField |  |  |
| 19 | `LBRPTS.PARAM.LOCAL.REF` | `LbrptsParameter_LocalRef` |  |  |  |
| 20 | `LBRPTS.PARAM.OVERRIDE` | `LbrptsParameter_Override` |  |  |  |
| 21 | `LBRPTS.PARAM.RECORD.STATUS` | `LbrptsParameter_RecordStatus` | String |  | Indicates the record status |
| 22 | `LBRPTS.PARAM.CURR.NO` | `LbrptsParameter_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 23 | `LBRPTS.PARAM.INPUTTER` | `LbrptsParameter_Inputter` |  |  |  |
| 24 | `LBRPTS.PARAM.DATE.TIME` | `LbrptsParameter_DateTime` |  |  |  |
| 25 | `LBRPTS.PARAM.AUTHORISER` | `LbrptsParameter_Authoriser` | String |  |  |
| 26 | `LBRPTS.PARAM.CO.CODE` | `LbrptsParameter_CoCode` | String |  |  |
| 27 | `LBRPTS.PARAM.DEPT.CODE` | `LbrptsParameter_DeptCode` | String |  |  |
| 28 | `LBRPTS.PARAM.AUDITOR.CODE` | `LbrptsParameter_AuditorCode` | String |  |  |
| 29 | `LBRPTS.PARAM.AUDIT.DATE.TIME` | `LbrptsParameter_AuditDateTime` | String |  |  |
