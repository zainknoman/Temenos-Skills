# DESCTX.SECTRAS.STATIC.INFORMATION — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.STATIC.INFORMATION` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.STATIC.ACTUAL.CUSTOMER.ID` | `DesctxSectrasStaticInformation_ActualCustomerId` | TField |  | It denotes the Customer Id to which the extract is made |
| 2 | `SECTRAS.STATIC.PARTNER.GROUP.ID` | `DesctxSectrasStaticInformation_PartnerGroupId` | TField |  | It denotes the Partner group Id of the customer extracted. It will be combination of two partner Customer Id's or Account number generated for Customers |
| 3 | `SECTRAS.STATIC.STATIC.REQUEST.MSG` | `DesctxSectrasStaticInformation_StaticRequestMsg` |  |  |  |
| 4 | `SECTRAS.STATIC.STATIC.RESPONSE.MSG` | `DesctxSectrasStaticInformation_StaticResponseMsg` |  |  |  |
| 5 | `SECTRAS.STATIC.STATUS` | `DesctxSectrasStaticInformation_Status` | TField |  | It denotes the status of the response message whether it got processed or not Possible values are Success, Error |
| 6 | `SECTRAS.STATIC.RETURN.CODE` | `DesctxSectrasStaticInformation_ReturnCode` | TField |  | It describes the return code sent by the sectras system for the extract |
| 7 | `SECTRAS.STATIC.DETAIL.RETURN.CODE` | `DesctxSectrasStaticInformation_DetailReturnCode` | TField |  | It denotes the detailed description of the return code from the sectras system |
| 8 | `SECTRAS.STATIC.RETURN.ATTRIBUTE` | `DesctxSectrasStaticInformation_ReturnAttribute` |  |  |  |
| 9 | `SECTRAS.STATIC.LOCAL.REF` | `DesctxSectrasStaticInformation_LocalRef` |  |  |  |
| 10 | `SECTRAS.STATIC.RESERVED.8` | `DesctxSectrasStaticInformation_Reserved8` | TField |  |  |
| 11 | `SECTRAS.STATIC.RESERVED.7` | `DesctxSectrasStaticInformation_Reserved7` | TField |  |  |
| 12 | `SECTRAS.STATIC.RESERVED.6` | `DesctxSectrasStaticInformation_Reserved6` | TField |  |  |
| 13 | `SECTRAS.STATIC.RESERVED.5` | `DesctxSectrasStaticInformation_Reserved5` | TField |  |  |
| 14 | `SECTRAS.STATIC.RESERVED.4` | `DesctxSectrasStaticInformation_Reserved4` | TField |  |  |
| 15 | `SECTRAS.STATIC.RESERVED.3` | `DesctxSectrasStaticInformation_Reserved3` | TField |  |  |
| 16 | `SECTRAS.STATIC.RESERVED.2` | `DesctxSectrasStaticInformation_Reserved2` | TField |  |  |
| 17 | `SECTRAS.STATIC.RESERVED.1` | `DesctxSectrasStaticInformation_Reserved1` | TField |  |  |
| 18 | `SECTRAS.STATIC.OVERRIDE` | `DesctxSectrasStaticInformation_Override` |  |  |  |
| 19 | `SECTRAS.STATIC.RECORD.STATUS` | `DesctxSectrasStaticInformation_RecordStatus` | String |  |  |
| 20 | `SECTRAS.STATIC.CURR.NO` | `DesctxSectrasStaticInformation_CurrNo` | String |  |  |
| 21 | `SECTRAS.STATIC.INPUTTER` | `DesctxSectrasStaticInformation_Inputter` |  |  |  |
| 22 | `SECTRAS.STATIC.DATE.TIME` | `DesctxSectrasStaticInformation_DateTime` |  |  |  |
| 23 | `SECTRAS.STATIC.AUTHORISER` | `DesctxSectrasStaticInformation_Authoriser` | String |  |  |
| 24 | `SECTRAS.STATIC.CO.CODE` | `DesctxSectrasStaticInformation_CoCode` | String |  |  |
| 25 | `SECTRAS.STATIC.DEPT.CODE` | `DesctxSectrasStaticInformation_DeptCode` | String |  |  |
| 26 | `SECTRAS.STATIC.AUDITOR.CODE` | `DesctxSectrasStaticInformation_AuditorCode` | String |  |  |
| 27 | `SECTRAS.STATIC.AUDIT.DATE.TIME` | `DesctxSectrasStaticInformation_AuditDateTime` | String |  |  |
| 28 | `SECTRAS.STATIC.PSD.COMPONENTS` | `DesctxSectrasStaticInformation_PsdComponents` |  |  |  |
| 29 | `SECTRAS.STATIC.RELATION.CUSTOMER.ID` | `DesctxSectrasStaticInformation_RelationCustomerId` | TField |  | This field is used to store the contractual relationship Id, if it is available as part of the transaction |
| 30 | `SECTRAS.STATIC.POA.ID` | `DesctxSectrasStaticInformation_PoaId` | TField |  | This field is to store the ID of the power of attorney |
| 31 | `SECTRAS.STATIC.ACCOUNT.NO` | `DesctxSectrasStaticInformation_AccountNo` | TField |  | It holds the account number. This will be updated only if the 'account' component is delivered |
