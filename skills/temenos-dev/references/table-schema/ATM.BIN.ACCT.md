# ATM.BIN.ACCT — Table Schema

> Source: `INSERTS/I_F.ATM.BIN.ACCT` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AT.BIN.DESCRIPTION` | `AtmBinAcct_Description` |  |  |  |
| 2 | `AT.BIN.BIN.TYPE` | `AtmBinAcct_BinType` | TField |  | This field is used to indicate whether the Network is Internal or External.Possible values are ON-US and OFF-US.ON-US value indicates that this is belongs to host bank.OFF-US indicates that this is belongs to other banksEg: ON-US |
| 3 | `AT.BIN.PAY.ACCT.CATEG` | `AtmBinAcct_PayAcctCateg` | TField |  | This field used to configure the GL account category to be used for processing the Debit Transactions. In this field a valid Category can be parameterized or full T24 Internal Account can be parameterized.Validation: The value should be valid record from a CATEGORY table or from ACCOUNT tableIf Category is parameterized then system will use Transaction Login Branch for forming the Full Internal Account and Login Branch for each transactions are based on Customer Account branch.Eg: 10001, CAD1000100011000 |
| 4 | `AT.BIN.RECEIVE.ACCT.CATEG` | `AtmBinAcct_ReceiveAcctCateg` | TField |  | This field used to configure the GL account category to be used for processing the Credit Transactions. In this field with valid Category can be parameterized or full T24 Internal Account can be parameterized.Validation: The value should be valid record from a CATEGORY table or from ACCOUNT tableIf Category is parameterized then system will use Transaction Login Branch for forming the Full Internal Account and Login Branch for each transactions are based on Customer Account branch.Eg: 10001, CAD1000100011000 |
| 5 | `AT.BIN.FP.INT.ACCT` | `AtmBinAcct_FpIntAcct` | TField |  | This field used to define different GL account for Force Post transactions received from ATM.Validation: The value should be valid record from an ACCOUNT tableEg: CAD1000100011000 |
| 6 | `AT.BIN.FP.INT.ACCT.POS` | `AtmBinAcct_FpIntAcctPos` | TField |  | This field used to define different GL account for Force Post transactions received from POS.Validation: The value should be valid record from an ACCOUNT tableEg: CAD1000100011000 |
| 7 | `AT.BIN.POS.CATEGORY` | `AtmBinAcct_PosCategory` | TField |  | This field used to configure the GL category to be used for processing the POS Transactions.Validation: In this field a valid CATEGORY should be parameterized.If Category is parameterized then system will use Transaction Login Branch for forming the Full Internal Account and Login Branch for each transactions are based on Customer Account branch.Eg: 10001 |
| 8 | `AT.BIN.POS.INT.ACCT` | `AtmBinAcct_PosIntAcct` | TField |  | This field used to configure the internal account to be used for processing the POS Transactions.Validation: In this field a valid ACCOUNT should be parameterized.Eg: CAD1000100011000 |
| 9 | `AT.BIN.FP.INT.CATEGORY` | `AtmBinAcct_FpIntCategory` | TField |  | This field used to define different GL category for Force Post transactions received from ATM.Validation: The value should be valid record from CATEGORY tableEg: 10001 |
| 10 | `AT.BIN.FP.INT.CATEG.POS` | `AtmBinAcct_FpIntCategoryPos` |  |  |  |
| 11 | `AT.BIN.USE.INC.CURR` | `AtmBinAcct_UseIncCurr` | TField |  | This field is used to define whether the SYSTEM has to use the foreign currency from the ISO message for performing the transaction or not.Possible values are YES or NO or &lt;NULL&gt;YES - The system will use the incoming foreign currency to perform the transaction.NO - Irrespective of currency in the incoming ISO message transaction will be performed with local currency.&lt;NULL&gt; - If no value is inputted then NO is considered.This field is used only if the Switch provider for ATM/POS is EVERLINKEg: YES |
| 12 | `AT.BIN.EXCH.CURRENCY` | `AtmBinAcct_ExchCurrency` | TField |  | This field used to define a valid currency which can be used as a default currency irrespective of the currency coming in ISO request for foreign transactions. This default currency will be used to calculate the equalent local currency amount to be debited from the customer account.Validation: A valid CURRENCY record id.Eg: USD |
| 13 | `AT.BIN.RESERVED.3` | `AtmBinAcct_Reserved3` | TField |  |  |
| 14 | `AT.BIN.RESERVED.4` | `AtmBinAcct_Reserved4` | TField |  |  |
| 15 | `AT.BIN.LOCAL.REF` | `AtmBinAcct_LocalRef` |  |  |  |
| 16 | `AT.BIN.OVERRIDE` | `AtmBinAcct_Override` |  |  |  |
| 17 | `AT.BIN.RECORD.STATUS` | `AtmBinAcct_RecordStatus` | String |  |  |
| 18 | `AT.BIN.CURR.NO` | `AtmBinAcct_CurrNo` | String |  |  |
| 19 | `AT.BIN.INPUTTER` | `AtmBinAcct_Inputter` |  |  |  |
| 20 | `AT.BIN.DATE.TIME` | `AtmBinAcct_DateTime` |  |  |  |
| 21 | `AT.BIN.AUTHORISER` | `AtmBinAcct_Authoriser` | String |  |  |
| 22 | `AT.BIN.CO.CODE` | `AtmBinAcct_CoCode` | String |  |  |
| 23 | `AT.BIN.DEPT.CODE` | `AtmBinAcct_DeptCode` | String |  |  |
| 24 | `AT.BIN.AUDITOR.CODE` | `AtmBinAcct_AuditorCode` | String |  |  |
| 25 | `AT.BIN.AUDIT.DATE.TIME` | `AtmBinAcct_AuditDateTime` | String |  |  |
