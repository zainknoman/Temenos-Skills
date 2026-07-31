# DEBAIS.PAYMENT.STAT.CONCAT — Table Schema

> Source: `INSERTS/I_F.DEBAIS.PAYMENT.STAT.CONCAT` in `DEBAIS_PaymentStatistics.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBAIS.CONCAT.START.POSITION` | `DebaisPaymentStatConcat_StartPosition` | TField |  | Position of the transaction in the file. Matches with VDRLZ in the extract file |
| 2 | `DEBAIS.CONCAT.STAT.PAYMENT.AMOUNT` | `DebaisPaymentStatConcat_StatPaymentAmount` | TField |  | Amount of the transaction |
| 3 | `DEBAIS.CONCAT.STAT.PAYMENT.CURRENCY` | `DebaisPaymentStatConcat_StatPaymentCurrency` | TField |  | Currency of the transaction |
| 4 | `DEBAIS.CONCAT.STAT.ORGN.COUNTRY` | `DebaisPaymentStatConcat_StatOrgnCountry` | TField |  | Originating country of the transaction |
| 5 | `DEBAIS.CONCAT.STAT.DEST.COUNTRY` | `DebaisPaymentStatConcat_StatDestCountry` | TField |  | Destination country of the transaction |
| 6 | `DEBAIS.CONCAT.STAT.PAYMENT.DIRECTION` | `DebaisPaymentStatConcat_StatPaymentDirection` | TField |  | Direction of the payment, I/O/B |
| 7 | `DEBAIS.CONCAT.RESERVED.10` | `DebaisPaymentStatConcat_Reserved10` | TField |  | Reserved for Future Use. |
| 8 | `DEBAIS.CONCAT.RESERVED.9` | `DebaisPaymentStatConcat_Reserved9` | TField |  | Reserved for Future Use. |
| 9 | `DEBAIS.CONCAT.RESERVED.8` | `DebaisPaymentStatConcat_Reserved8` | TField |  | Reserved for Future Use. |
| 10 | `DEBAIS.CONCAT.RESERVED.7` | `DebaisPaymentStatConcat_Reserved7` | TField |  | Reserved for Future Use. |
| 11 | `DEBAIS.CONCAT.RESERVED.6` | `DebaisPaymentStatConcat_Reserved6` | TField |  | Reserved for Future Use. |
| 12 | `DEBAIS.CONCAT.RESERVED.5` | `DebaisPaymentStatConcat_Reserved5` | TField |  | Reserved for Future Use. |
| 13 | `DEBAIS.CONCAT.RESERVED.4` | `DebaisPaymentStatConcat_Reserved4` | TField |  | Reserved for Future Use. |
| 14 | `DEBAIS.CONCAT.RESERVED.3` | `DebaisPaymentStatConcat_Reserved3` | TField |  | Reserved for Future Use. |
| 15 | `DEBAIS.CONCAT.RESERVED.2` | `DebaisPaymentStatConcat_Reserved2` | TField |  | Reserved for Future Use. |
| 16 | `DEBAIS.CONCAT.RESERVED.1` | `DebaisPaymentStatConcat_Reserved1` | TField |  | Reserved for Future Use. |
| 17 | `DEBAIS.CONCAT.LOCAL.REF` | `DebaisPaymentStatConcat_LocalRef` |  |  |  |
| 18 | `DEBAIS.CONCAT.OVERRIDE` | `DebaisPaymentStatConcat_Override` |  |  |  |
