# FICOLL.TO.BE.RENEWED.COL — Table Schema

> Source: `INSERTS/I_F.FICOLL.TO.BE.RENEWED.COL` in `FICOLL_AutomaticRenewalProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.CUSTOMER.ID` | `FicollToBeRenewedCol_CustomerId` | TField |  | Customer ID |
| 2 | `FICOLL.NOTIFICATION.DATE` | `FicollToBeRenewedCol_NotificationDate` |  |  |  |
| 3 | `FICOLL.EXPIRY.DATE` | `FicollToBeRenewedCol_ExpiryDate` | TField |  | Expiry date of Collateral |
| 4 | `FICOLL.RESERVED.5` | `FicollToBeRenewedCol_Reserved5` | TField |  |  |
| 5 | `FICOLL.RESERVED.4` | `FicollToBeRenewedCol_Reserved4` | TField |  |  |
| 6 | `FICOLL.RESERVED.3` | `FicollToBeRenewedCol_Reserved3` | TField |  |  |
| 7 | `FICOLL.RESERVED.2` | `FicollToBeRenewedCol_Reserved2` | TField |  |  |
| 8 | `FICOLL.RESERVED.1` | `FicollToBeRenewedCol_Reserved1` | TField |  |  |
| 9 | `FICOLL.LOCAL.REF` | `FicollToBeRenewedCol_LocalRef` |  |  |  |
