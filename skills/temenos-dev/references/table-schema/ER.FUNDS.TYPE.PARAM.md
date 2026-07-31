# ER.FUNDS.TYPE.PARAM — Table Schema

> Source: `INSERTS/I_F.ER.FUNDS.TYPE.PARAM` in `ER_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ERFP.DESCRIPTION` | `ErFundsTypeParam_Description` |  |  |  |
| 2 | `ERFP.TYPE.CR.DR` | `ErFundsTypeParam_TypeCrDr` | TField |  | Field to indicate the type of matching item. Validation Rules: Has two options - CREDIT/DEBIT Defaulted to DEBIT. |
| 3 | `ERFP.FWD.DB.ACC.FIELD` | `ErFundsTypeParam_FwdDbAccField` | A (Alphanumeric) | No | Field to indicate Field to indicate if Debit Forward entries should be raised for unmatched matching items of this type.The field in the AC.EXPETCTED.RECS which stores the account must be indicated here. Valid field of AC.EXPECTED.RECS. Validation Rules: Valid field in AC.EXPECTED.RECS. 1-35 type A (Alphanumeric) characters. (Optional input.) |
| 4 | `ERFP.FWD.CR.ACC.FIELD` | `ErFundsTypeParam_FwdCrAccField` | A (Alphanumeric) | No | Field to indicate Field to indicate if Credit Forward entries should be raised for unmatched matching items of this type.The field in the AC.EXPETCTED.RECS which stores the account must be indicated here. Valid field of AC.EXPECTED.RECS. Validation Rules: Valid field in AC.EXPECTED.RECS. 1-35 type A (Alphanumeric) characters. (Optional input.) |
| 5 | `ERFP.FWD.DB.TXN.CODE` | `ErFundsTypeParam_FwdDbTxnCode` | TField | No | Field to indicate transaction code for debit forward entries. Validation Rules: Drop down menu for TRANSACTION records 1-10 type TXN (Transaction) characters. (Optional input.) |
| 6 | `ERFP.FWD.CR.TXN.CODE` | `ErFundsTypeParam_FwdCrTxnCode` | TField | No | Field to indicate transaction code for credit forward entries. Validation Rules: Drop down menu for TRANSACTION records 1-10 type TXN (Transaction) characters. (Optional input.) |
| 7 | `ERFP.MATCH.CONDITION` | `ErFundsTypeParam_MatchCondition` |  |  |  |
| 8 | `ERFP.EXCLUDE.CURRENCIES` | `ErFundsTypeParam_ExcludeCurrencies` |  |  |  |
| 9 | `ERFP.CHECK.CUT.OFF` | `ErFundsTypeParam_CheckCutOff` | TField |  |  |
| 10 | `ERFP.STORE.BIC8` | `ErFundsTypeParam_StoreBic8` | TField | Yes | If this is set to Yes the system will populate the Correspondent BIC with the first 8 chars of the Original Correspondent BIC received in the incoming messages/API. Validation Rules: Mandatory YES/NO field. Defaulted to NO. Defaulted to YES. |
| 11 | `ERFP.RESERVED.5` | `ErFundsTypeParam_Reserved5` | TField |  | This field is reserved for future use. |
| 12 | `ERFP.RESERVED.4` | `ErFundsTypeParam_Reserved4` | TField |  | This field is reserved for future use. |
| 13 | `ERFP.RESERVED.3` | `ErFundsTypeParam_Reserved3` | TField |  | This field is reserved for future use. |
| 14 | `ERFP.RESERVED.2` | `ErFundsTypeParam_Reserved2` | TField |  | This field is reserved for future use. |
| 15 | `ERFP.RESERVED.1` | `ErFundsTypeParam_Reserved1` | TField |  | This field is reserved for future use. |
| 16 | `ERFP.LOCAL.REF` | `ErFundsTypeParam_LocalRef` |  |  |  |
| 17 | `ERFP.OVERRIDE` | `ErFundsTypeParam_Override` |  |  |  |
| 18 | `ERFP.RECORD.STATUS` | `ErFundsTypeParam_RecordStatus` | String |  |  |
| 19 | `ERFP.CURR.NO` | `ErFundsTypeParam_CurrNo` | String |  |  |
| 20 | `ERFP.INPUTTER` | `ErFundsTypeParam_Inputter` |  |  |  |
| 21 | `ERFP.DATE.TIME` | `ErFundsTypeParam_DateTime` |  |  |  |
| 22 | `ERFP.AUTHORISER` | `ErFundsTypeParam_Authoriser` | String |  |  |
| 23 | `ERFP.CO.CODE` | `ErFundsTypeParam_CoCode` | String |  |  |
| 24 | `ERFP.DEPT.CODE` | `ErFundsTypeParam_DeptCode` | String |  |  |
| 25 | `ERFP.AUDITOR.CODE` | `ErFundsTypeParam_AuditorCode` | String |  |  |
| 26 | `ERFP.AUDIT.DATE.TIME` | `ErFundsTypeParam_AuditDateTime` | String |  |  |
| 27 | `ERFP.MATCH.FUNDS.TYPE` | `ErFundsTypeParam_MatchFundsType` |  |  |  |
