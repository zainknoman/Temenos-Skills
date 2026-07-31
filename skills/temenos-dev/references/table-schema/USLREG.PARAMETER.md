# USLREG.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USLREG.PARAMETER` in `USLREG_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLREG.PARAM.DESCRIPTION` | `UslregParameter_Description` |  |  |  |
| 2 | `USLREG.PARAM.RESERVED.61` | `UslregParameter_Reserved61` |  |  |  |
| 3 | `USLREG.PARAM.RESERVED.60` | `UslregParameter_Reserved60` |  |  |  |
| 4 | `USLREG.PARAM.RESERVED.59` | `UslregParameter_Reserved59` |  |  |  |
| 5 | `USLREG.PARAM.RESERVED.58` | `UslregParameter_Reserved58` |  |  |  |
| 6 | `USLREG.PARAM.RESERVED.57` | `UslregParameter_Reserved57` |  |  |  |
| 7 | `USLREG.PARAM.RESERVED.56` | `UslregParameter_Reserved56` |  |  |  |
| 8 | `USLREG.PARAM.RESERVED.55` | `UslregParameter_Reserved55` | TField |  | Reserved for future developments |
| 9 | `USLREG.PARAM.RESERVED.54` | `UslregParameter_Reserved54` |  |  |  |
| 10 | `USLREG.PARAM.RESERVED.53` | `UslregParameter_Reserved53` |  |  |  |
| 11 | `USLREG.PARAM.RESERVED.52` | `UslregParameter_Reserved52` |  |  |  |
| 12 | `USLREG.PARAM.RESERVED.51` | `UslregParameter_Reserved51` |  |  |  |
| 13 | `USLREG.PARAM.RESERVED.50` | `UslregParameter_Reserved50` |  |  |  |
| 14 | `USLREG.PARAM.POSTING.RESTRICT` | `UslregParameter_PostingRestrict` | TField |  | Validation Rules:Upto 4 numeric character Posting Restriction code, based on EB.OBJECT.It must be an existing code on the POSTING.RESTRICT table. |
| 15 | `USLREG.PARAM.LATEFEE.PROPERTY` | `UslregParameter_LatefeeProperty` |  |  |  |
| 16 | `USLREG.PARAM.PRINCIPALINT.PROPERTY` | `UslregParameter_PrincipalintProperty` | TField |  | This field is used to define the principal interest property which gets principal interest amount. |
| 17 | `USLREG.PARAM.PENALTYINT.PROPERTY` | `UslregParameter_PenaltyintProperty` | TField |  | This field is used to define the penalty interest property which gets penalty interest amount |
| 18 | `USLREG.PARAM.REL.INT.CODE` | `UslregParameter_RelIntCode` |  |  |  |
| 19 | `USLREG.PARAM.PAYOFF.FEE.PROP` | `UslregParameter_PayoffFeeProp` |  |  |  |
| 20 | `USLREG.PARAM.RESERVED.44` | `UslregParameter_Reserved44` | TField |  | Reserved for future developments |
| 21 | `USLREG.PARAM.RESERVED.43` | `UslregParameter_Reserved43` | TField |  | Reserved for future developments |
| 22 | `USLREG.PARAM.RESERVED.42` | `UslregParameter_Reserved42` | TField |  | Reserved for future developments |
| 23 | `USLREG.PARAM.RESERVED.41` | `UslregParameter_Reserved41` | TField |  | Reserved for future developments |
| 24 | `USLREG.PARAM.RESERVED.40` | `UslregParameter_Reserved40` | TField |  | Reserved for future developments |
| 25 | `USLREG.PARAM.RESERVED.39` | `UslregParameter_Reserved39` | TField |  | Reserved for future developments |
| 26 | `USLREG.PARAM.RESERVED.38` | `UslregParameter_Reserved38` | TField |  | Reserved for future developments |
| 27 | `USLREG.PARAM.RESERVED.37` | `UslregParameter_Reserved37` | TField |  | Reserved for future developments |
| 28 | `USLREG.PARAM.RESERVED.36` | `UslregParameter_Reserved36` | TField |  | Reserved for future developments |
| 29 | `USLREG.PARAM.RESERVED.35` | `UslregParameter_Reserved35` | TField |  | Reserved for future developments |
| 30 | `USLREG.PARAM.RESERVED.34` | `UslregParameter_Reserved34` | TField |  | Reserved for future developments |
| 31 | `USLREG.PARAM.RESERVED.33` | `UslregParameter_Reserved33` | TField |  | Reserved for future developments |
| 32 | `USLREG.PARAM.RESERVED.32` | `UslregParameter_Reserved32` | TField |  | Reserved for future developments |
| 33 | `USLREG.PARAM.RESERVED.31` | `UslregParameter_Reserved31` | TField |  | Reserved for future developments |
| 34 | `USLREG.PARAM.RESERVED.30` | `UslregParameter_Reserved30` | TField |  | Reserved for future developments |
| 35 | `USLREG.PARAM.RESERVED.29` | `UslregParameter_Reserved29` | TField |  | Reserved for future developments |
| 36 | `USLREG.PARAM.RESERVED.28` | `UslregParameter_Reserved28` | TField |  | Reserved for future developments |
| 37 | `USLREG.PARAM.RESERVED.27` | `UslregParameter_Reserved27` | TField |  | Reserved for future developments |
| 38 | `USLREG.PARAM.RESERVED.26` | `UslregParameter_Reserved26` | TField |  | Reserved for future developments |
| 39 | `USLREG.PARAM.RESERVED.25` | `UslregParameter_Reserved25` | TField |  | Reserved for future developments |
| 40 | `USLREG.PARAM.RESERVED.24` | `UslregParameter_Reserved24` | TField |  | Reserved for future developments |
| 41 | `USLREG.PARAM.RESERVED.23` | `UslregParameter_Reserved23` | TField |  | Reserved for future developments |
| 42 | `USLREG.PARAM.RESERVED.22` | `UslregParameter_Reserved22` | TField |  | Reserved for future developments |
| 43 | `USLREG.PARAM.RESERVED.21` | `UslregParameter_Reserved21` | TField |  | Reserved for future developments |
| 44 | `USLREG.PARAM.RESERVED.20` | `UslregParameter_Reserved20` | TField |  | Reserved for future developments |
| 45 | `USLREG.PARAM.RESERVED.19` | `UslregParameter_Reserved19` | TField |  | Reserved for future developments |
| 46 | `USLREG.PARAM.RESERVED.18` | `UslregParameter_Reserved18` | TField |  | Reserved for future developments |
| 47 | `USLREG.PARAM.RESERVED.17` | `UslregParameter_Reserved17` | TField |  | Reserved for future developments |
| 48 | `USLREG.PARAM.RESERVED.16` | `UslregParameter_Reserved16` | TField |  | Reserved for future developments |
| 49 | `USLREG.PARAM.RESERVED.15` | `UslregParameter_Reserved15` | TField |  | Reserved for future developments |
| 50 | `USLREG.PARAM.RESERVED.14` | `UslregParameter_Reserved14` | TField |  | Reserved for future developments |
| 51 | `USLREG.PARAM.RESERVED.13` | `UslregParameter_Reserved13` | TField |  | Reserved for future developments |
| 52 | `USLREG.PARAM.RESERVED.12` | `UslregParameter_Reserved12` | TField |  | Reserved for future developments |
| 53 | `USLREG.PARAM.RESERVED.11` | `UslregParameter_Reserved11` | TField |  | Reserved for future developments |
| 54 | `USLREG.PARAM.RESERVED.10` | `UslregParameter_Reserved10` | TField |  | Reserved for future developments |
| 55 | `USLREG.PARAM.RESERVED.9` | `UslregParameter_Reserved9` | TField |  | Reserved for future developments |
| 56 | `USLREG.PARAM.RESERVED.8` | `UslregParameter_Reserved8` | TField |  | Reserved for future developments |
| 57 | `USLREG.PARAM.RESERVED.7` | `UslregParameter_Reserved7` | TField |  | Reserved for future developments |
| 58 | `USLREG.PARAM.RESERVED.6` | `UslregParameter_Reserved6` | TField |  | Reserved for future developments |
| 59 | `USLREG.PARAM.RESERVED.5` | `UslregParameter_Reserved5` | TField |  | Reserved for future developments |
| 60 | `USLREG.PARAM.RESERVED.4` | `UslregParameter_Reserved4` | TField |  | Reserved for future developments |
| 61 | `USLREG.PARAM.RESERVED.3` | `UslregParameter_Reserved3` | TField |  | Reserved for future developments |
| 62 | `USLREG.PARAM.RESERVED.2` | `UslregParameter_Reserved2` | TField |  | Reserved for future developments |
| 63 | `USLREG.PARAM.RESERVED.1` | `UslregParameter_Reserved1` | TField |  | Reserved for future developments |
| 64 | `USLREG.PARAM.OVERRIDE` | `UslregParameter_Override` |  |  |  |
| 65 | `USLREG.PARAM.RECORD.STATUS` | `UslregParameter_RecordStatus` | String |  |  |
| 66 | `USLREG.PARAM.CURR.NO` | `UslregParameter_CurrNo` | String |  |  |
| 67 | `USLREG.PARAM.INPUTTER` | `UslregParameter_Inputter` |  |  |  |
| 68 | `USLREG.PARAM.DATE.TIME` | `UslregParameter_DateTime` |  |  |  |
| 69 | `USLREG.PARAM.AUTHORISER` | `UslregParameter_Authoriser` | String |  |  |
| 70 | `USLREG.PARAM.CO.CODE` | `UslregParameter_CoCode` | String |  |  |
| 71 | `USLREG.PARAM.DEPT.CODE` | `UslregParameter_DeptCode` | String |  |  |
| 72 | `USLREG.PARAM.AUDITOR.CODE` | `UslregParameter_AuditorCode` | String |  |  |
| 73 | `USLREG.PARAM.AUDIT.DATE.TIME` | `UslregParameter_AuditDateTime` | String |  |  |
