# ARTAXS.STANDARD.PRODUCT.PARAM — Table Schema

> Source: `INSERTS/I_F.ARTAXS.STANDARD.PRODUCT.PARAM` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRODUCT.PARAM.BANK.PRODUCT` | `ArtaxsStandardProductParam_BankProduct` |  |  |  |
| 2 | `PRODUCT.PARAM.STANDARD.PRODUCT` | `ArtaxsStandardProductParam_StandardProduct` |  |  |  |
| 3 | `PRODUCT.PARAM.RESERVED.15` | `ArtaxsStandardProductParam_Reserved15` | TField |  | Field reserved for future use. |
| 4 | `PRODUCT.PARAM.RESERVED.14` | `ArtaxsStandardProductParam_Reserved14` | TField |  | Field reserved for future use. |
| 5 | `PRODUCT.PARAM.RESERVED.13` | `ArtaxsStandardProductParam_Reserved13` | TField |  | Field reserved for future use. |
| 6 | `PRODUCT.PARAM.RESERVED.12` | `ArtaxsStandardProductParam_Reserved12` | TField |  | Field reserved for future use. |
| 7 | `PRODUCT.PARAM.RESERVED.11` | `ArtaxsStandardProductParam_Reserved11` | TField |  | Field reserved for future use. |
| 8 | `PRODUCT.PARAM.RESERVED.10` | `ArtaxsStandardProductParam_Reserved10` | TField |  | Field reserved for future use. |
| 9 | `PRODUCT.PARAM.RESERVED.9` | `ArtaxsStandardProductParam_Reserved9` | TField |  | Field reserved for future use. |
| 10 | `PRODUCT.PARAM.RESERVED.8` | `ArtaxsStandardProductParam_Reserved8` | TField |  | Field reserved for future use. |
| 11 | `PRODUCT.PARAM.RESERVED.7` | `ArtaxsStandardProductParam_Reserved7` | TField |  | Field reserved for future use. |
| 12 | `PRODUCT.PARAM.RESERVED.6` | `ArtaxsStandardProductParam_Reserved6` | TField |  | Field reserved for future use. |
| 13 | `PRODUCT.PARAM.RESERVED.5` | `ArtaxsStandardProductParam_Reserved5` | TField |  | Field reserved for future use. |
| 14 | `PRODUCT.PARAM.RESERVED.4` | `ArtaxsStandardProductParam_Reserved4` | TField |  | Field reserved for future use. |
| 15 | `PRODUCT.PARAM.RESERVED.3` | `ArtaxsStandardProductParam_Reserved3` | TField |  | Field reserved for future use. |
| 16 | `PRODUCT.PARAM.RESERVED.2` | `ArtaxsStandardProductParam_Reserved2` | TField |  | Field reserved for future use. |
| 17 | `PRODUCT.PARAM.RESERVED.1` | `ArtaxsStandardProductParam_Reserved1` | TField |  | Field reserved for future use. |
| 18 | `PRODUCT.PARAM.LOCAL.REF` | `ArtaxsStandardProductParam_LocalRef` |  |  |  |
| 19 | `PRODUCT.PARAM.OVERRIDE` | `ArtaxsStandardProductParam_Override` |  |  |  |
| 20 | `PRODUCT.PARAM.RECORD.STATUS` | `ArtaxsStandardProductParam_RecordStatus` | String |  |  |
| 21 | `PRODUCT.PARAM.CURR.NO` | `ArtaxsStandardProductParam_CurrNo` | String |  |  |
| 22 | `PRODUCT.PARAM.INPUTTER` | `ArtaxsStandardProductParam_Inputter` |  |  |  |
| 23 | `PRODUCT.PARAM.DATE.TIME` | `ArtaxsStandardProductParam_DateTime` |  |  |  |
| 24 | `PRODUCT.PARAM.AUTHORISER` | `ArtaxsStandardProductParam_Authoriser` | String |  |  |
| 25 | `PRODUCT.PARAM.CO.CODE` | `ArtaxsStandardProductParam_CoCode` | String |  |  |
| 26 | `PRODUCT.PARAM.DEPT.CODE` | `ArtaxsStandardProductParam_DeptCode` | String |  |  |
| 27 | `PRODUCT.PARAM.AUDITOR.CODE` | `ArtaxsStandardProductParam_AuditorCode` | String |  |  |
| 28 | `PRODUCT.PARAM.AUDIT.DATE.TIME` | `ArtaxsStandardProductParam_AuditDateTime` | String |  |  |
