# CHQ.NOMINEE.CUMUL — Table Schema

> Source: `INSERTS/I_F.CHQ.NOMINEE.CUMUL` in `CACQMG_ChequeManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHQ.NOM.AA.REF` | `ChqNomineeCumul_AaRef` |  |  |  |
| 2 | `CHQ.NOM.PO.REF` | `ChqNomineeCumul_PoRef` |  |  |  |
| 3 | `CHQ.NOM.PO.AMOUNT` | `ChqNomineeCumul_PoAmount` |  |  |  |
| 4 | `CHQ.NOM.RESERVED.13` | `ChqNomineeCumul_Reserved13` |  |  |  |
| 5 | `CHQ.NOM.RESERVED.12` | `ChqNomineeCumul_Reserved12` |  |  |  |
| 6 | `CHQ.NOM.RESERVED.11` | `ChqNomineeCumul_Reserved11` |  |  |  |
| 7 | `CHQ.NOM.TOTAL.PO.AMOUNT` | `ChqNomineeCumul_TotalPoAmount` | TField |  | This field will carry the sum of all the PO.AMOUNT filed.Valid amount to be stored here. |
| 8 | `CHQ.NOM.NOMINEE.ACCOUNT` | `ChqNomineeCumul_NomineeAccount` | TField |  | This field will carry the demand account used for psoting the consolidated payment to nominee.Valid entry from AA.ARRANGEMENT |
| 9 | `CHQ.NOM.CONSOL.PO.REF` | `ChqNomineeCumul_ConsolPoRef` | TField |  | This field will carry the PAYMENT.ORDER reference of the consolidated payment.Valid entry from PAYMENT.ORDER |
| 10 | `CHQ.NOM.CONSOL.FT.REF` | `ChqNomineeCumul_ConsolFtRef` | TField |  |  |
| 11 | `CHQ.NOM.RESERVED.10` | `ChqNomineeCumul_Reserved10` | TField |  |  |
| 12 | `CHQ.NOM.RESERVED.9` | `ChqNomineeCumul_Reserved9` | TField |  |  |
| 13 | `CHQ.NOM.RESERVED.8` | `ChqNomineeCumul_Reserved8` | TField |  |  |
| 14 | `CHQ.NOM.RESERVED.7` | `ChqNomineeCumul_Reserved7` | TField |  |  |
| 15 | `CHQ.NOM.RESERVED.6` | `ChqNomineeCumul_Reserved6` | TField |  |  |
| 16 | `CHQ.NOM.RESERVED.5` | `ChqNomineeCumul_Reserved5` | TField |  |  |
| 17 | `CHQ.NOM.RESERVED.4` | `ChqNomineeCumul_Reserved4` | TField |  |  |
| 18 | `CHQ.NOM.RESERVED.3` | `ChqNomineeCumul_Reserved3` | TField |  |  |
| 19 | `CHQ.NOM.RESERVED.2` | `ChqNomineeCumul_Reserved2` | TField |  |  |
| 20 | `CHQ.NOM.RESERVED.1` | `ChqNomineeCumul_Reserved1` | TField |  |  |
