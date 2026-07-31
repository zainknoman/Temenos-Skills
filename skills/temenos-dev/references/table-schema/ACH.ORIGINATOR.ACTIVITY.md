# ACH.ORIGINATOR.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.ACH.ORIGINATOR.ACTIVITY` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHORIG.ACT.ORIGINATOR.ID` | `AchOriginatorActivity_OriginatorId` | TField |  | Originator id of the ACH entry. |
| 2 | `ACHORIG.ACT.COMPANY.ID` | `AchOriginatorActivity_CompanyId` | TField |  | Company id of ACH batch. |
| 3 | `ACHORIG.ACT.ACTIVITY.MONTH` | `AchOriginatorActivity_ActivityMonth` | TField |  | To store the month of ACH batch date. |
| 4 | `ACHORIG.ACT.CONSOLIDATE.KEY` | `AchOriginatorActivity_ConsolidateKey` |  |  |  |
| 5 | `ACHORIG.ACT.TXN.COUNT` | `AchOriginatorActivity_TxnCount` |  |  |  |
| 6 | `ACHORIG.ACT.AMOUNT` | `AchOriginatorActivity_Amount` |  |  |  |
| 7 | `ACHORIG.ACT.EFFECTIVE.DATE` | `AchOriginatorActivity_EffectiveDate` |  |  |  |
| 8 | `ACHORIG.ACT.CREDIT.TOTAL` | `AchOriginatorActivity_CreditTotal` |  |  |  |
| 9 | `ACHORIG.ACT.DEBIT.TOTAL` | `AchOriginatorActivity_DebitTotal` |  |  |  |
| 10 | `ACHORIG.ACT.RESERVED.22` | `AchOriginatorActivity_Reserved22` | TField |  |  |
| 11 | `ACHORIG.ACT.RESERVED.21` | `AchOriginatorActivity_Reserved21` | TField |  |  |
| 12 | `ACHORIG.ACT.RESERVED.20` | `AchOriginatorActivity_Reserved20` | TField |  |  |
| 13 | `ACHORIG.ACT.RESERVED.19` | `AchOriginatorActivity_Reserved19` | TField |  |  |
| 14 | `ACHORIG.ACT.RESERVED.18` | `AchOriginatorActivity_Reserved18` | TField |  |  |
| 15 | `ACHORIG.ACT.RESERVED.17` | `AchOriginatorActivity_Reserved17` | TField |  |  |
| 16 | `ACHORIG.ACT.RESERVED.16` | `AchOriginatorActivity_Reserved16` | TField |  |  |
| 17 | `ACHORIG.ACT.RESERVED.15` | `AchOriginatorActivity_Reserved15` | TField |  |  |
| 18 | `ACHORIG.ACT.RESERVED.14` | `AchOriginatorActivity_Reserved14` | TField |  |  |
| 19 | `ACHORIG.ACT.RESERVED.13` | `AchOriginatorActivity_Reserved13` | TField |  |  |
| 20 | `ACHORIG.ACT.RESERVED.12` | `AchOriginatorActivity_Reserved12` | TField |  |  |
| 21 | `ACHORIG.ACT.RESERVED.11` | `AchOriginatorActivity_Reserved11` | TField |  |  |
| 22 | `ACHORIG.ACT.RESERVED.10` | `AchOriginatorActivity_Reserved10` | TField |  |  |
| 23 | `ACHORIG.ACT.RESERVED.9` | `AchOriginatorActivity_Reserved9` | TField |  |  |
| 24 | `ACHORIG.ACT.RESERVED.8` | `AchOriginatorActivity_Reserved8` | TField |  |  |
| 25 | `ACHORIG.ACT.RESERVED.7` | `AchOriginatorActivity_Reserved7` | TField |  |  |
| 26 | `ACHORIG.ACT.RESERVED.6` | `AchOriginatorActivity_Reserved6` | TField |  |  |
| 27 | `ACHORIG.ACT.RESERVED.5` | `AchOriginatorActivity_Reserved5` | TField |  |  |
| 28 | `ACHORIG.ACT.RESERVED.4` | `AchOriginatorActivity_Reserved4` | TField |  |  |
| 29 | `ACHORIG.ACT.RESERVED.3` | `AchOriginatorActivity_Reserved3` | TField |  |  |
| 30 | `ACHORIG.ACT.RESERVED.2` | `AchOriginatorActivity_Reserved2` | TField |  |  |
| 31 | `ACHORIG.ACT.RESERVED.1` | `AchOriginatorActivity_Reserved1` | TField |  |  |
| 32 | `ACHORIG.ACT.LOCAL.REF` | `AchOriginatorActivity_LocalRef` |  |  |  |
| 33 | `ACHORIG.ACT.OVERRIDE` | `AchOriginatorActivity_Override` |  |  |  |
