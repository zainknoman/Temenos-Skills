# TY.DEALER.TXN.LIMIT — Table Schema

> Source: `INSERTS/I_F.TY.DEALER.TXN.LIMIT` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.DEALER.TXN.LIMIT.DESCRIPTION` | `TyDealerTxnLimit_Description` |  |  |  |
| 2 | `TY.DEALER.TXN.LIMIT.LIMIT.PRODUCT` | `TyDealerTxnLimit_LimitProduct` |  |  |  |
| 3 | `TY.DEALER.TXN.LIMIT.DEAL.CCY` | `TyDealerTxnLimit_DealCcy` |  |  |  |
| 4 | `TY.DEALER.TXN.LIMIT.LIMIT.AMOUNT` | `TyDealerTxnLimit_LimitAmount` |  |  |  |
| 5 | `TY.DEALER.TXN.LIMIT.LIMIT.UTILIZED` | `TyDealerTxnLimit_LimitUtilized` |  |  |  |
| 6 | `TY.DEALER.TXN.LIMIT.LIMIT.AVAIL` | `TyDealerTxnLimit_LimitAvail` |  |  |  |
| 7 | `TY.DEALER.TXN.LIMIT.TXN.LIMIT.CCY` | `TyDealerTxnLimit_TxnLimitCcy` | TField |  | An user defined field to define the currency if transactions are monitored in any particular currency can be defined over here. Validations: Valid currency. Input in the field will require inputs in TXN.LIMIT.AMT. |
| 8 | `TY.DEALER.TXN.LIMIT.TXN.LIMIT.AMT` | `TyDealerTxnLimit_TxnLimitAmt` | TField |  | An user defined field to define the amounts if transactions are to be monitored in any particular currency can be defined over here. Validations: Input in the field will require inputs in TXN.LIMIT.CCY. |
| 9 | `TY.DEALER.TXN.LIMIT.RESERVED.10` | `TyDealerTxnLimit_Reserved10` | TField |  |  |
| 10 | `TY.DEALER.TXN.LIMIT.RESERVED.9` | `TyDealerTxnLimit_Reserved9` | TField |  |  |
| 11 | `TY.DEALER.TXN.LIMIT.RESERVED.8` | `TyDealerTxnLimit_Reserved8` | TField |  |  |
| 12 | `TY.DEALER.TXN.LIMIT.RESERVED.7` | `TyDealerTxnLimit_Reserved7` | TField |  |  |
| 13 | `TY.DEALER.TXN.LIMIT.RESERVED.6` | `TyDealerTxnLimit_Reserved6` | TField |  |  |
| 14 | `TY.DEALER.TXN.LIMIT.RESERVED.5` | `TyDealerTxnLimit_Reserved5` | TField |  |  |
| 15 | `TY.DEALER.TXN.LIMIT.RESERVED.4` | `TyDealerTxnLimit_Reserved4` | TField |  |  |
| 16 | `TY.DEALER.TXN.LIMIT.RESERVED.3` | `TyDealerTxnLimit_Reserved3` | TField |  |  |
| 17 | `TY.DEALER.TXN.LIMIT.RESERVED.2` | `TyDealerTxnLimit_Reserved2` | TField |  |  |
| 18 | `TY.DEALER.TXN.LIMIT.RESERVED.1` | `TyDealerTxnLimit_Reserved1` | TField |  |  |
| 19 | `TY.DEALER.TXN.LIMIT.LOCAL.REF` | `TyDealerTxnLimit_LocalRef` |  |  |  |
| 20 | `TY.DEALER.TXN.LIMIT.RECORD.STATUS` | `TyDealerTxnLimit_RecordStatus` | String |  |  |
| 21 | `TY.DEALER.TXN.LIMIT.CURR.NO` | `TyDealerTxnLimit_CurrNo` | String |  |  |
| 22 | `TY.DEALER.TXN.LIMIT.INPUTTER` | `TyDealerTxnLimit_Inputter` |  |  |  |
| 23 | `TY.DEALER.TXN.LIMIT.DATE.TIME` | `TyDealerTxnLimit_DateTime` |  |  |  |
| 24 | `TY.DEALER.TXN.LIMIT.AUTHORISER` | `TyDealerTxnLimit_Authoriser` | String |  |  |
| 25 | `TY.DEALER.TXN.LIMIT.CO.CODE` | `TyDealerTxnLimit_CoCode` | String |  |  |
| 26 | `TY.DEALER.TXN.LIMIT.DEPT.CODE` | `TyDealerTxnLimit_DeptCode` | String |  |  |
| 27 | `TY.DEALER.TXN.LIMIT.AUDITOR.CODE` | `TyDealerTxnLimit_AuditorCode` | String |  |  |
| 28 | `TY.DEALER.TXN.LIMIT.AUDIT.DATE.TIME` | `TyDealerTxnLimit_AuditDateTime` | String |  |  |
