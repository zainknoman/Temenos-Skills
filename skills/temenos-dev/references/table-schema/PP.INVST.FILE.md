# PP.INVST.FILE — Table Schema

> Source: `INSERTS/I_F.PP.INVST.FILE` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.INV.Status` | `PpInvstFile_Status` | TField |  | Status Description of an Investigation Message. |
| 2 | `PP.INV.LOCAL.REF` | `PpInvstFile_LocalRef` |  |  |  |
| 3 | `PP.INV.OVERRIDE` | `PpInvstFile_Override` |  |  |  |
| 4 | `PP.INV.RECORD.STATUS` | `PpInvstFile_RecordStatus` | String |  |  |
| 5 | `PP.INV.CURR.NO` | `PpInvstFile_CurrNo` | String |  |  |
| 6 | `PP.INV.INPUTTER` | `PpInvstFile_Inputter` |  |  |  |
| 7 | `PP.INV.DATE.TIME` | `PpInvstFile_DateTime` |  |  |  |
| 8 | `PP.INV.AUTHORISER` | `PpInvstFile_Authoriser` | String |  |  |
| 9 | `PP.INV.CO.CODE` | `PpInvstFile_CoCode` | String |  |  |
| 10 | `PP.INV.DEPT.CODE` | `PpInvstFile_DeptCode` | String |  |  |
| 11 | `PP.INV.AUDITOR.CODE` | `PpInvstFile_AuditorCode` | String |  |  |
| 12 | `PP.INV.AUDIT.DATE.TIME` | `PpInvstFile_AuditDateTime` | String |  |  |
| 13 | `PP.INV.SettlementDate` | `PpInvstFile_Settlementdate` | TField |  | Payment settlement Date. Cannot be a future Date. |
| 14 | `PP.INV.ReasonCodeForRejection` | `PpInvstFile_Reasoncodeforrejection` | TField |  | Reason Code for Payment Rejection. |
| 15 | `PP.INV.StatusAcceptanceCode` | `PpInvstFile_Statusacceptancecode` | TField |  | Acceptance Or Reject reason code for the Payment. Possible Values: ACCP, RJCT, ACSP, ACWC |
| 16 | `PP.INV.AdditionalInfo` | `PpInvstFile_Additionalinfo` | TField |  | Free Text of 35 Char. |
| 17 | `PP.INV.FieldName` | `PpInvstFile_Fieldname` |  |  |  |
| 18 | `PP.INV.Operand` | `PpInvstFile_Operand` |  |  |  |
| 19 | `PP.INV.FieldValue` | `PpInvstFile_Fieldvalue` |  |  |  |
| 20 | `PP.INV.Sample` | `PpInvstFile_Sample` | TField |  | This field is used to capture the sample size to make a select in POR.SUPPLEMENTARY.INFO table. Validation Rules: It hold upto maxium of 200, sytem default automatically to 200 sample size when the user keys in beyond 200. |
| 21 | `PP.INV.IsoCxlReasonCode` | `PpInvstFile_Isocxlreasoncode` | TField |  | Specifies the ISO reason code provided by the originating party of the cancellation request. Used to map tag 79 of n92 message along with Original message narrative. Validation Rules: 4 characters of alphatypenumeric Allowed codes as per ISO are DuplicatePayment[DUPL],IncorrectAgent[AGNT],IncorrectCurrency[CURR],RequestedByCustomer[CUST],UnduePayment[UPAY],CancelUponUnableToApply[CUTA],TechnicalProblem[TECH],FraudulentOrigin[FRAD] |
| 22 | `PP.INV.CxlReasonCode` | `PpInvstFile_Cxlreasoncode` | TField |  | Specifies the ISO reason code provided by the originating party of the cancellation request. If Reason ISO code is provided then this proprietary reason field cannot be entered Validation Rules: 35 characters of alphatypenumeric |
| 23 | `PP.INV.CxlAddInfo` | `PpInvstFile_Cxladdinfo` | TField |  | This field is used to provide further information on the reason for cancellation |
| 24 | `PP.INV.FTNumber` | `PpInvstFile_Ftnumber` |  |  |  |
| 25 | `PP.INV.RESERVED.2` | `PpInvstFile_Reserved2` | TField |  |  |
| 26 | `PP.INV.RESERVED.1` | `PpInvstFile_Reserved1` | TField |  |  |
