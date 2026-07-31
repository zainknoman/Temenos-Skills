# AFRBOP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AFRBOP.PARAMETER` in `AFRBOP_BalanceOfPayment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRBOP.PARAM.BANK.CODE` | `AfrbopParameter_BankCode` | TField |  | This field holds the Bank code |
| 2 | `AFRBOP.PARAM.CUSTOMER.TYPE` | `AfrbopParameter_CustomerType` |  |  |  |
| 3 | `AFRBOP.PARAM.START.RANGE.SECTOR` | `AfrbopParameter_StartRangeSector` |  |  |  |
| 4 | `AFRBOP.PARAM.END.RANGE.SECTOR` | `AfrbopParameter_EndRangeSector` |  |  |  |
| 5 | `AFRBOP.PARAM.OPER.CODE` | `AfrbopParameter_OperCode` |  |  |  |
| 6 | `AFRBOP.PARAM.TRANSACTION.CODE` | `AfrbopParameter_TransactionCode` |  |  |  |
| 7 | `AFRBOP.PARAM.FILE.TYPE` | `AfrbopParameter_FileType` |  |  |  |
| 8 | `AFRBOP.PARAM.APPLICATION` | `AfrbopParameter_Application` |  |  |  |
| 9 | `AFRBOP.PARAM.MANDATORY.FIELDS` | `AfrbopParameter_MandatoryFields` |  |  |  |
| 10 | `AFRBOP.PARAM.CUSTOMER.CLASS` | `AfrbopParameter_CustomerClass` |  |  |  |
| 11 | `AFRBOP.PARAM.CUSTOMER.STATUS` | `AfrbopParameter_CustomerStatus` |  |  |  |
| 12 | `AFRBOP.PARAM.LOCAL.REF` | `AfrbopParameter_LocalRef` |  |  |  |
| 13 | `AFRBOP.PARAM.RESERVED.5` | `AfrbopParameter_Reserved5` | TField |  | This field is reserved for future use |
| 14 | `AFRBOP.PARAM.RESERVED.4` | `AfrbopParameter_Reserved4` | TField |  | This field is reserved for future use |
| 15 | `AFRBOP.PARAM.RESERVED.3` | `AfrbopParameter_Reserved3` | TField |  | This field is reserved for future use |
| 16 | `AFRBOP.PARAM.RESERVED.2` | `AfrbopParameter_Reserved2` | TField |  | This field is reserved for future use |
| 17 | `AFRBOP.PARAM.RESERVED.1` | `AfrbopParameter_Reserved1` | TField |  | This field is reserved for future use |
| 18 | `AFRBOP.PARAM.OVERRIDE` | `AfrbopParameter_Override` |  |  |  |
| 19 | `AFRBOP.PARAM.RECORD.STATUS` | `AfrbopParameter_RecordStatus` | String |  |  |
| 20 | `AFRBOP.PARAM.CURR.NO` | `AfrbopParameter_CurrNo` | String |  |  |
| 21 | `AFRBOP.PARAM.INPUTTER` | `AfrbopParameter_Inputter` |  |  |  |
| 22 | `AFRBOP.PARAM.DATE.TIME` | `AfrbopParameter_DateTime` |  |  |  |
| 23 | `AFRBOP.PARAM.AUTHORISER` | `AfrbopParameter_Authoriser` | String |  |  |
| 24 | `AFRBOP.PARAM.CO.CODE` | `AfrbopParameter_CoCode` | String |  |  |
| 25 | `AFRBOP.PARAM.DEPT.CODE` | `AfrbopParameter_DeptCode` | String |  |  |
| 26 | `AFRBOP.PARAM.AUDITOR.CODE` | `AfrbopParameter_AuditorCode` | String |  |  |
| 27 | `AFRBOP.PARAM.AUDIT.DATE.TIME` | `AfrbopParameter_AuditDateTime` | String |  |  |
