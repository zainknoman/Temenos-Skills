# LBNCDR.PARTNER.TYPE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.PARTNER.TYPE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.PA.DESCRIPTION.LATIN` | `LbncdrPartnerType_DescriptionLatin` | TField |  | Holds Partner Description value Validation Rules 50 A |
| 2 | `LBNCDR.PA.RESERVED.10` | `LbncdrPartnerType_Reserved10` | TField |  | Validation Rules |
| 3 | `LBNCDR.PA.RESERVED.9` | `LbncdrPartnerType_Reserved9` | TField |  | Validation Rules |
| 4 | `LBNCDR.PA.RESERVED.8` | `LbncdrPartnerType_Reserved8` | TField |  | Validation Rules |
| 5 | `LBNCDR.PA.RESERVED.7` | `LbncdrPartnerType_Reserved7` | TField |  | Validation Rules |
| 6 | `LBNCDR.PA.RESERVED.6` | `LbncdrPartnerType_Reserved6` | TField |  | Validation Rules |
| 7 | `LBNCDR.PA.RESERVED.5` | `LbncdrPartnerType_Reserved5` | TField |  | Validation Rules |
| 8 | `LBNCDR.PA.RESERVED.4` | `LbncdrPartnerType_Reserved4` | TField |  | Validation Rules |
| 9 | `LBNCDR.PA.RESERVED.3` | `LbncdrPartnerType_Reserved3` | TField |  | Validation Rules |
| 10 | `LBNCDR.PA.RESERVED.2` | `LbncdrPartnerType_Reserved2` | TField |  | Validation Rules |
| 11 | `LBNCDR.PA.RESERVED.1` | `LbncdrPartnerType_Reserved1` | TField |  | Validation Rules |
| 12 | `LBNCDR.PA.OVERRIDE` | `LbncdrPartnerType_Override` |  |  |  |
| 13 | `LBNCDR.PA.RECORD.STATUS` | `LbncdrPartnerType_RecordStatus` | String |  |  |
| 14 | `LBNCDR.PA.CURR.NO` | `LbncdrPartnerType_CurrNo` | String |  |  |
| 15 | `LBNCDR.PA.INPUTTER` | `LbncdrPartnerType_Inputter` |  |  |  |
| 16 | `LBNCDR.PA.DATE.TIME` | `LbncdrPartnerType_DateTime` |  |  |  |
| 17 | `LBNCDR.PA.AUTHORISER` | `LbncdrPartnerType_Authoriser` | String |  |  |
| 18 | `LBNCDR.PA.CO.CODE` | `LbncdrPartnerType_CoCode` | String |  |  |
| 19 | `LBNCDR.PA.DEPT.CODE` | `LbncdrPartnerType_DeptCode` | String |  |  |
| 20 | `LBNCDR.PA.AUDITOR.CODE` | `LbncdrPartnerType_AuditorCode` | String |  |  |
| 21 | `LBNCDR.PA.AUDIT.DATE.TIME` | `LbncdrPartnerType_AuditDateTime` | String |  |  |
