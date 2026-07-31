# DB.DEBIT.COLLECTION.PRODUCT — Table Schema

> Source: `INSERTS/I_F.DB.DEBIT.COLLECTION.PRODUCT` in `DB_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DB.PRO.DESCRIPTION` | `DbDebitCollectionProduct_Description` |  |  |  |
| 2 | `DB.PRO.ALLOWED.PAYMENT.CCY` | `DbDebitCollectionProduct_AllowedPaymentCcy` |  |  |  |
| 3 | `DB.PRO.DUPLICATE.CHECK` | `DbDebitCollectionProduct_DuplicateCheck` |  |  |  |
| 4 | `DB.PRO.TRANSACTION.LIMIT` | `DbDebitCollectionProduct_TransactionLimit` | TField |  | The max 'Collection Amount' that can be captured Validation Rules: Must be a valid Amount |
| 5 | `DB.PRO.ALLOW.FUTURE.DATE` | `DbDebitCollectionProduct_AllowFutureDate` | TField |  |  |
| 6 | `DB.PRO.VALIDATE.API` | `DbDebitCollectionProduct_ValidateApi` | TField |  | API to perform validations specific to a product Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record PAYMENT.PRODUCT.VALIDATE.API.HOOK. |
| 7 | `DB.PRO.REACHABILITY.CHECK` | `DbDebitCollectionProduct_ReachabilityCheck` | TField |  | This defines whether reachability check is required or not. Validation Rules: Possible values: 'Yes' or 'No' Default option is 'No' |
| 8 | `DB.PRO.ALLOWED.CHARGE.OPTIONS` | `DbDebitCollectionProduct_AllowedChargeOptions` |  |  |  |
| 9 | `DB.PRO.DEFAULT.CHARGE.OPTION` | `DbDebitCollectionProduct_DefaultChargeOption` | TField |  | Default Charger bearer for the Debit collection product. If charge bearer is not defined in DB.DEBIT.COLLECTION.ORDER, then the default charge bearer to be populated. Default option is 'None' Validation Rules: Values allowed are BEN, OUR or SHA. Must be an allowed charge as mentioned in the ALLOWED.CHARGE.OPTIONS field. |
| 10 | `DB.PRO.CLEARING.CHANNEL` | `DbDebitCollectionProduct_ClearingChannel` |  |  |  |
| 11 | `DB.PRO.CLEARING.CODE.FORMAT` | `DbDebitCollectionProduct_ClearingCodeFormat` |  |  |  |
| 12 | `DB.PRO.CUTOFF.TIME` | `DbDebitCollectionProduct_CutoffTime` | TField |  |  |
| 13 | `DB.PRO.CUTOFF.DAYS.SHIFT` | `DbDebitCollectionProduct_CutoffDaysShift` | TField |  |  |
| 14 | `DB.PRO.CUTOFF.PRODUCT` | `DbDebitCollectionProduct_CutoffProduct` | TField |  |  |
| 15 | `DB.PRO.RESERVED.11` | `DbDebitCollectionProduct_Reserved11` | TField |  |  |
| 16 | `DB.PRO.RESERVED.10` | `DbDebitCollectionProduct_Reserved10` | TField |  |  |
| 17 | `DB.PRO.RESERVED.9` | `DbDebitCollectionProduct_Reserved9` | TField |  |  |
| 18 | `DB.PRO.RESERVED.8` | `DbDebitCollectionProduct_Reserved8` | TField |  |  |
| 19 | `DB.PRO.RESERVED.7` | `DbDebitCollectionProduct_Reserved7` | TField |  |  |
| 20 | `DB.PRO.RESERVED.6` | `DbDebitCollectionProduct_Reserved6` | TField |  |  |
| 21 | `DB.PRO.RESERVED.5` | `DbDebitCollectionProduct_Reserved5` | TField |  |  |
| 22 | `DB.PRO.RESERVED.4` | `DbDebitCollectionProduct_Reserved4` | TField |  |  |
| 23 | `DB.PRO.RESERVED.3` | `DbDebitCollectionProduct_Reserved3` | TField |  |  |
| 24 | `DB.PRO.RESERVED.2` | `DbDebitCollectionProduct_Reserved2` | TField |  |  |
| 25 | `DB.PRO.RESERVED.1` | `DbDebitCollectionProduct_Reserved1` | TField |  |  |
| 26 | `DB.PRO.LOCAL.REF` | `DbDebitCollectionProduct_LocalRef` |  |  |  |
| 27 | `DB.PRO.OVERRIDE` | `DbDebitCollectionProduct_Override` |  |  |  |
| 28 | `DB.PRO.RECORD.STATUS` | `DbDebitCollectionProduct_RecordStatus` | String |  |  |
| 29 | `DB.PRO.CURR.NO` | `DbDebitCollectionProduct_CurrNo` | String |  |  |
| 30 | `DB.PRO.INPUTTER` | `DbDebitCollectionProduct_Inputter` |  |  |  |
| 31 | `DB.PRO.DATE.TIME` | `DbDebitCollectionProduct_DateTime` |  |  |  |
| 32 | `DB.PRO.AUTHORISER` | `DbDebitCollectionProduct_Authoriser` | String |  |  |
| 33 | `DB.PRO.CO.CODE` | `DbDebitCollectionProduct_CoCode` | String |  |  |
| 34 | `DB.PRO.DEPT.CODE` | `DbDebitCollectionProduct_DeptCode` | String |  |  |
| 35 | `DB.PRO.AUDITOR.CODE` | `DbDebitCollectionProduct_AuditorCode` | String |  |  |
| 36 | `DB.PRO.AUDIT.DATE.TIME` | `DbDebitCollectionProduct_AuditDateTime` | String |  |  |
