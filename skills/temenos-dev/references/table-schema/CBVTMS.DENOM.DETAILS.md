# CBVTMS.DENOM.DETAILS — Table Schema

> Source: `INSERTS/I_F.CBVTMS.DENOM.DETAILS` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.REQUEST.ID` | `CbvtmsDenomDetails_RequestId` | TField |  | Request Id for reference |
| 2 | `VTMS.TXN.DATE` | `CbvtmsDenomDetails_TxnDate` | TField |  | Teller Transaction date |
| 3 | `VTMS.DEBIT.ACCOUNT` | `CbvtmsDenomDetails_DebitAccount` | TField |  | Debit Account |
| 4 | `VTMS.CREDIT.ACCOUNT` | `CbvtmsDenomDetails_CreditAccount` | TField |  | Credit Account |
| 5 | `VTMS.DENOM.TYPE` | `CbvtmsDenomDetails_DenomType` |  |  |  |
| 6 | `VTMS.RESERVED.12` | `CbvtmsDenomDetails_Reserved12` |  |  |  |
| 7 | `VTMS.RESERVED.11` | `CbvtmsDenomDetails_Reserved11` |  |  |  |
| 8 | `VTMS.RESERVED.10` | `CbvtmsDenomDetails_Reserved10` |  |  |  |
| 9 | `VTMS.RESERVED.9` | `CbvtmsDenomDetails_Reserved9` |  |  |  |
| 10 | `VTMS.UNIT` | `CbvtmsDenomDetails_Unit` |  |  |  |
| 11 | `VTMS.TELLER.ID.1` | `CbvtmsDenomDetails_TellerId1` | TField |  |  |
| 12 | `VTMS.TELLER.ID.2` | `CbvtmsDenomDetails_TellerId2` | TField |  |  |
| 13 | `VTMS.RESERVED.6` | `CbvtmsDenomDetails_Reserved6` | TField |  | Reserved field for future use |
| 14 | `VTMS.RESERVED.5` | `CbvtmsDenomDetails_Reserved5` | TField |  | Reserved field for future use |
| 15 | `VTMS.RESERVED.4` | `CbvtmsDenomDetails_Reserved4` | TField |  | Reserved field for future use |
| 16 | `VTMS.RESERVED.3` | `CbvtmsDenomDetails_Reserved3` | TField |  | Reserved field for future use |
| 17 | `VTMS.RESERVED.2` | `CbvtmsDenomDetails_Reserved2` | TField |  | Reserved field for future use |
| 18 | `VTMS.RESERVED.1` | `CbvtmsDenomDetails_Reserved1` | TField |  | Reserved field for future use |
| 19 | `VTMS.RECORD.STATUS` | `CbvtmsDenomDetails_RecordStatus` | String |  |  |
| 20 | `VTMS.CURR.NO` | `CbvtmsDenomDetails_CurrNo` | String |  |  |
| 21 | `VTMS.INPUTTER` | `CbvtmsDenomDetails_Inputter` |  |  |  |
| 22 | `VTMS.DATE.TIME` | `CbvtmsDenomDetails_DateTime` |  |  |  |
| 23 | `VTMS.AUTHORISER` | `CbvtmsDenomDetails_Authoriser` | String |  |  |
| 24 | `VTMS.CO.CODE` | `CbvtmsDenomDetails_CoCode` | String |  |  |
| 25 | `VTMS.DEPT.CODE` | `CbvtmsDenomDetails_DeptCode` | String |  |  |
| 26 | `VTMS.AUDITOR.CODE` | `CbvtmsDenomDetails_AuditorCode` | String |  |  |
| 27 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsDenomDetails_AuditDateTime` | String |  |  |
