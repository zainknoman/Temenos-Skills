# TAX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TAX.PARAMETER` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TP.DESCRIPTION` | `TaxParameter_Description` |  |  |  |
| 2 | `TP.REFERENCE.NUMBER` | `TaxParameter_ReferenceNumber` | TField |  | The Reference Number allocated to the Bank from the Tax authorities. The tax authorities allocate a reference number to each bank which must be quoted on the Tax returns. That Reference Number must be input in this field. Validation Rules: Upto 12 character Alphanumeric data. |
| 3 | `TP.DEPOSIT.TAKER.NM` | `TaxParameter_DepositTakerNm` | TField |  | The Full name of the Bank as recogonised by the Tax authorities. The data input in this field will be used in the Tax returns. Validation Rules: Upto 50 character Alpha numeric data. |
| 4 | `TP.BRANCH.NAME` | `TaxParameter_BranchName` | TField |  | The Branch name for which the Tax returns are to be sent. The Branch Name entered in this field will be sent on the Tax Returns. Validation Rules: Upto 50 character Alphanumeric. |
| 5 | `TP.SORT.CODE` | `TaxParameter_SortCode` | TField |  | The Sort Code of this Bank/Branch. The Sort code is given to each branch of the bank and it must be entered in this field so that it can be sent in the Tax Returns. Validation Rules: Must exist on BC.SORT.CODE file. Upto 10 character Alphanumeric. |
| 6 | `TP.OUTPUT.DIRECTORY` | `TaxParameter_OutputDirectory` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory input. A maximum of 25 characters may be entered. |
| 7 | `TP.OUTPUT.FILE` | `TaxParameter_OutputFile` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory input. A maximum of 25 characters may be entered. |
| 8 | `TP.LOC.REF.NAME` | `TaxParameter_LocRefName` |  |  |  |
| 9 | `TP.LOC.REF.APP` | `TaxParameter_LocRefApp` |  |  |  |
| 10 | `TP.LOC.REF.POS` | `TaxParameter_LocRefPos` |  |  |  |
| 11 | `TP.TAX.REPORTING` | `TaxParameter_TaxReporting` | TField |  | Field which decides if tax reporting file has to be updated for each tax entry raised from a transaction When set to YES, system would update ST.TAX.REPORT.DETAILS file with tax details for each T24 financial transaction which raises tax entries When set to No/None - no tax details update would happen Validation Rules: Input either YES or NO |
| 12 | `TP.LOCAL.REF` | `TaxParameter_LocalRef` |  |  |  |
| 13 | `TP.RETURN.NO` | `TaxParameter_ReturnNo` |  |  |  |
| 14 | `TP.CURR.TAX.YEAR` | `TaxParameter_CurrTaxYear` |  |  |  |
| 15 | `TP.CURR.TAX.START` | `TaxParameter_CurrTaxStart` |  |  |  |
| 16 | `TP.CURR.TAX.END` | `TaxParameter_CurrTaxEnd` |  |  |  |
| 17 | `TP.BASE.FILE` | `TaxParameter_BaseFile` |  |  |  |
| 18 | `TP.REPORT.CONTROL` | `TaxParameter_ReportControl` |  |  |  |
| 19 | `TP.EXCLUDE.ITEM` | `TaxParameter_ExcludeItem` |  |  |  |
| 20 | `TP.INCLUDE.ITEM` | `TaxParameter_IncludeItem` |  |  |  |
| 21 | `TP.REPORT.ITEM` | `TaxParameter_ReportItem` |  |  |  |
| 22 | `TP.REP.ITEM.VAL` | `TaxParameter_RepItemVal` |  |  |  |
| 23 | `TP.REP.RESERVE5` | `TaxParameter_RepReserve5` |  |  |  |
| 24 | `TP.REP.RESERVE4` | `TaxParameter_RepReserve4` |  |  |  |
| 25 | `TP.REP.RESERVE3` | `TaxParameter_RepReserve3` |  |  |  |
| 26 | `TP.REP.RESERVE2` | `TaxParameter_RepReserve2` |  |  |  |
| 27 | `TP.REP.RESERVE1` | `TaxParameter_RepReserve1` |  |  |  |
| 28 | `TP.RESERVED.3` | `TaxParameter_Reserved3` |  |  |  |
| 29 | `TP.RESERVED.2` | `TaxParameter_Reserved2` |  |  |  |
| 30 | `TP.RESERVED.1` | `TaxParameter_Reserved1` |  |  |  |
| 31 | `TP.ACCT.CLASS.TYPE` | `TaxParameter_AcctClassType` |  |  |  |
| 32 | `TP.ACCT.CLASS.ID` | `TaxParameter_AcctClassId` |  |  |  |
| 33 | `TP.LOCAL.CUST.NO` | `TaxParameter_LocalCustNo` |  |  |  |
| 34 | `TP.ITEM.LABEL` | `TaxParameter_ItemLabel` |  |  |  |
| 35 | `TP.ITEM.FIELD` | `TaxParameter_ItemField` |  |  |  |
| 36 | `TP.ITEM.COND` | `TaxParameter_ItemCond` |  |  |  |
| 37 | `TP.ITEM.DATA` | `TaxParameter_ItemData` |  |  |  |
| 38 | `TP.ITEM.RES3` | `TaxParameter_ItemRes3` |  |  |  |
| 39 | `TP.ITEM.RES2` | `TaxParameter_ItemRes2` |  |  |  |
| 40 | `TP.ITEM.RES1` | `TaxParameter_ItemRes1` |  |  |  |
| 41 | `TP.RECORD.STATUS` | `TaxParameter_RecordStatus` | String |  | Reserved for future use. Validation Rules: Noinput |
| 42 | `TP.CURR.NO` | `TaxParameter_CurrNo` | String |  | Reserved for future use. Validation Rules: Noinput |
| 43 | `TP.INPUTTER` | `TaxParameter_Inputter` |  |  |  |
| 44 | `TP.DATE.TIME` | `TaxParameter_DateTime` |  |  |  |
| 45 | `TP.AUTHORISER` | `TaxParameter_Authoriser` | String |  | Reserved for future use. End of Multi value set associated with RETURN.NO field. |
| 46 | `TP.CO.CODE` | `TaxParameter_CoCode` | String |  | Reserved for future use. |
| 47 | `TP.DEPT.CODE` | `TaxParameter_DeptCode` | String |  | Reserved for future use. Start of Multi value set. |
| 48 | `TP.AUDITOR.CODE` | `TaxParameter_AuditorCode` | String |  | Reserved. |
| 49 | `TP.AUDIT.DATE.TIME` | `TaxParameter_AuditDateTime` | String |  | Reserevd. |
