# CHANNEL.PERMISSION — Table Schema

> Source: `INSERTS/I_F.CHANNEL.PERMISSION` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AI.PER.DESCRIPTION` | `ChannelPermission_Description` |  |  |  |
| 2 | `AI.PER.PERMISSION.TYPE` | `ChannelPermission_PermissionType` | TField |  | Defines the type of permission.Individual type for Personal user and group type for Corporate or Intermediary user. Valid values INDIVIDUAL and GROUP. |
| 3 | `AI.PER.CUSTOMER` | `ChannelPermission_Customer` |  |  |  |
| 4 | `AI.PER.RELATED.CUSTOMER` | `ChannelPermission_RelatedCustomer` |  |  |  |
| 5 | `AI.PER.PRODUCT.GROUPS` | `ChannelPermission_ProductGroups` |  |  |  |
| 6 | `AI.PER.PRODUCT.GROUP.SEL` | `ChannelPermission_ProductGroupSel` |  |  |  |
| 7 | `AI.PER.DISPLAY.PRODUCTS` | `ChannelPermission_DisplayProducts` |  |  |  |
| 8 | `AI.PER.PRODUCT` | `ChannelPermission_Product` |  |  |  |
| 9 | `AI.PER.PRODUCT.SEL` | `ChannelPermission_ProductSel` |  |  |  |
| 10 | `AI.PER.SV.RESERVED.5` | `ChannelPermission_SvReserved5` |  |  |  |
| 11 | `AI.PER.SV.RESERVED.4` | `ChannelPermission_SvReserved4` |  |  |  |
| 12 | `AI.PER.SV.RESERVED.3` | `ChannelPermission_SvReserved3` |  |  |  |
| 13 | `AI.PER.SV.RESERVED.2` | `ChannelPermission_SvReserved2` |  |  |  |
| 14 | `AI.PER.SV.RESERVED.1` | `ChannelPermission_SvReserved1` |  |  |  |
| 15 | `AI.PER.RESERVED.5` | `ChannelPermission_Reserved5` | TField |  |  |
| 16 | `AI.PER.RESERVED.4` | `ChannelPermission_Reserved4` | TField |  |  |
| 17 | `AI.PER.RESERVED.3` | `ChannelPermission_Reserved3` | TField |  |  |
| 18 | `AI.PER.RESERVED.2` | `ChannelPermission_Reserved2` | TField |  |  |
| 19 | `AI.PER.RESERVED.1` | `ChannelPermission_Reserved1` | TField |  |  |
| 20 | `AI.PER.LOCAL.REF` | `ChannelPermission_LocalRef` |  |  |  |
| 21 | `AI.PER.OVERRIDE` | `ChannelPermission_Override` |  |  |  |
| 22 | `AI.PER.RECORD.STATUS` | `ChannelPermission_RecordStatus` | String |  |  |
| 23 | `AI.PER.CURR.NO` | `ChannelPermission_CurrNo` | String |  |  |
| 24 | `AI.PER.INPUTTER` | `ChannelPermission_Inputter` |  |  |  |
| 25 | `AI.PER.DATE.TIME` | `ChannelPermission_DateTime` |  |  |  |
| 26 | `AI.PER.AUTHORISER` | `ChannelPermission_Authoriser` | String |  |  |
| 27 | `AI.PER.CO.CODE` | `ChannelPermission_CoCode` | String |  |  |
| 28 | `AI.PER.DEPT.CODE` | `ChannelPermission_DeptCode` | String |  |  |
| 29 | `AI.PER.AUDITOR.CODE` | `ChannelPermission_AuditorCode` | String |  |  |
| 30 | `AI.PER.AUDIT.DATE.TIME` | `ChannelPermission_AuditDateTime` | String |  |  |
