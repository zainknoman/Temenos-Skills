# ARTAXS.RETURN.TAX.FILE.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARTAXS.RETURN.TAX.FILE.DETAILS` in `ARTAXS_TaxReturns.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARTAXD.FILE.NAME` | `ArtaxsReturnTaxFileDetails_FileName` | TField |  | Processed file name. |
| 2 | `ARTAXD.FILE.RECEIVED.DATE` | `ArtaxsReturnTaxFileDetails_FileReceivedDate` | TField |  | Date when the file was received. |
| 3 | `ARTAXD.JURISDICTION` | `ArtaxsReturnTaxFileDetails_Jurisdiction` | TField |  | Jurisdiction from which the file is being processed. Has the value associated with EB.LOOKUPs with PROVINCE as virtual table. |
| 4 | `ARTAXD.CUSTOMER.LEGAL.ID` | `ArtaxsReturnTaxFileDetails_CustomerLegalId` | TField |  | Customer Legal Id mapped from the file. |
| 5 | `ARTAXD.CUSTOMER.NUMBER` | `ArtaxsReturnTaxFileDetails_CustomerNumber` | TField |  | Customer Number will have a values if a valid Customer Legal Id was mapped. |
| 6 | `ARTAXD.CUSTOMER.NAME` | `ArtaxsReturnTaxFileDetails_CustomerName` | TField |  | Customer Name mapped from the file. |
| 7 | `ARTAXD.BANK.CODE` | `ArtaxsReturnTaxFileDetails_BankCode` | TField |  | Bank Code mapped from the file. |
| 8 | `ARTAXD.PERIOD.START.DATE` | `ArtaxsReturnTaxFileDetails_PeriodStartDate` | TField |  | Period Start Date mapped from the file |
| 9 | `ARTAXD.PERIOD.END.DATE` | `ArtaxsReturnTaxFileDetails_PeriodEndDate` | TField |  | Period End Date mapped from the file (If not mapped, values will be !TODAY). |
| 10 | `ARTAXD.ACCOUNT.CBU` | `ArtaxsReturnTaxFileDetails_AccountCbu` | TField |  | Account Cbu mapped form the file. |
| 11 | `ARTAXD.AMOUNT` | `ArtaxsReturnTaxFileDetails_Amount` | TField |  | Amount value mapped from the file. |
| 12 | `ARTAXD.STATUS` | `ArtaxsReturnTaxFileDetails_Status` | TField |  | Status of the process file. Has the value associated with EB.LOOKUPs with ARTAXS.FILE.STATUS as virtual table. |
| 13 | `ARTAXD.ACCOUNT.TO.REFUND` | `ArtaxsReturnTaxFileDetails_AccountToRefund` |  |  |  |
| 14 | `ARTAXD.PAYMENT.ORDER.ID` | `ArtaxsReturnTaxFileDetails_PaymentOrderId` |  |  |  |
| 15 | `ARTAXD.PAYMENT.ORDER.STATUS` | `ArtaxsReturnTaxFileDetails_PaymentOrderStatus` |  |  |  |
| 16 | `ARTAXD.RESERVED.10` | `ArtaxsReturnTaxFileDetails_Reserved10` |  |  |  |
| 17 | `ARTAXD.RESERVED.9` | `ArtaxsReturnTaxFileDetails_Reserved9` |  |  |  |
| 18 | `ARTAXD.RESERVED.8` | `ArtaxsReturnTaxFileDetails_Reserved8` |  |  |  |
| 19 | `ARTAXD.RESERVED.7` | `ArtaxsReturnTaxFileDetails_Reserved7` |  |  |  |
| 20 | `ARTAXD.RESERVED.6` | `ArtaxsReturnTaxFileDetails_Reserved6` |  |  |  |
| 21 | `ARTAXD.RESERVED.5` | `ArtaxsReturnTaxFileDetails_Reserved5` |  |  |  |
| 22 | `ARTAXD.RESERVED.4` | `ArtaxsReturnTaxFileDetails_Reserved4` |  |  |  |
| 23 | `ARTAXD.RESERVED.3` | `ArtaxsReturnTaxFileDetails_Reserved3` |  |  |  |
| 24 | `ARTAXD.RESERVED.2` | `ArtaxsReturnTaxFileDetails_Reserved2` |  |  |  |
| 25 | `ARTAXD.RESERVED.1` | `ArtaxsReturnTaxFileDetails_Reserved1` | TField |  |  |
| 26 | `ARTAXD.RECORD.STATUS` | `ArtaxsReturnTaxFileDetails_RecordStatus` | String |  |  |
| 27 | `ARTAXD.CURR.NO` | `ArtaxsReturnTaxFileDetails_CurrNo` | String |  |  |
| 28 | `ARTAXD.INPUTTER` | `ArtaxsReturnTaxFileDetails_Inputter` |  |  |  |
| 29 | `ARTAXD.DATE.TIME` | `ArtaxsReturnTaxFileDetails_DateTime` |  |  |  |
| 30 | `ARTAXD.AUTHORISER` | `ArtaxsReturnTaxFileDetails_Authoriser` | String |  |  |
| 31 | `ARTAXD.CO.CODE` | `ArtaxsReturnTaxFileDetails_CoCode` | String |  |  |
| 32 | `ARTAXD.DEPT.CODE` | `ArtaxsReturnTaxFileDetails_DeptCode` | String |  |  |
| 33 | `ARTAXD.AUDITOR.CODE` | `ArtaxsReturnTaxFileDetails_AuditorCode` | String |  |  |
| 34 | `ARTAXD.AUDIT.DATE.TIME` | `ArtaxsReturnTaxFileDetails_AuditDateTime` | String |  |  |
