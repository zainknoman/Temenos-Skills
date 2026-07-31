# NORACC.AVAILABLE.LIMIT — Table Schema

> Source: `INSERTS/I_F.NORACC.AVAILABLE.LIMIT` in `FICUST_AccountLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AVAIL.LIMIT.LIMIT.CUSTOMER` | `NoraccAvailableLimit_LimitCustomer` | TField |  | Customer's Limit value |
| 2 | `AVAIL.LIMIT.SSN.ID` | `NoraccAvailableLimit_SsnId` | TField |  | SSN.ID of the customer |
| 3 | `AVAIL.LIMIT.LIMIT.ACCOUNT` | `NoraccAvailableLimit_LimitAccount` | TField |  | Account of the customer having limit |
| 4 | `AVAIL.LIMIT.LIMIT.ACCOUNT.IBAN` | `NoraccAvailableLimit_LimitAccountIban` | TField |  | IBAN of the account having limit |
| 5 | `AVAIL.LIMIT.ONLINE.LIMIT` | `NoraccAvailableLimit_OnlineLimit` | TField |  | Online Limit |
| 6 | `AVAIL.LIMIT.AMOUNT.OUTSTANDING` | `NoraccAvailableLimit_AmountOutstanding` | TField |  | Outstanding amount |
| 7 | `AVAIL.LIMIT.AMOUNT.AVAILABLE` | `NoraccAvailableLimit_AmountAvailable` | TField |  | Online limit less Amount outstanding |
| 8 | `AVAIL.LIMIT.PREVIOUS.OUTSTANDING` | `NoraccAvailableLimit_PreviousOutstanding` | TField |  | Previous Outstanding amount |
| 9 | `AVAIL.LIMIT.LAST.MOVEMENT.DATE` | `NoraccAvailableLimit_LastMovementDate` | TField |  | Date on which amount is moved last |
| 10 | `AVAIL.LIMIT.LIMIT.OFFICER` | `NoraccAvailableLimit_LimitOfficer` | TField |  | Limit officer |
| 11 | `AVAIL.LIMIT.RESERVED.10` | `NoraccAvailableLimit_Reserved10` | TField |  | Reserved for future use |
| 12 | `AVAIL.LIMIT.RESERVED.9` | `NoraccAvailableLimit_Reserved9` | TField |  | Reserved for future use |
| 13 | `AVAIL.LIMIT.RESERVED.8` | `NoraccAvailableLimit_Reserved8` | TField |  | Reserved for future use |
| 14 | `AVAIL.LIMIT.RESERVED.7` | `NoraccAvailableLimit_Reserved7` | TField |  | Reserved for future use |
| 15 | `AVAIL.LIMIT.RESERVED.6` | `NoraccAvailableLimit_Reserved6` | TField |  | Reserved for future use |
| 16 | `AVAIL.LIMIT.RESERVED.5` | `NoraccAvailableLimit_Reserved5` | TField |  | Reserved for future use |
| 17 | `AVAIL.LIMIT.RESERVED.4` | `NoraccAvailableLimit_Reserved4` | TField |  | Reserved for future use |
| 18 | `AVAIL.LIMIT.RESERVED.3` | `NoraccAvailableLimit_Reserved3` | TField |  | Reserved for future use |
| 19 | `AVAIL.LIMIT.RESERVED.2` | `NoraccAvailableLimit_Reserved2` | TField |  | Reserved for future use |
| 20 | `AVAIL.LIMIT.RESERVED.1` | `NoraccAvailableLimit_Reserved1` | TField |  | Reserved for future use |
| 21 | `AVAIL.LIMIT.LOCAL.REF` | `NoraccAvailableLimit_LocalRef` |  |  |  |
