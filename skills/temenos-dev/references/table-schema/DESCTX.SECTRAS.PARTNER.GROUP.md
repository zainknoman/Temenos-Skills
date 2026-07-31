# DESCTX.SECTRAS.PARTNER.GROUP — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.PARTNER.GROUP` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.GROUP.OPEN.DATE` | `DesctxSectrasPartnerGroup_OpenDate` | TField |  | This field is used to capture the date when the partner group was created |
| 2 | `SECTRAS.GROUP.RPT.LANGUAGE` | `DesctxSectrasPartnerGroup_RptLanguage` | TField |  | This field is used to define the language of the Managing Customer |
| 3 | `SECTRAS.GROUP.LEGAL.TYPE` | `DesctxSectrasPartnerGroup_LegalType` | TField |  | This field is used to define the legal type id of the Customer |
| 4 | `SECTRAS.GROUP.EXT.CODE` | `DesctxSectrasPartnerGroup_ExtCode` | TField |  | This field is used to capture the partner group id |
| 5 | `SECTRAS.GROUP.EXT.CODE.TYPE` | `DesctxSectrasPartnerGroup_ExtCodeType` | TField |  | This field is used to define the data type of the partner group id, i.e Alphanumeric or Numeric |
| 6 | `SECTRAS.GROUP.GROUP.TYPE` | `DesctxSectrasPartnerGroup_GroupType` | TField |  | This field is used to define the type of the partner group created. Various type of partner group are as below I-Individual C-Couple P-Partner F-Corporate P-Saving Club S-Trustee |
| 7 | `SECTRAS.GROUP.VALID.FROM` | `DesctxSectrasPartnerGroup_ValidFrom` | TField |  | This field is used to define the date from which the partner group is valid |
| 8 | `SECTRAS.GROUP.MANAGING.PARTNER` | `DesctxSectrasPartnerGroup_ManagingPartner` |  |  |  |
| 9 | `SECTRAS.GROUP.ROLE.OWNERSHIP` | `DesctxSectrasPartnerGroup_RoleOwnership` |  |  |  |
| 10 | `SECTRAS.GROUP.ROLE.BEN.ONWER` | `DesctxSectrasPartnerGroup_RoleBenOnwer` |  |  |  |
| 11 | `SECTRAS.GROUP.AC.EXT.CODE.TYPE` | `DesctxSectrasPartnerGroup_AcExtCodeType` |  |  |  |
| 12 | `SECTRAS.GROUP.AC.EXT.CODE` | `DesctxSectrasPartnerGroup_AcExtCode` |  |  |  |
| 13 | `SECTRAS.GROUP.LOCAL.REF` | `DesctxSectrasPartnerGroup_LocalRef` |  |  |  |
| 14 | `SECTRAS.GROUP.CLOSE.DATE` | `DesctxSectrasPartnerGroup_CloseDate` | TField |  | This field is used to capture the close date of the partner group |
| 15 | `SECTRAS.GROUP.CLOSE.REASON` | `DesctxSectrasPartnerGroup_CloseReason` | TField |  | This field is used to capture the closure reason of the partner group |
| 16 | `SECTRAS.GROUP.TAX.SETTLEMENT.ACCOUNT` | `DesctxSectrasPartnerGroup_TaxSettlementAccount` | TField |  | This field is used to capture the tax settlement account of the partner group |
| 17 | `SECTRAS.GROUP.ALTERNATE.ID` | `DesctxSectrasPartnerGroup_AlternateId` | TField |  | This field is used for migration purposes and will contain the ID of the partner group of the legacy system |
| 18 | `SECTRAS.GROUP.CONTROLLING.PERSON` | `DesctxSectrasPartnerGroup_ControllingPerson` | TField |  |  |
| 19 | `SECTRAS.GROUP.RESERVED.3` | `DesctxSectrasPartnerGroup_Reserved3` | TField |  |  |
| 20 | `SECTRAS.GROUP.RESERVED.2` | `DesctxSectrasPartnerGroup_Reserved2` | TField |  |  |
| 21 | `SECTRAS.GROUP.RESERVED.1` | `DesctxSectrasPartnerGroup_Reserved1` | TField |  |  |
| 22 | `SECTRAS.GROUP.OVERRIDE` | `DesctxSectrasPartnerGroup_Override` |  |  |  |
| 23 | `SECTRAS.GROUP.RECORD.STATUS` | `DesctxSectrasPartnerGroup_RecordStatus` | String |  |  |
| 24 | `SECTRAS.GROUP.CURR.NO` | `DesctxSectrasPartnerGroup_CurrNo` | String |  |  |
| 25 | `SECTRAS.GROUP.INPUTTER` | `DesctxSectrasPartnerGroup_Inputter` |  |  |  |
| 26 | `SECTRAS.GROUP.DATE.TIME` | `DesctxSectrasPartnerGroup_DateTime` |  |  |  |
| 27 | `SECTRAS.GROUP.AUTHORISER` | `DesctxSectrasPartnerGroup_Authoriser` | String |  |  |
| 28 | `SECTRAS.GROUP.CO.CODE` | `DesctxSectrasPartnerGroup_CoCode` | String |  |  |
| 29 | `SECTRAS.GROUP.DEPT.CODE` | `DesctxSectrasPartnerGroup_DeptCode` | String |  |  |
| 30 | `SECTRAS.GROUP.AUDITOR.CODE` | `DesctxSectrasPartnerGroup_AuditorCode` | String |  |  |
| 31 | `SECTRAS.GROUP.AUDIT.DATE.TIME` | `DesctxSectrasPartnerGroup_AuditDateTime` | String |  |  |
