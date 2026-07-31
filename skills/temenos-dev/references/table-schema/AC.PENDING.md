# AC.PENDING — Table Schema

> Source: `INSERTS/I_F.AC.PENDING` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACP.ORIG.CAP.DATE` | `AcPending_OrigCapDate` | TField |  | The original capitalisation date when this account capitalised the underlying details. Validation Rules: This is a NOINPUT field. |
| 2 | `ACP.APPL.DATE` | `AcPending_ApplDate` | TField |  | This date denotes the date on which the actual account will be debited with the interest or charge amounts. On this date the suspense account will be credited as well with the same amounts. Validation Rules: This is a NOINPUT field. Automatically updated. |
| 3 | `ACP.ENTRY.TYPE` | `AcPending_EntryType` |  |  |  |
| 4 | `ACP.PENDING.SUSP.AC` | `AcPending_PendingSuspAc` |  |  |  |
| 5 | `ACP.RECD.PL` | `AcPending_RecdPl` |  |  |  |
| 6 | `ACP.SUSP.TXN.CODE` | `AcPending_SuspTxnCode` |  |  |  |
| 7 | `ACP.PL.TXN.CODE` | `AcPending_PlTxnCode` |  |  |  |
| 8 | `ACP.ORIG.AMT` | `AcPending_OrigAmt` |  |  |  |
| 9 | `ACP.NEW.AMT` | `AcPending_NewAmt` |  |  |  |
| 10 | `ACP.TAX.CODE` | `AcPending_TaxCode` |  |  |  |
| 11 | `ACP.TAX.AMT` | `AcPending_TaxAmt` |  |  |  |
| 12 | `ACP.PENDING.TAXSUSP` | `AcPending_PendingTaxsusp` |  |  |  |
| 13 | `ACP.DATE.OF.ADJ` | `AcPending_DateOfAdj` |  |  |  |
| 14 | `ACP.OLD.AMT` | `AcPending_OldAmt` |  |  |  |
| 15 | `ACP.OLD.TAX.AMT` | `AcPending_OldTaxAmt` |  |  |  |
| 16 | `ACP.WAIVE.ALL` | `AcPending_WaiveAll` | TField | No | This field may be used to specify that all the debit interest, charges &amp; taxes specified on this record are to be waived all at once. If this field is set to 'YES' then no charges, interest or tax will be actually applied to the account. Validation Rules: Optional input. Valid values 'YES' or 'NO'. |
| 17 | `ACP.TOTAL.PENDING` | `AcPending_TotalPending` | TField |  | Indicates the total pending amount of debit interest or charges with or without taxes. Validation Rules: This is a NOINPUT field. |
| 18 | `ACP.CONFIRM.SENT` | `AcPending_ConfirmSent` | TField |  | The delivery id used to send out a confirmation message '1970' type. Validation Rules: This is a NOINPUT field. Automatically updated. |
| 19 | `ACP.NARRATIVE` | `AcPending_Narrative` |  |  |  |
| 20 | `ACP.LOCAL.REF` | `AcPending_LocalRef` |  |  |  |
| 21 | `ACP.CALCULATED.AMT` | `AcPending_CalculatedAmt` | TField |  | The system calculated total amount pending. This amount is automatically adjusted when back valued corrections are made but is not affected by manual adjustments. |
| 22 | `ACP.ADJ.ADVICE` | `AcPending_AdjAdvice` |  |  |  |
| 23 | `ACP.MAN.ADJ.TYP` | `AcPending_ManAdjTyp` |  |  |  |
| 24 | `ACP.MAN.ADJ.AMT` | `AcPending_ManAdjAmt` |  |  |  |
| 25 | `ACP.RESERVED.1` | `AcPending_Reserved1` | TField |  |  |
| 26 | `ACP.STMT.NO` | `AcPending_StmtNo` |  |  |  |
| 27 | `ACP.OVERRIDE` | `AcPending_Override` |  |  |  |
| 28 | `ACP.RECORD.STATUS` | `AcPending_RecordStatus` | String |  |  |
| 29 | `ACP.CURR.NO` | `AcPending_CurrNo` | String |  |  |
| 30 | `ACP.INPUTTER` | `AcPending_Inputter` |  |  |  |
| 31 | `ACP.DATE.TIME` | `AcPending_DateTime` |  |  |  |
| 32 | `ACP.AUTHORISER` | `AcPending_Authoriser` | String |  |  |
| 33 | `ACP.CO.CODE` | `AcPending_CoCode` | String |  |  |
| 34 | `ACP.DEPT.CODE` | `AcPending_DeptCode` | String |  |  |
| 35 | `ACP.AUDITOR.CODE` | `AcPending_AuditorCode` | String |  |  |
| 36 | `ACP.AUDIT.DATE.TIME` | `AcPending_AuditDateTime` | String |  |  |
