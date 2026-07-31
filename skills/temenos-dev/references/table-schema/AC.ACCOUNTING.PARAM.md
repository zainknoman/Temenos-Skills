# AC.ACCOUNTING.PARAM — Table Schema

> Source: `INSERTS/I_F.AC.ACCOUNTING.PARAM` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.PARAM.MAX.NO.OF.SPLITS` | `AcAccountingParam_MaxNoOfSplits` | TField |  | Numeric field. Field to define the count of multi-values(i.e. number of entry ids) to be maintained in a record. Validation : Allowed value is greater than 200. |
| 2 | `AC.PARAM.MAX.SIZE.RECS` | `AcAccountingParam_MaxSizeRecs` | TField |  | Numeric field. Field to define the size of the record based on the length of the field values. |
| 3 | `AC.PARAM.LOCK.RESERVE.CONDITION` | `AcAccountingParam_LockReserveCondition` |  |  |  |
| 4 | `AC.PARAM.AC.OVERDRAWN.BAL` | `AcAccountingParam_AcOverdrawnBal` | TField |  | This field decides the Overdrawn monitoring and reporting behaviour of the Transact system Allowed Options: ACTUAL.BALANCE � Overdrawn Monitoring will be based on individual Account Booked or Ledger Balance only. Limit Excess utilisation will not be monitored and reported in Account Overdrawn file irrespective of whether limit is linked to account or contract. NO/NULL � Overdrawn Monitoring will be based on Account Cleared Outstanding Balance for Accounts not linked to an Overdraft Limit and For Limits Excess utilisation is also monitored based Limit Outstanding Validation Rules: Once system is configured to follow ACTUAL.BALANCE, any further amendment to this field is restricted |
| 5 | `AC.PARAM.RESERVED13` | `AcAccountingParam_Reserved13` |  |  |  |
| 6 | `AC.PARAM.RESERVED12` | `AcAccountingParam_Reserved12` |  |  |  |
| 7 | `AC.PARAM.RESERVED11` | `AcAccountingParam_Reserved11` |  |  |  |
| 8 | `AC.PARAM.RESERVED10` | `AcAccountingParam_Reserved10` |  |  |  |
| 9 | `AC.PARAM.RESERVED09` | `AcAccountingParam_Reserved09` |  |  |  |
| 10 | `AC.PARAM.RESERVED08` | `AcAccountingParam_Reserved08` |  |  |  |
| 11 | `AC.PARAM.RESERVED07` | `AcAccountingParam_Reserved07` |  |  |  |
| 12 | `AC.PARAM.RESERVED06` | `AcAccountingParam_Reserved06` | TField |  |  |
| 13 | `AC.PARAM.RESERVED05` | `AcAccountingParam_Reserved05` | TField |  |  |
| 14 | `AC.PARAM.RESERVED04` | `AcAccountingParam_Reserved04` | TField |  |  |
| 15 | `AC.PARAM.RESERVED03` | `AcAccountingParam_Reserved03` | TField |  |  |
| 16 | `AC.PARAM.RESERVED02` | `AcAccountingParam_Reserved02` | TField |  |  |
| 17 | `AC.PARAM.RESERVED01` | `AcAccountingParam_Reserved01` | TField |  |  |
| 18 | `AC.PARAM.LOCAL.REF` | `AcAccountingParam_LocalRef` |  |  |  |
| 19 | `AC.PARAM.OVERRIDE` | `AcAccountingParam_Override` |  |  |  |
| 20 | `AC.PARAM.RECORD.STATUS` | `AcAccountingParam_RecordStatus` | String |  |  |
| 21 | `AC.PARAM.CURR.NO` | `AcAccountingParam_CurrNo` | String |  |  |
| 22 | `AC.PARAM.INPUTTER` | `AcAccountingParam_Inputter` |  |  |  |
| 23 | `AC.PARAM.DATE.TIME` | `AcAccountingParam_DateTime` |  |  |  |
| 24 | `AC.PARAM.AUTHORISER` | `AcAccountingParam_Authoriser` | String |  |  |
| 25 | `AC.PARAM.CO.CODE` | `AcAccountingParam_CoCode` | String |  |  |
| 26 | `AC.PARAM.DEPT.CODE` | `AcAccountingParam_DeptCode` | String |  |  |
| 27 | `AC.PARAM.AUDITOR.CODE` | `AcAccountingParam_AuditorCode` | String |  |  |
| 28 | `AC.PARAM.AUDIT.DATE.TIME` | `AcAccountingParam_AuditDateTime` | String |  |  |
