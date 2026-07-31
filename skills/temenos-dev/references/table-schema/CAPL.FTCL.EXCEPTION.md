# CAPL.FTCL.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.CAPL.FTCL.EXCEPTION` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLR.EXP.DESCRIPTION` | `CaplFtclException_Description` | TField |  | Free text field to define the description of the table. |
| 2 | `CLR.EXP.CLR.TXN.CODE` | `CaplFtclException_ClrTxnCode` | TField |  | Field to store the CPA Transaction code in the clearing record.Mapped from the incoming file. |
| 3 | `CLR.EXP.CURRENCY` | `CaplFtclException_Currency` | TField |  | Field is used to store the Currency for the Customer Account who posts this transaction.Eg. CAD |
| 4 | `CLR.EXP.CUST.ACCT.NO` | `CaplFtclException_CustAcctNo` | TField |  | Field is used to store the Member Account number which is debited or credited.Validation - record from ACCOUNT application. |
| 5 | `CLR.EXP.CLR.SUS.ACCT` | `CaplFtclException_ClrSusAcct` | TField |  | Field is used to store the Suspense Account number which is debited or credited for clearing.Validation - record from ACCOUNT application. |
| 6 | `CLR.EXP.RET.SUS.ACCT` | `CaplFtclException_RetSusAcct` | TField |  | Field is used to store the suspense Account number which is debited or credited for return items.Validation - record from ACCOUNT application. |
| 7 | `CLR.EXP.DR.REF` | `CaplFtclException_DrRef` | TField |  | Field to store the Debit their Reference of the Clearing FT transaction.Application if the transaction is credit type. |
| 8 | `CLR.EXP.CR.REF` | `CaplFtclException_CrRef` | TField |  | Field to store the Credit their Reference of the Clearing FT transaction.Application if the transaction is Debit type. |
| 9 | `CLR.EXP.TRANS.REF` | `CaplFtclException_TransRef` |  |  |  |
| 10 | `CLR.EXP.TRANS.STATUS` | `CaplFtclException_TransStatus` |  |  |  |
| 11 | `CLR.EXP.CLR.OVERRIDE.MSG` | `CaplFtclException_ClrOverrideMsg` |  |  |  |
| 12 | `CLR.EXP.ERROR.MSG` | `CaplFtclException_ErrorMsg` |  |  |  |
| 13 | `CLR.EXP.CLR.POST.COMP` | `CaplFtclException_ClrPostComp` | TField |  | This field will have an ID of the COMPANY where the Clearing transaction was posted.Validation - Record of COMPANY |
| 14 | `CLR.EXP.AMOUNT` | `CaplFtclException_Amount` | TField |  | Field is used to store the amount of the clearing transaction. |
| 15 | `CLR.EXP.VALUE.DATE` | `CaplFtclException_ValueDate` | TField |  |  |
| 16 | `CLR.EXP.POST.ENTRIES` | `CaplFtclException_PostEntries` | TField |  | Field is used to indicate whether accounting entries to be posted for reject transactions.Allowed inputs : YES / NOThis will need to be set to 'YES' when we want to raise entries while rejecting the clearing. |
| 17 | `CLR.EXP.DEF.CHG.TYPE` | `CaplFtclException_DefChgType` |  |  |  |
| 18 | `CLR.EXP.WAIVE.CHG` | `CaplFtclException_WaiveChg` |  |  |  |
| 19 | `CLR.EXP.CHG.AMT` | `CaplFtclException_ChgAmt` |  |  |  |
| 20 | `CLR.EXP.TRACE.ID` | `CaplFtclException_TraceId` | TField |  | Field to store the Tracer ID from the clearing file. |
| 21 | `CLR.EXP.INTRF.FIELD.NM` | `CaplFtclException_IntrfFieldNm` |  |  |  |
| 22 | `CLR.EXP.INTRF.FIELD.VL` | `CaplFtclException_IntrfFieldVl` |  |  |  |
| 23 | `CLR.EXP.CLR.STATUS` | `CaplFtclException_ClrStatus` | TField |  | Field is used to store the stauts of the clearing transactions processed.Valid Values are :-CLEARED - Cleared without overrideLOW.RESTR - Soft RestrictionsHIGH.RESTR - Hard RestrictionsINVALID.MICR - Invalid MICR EncodingERROR - Error message due to which the transaction is not posted.The Clearing Interface has to update the status as 'CLEARED' for transaction without any override. 'LOW.RESTR' for transaction with an override, 'HIGH.RESTR' for transaction with an override class, 'INVALID.MICR' for Invalid MICR Encoding, 'ERROR' for Unable to post transaction due to error message. |
| 24 | `CLR.EXP.ORIG.STATUS` | `CaplFtclException_OrigStatus` | TField |  | Obsolete. Not in use now. |
| 25 | `CLR.EXP.RET.REASON` | `CaplFtclException_RetReason` |  |  |  |
| 26 | `CLR.EXP.RET.RESN.TXT` | `CaplFtclException_RetResnTxt` |  |  |  |
| 27 | `CLR.EXP.ENTRY.NOTES` | `CaplFtclException_EntryNotes` |  |  |  |
| 28 | `CLR.EXP.RET.STATUS` | `CaplFtclException_RetStatus` | TField |  | This field is used to indicate the transaction status for return items.Allowed options 1.ACCEPT - 2. REJECT 3. CHARGE.BACK. Based on these status, charge will be decided and deducted or Waived. |
| 29 | `CLR.EXP.CHQ.RET.CERT` | `CaplFtclException_ChqRetCert` | TField |  |  |
| 30 | `CLR.EXP.CHEQUE.NO` | `CaplFtclException_ChequeNo` | TField |  |  |
| 31 | `CLR.EXP.INSTITUTE.NO` | `CaplFtclException_InstituteNo` | TField |  |  |
| 32 | `CLR.EXP.TRANSIT` | `CaplFtclException_Transit` | TField |  |  |
| 33 | `CLR.EXP.MICR.ACCT.NO` | `CaplFtclException_MicrAcctNo` | TField |  |  |
| 34 | `CLR.EXP.CLOSE.DATE.TIME` | `CaplFtclException_CloseDateTime` |  |  |  |
| 35 | `CLR.EXP.RET.REF.NO` | `CaplFtclException_RetRefNo` | TField |  | This field is used to store the credit reference number from the incoming file. |
| 36 | `CLR.EXP.ORG.LONG.NM` | `CaplFtclException_OrgLongNm` | TField |  | This field is used to store the Organisation name from the incoming file. |
| 37 | `CLR.EXP.RESERVED.4` | `CaplFtclException_Reserved4` | TField |  |  |
| 38 | `CLR.EXP.RESERVED.3` | `CaplFtclException_Reserved3` | TField |  |  |
| 39 | `CLR.EXP.RESERVED.2` | `CaplFtclException_Reserved2` | TField |  |  |
| 40 | `CLR.EXP.RESERVED.1` | `CaplFtclException_Reserved1` | TField |  |  |
| 41 | `CLR.EXP.LOCAL.REF` | `CaplFtclException_LocalRef` |  |  |  |
| 42 | `CLR.EXP.OVERRIDE` | `CaplFtclException_Override` |  |  |  |
| 43 | `CLR.EXP.RECORD.STATUS` | `CaplFtclException_RecordStatus` | String |  |  |
| 44 | `CLR.EXP.CURR.NO` | `CaplFtclException_CurrNo` | String |  |  |
| 45 | `CLR.EXP.INPUTTER` | `CaplFtclException_Inputter` |  |  |  |
| 46 | `CLR.EXP.DATE.TIME` | `CaplFtclException_DateTime` |  |  |  |
| 47 | `CLR.EXP.AUTHORISER` | `CaplFtclException_Authoriser` | String |  |  |
| 48 | `CLR.EXP.CO.CODE` | `CaplFtclException_CoCode` | String |  |  |
| 49 | `CLR.EXP.DEPT.CODE` | `CaplFtclException_DeptCode` | String |  |  |
| 50 | `CLR.EXP.AUDITOR.CODE` | `CaplFtclException_AuditorCode` | String |  |  |
| 51 | `CLR.EXP.AUDIT.DATE.TIME` | `CaplFtclException_AuditDateTime` | String |  |  |
