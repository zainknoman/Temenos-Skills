# INLEND.EDPMS.EBRC — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.EBRC` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.EBRC.NAME` | `InlendEdpmsEbrc_Name` | TField |  | Name of the Exporter. |
| 2 | `INLEND.EBRC.BRC.PROCESS.NAME` | `InlendEdpmsEbrc_BrcProcessName` | TField |  | Field to capture the process name of BRC. |
| 3 | `INLEND.EBRC.SHIPPING.BILL.CURRENCY` | `InlendEdpmsEbrc_ShippingBillCurrency` | TField |  |  |
| 4 | `INLEND.EBRC.BRANCH.IFSC.CODE` | `InlendEdpmsEbrc_BranchIfscCode` | TField |  | Bank (IFSEC) code which generated BRC. |
| 5 | `INLEND.EBRC.BILL.ID` | `InlendEdpmsEbrc_BillId` | TField |  | Unique Bill id. |
| 6 | `INLEND.EBRC.TRANSACTION.CURRENCY` | `InlendEdpmsEbrc_TransactionCurrency` | TField |  | Currency of realisation. |
| 7 | `INLEND.EBRC.TOTAL.REALISED.VALUE` | `InlendEdpmsEbrc_TotalRealisedValue` | TField |  | Total realised value in currency of realisation. |
| 8 | `INLEND.EBRC.TRANSACTION.DATE` | `InlendEdpmsEbrc_TransactionDate` | TField |  | Date of Realisation of bill. |
| 9 | `INLEND.EBRC.EBRC.EXCHANGE.RATE` | `InlendEdpmsEbrc_EbrcExchangeRate` | TField |  | Exchange rate at which the Realised value in CC has to be converted to INR. |
| 10 | `INLEND.EBRC.TOTAL.REALISED.VALUE.INR` | `InlendEdpmsEbrc_TotalRealisedValueInr` | TField |  | Total realised value in INR. |
| 11 | `INLEND.EBRC.EBRC.NUMBER` | `InlendEdpmsEbrc_EbrcNumber` | TField |  | Updated using routine logic provided for generating eBRC number. |
| 13 | `INLEND.EBRC.STATUS.BRC` | `InlendEdpmsEbrc_StatusBrc` | TField |  | Status of eBRC. |
| 14 | `INLEND.EBRC.EBRC.CANCEL.DATE` | `InlendEdpmsEbrc_EbrcCancelDate` | TField |  | Date of cancellation of eBRC. |
| 15 | `INLEND.EBRC.PREVIOUS.EBRC.NUMBER` | `InlendEdpmsEbrc_PreviousEbrcNumber` |  |  |  |
| 16 | `INLEND.EBRC.PREVIOUS.EBRC.DATE` | `InlendEdpmsEbrc_PreviousEbrcDate` |  |  |  |
| 17 | `INLEND.EBRC.PREVIOUS.EBRC.AMOUNT` | `InlendEdpmsEbrc_PreviousEbrcAmount` |  |  |  |
| 18 | `INLEND.EBRC.REISSUE.EBRC.AMOUNT` | `InlendEdpmsEbrc_ReissueEbrcAmount` | TField |  | This field is used in case of eBRC reissue. |
| 19 | `INLEND.EBRC.ERROR.CODE` | `InlendEdpmsEbrc_ErrorCode` | TField |  | Error Code from the acknowledgement file from DGFT to Bank.A Valid entry from Error Code Table. |
| 20 | `INLEND.EBRC.RESERVED.5` | `InlendEdpmsEbrc_Reserved5` | TField |  |  |
| 21 | `INLEND.EBRC.RESERVED.4` | `InlendEdpmsEbrc_Reserved4` | TField |  |  |
| 22 | `INLEND.EBRC.RESERVED.3` | `InlendEdpmsEbrc_Reserved3` | TField |  |  |
| 23 | `INLEND.EBRC.RESERVED.2` | `InlendEdpmsEbrc_Reserved2` | TField |  |  |
| 24 | `INLEND.EBRC.RESERVED.1` | `InlendEdpmsEbrc_Reserved1` | TField |  |  |
| 25 | `INLEND.EBRC.LOCAL.REF` | `InlendEdpmsEbrc_LocalRef` |  |  |  |
| 26 | `INLEND.EBRC.OVERRIDE` | `InlendEdpmsEbrc_Override` |  |  |  |
| 27 | `INLEND.EBRC.RECORD.STATUS` | `InlendEdpmsEbrc_RecordStatus` | String |  |  |
| 28 | `INLEND.EBRC.CURR.NO` | `InlendEdpmsEbrc_CurrNo` | String |  |  |
| 29 | `INLEND.EBRC.INPUTTER` | `InlendEdpmsEbrc_Inputter` |  |  |  |
| 30 | `INLEND.EBRC.DATE.TIME` | `InlendEdpmsEbrc_DateTime` |  |  |  |
| 31 | `INLEND.EBRC.AUTHORISER` | `InlendEdpmsEbrc_Authoriser` | String |  |  |
| 32 | `INLEND.EBRC.CO.CODE` | `InlendEdpmsEbrc_CoCode` | String |  |  |
| 33 | `INLEND.EBRC.DEPT.CODE` | `InlendEdpmsEbrc_DeptCode` | String |  |  |
| 34 | `INLEND.EBRC.AUDITOR.CODE` | `InlendEdpmsEbrc_AuditorCode` | String |  |  |
| 35 | `INLEND.EBRC.AUDIT.DATE.TIME` | `InlendEdpmsEbrc_AuditDateTime` | String |  |  |
