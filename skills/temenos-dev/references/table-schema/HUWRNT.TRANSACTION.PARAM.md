# HUWRNT.TRANSACTION.PARAM — Table Schema

> Source: `INSERTS/I_F.HUWRNT.TRANSACTION.PARAM` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.TXN.PARAM.EXT.TXN.CODE` | `HuwrntTransactionParam_ExtTxnCode` |  |  |  |
| 2 | `HUWRNT.TXN.PARAM.TYPE.CODE` | `HuwrntTransactionParam_TypeCode` |  |  |  |
| 3 | `HUWRNT.TXN.PARAM.EXPIRY.DATE.REQUIRED` | `HuwrntTransactionParam_ExpiryDateRequired` |  |  |  |
| 4 | `HUWRNT.TXN.PARAM.POSTING.RESTRICT.CODES` | `HuwrntTransactionParam_PostingRestrictCodes` |  |  |  |
| 5 | `HUWRNT.TXN.PARAM.RESERVED.13` | `HuwrntTransactionParam_Reserved13` | TField |  | Reserved for Future Use. |
| 6 | `HUWRNT.TXN.PARAM.RESERVED.12` | `HuwrntTransactionParam_Reserved12` | TField |  | Reserved for Future Use. |
| 7 | `HUWRNT.TXN.PARAM.RESERVED.11` | `HuwrntTransactionParam_Reserved11` | TField |  | Reserved for Future Use. |
| 8 | `HUWRNT.TXN.PARAM.RESERVED.10` | `HuwrntTransactionParam_Reserved10` | TField |  | Reserved for Future Use. |
| 9 | `HUWRNT.TXN.PARAM.RESERVED.9` | `HuwrntTransactionParam_Reserved9` | TField |  | Reserved for Future Use. |
| 10 | `HUWRNT.TXN.PARAM.RESERVED.8` | `HuwrntTransactionParam_Reserved8` | TField |  | Reserved for Future Use. |
| 11 | `HUWRNT.TXN.PARAM.RESERVED.7` | `HuwrntTransactionParam_Reserved7` | TField |  | Reserved for Future Use. |
| 12 | `HUWRNT.TXN.PARAM.RESERVED.6` | `HuwrntTransactionParam_Reserved6` | TField |  | Reserved for Future Use. |
| 13 | `HUWRNT.TXN.PARAM.RESERVED.5` | `HuwrntTransactionParam_Reserved5` | TField |  | Reserved for Future Use. |
| 14 | `HUWRNT.TXN.PARAM.RESERVED.4` | `HuwrntTransactionParam_Reserved4` | TField |  | Reserved for Future Use. |
| 15 | `HUWRNT.TXN.PARAM.RESERVED.3` | `HuwrntTransactionParam_Reserved3` | TField |  | Reserved for Future Use. |
| 16 | `HUWRNT.TXN.PARAM.RESERVED.2` | `HuwrntTransactionParam_Reserved2` | TField |  | Reserved for Future Use. |
| 17 | `HUWRNT.TXN.PARAM.RESERVED.1` | `HuwrntTransactionParam_Reserved1` | TField |  | Reserved for Future Use. |
| 18 | `HUWRNT.TXN.PARAM.LOCAL.REF` | `HuwrntTransactionParam_LocalRef` |  |  |  |
| 19 | `HUWRNT.TXN.PARAM.OVERRIDE` | `HuwrntTransactionParam_Override` |  |  |  |
| 20 | `HUWRNT.TXN.PARAM.RECORD.STATUS` | `HuwrntTransactionParam_RecordStatus` | String |  |  |
| 21 | `HUWRNT.TXN.PARAM.CURR.NO` | `HuwrntTransactionParam_CurrNo` | String |  |  |
| 22 | `HUWRNT.TXN.PARAM.INPUTTER` | `HuwrntTransactionParam_Inputter` |  |  |  |
| 23 | `HUWRNT.TXN.PARAM.DATE.TIME` | `HuwrntTransactionParam_DateTime` |  |  |  |
| 24 | `HUWRNT.TXN.PARAM.AUTHORISER` | `HuwrntTransactionParam_Authoriser` | String |  |  |
| 25 | `HUWRNT.TXN.PARAM.CO.CODE` | `HuwrntTransactionParam_CoCode` | String |  |  |
| 26 | `HUWRNT.TXN.PARAM.DEPT.CODE` | `HuwrntTransactionParam_DeptCode` | String |  |  |
| 27 | `HUWRNT.TXN.PARAM.AUDITOR.CODE` | `HuwrntTransactionParam_AuditorCode` | String |  |  |
| 28 | `HUWRNT.TXN.PARAM.AUDIT.DATE.TIME` | `HuwrntTransactionParam_AuditDateTime` | String |  |  |
