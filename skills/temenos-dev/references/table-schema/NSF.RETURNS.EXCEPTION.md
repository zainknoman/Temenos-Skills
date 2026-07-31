# NSF.RETURNS.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.NSF.RETURNS.EXCEPTION` in `NSFDES_Queue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NSFEX.ACCOUNT.NUMBER` | `NsfReturnsException_AccountNumber` | TField |  | Account number which has the exception transaction |
| 2 | `NSFEX.CUSTOMER.NUMBER` | `NsfReturnsException_CustomerNumber` |  |  |  |
| 3 | `NSFEX.ACFA.ID` | `NsfReturnsException_AcfaId` | TField |  | ID NSF Exception transaction available in AC.FUNDS.AUTHORISATION table |
| 4 | `NSFEX.TXN.AMT` | `NsfReturnsException_TxnAmt` | TField |  | Transaction amount of the exception transaction |
| 5 | `NSFEX.AAA.ID` | `NsfReturnsException_AaaId` | TField |  | Debit transaction reference that caused the NSF exception, available in AA.ARRANGEMENT.ACTIVITY |
| 6 | `NSFEX.TXN.CONTRACT.ID` | `NsfReturnsException_TxnContractId` | TField |  | Originating transaction reference of the underlying NSF transaction. It can be clearing, PH or FT reference for example |
| 7 | `NSFEX.TXN.SYSTEM.ID` | `NsfReturnsException_TxnSystemId` | TField |  | The EB.SYSTEM.ID used by the underlying transaction for posting accounting entries. This information will be useful in identifying the source of the original transaction |
| 8 | `NSFEX.REV.TXN.ID` | `NsfReturnsException_RevTxnId` | TField |  | The reversal or correction transaction reference that was attempted, but failed |
| 9 | `NSFEX.REV.TXN.DETAILS` | `NsfReturnsException_RevTxnDetails` |  |  |  |
| 10 | `NSFEX.STATUS` | `NsfReturnsException_Status` | TField |  | Status of the reversal or correction transaction. Can be IHLD or DELETE. If it is IHLD, then the reversal record is in exception. If it is DELETE, then the reversal transaction does not exist in exception or live |
| 11 | `NSFEX.RESOLVED` | `NsfReturnsException_Resolved` | TField |  | To be updated manualy by an officer to classify if the correction for Return transactions were posted or not |
| 12 | `NSFEX.COMMENTS` | `NsfReturnsException_Comments` |  |  |  |
| 13 | `NSFEX.RESERVED.10` | `NsfReturnsException_Reserved10` | TField |  |  |
| 14 | `NSFEX.RESERVED.9` | `NsfReturnsException_Reserved9` | TField |  |  |
| 15 | `NSFEX.RESERVED.8` | `NsfReturnsException_Reserved8` | TField |  |  |
| 16 | `NSFEX.RESERVED.7` | `NsfReturnsException_Reserved7` | TField |  |  |
| 17 | `NSFEX.RESERVED.6` | `NsfReturnsException_Reserved6` | TField |  |  |
| 18 | `NSFEX.RESERVED.5` | `NsfReturnsException_Reserved5` | TField |  |  |
| 19 | `NSFEX.RESERVED.4` | `NsfReturnsException_Reserved4` | TField |  |  |
| 20 | `NSFEX.RESERVED.3` | `NsfReturnsException_Reserved3` | TField |  |  |
| 21 | `NSFEX.RESERVED.2` | `NsfReturnsException_Reserved2` | TField |  |  |
| 22 | `NSFEX.RESERVED.1` | `NsfReturnsException_Reserved1` | TField |  |  |
| 23 | `NSFEX.OVERRIDE` | `NsfReturnsException_Override` |  |  |  |
| 24 | `NSFEX.RECORD.STATUS` | `NsfReturnsException_RecordStatus` | String |  |  |
| 25 | `NSFEX.CURR.NO` | `NsfReturnsException_CurrNo` | String |  |  |
| 26 | `NSFEX.INPUTTER` | `NsfReturnsException_Inputter` |  |  |  |
| 27 | `NSFEX.DATE.TIME` | `NsfReturnsException_DateTime` |  |  |  |
| 28 | `NSFEX.AUTHORISER` | `NsfReturnsException_Authoriser` | String |  |  |
| 29 | `NSFEX.CO.CODE` | `NsfReturnsException_CoCode` | String |  |  |
| 30 | `NSFEX.DEPT.CODE` | `NsfReturnsException_DeptCode` | String |  |  |
| 31 | `NSFEX.AUDITOR.CODE` | `NsfReturnsException_AuditorCode` | String |  |  |
| 32 | `NSFEX.AUDIT.DATE.TIME` | `NsfReturnsException_AuditDateTime` | String |  |  |
