# EU.TAX.PARAM — Table Schema

> Source: `INSERTS/I_F.EU.TAX.PARAM` in `ET_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EU.TAX.TAX.OPTION` | `EuTaxParam_TaxOption` | TField | Yes | This field holds the type of EU tax option which defines the company level setting on the levy of EU tax or exchange of information. The amendment in this field is allowed only when there is no records exists in EU.TAX.LINK file. There are two types of EUSD tax options available, 1. WHT- With-Holding Customer 2. INFO- Reporting Customer Validation Rules: Valid Inputs are 'WHT' or 'INFO' This is a Mandatory field |
| 2 | `EU.TAX.SC.HOLD.PERIOD` | `EuTaxParam_ScHoldPeriod` | TField | Yes | This field holds the type to consider the date to calculate the holding period. Validation Rules: Valid Inputs are 'BUY.DATE', 'STATUS.DATE' or 'EU.DATE' This is a Mandatory field |
| 3 | `EU.TAX.TAX.BASIS` | `EuTaxParam_TaxBasis` | TField | Yes | This field holds the type of transaction basis for the allocation/unallocation of nominals in ET files. Validation Rules: Valid Inputs are 'FIFO'(First In First Out) ,'LIFO' (Last In First Out) or 'AVERAGE' This is a Mandatory field |
| 4 | `EU.TAX.CU.EFF.DATE.FLD` | `EuTaxParam_CuEffDateFld` | TField | Yes | This field holds the local reference field name from the CUSTOMER record which contains the customer effective date to check whether the customer involved are in EU scope. Validation Rules: Valid Inputs are 'A valid local reference field from CUSTOMER application.' This is a Mandatory field |
| 5 | `EU.TAX.SM.EFF.DATE.FLD` | `EuTaxParam_SmEffDateFld` | TField | Yes | This field holds the local reference field name from the SECURITY.MASTER record which contains the security effective date to check whether the security involved are in EU scope. Validation Rules: Valid Inputs are 'A valid local reference field from SECURITY.MASTER application.' This is a Mandatory field |
| 6 | `EU.TAX.CU.TAX.GRP` | `EuTaxParam_CuTaxGrp` |  |  |  |
| 7 | `EU.TAX.TAX.UPD.MODE` | `EuTaxParam_TaxUpdMode` | TField |  | This field holds the value 'ONLINE' for With-Holding customer whenever the tax group is set. Validation Rules: Valid Inputs are 'ONLINE' |
| 8 | `EU.TAX.CU.INFO.GRP` | `EuTaxParam_CuInfoGrp` |  |  |  |
| 9 | `EU.TAX.INFO.UPD.MODE` | `EuTaxParam_InfoUpdMode` | TField |  | This field holds the value 'BATCH' for reporting customer whenever the info group is set. Validation Rules: Valid Inputs are 'BATCH' |
| 10 | `EU.TAX.CU.EXEMPT.GRP` | `EuTaxParam_CuExemptGrp` |  |  |  |
| 11 | `EU.TAX.UPDATE.LOG` | `EuTaxParam_UpdateLog` | TField |  | This field tells whether to update the EUSD log file(EU.UPATE.LOG) or not, whenever the in-scope ET customer involved in purchase/sale with ET security. Validation Rules: Valid Inputs are 'YES' or 'NO' |
| 12 | `EU.TAX.EU.PURGE.DATE` | `EuTaxParam_EuPurgeDate` | TField |  | This field holds the date on which the ET records are purged and moved those records to archive file. This field holds the date on when the last purging happens (i.e.) The transaction details upto this date would be purged from EU.TAX.LINK file and moved to EU.TAX.LINK.PAST file. It provides the user with the ability to purge transactions from the EU.TAX.LINK file and move them to the EU.TAX.LINK.PAST file. All transactions prior to the purge date that have an available nominal of zero are purged and moved during the course of the next COB run. Validation Rules: Valid T24 Date |
| 13 | `EU.TAX.INC.SOURCE.TAX` | `EuTaxParam_IncSourceTax` | TField |  | Indicate whether SOURCE.TAX.AMT to be included in deal amount calculation from ENTITLEMENT. By default the source tax will not be considered. |
| 14 | `EU.TAX.TOTAL.DISC.PREM` | `EuTaxParam_TotalDiscPrem` | TField |  | This is the total Discount/premium of a security in this company for exemption of EUSD tax calculation. The tax exemption is applicable only if total discount and period discount calculated using Issue price and Redem price of SECURITY.MASTER doesn't exceed the values defined in TOTAL.DISC.PREM and PERIOD.DISC.PREM. |
| 15 | `EU.TAX.PERIOD.DISC.PREM` | `EuTaxParam_PeriodDiscPrem` | TField |  | This is the Discount/premium of a security in this company for currecnt period for exemption of EUSD tax calculation. The tax exemption is applicable only if total discount and period discount calculated using Issue price and Redem price of SECURITY.MASTER doesn't exceed the values defined in TOTAL.DISC.PREM and PERIOD.DISC.PREM. |
| 16 | `EU.TAX.RESERVED8` | `EuTaxParam_Reserved8` | TField |  |  |
| 17 | `EU.TAX.RESERVED7` | `EuTaxParam_Reserved7` | TField |  |  |
| 18 | `EU.TAX.RESERVED6` | `EuTaxParam_Reserved6` | TField |  |  |
| 19 | `EU.TAX.RESERVED5` | `EuTaxParam_Reserved5` | TField |  |  |
| 20 | `EU.TAX.RESERVED4` | `EuTaxParam_Reserved4` | TField |  |  |
| 21 | `EU.TAX.RESERVED3` | `EuTaxParam_Reserved3` | TField |  |  |
| 22 | `EU.TAX.RESERVED2` | `EuTaxParam_Reserved2` | TField |  |  |
| 23 | `EU.TAX.RESERVED1` | `EuTaxParam_Reserved1` | TField |  |  |
| 24 | `EU.TAX.LOCAL.REF` | `EuTaxParam_LocalRef` |  |  |  |
| 25 | `EU.TAX.RECORD.STATUS` | `EuTaxParam_RecordStatus` | String |  |  |
| 26 | `EU.TAX.CURR.NO` | `EuTaxParam_CurrNo` | String |  |  |
| 27 | `EU.TAX.INPUTTER` | `EuTaxParam_Inputter` |  |  |  |
| 28 | `EU.TAX.DATE.TIME` | `EuTaxParam_DateTime` |  |  |  |
| 29 | `EU.TAX.AUTHORISER` | `EuTaxParam_Authoriser` | String |  |  |
| 30 | `EU.TAX.CO.CODE` | `EuTaxParam_CoCode` | String |  |  |
| 31 | `EU.TAX.DEPT.CODE` | `EuTaxParam_DeptCode` | String |  |  |
| 32 | `EU.TAX.AUDITOR.CODE` | `EuTaxParam_AuditorCode` | String |  |  |
| 33 | `EU.TAX.AUDIT.DATE.TIME` | `EuTaxParam_AuditDateTime` | String |  |  |
