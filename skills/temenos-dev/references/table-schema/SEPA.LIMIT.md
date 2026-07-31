# SEPA.LIMIT — Table Schema

> Source: `INSERTS/I_F.SEPA.LIMIT` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEPA.LIMIT.DESCRIPTION` | `SepaLimit_Description` |  |  |  |
| 2 | `SEPA.LIMIT.LIMIT.CHECK.STATUS` | `SepaLimit_LimitCheckStatus` | TField |  | This field denotes the status of the DD limit check record. Validation Rules Allowed Values are ACTIVE and INACTIVE |
| 3 | `SEPA.LIMIT.OUR.ACCOUNT` | `SepaLimit_OurAccount` | TField |  | This field holds the value of a valid T24 Account ID Validation Rules Value upto 19 type ACC(Account Type) and should be a valid record in ACCOUNT application |
| 4 | `SEPA.LIMIT.OUR.ACCT.TITLE` | `SepaLimit_OurAcctTitle` | A (Alphanumeric) |  | This field is a no inputtable field Validation Rules Value upto 65 type A(Alphanumeric) |
| 5 | `SEPA.LIMIT.OUR.IBAN` | `SepaLimit_OurIban` | A (Alphanumeric) |  | This field is a no inputtable field and holds the value of a valid T24 IBAN Validation Rules Value upto 65 type A(Alphanumeric) |
| 6 | `SEPA.LIMIT.MANDATE.ID` | `SepaLimit_MandateId` | A (Alphanumeric) |  | This field is a no inputtable field Validation Rules Value upto 65 type A(Alphanumeric) |
| 7 | `SEPA.LIMIT.THEIR.IBAN` | `SepaLimit_TheirIban` | A (Alphanumeric) |  | This field holds the value of a valid Beneficiary IBAN Validation Rules Value upto 65 type A(Alphanumeric) |
| 8 | `SEPA.LIMIT.THEIR.NAME` | `SepaLimit_TheirName` | A (Alphanumeric) |  | This field holds the value of a Beneficiary Name Validation Rules Value upto 65 type A(Alphanumeric) |
| 9 | `SEPA.LIMIT.CREDITOR.ID` | `SepaLimit_CreditorId` | A (Alphanumeric) |  | This field is a no inputtable field Validation Rules Value upto 65 type A(Alphanumeric) |
| 10 | `SEPA.LIMIT.RESERVED.14` | `SepaLimit_Reserved14` | TField |  |  |
| 11 | `SEPA.LIMIT.RESERVED.13` | `SepaLimit_Reserved13` | TField |  |  |
| 12 | `SEPA.LIMIT.RESERVED.12` | `SepaLimit_Reserved12` | TField |  |  |
| 13 | `SEPA.LIMIT.RESERVED.11` | `SepaLimit_Reserved11` | TField |  |  |
| 14 | `SEPA.LIMIT.LIMIT.START.DATE` | `SepaLimit_LimitStartDate` |  |  |  |
| 15 | `SEPA.LIMIT.LIMIT.FREQUENCY` | `SepaLimit_LimitFrequency` |  |  |  |
| 16 | `SEPA.LIMIT.LIMIT.END.DATE` | `SepaLimit_LimitEndDate` |  |  |  |
| 17 | `SEPA.LIMIT.LIMIT.STATUS` | `SepaLimit_LimitStatus` |  |  |  |
| 18 | `SEPA.LIMIT.NO.TRANS.ALLOW` | `SepaLimit_NoTransAllow` |  |  |  |
| 19 | `SEPA.LIMIT.NO.TRANS.PROCESS` | `SepaLimit_NoTransProcess` |  |  |  |
| 20 | `SEPA.LIMIT.SUM.AMOUNT.ALLOW` | `SepaLimit_SumAmountAllow` |  |  |  |
| 21 | `SEPA.LIMIT.SUM.AMOUNT.PROCESS` | `SepaLimit_SumAmountProcess` |  |  |  |
| 22 | `SEPA.LIMIT.MAX.AMOUNT.ALLOW` | `SepaLimit_MaxAmountAllow` |  |  |  |
| 23 | `SEPA.LIMIT.PROC.DATE.REF` | `SepaLimit_ProcDateRef` |  |  |  |
| 24 | `SEPA.LIMIT.LIMIT.REF` | `SepaLimit_LimitRef` | A (Alphanumeric) |  | This field is a no inputtable field Validation Rules Value upto 120 type A(Alphanumeric) |
| 25 | `SEPA.LIMIT.FTTC` | `SepaLimit_Fttc` | A (Alphanumeric) |  | This field holds the value of a valid Transaction Condition Validation Rules Value upto 4 type A(Alphanumeric) and should be a valid record in FT.TXN.TYPE.CONDITION application |
| 26 | `SEPA.LIMIT.PROCESS.TYPE` | `SepaLimit_ProcessType` | A (Alphanumeric) |  | Validation Rules Value upto 3 type A(Alphanumeric) |
| 27 | `SEPA.LIMIT.REASON.CODE` | `SepaLimit_ReasonCode` | A (Alphanumeric) |  | This field holds the value of a proper Reason Code Validation Rules Value upto 4 type A(Alphanumeric) and should be a valid record in SEPA.REASONS application |
| 28 | `SEPA.LIMIT.RESERVED.10` | `SepaLimit_Reserved10` | TField |  |  |
| 29 | `SEPA.LIMIT.RESERVED.9` | `SepaLimit_Reserved9` | TField |  |  |
| 30 | `SEPA.LIMIT.RESERVED.8` | `SepaLimit_Reserved8` | TField |  |  |
| 31 | `SEPA.LIMIT.RESERVED.7` | `SepaLimit_Reserved7` | TField |  |  |
| 32 | `SEPA.LIMIT.RESERVED.6` | `SepaLimit_Reserved6` | TField |  |  |
| 33 | `SEPA.LIMIT.RESERVED.5` | `SepaLimit_Reserved5` | TField |  |  |
| 34 | `SEPA.LIMIT.RESERVED.4` | `SepaLimit_Reserved4` | TField |  |  |
| 35 | `SEPA.LIMIT.RESERVED.3` | `SepaLimit_Reserved3` | TField |  |  |
| 36 | `SEPA.LIMIT.RESERVED.2` | `SepaLimit_Reserved2` | TField |  |  |
| 37 | `SEPA.LIMIT.RESERVED.1` | `SepaLimit_Reserved1` | TField |  |  |
| 38 | `SEPA.LIMIT.LOCAL.REF` | `SepaLimit_LocalRef` |  |  |  |
| 39 | `SEPA.LIMIT.OVERRIDE` | `SepaLimit_Override` |  |  |  |
| 40 | `SEPA.LIMIT.RECORD.STATUS` | `SepaLimit_RecordStatus` | String |  |  |
| 41 | `SEPA.LIMIT.CURR.NO` | `SepaLimit_CurrNo` | String |  |  |
| 42 | `SEPA.LIMIT.INPUTTER` | `SepaLimit_Inputter` |  |  |  |
| 43 | `SEPA.LIMIT.DATE.TIME` | `SepaLimit_DateTime` |  |  |  |
| 44 | `SEPA.LIMIT.AUTHORISER` | `SepaLimit_Authoriser` | String |  |  |
| 45 | `SEPA.LIMIT.CO.CODE` | `SepaLimit_CoCode` | String |  |  |
| 46 | `SEPA.LIMIT.DEPT.CODE` | `SepaLimit_DeptCode` | String |  |  |
| 47 | `SEPA.LIMIT.AUDITOR.CODE` | `SepaLimit_AuditorCode` | String |  |  |
| 48 | `SEPA.LIMIT.AUDIT.DATE.TIME` | `SepaLimit_AuditDateTime` | String |  |  |
