# USREGS.OVERDRAFT.NFS — Table Schema

> Source: `INSERTS/I_F.USREGS.OVERDRAFT.NFS` in `NACUST_CustomerHolds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USREGS.OVDT.RESERVED.16` | `UsregsOverdraftNfs_Reserved16` | TField |  |  |
| 2 | `USREGS.OVDT.RESERVED.15` | `UsregsOverdraftNfs_Reserved15` | TField |  |  |
| 3 | `USREGS.OVDT.NEXT.AVAIL.AMOUNT` | `UsregsOverdraftNfs_NextAvailAmount` | TField |  | This field is used to indicate that the amount which is next available to the customer. It will get cleared on a daily basis in a cob job. |
| 4 | `USREGS.OVDT.AGR.CHECK.TOTAL` | `UsregsOverdraftNfs_AgrCheckTotal` | TField |  |  |
| 5 | `USREGS.OVDT.RESERVED.14` | `UsregsOverdraftNfs_Reserved14` | TField |  |  |
| 6 | `USREGS.OVDT.RESERVED.13` | `UsregsOverdraftNfs_Reserved13` | TField |  |  |
| 7 | `USREGS.OVDT.RESERVED.12` | `UsregsOverdraftNfs_Reserved12` | TField |  |  |
| 8 | `USREGS.OVDT.RESERVED.11` | `UsregsOverdraftNfs_Reserved11` | TField |  |  |
| 9 | `USREGS.OVDT.RESERVED.10` | `UsregsOverdraftNfs_Reserved10` | TField |  |  |
| 10 | `USREGS.OVDT.RESERVED.9` | `UsregsOverdraftNfs_Reserved9` | TField |  |  |
| 11 | `USREGS.OVDT.RESERVED.8` | `UsregsOverdraftNfs_Reserved8` | TField |  |  |
| 12 | `USREGS.OVDT.RESERVED.7` | `UsregsOverdraftNfs_Reserved7` | TField |  |  |
| 13 | `USREGS.OVDT.RESERVED.6` | `UsregsOverdraftNfs_Reserved6` | TField |  |  |
| 14 | `USREGS.OVDT.RESERVED.5` | `UsregsOverdraftNfs_Reserved5` | TField |  |  |
| 15 | `USREGS.OVDT.RESERVED.4` | `UsregsOverdraftNfs_Reserved4` | TField |  |  |
| 16 | `USREGS.OVDT.RESERVED.3` | `UsregsOverdraftNfs_Reserved3` | TField |  |  |
| 17 | `USREGS.OVDT.RESERVED.2` | `UsregsOverdraftNfs_Reserved2` | TField |  |  |
| 18 | `USREGS.OVDT.RESERVED.1` | `UsregsOverdraftNfs_Reserved1` | TField |  |  |
