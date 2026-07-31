# FICOLL.CR.CONTACT.LEASE.CONCAT — Table Schema

> Source: `INSERTS/I_F.FICOLL.CR.CONTACT.LEASE.CONCAT` in `FICOLL_CollateralLease.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FI.CR.LEASE.EXPIRY.DATE` | `FicollCrContactLeaseConcat_LeaseExpiryDate` |  |  |  |
| 2 | `FI.CR.CR.CONTACT.REFERENCE` | `FicollCrContactLeaseConcat_CrContactReference` |  |  |  |
| 3 | `FI.CR.RESERVED.10` | `FicollCrContactLeaseConcat_Reserved10` | TField |  |  |
| 4 | `FI.CR.RESERVED.9` | `FicollCrContactLeaseConcat_Reserved9` | TField |  |  |
| 5 | `FI.CR.RESERVED.8` | `FicollCrContactLeaseConcat_Reserved8` | TField |  |  |
| 6 | `FI.CR.RESERVED.7` | `FicollCrContactLeaseConcat_Reserved7` | TField |  |  |
| 7 | `FI.CR.RESERVED.6` | `FicollCrContactLeaseConcat_Reserved6` | TField |  |  |
| 8 | `FI.CR.RESERVED.5` | `FicollCrContactLeaseConcat_Reserved5` | TField |  |  |
| 9 | `FI.CR.RESERVED.4` | `FicollCrContactLeaseConcat_Reserved4` | TField |  |  |
| 10 | `FI.CR.RESERVED.3` | `FicollCrContactLeaseConcat_Reserved3` | TField |  |  |
| 11 | `FI.CR.RESERVED.2` | `FicollCrContactLeaseConcat_Reserved2` | TField |  |  |
| 12 | `FI.CR.RESERVED.1` | `FicollCrContactLeaseConcat_Reserved1` | TField |  |  |
| 13 | `FI.CR.LOCAL.REF` | `FicollCrContactLeaseConcat_LocalRef` |  |  |  |
