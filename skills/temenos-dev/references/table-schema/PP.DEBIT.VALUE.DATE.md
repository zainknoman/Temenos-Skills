# PP.DEBIT.VALUE.DATE — Table Schema

> Source: `INSERTS/I_F.PP.DEBIT.VALUE.DATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.DVD.StartDate` | `PpDebitValueDate_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 2 | `PP.DVD.EndDate` | `PpDebitValueDate_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 3 | `PP.DVD.Ranking` | `PpDebitValueDate_Ranking` |  |  |  |
| 4 | `PP.DVD.PaymentDirection` | `PpDebitValueDate_Paymentdirection` |  |  |  |
| 5 | `PP.DVD.DebitAccountType` | `PpDebitValueDate_Debitaccounttype` |  |  |  |
| 6 | `PP.DVD.CTRBTRIndicator` | `PpDebitValueDate_Ctrbtrindicator` |  |  |  |
| 7 | `PP.DVD.Source` | `PpDebitValueDate_Source` |  |  |  |
| 8 | `PP.DVD.Channel` | `PpDebitValueDate_Channel` |  |  |  |
| 9 | `PP.DVD.ClearingTransactionType` | `PpDebitValueDate_Clearingtransactiontype` |  |  |  |
| 10 | `PP.DVD.FloatsIndicator` | `PpDebitValueDate_Floatsindicator` |  |  |  |
| 11 | `PP.DVD.PSDFlag` | `PpDebitValueDate_Psdflag` |  |  |  |
| 12 | `PP.DVD.ApplyDebitFloat` | `PpDebitValueDate_Applydebitfloat` |  |  |  |
| 13 | `PP.DVD.DVDOutput` | `PpDebitValueDate_Dvdoutput` |  |  |  |
| 14 | `PP.DVD.RESERVED.5` | `PpDebitValueDate_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 15 | `PP.DVD.RESERVED.4` | `PpDebitValueDate_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 16 | `PP.DVD.RESERVED.3` | `PpDebitValueDate_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 17 | `PP.DVD.RESERVED.2` | `PpDebitValueDate_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 18 | `PP.DVD.RESERVED.1` | `PpDebitValueDate_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 19 | `PP.DVD.LOCAL.REF` | `PpDebitValueDate_LocalRef` |  |  |  |
| 20 | `PP.DVD.OVERRIDE` | `PpDebitValueDate_Override` |  |  |  |
| 21 | `PP.DVD.RECORD.STATUS` | `PpDebitValueDate_RecordStatus` | String |  |  |
| 22 | `PP.DVD.CURR.NO` | `PpDebitValueDate_CurrNo` | String |  |  |
| 23 | `PP.DVD.INPUTTER` | `PpDebitValueDate_Inputter` |  |  |  |
| 24 | `PP.DVD.DATE.TIME` | `PpDebitValueDate_DateTime` |  |  |  |
| 25 | `PP.DVD.AUTHORISER` | `PpDebitValueDate_Authoriser` | String |  |  |
| 26 | `PP.DVD.CO.CODE` | `PpDebitValueDate_CoCode` | String |  |  |
| 27 | `PP.DVD.DEPT.CODE` | `PpDebitValueDate_DeptCode` | String |  |  |
| 28 | `PP.DVD.AUDITOR.CODE` | `PpDebitValueDate_AuditorCode` | String |  |  |
| 29 | `PP.DVD.AUDIT.DATE.TIME` | `PpDebitValueDate_AuditDateTime` | String |  |  |
