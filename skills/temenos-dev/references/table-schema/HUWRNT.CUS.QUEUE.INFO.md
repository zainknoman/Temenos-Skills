# HUWRNT.CUS.QUEUE.INFO — Table Schema

> Source: `INSERTS/I_F.HUWRNT.CUS.QUEUE.INFO` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWCQI.QUEUE.REFERENCE` | `HuwrntCusQueueInfo_QueueReference` |  |  |  |
| 2 | `HUWCQI.ACCOUNT.NUMBER` | `HuwrntCusQueueInfo_AccountNumber` |  |  |  |
| 3 | `HUWCQI.CURRENCY` | `HuwrntCusQueueInfo_Currency` |  |  |  |
| 4 | `HUWCQI.EFFECTIVE.DATE` | `HuwrntCusQueueInfo_EffectiveDate` |  |  |  |
| 5 | `HUWCQI.LOCKED.AMOUNT` | `HuwrntCusQueueInfo_LockedAmount` |  |  |  |
| 6 | `HUWCQI.LOCK.REFERENCE` | `HuwrntCusQueueInfo_LockReference` |  |  |  |
| 7 | `HUWCQI.EQUIVALENT.LOCKED.AMOUNT` | `HuwrntCusQueueInfo_EquivalentLockedAmount` |  |  |  |
| 8 | `HUWCQI.STATUS` | `HuwrntCusQueueInfo_Status` |  |  |  |
| 9 | `HUWCQI.DEPOSIT.ACCOUNTS` | `HuwrntCusQueueInfo_DepositAccounts` |  |  |  |
| 10 | `HUWCQI.EXEMPT.QUEUE.REFERENCE` | `HuwrntCusQueueInfo_ExemptQueueReference` | TField |  | Specifies the regulatory QueueReference for which exempt amount is currently calculated |
| 11 | `HUWCQI.RESERVED.13` | `HuwrntCusQueueInfo_Reserved13` | TField |  | Reserved for future use. |
| 12 | `HUWCQI.RESERVED.12` | `HuwrntCusQueueInfo_Reserved12` | TField |  | Reserved for future use. |
| 13 | `HUWCQI.RESERVED.11` | `HuwrntCusQueueInfo_Reserved11` | TField |  | Reserved for future use. |
| 14 | `HUWCQI.RESERVED.10` | `HuwrntCusQueueInfo_Reserved10` | TField |  | Reserved for future use. |
| 15 | `HUWCQI.RESERVED.9` | `HuwrntCusQueueInfo_Reserved9` | TField |  | Reserved for future use. |
| 16 | `HUWCQI.RESERVED.8` | `HuwrntCusQueueInfo_Reserved8` | TField |  | Reserved for future use. |
| 17 | `HUWCQI.RESERVED.7` | `HuwrntCusQueueInfo_Reserved7` | TField |  | Reserved for future use. |
| 18 | `HUWCQI.RESERVED.6` | `HuwrntCusQueueInfo_Reserved6` | TField |  | Reserved for future use. |
| 19 | `HUWCQI.RESERVED.5` | `HuwrntCusQueueInfo_Reserved5` | TField |  | Reserved for future use. |
| 20 | `HUWCQI.RESERVED.4` | `HuwrntCusQueueInfo_Reserved4` | TField |  | Reserved for future use. |
| 21 | `HUWCQI.RESERVED.3` | `HuwrntCusQueueInfo_Reserved3` | TField |  | Reserved for future use. |
| 22 | `HUWCQI.RESERVED.2` | `HuwrntCusQueueInfo_Reserved2` | TField |  | Reserved for future use. |
| 23 | `HUWCQI.RESERVED.1` | `HuwrntCusQueueInfo_Reserved1` | TField |  | Reserved for future use. |
| 24 | `HUWCQI.LOCAL.REF` | `HuwrntCusQueueInfo_LocalRef` |  |  |  |
| 25 | `HUWCQI.CONFIRMED.AMOUNT.LOAN` | `HuwrntCusQueueInfo_ConfirmedAmountLoan` |  |  |  |
