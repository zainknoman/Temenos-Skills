# ESCROW.WAREHOUSE — Table Schema

> Source: `INSERTS/I_F.ESCROW.WAREHOUSE` in `ESCROW_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.WH.COMPANY.CODE` | `EscrowWarehouse_CompanyCode` | TField |  | T24 Company code translated from FIN.CODE as received in the file. |
| 2 | `ESCROW.WH.FILE.NAME` | `EscrowWarehouse_FileName` | TField |  | Is the name of the file that was dropped in INPUT.DIR for upload. |
| 3 | `ESCROW.WH.PROCESSING.DATE` | `EscrowWarehouse_ProcessingDate` | TField |  | Will be current system date on which the upload file was processed. |
| 4 | `ESCROW.WH.PAYEE.ID` | `EscrowWarehouse_PayeeId` | TField |  | Payee Id Code as received in file. |
| 5 | `ESCROW.WH.ESCROW.ACCOUNT.ID` | `EscrowWarehouse_EscrowAccountId` | TField |  | Customer�s escrow account number in T24 as received in file. |
| 6 | `ESCROW.WH.REFERENCE.NAME` | `EscrowWarehouse_ReferenceName` | TField |  | A name that describes the reference data, for example, the Policy Number Tax ID, and so forth as received in file. Corresponds to Payee Reference Number in escrow account. |
| 7 | `ESCROW.WH.CUSTOMER.NAME` | `EscrowWarehouse_CustomerName` | TField |  | Given Names of customer as received in file. |
| 8 | `ESCROW.WH.DISBURSE.DATE` | `EscrowWarehouse_DisburseDate` | TField |  | Forthcoming disbursement due date(s) to the corresponding escrow payee(PAYEE.ID) as received in file. |
| 9 | `ESCROW.WH.DISBURSE.AMOUNT` | `EscrowWarehouse_DisburseAmount` | TField |  | Disbursement amount(s) to the escrow payee for the corresponding the DISBURSE.DATE as received in file. |
| 10 | `ESCROW.WH.STATUS` | `EscrowWarehouse_Status` | TField |  | Denotes the upload status of the record. Possible values are UNMATCHED: When a new file is received, the service will create new records in ESCROW.WAREHOUSE with status as UNMATCHED MATCHED: The batch job in ESCROW.PAYEE.FILE.UPLOAD will match the records received in upload file with T24 records. For records matched exactly with T24 record, the status is updated as MATCHED Rest of the records remain in UNMATCHED status for are manually investigated RETURNED: Manually updated for records those have to be sent back to the originator in the return file CANCEL: Manually updated for records, those have to be ignored and are not required to be part of return file |
| 11 | `ESCROW.WH.RETURN.REASON` | `EscrowWarehouse_ReturnReason` | TField |  | Reason for return from T24. Manually Input by user during manual investigation of UNMATCHED items. |
| 12 | `ESCROW.WH.RELEASE.DATE` | `EscrowWarehouse_ReleaseDate` | TField |  | This field is to capture the release date when incoming file is being uploaded in escrow warehouse table. The release date is determined based on the ESCROW.BLOCKED.FUNDS table. If there is no advance settlement issued for the account then the RELEASE.DATE would be today. If advance settlement issued and we have any record in ESCROW.BLOCKED.FUNDS for the account then system will update the next date after the expiry date of blocked funds. |
| 13 | `ESCROW.WH.RESERVED.9` | `EscrowWarehouse_Reserved9` | TField |  |  |
| 14 | `ESCROW.WH.RESERVED.8` | `EscrowWarehouse_Reserved8` | TField |  |  |
| 15 | `ESCROW.WH.RESERVED.7` | `EscrowWarehouse_Reserved7` | TField |  |  |
| 16 | `ESCROW.WH.RESERVED.6` | `EscrowWarehouse_Reserved6` | TField |  |  |
| 17 | `ESCROW.WH.RESERVED.5` | `EscrowWarehouse_Reserved5` | TField |  |  |
| 18 | `ESCROW.WH.RESERVED.4` | `EscrowWarehouse_Reserved4` | TField |  |  |
| 19 | `ESCROW.WH.RESERVED.3` | `EscrowWarehouse_Reserved3` | TField |  |  |
| 20 | `ESCROW.WH.RESERVED.2` | `EscrowWarehouse_Reserved2` | TField |  |  |
| 21 | `ESCROW.WH.RESERVED.1` | `EscrowWarehouse_Reserved1` | TField |  |  |
| 22 | `ESCROW.WH.LOCAL.REF` | `EscrowWarehouse_LocalRef` |  |  |  |
| 23 | `ESCROW.WH.OVERRIDE` | `EscrowWarehouse_Override` |  |  |  |
| 24 | `ESCROW.WH.RECORD.STATUS` | `EscrowWarehouse_RecordStatus` | String |  |  |
| 25 | `ESCROW.WH.CURR.NO` | `EscrowWarehouse_CurrNo` | String |  |  |
| 26 | `ESCROW.WH.INPUTTER` | `EscrowWarehouse_Inputter` |  |  |  |
| 27 | `ESCROW.WH.DATE.TIME` | `EscrowWarehouse_DateTime` |  |  |  |
| 28 | `ESCROW.WH.AUTHORISER` | `EscrowWarehouse_Authoriser` | String |  |  |
| 29 | `ESCROW.WH.CO.CODE` | `EscrowWarehouse_CoCode` | String |  |  |
| 30 | `ESCROW.WH.DEPT.CODE` | `EscrowWarehouse_DeptCode` | String |  |  |
| 31 | `ESCROW.WH.AUDITOR.CODE` | `EscrowWarehouse_AuditorCode` | String |  |  |
| 32 | `ESCROW.WH.AUDIT.DATE.TIME` | `EscrowWarehouse_AuditDateTime` | String |  |  |
