# CAMB.H.SHARES.RULE — Table Schema

> Source: `INSERTS/I_F.CAMB.H.SHARES.RULE` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.SHARES.MEMBERSHIP.SHARES` | `CambHSharesRule_MembershipShares` | TField |  | This field is used to define whether the membership shares to be allotted or not.Yes_No type field.Yes - Membership shares allowed.No - Membership shares is not allowed.Note: Share Account Creation for Cif/Member is applicable for FI using container concept. |
| 2 | `CAMB.SHARES.MIN.QUANTITY` | `CambHSharesRule_MinQuantity` | TField |  | The purpose of this field is used to define the quantity of the share to be allotted for the membership.Allowed value are numeric valueEx. 5, 10 etc.Validation: If this field is blank, system will display a warning message. |
| 3 | `CAMB.SHARES.SECTOR.ALLOW` | `CambHSharesRule_SectorAllow` |  |  |  |
| 4 | `CAMB.SHARES.INDUSTRY.ALLOW` | `CambHSharesRule_IndustryAllow` |  |  |  |
| 5 | `CAMB.SHARES.ALLOW.MEMBERSHIP` | `CambHSharesRule_AllowMembership` | TField |  | The purpose of this field is used to define whether the shares account creation is allowed for membership/container or not. Allowed inputs: Yes_No_None Yes - Share Account creation is allowed for Members. No/None - Share Account creation is allowed for CIF and not Members. Note: Share Account Creation for Cif/Member is applicable for FI using container concept. |
| 6 | `CAMB.SHARES.RESERVED.2` | `CambHSharesRule_Reserved2` | TField |  |  |
| 7 | `CAMB.SHARES.RESERVED.3` | `CambHSharesRule_Reserved3` | TField |  |  |
| 8 | `CAMB.SHARES.RESERVED.4` | `CambHSharesRule_Reserved4` | TField |  |  |
| 9 | `CAMB.SHARES.RESERVED.5` | `CambHSharesRule_Reserved5` | TField |  |  |
| 10 | `CAMB.SHARES.RECORD.STATUS` | `CambHSharesRule_RecordStatus` | String |  |  |
| 11 | `CAMB.SHARES.CURR.NO` | `CambHSharesRule_CurrNo` | String |  |  |
| 12 | `CAMB.SHARES.INPUTTER` | `CambHSharesRule_Inputter` |  |  |  |
| 13 | `CAMB.SHARES.DATE.TIME` | `CambHSharesRule_DateTime` |  |  |  |
| 14 | `CAMB.SHARES.AUTHORISER` | `CambHSharesRule_Authoriser` | String |  |  |
| 15 | `CAMB.SHARES.CO.CODE` | `CambHSharesRule_CoCode` | String |  |  |
| 16 | `CAMB.SHARES.DEPT.CODE` | `CambHSharesRule_DeptCode` | String |  |  |
| 17 | `CAMB.SHARES.AUDITOR.CODE` | `CambHSharesRule_AuditorCode` | String |  |  |
| 18 | `CAMB.SHARES.AUDIT.DATE.TIME` | `CambHSharesRule_AuditDateTime` | String |  |  |
