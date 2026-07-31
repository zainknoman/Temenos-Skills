# DB.DEBIT.COLLECTION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DB.DEBIT.COLLECTION.PARAMETER` in `DB_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DB.PAR.PAYMENT.CONNECTION.METHOD` | `DbDebitCollectionParameter_PaymentConnectionMethod` | TField | Yes | Define the connection between the Payment system and the Debit Collection Order TPS - Send the Payment order details to TPS Validation Rules: Mandatory field To select TPS option PP must be installed in the company |
| 2 | `DB.PAR.DAYS.POST.COMPLETION` | `DbDebitCollectionParameter_DaysPostCompletion` | TField |  | No. of days that an order will remain in live (in the status defined in the above field) before moving to history Validation Rules: nC, nW - n denotes no. of days, C - calendar days, W- working days. It should be in validformat. Default 0 |
| 3 | `DB.PAR.RESERVED.20` | `DbDebitCollectionParameter_Reserved20` | TField |  |  |
| 4 | `DB.PAR.RESERVED.19` | `DbDebitCollectionParameter_Reserved19` | TField |  |  |
| 5 | `DB.PAR.RESERVED.18` | `DbDebitCollectionParameter_Reserved18` | TField |  |  |
| 6 | `DB.PAR.RESERVED.17` | `DbDebitCollectionParameter_Reserved17` | TField |  |  |
| 7 | `DB.PAR.RESERVED.16` | `DbDebitCollectionParameter_Reserved16` | TField |  |  |
| 8 | `DB.PAR.RESERVED.15` | `DbDebitCollectionParameter_Reserved15` | TField |  |  |
| 9 | `DB.PAR.RESERVED.14` | `DbDebitCollectionParameter_Reserved14` | TField |  |  |
| 10 | `DB.PAR.RESERVED.13` | `DbDebitCollectionParameter_Reserved13` | TField |  |  |
| 11 | `DB.PAR.RESERVED.12` | `DbDebitCollectionParameter_Reserved12` | TField |  |  |
| 12 | `DB.PAR.RESERVED.11` | `DbDebitCollectionParameter_Reserved11` | TField |  |  |
| 13 | `DB.PAR.RESERVED.10` | `DbDebitCollectionParameter_Reserved10` | TField |  |  |
| 14 | `DB.PAR.RESERVED.9` | `DbDebitCollectionParameter_Reserved9` | TField |  |  |
| 15 | `DB.PAR.RESERVED.8` | `DbDebitCollectionParameter_Reserved8` | TField |  |  |
| 16 | `DB.PAR.RESERVED.7` | `DbDebitCollectionParameter_Reserved7` | TField |  |  |
| 17 | `DB.PAR.RESERVED.6` | `DbDebitCollectionParameter_Reserved6` | TField |  |  |
| 18 | `DB.PAR.RESERVED.5` | `DbDebitCollectionParameter_Reserved5` | TField |  |  |
| 19 | `DB.PAR.RESERVED.4` | `DbDebitCollectionParameter_Reserved4` | TField |  |  |
| 20 | `DB.PAR.RESERVED.3` | `DbDebitCollectionParameter_Reserved3` | TField |  |  |
| 21 | `DB.PAR.RESERVED.2` | `DbDebitCollectionParameter_Reserved2` | TField |  |  |
| 22 | `DB.PAR.RESERVED.1` | `DbDebitCollectionParameter_Reserved1` | TField |  |  |
| 23 | `DB.PAR.LOCAL.REF` | `DbDebitCollectionParameter_LocalRef` |  |  |  |
| 24 | `DB.PAR.OVERRIDE` | `DbDebitCollectionParameter_Override` |  |  |  |
| 25 | `DB.PAR.RECORD.STATUS` | `DbDebitCollectionParameter_RecordStatus` | String |  |  |
| 26 | `DB.PAR.CURR.NO` | `DbDebitCollectionParameter_CurrNo` | String |  |  |
| 27 | `DB.PAR.INPUTTER` | `DbDebitCollectionParameter_Inputter` |  |  |  |
| 28 | `DB.PAR.DATE.TIME` | `DbDebitCollectionParameter_DateTime` |  |  |  |
| 29 | `DB.PAR.AUTHORISER` | `DbDebitCollectionParameter_Authoriser` | String |  |  |
| 30 | `DB.PAR.CO.CODE` | `DbDebitCollectionParameter_CoCode` | String |  |  |
| 31 | `DB.PAR.DEPT.CODE` | `DbDebitCollectionParameter_DeptCode` | String |  |  |
| 32 | `DB.PAR.AUDITOR.CODE` | `DbDebitCollectionParameter_AuditorCode` | String |  |  |
| 33 | `DB.PAR.AUDIT.DATE.TIME` | `DbDebitCollectionParameter_AuditDateTime` | String |  |  |
