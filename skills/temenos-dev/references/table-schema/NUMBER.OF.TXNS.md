# NUMBER.OF.TXNS — Table Schema

> Source: `INSERTS/I_F.NUMBER.OF.TXNS` in `IC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NO.TXN.CALCULATION.TYPE` | `NumberOfTxns_CalculationType` | TField | Yes | This field indicates whether the charge calculation is to be based on BAND or LEVEL type. For example if the number of transaction (both credit and debit) on 3.10.2003 is say 40. The values are set up as follows: 1. Calculation Type BAND 2.1 Upto Txn 10 4.1.1 Currency USD 5.1.1.Flat Charge 10.00 2.2 Upto Txn 20 4.2.1 Currency USD 5.2.1 Flat Charge 15 4.3.1 Currency USD 5.3.1 Flat Charge 20 In the above set up the accumulated charges will be calculated as follows: Number of transactions; 40 Charges; Type- band, First 10 transactions-USD10 Next 10 transactions-USD15 Remaining 20 transactions-USD20 Total---------------------------USD 45. Supposing Calculation type is given as level, then in the above case the charges will be USD20. Validation Rules: BAND or LEVEL Mandatory Field |
| 2 | `NO.TXN.UPTO.TXN` | `NumberOfTxns_UptoTxn` |  |  |  |
| 3 | `NO.TXN.DEFAULT.CHG` | `NumberOfTxns_DefaultChg` |  |  |  |
| 4 | `NO.TXN.CURRENCY` | `NumberOfTxns_Currency` |  |  |  |
| 5 | `NO.TXN.FLAT.CHARGE` | `NumberOfTxns_FlatCharge` |  |  |  |
| 6 | `NO.TXN.RESERVED.9` | `NumberOfTxns_Reserved9` | TField |  |  |
| 7 | `NO.TXN.RESERVED.8` | `NumberOfTxns_Reserved8` | TField |  |  |
| 8 | `NO.TXN.RESERVED.7` | `NumberOfTxns_Reserved7` | TField |  |  |
| 9 | `NO.TXN.RESERVED.6` | `NumberOfTxns_Reserved6` | TField |  |  |
| 10 | `NO.TXN.RESERVED.5` | `NumberOfTxns_Reserved5` | TField |  |  |
| 11 | `NO.TXN.RESERVED.4` | `NumberOfTxns_Reserved4` | TField |  |  |
| 12 | `NO.TXN.RESERVED.3` | `NumberOfTxns_Reserved3` | TField |  |  |
| 13 | `NO.TXN.RESERVED.2` | `NumberOfTxns_Reserved2` | TField |  |  |
| 14 | `NO.TXN.LOCAL.REF` | `NumberOfTxns_LocalRef` |  |  |  |
| 15 | `NO.TXN.OVERRIDE` | `NumberOfTxns_Override` |  |  |  |
| 16 | `NO.TXN.RECORD.STATUS` | `NumberOfTxns_RecordStatus` | String |  |  |
| 17 | `NO.TXN.CURR.NO` | `NumberOfTxns_CurrNo` | String |  |  |
| 18 | `NO.TXN.INPUTTER` | `NumberOfTxns_Inputter` |  |  |  |
| 19 | `NO.TXN.DATE.TIME` | `NumberOfTxns_DateTime` |  |  |  |
| 20 | `NO.TXN.AUTHORISER` | `NumberOfTxns_Authoriser` | String |  |  |
| 21 | `NO.TXN.CO.CODE` | `NumberOfTxns_CoCode` | String |  |  |
| 22 | `NO.TXN.DEPT.CODE` | `NumberOfTxns_DeptCode` | String |  |  |
| 23 | `NO.TXN.AUDITOR.CODE` | `NumberOfTxns_AuditorCode` | String |  |  |
| 24 | `NO.TXN.AUDIT.DATE.TIME` | `NumberOfTxns_AuditDateTime` | String |  |  |
