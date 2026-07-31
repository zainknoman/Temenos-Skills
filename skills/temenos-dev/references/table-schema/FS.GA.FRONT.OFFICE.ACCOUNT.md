# FS.GA.FRONT.OFFICE.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FRONT.OFFICE.ACCOUNT` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FRONT.OFFICE.ACCOUNT.PARENT.REF.ID` | `FsGaFrontOfficeAccount_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FRONT.OFFICE.ACCOUNT.ORA.ROWID` | `FsGaFrontOfficeAccount_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FRONT.OFFICE.ACCOUNT.SOURCE.ACCOUNT` | `FsGaFrontOfficeAccount_SourceAccount` | TField |  | Source Account Multifonds DB Column is AIMCOMPANY_ID. |
| 4 | `FS.GA.FRONT.OFFICE.ACCOUNT.MULTIFONDS.FUND` | `FsGaFrontOfficeAccount_MultifondsFund` | TField |  | Multifonds Fund Multifonds DB Column is PTF_MULTIFONDS. |
| 5 | `FS.GA.FRONT.OFFICE.ACCOUNT.MODEL.FUND.ID` | `FsGaFrontOfficeAccount_ModelFundId` | TField |  | Model Fund Id Multifonds DB Column is MODEL_FUND_ID. |
| 6 | `FS.GA.FRONT.OFFICE.ACCOUNT.CLIENT.FUND.ID` | `FsGaFrontOfficeAccount_ClientFundId` | TField |  | Client Fund Id Multifonds DB Column is CLIENT_FUND_ID. |
| 7 | `FS.GA.FRONT.OFFICE.ACCOUNT.COMPANY.ID` | `FsGaFrontOfficeAccount_CompanyId` | TField |  | Company Id Multifonds DB Column is COMPANY_ID. |
| 8 | `FS.GA.FRONT.OFFICE.ACCOUNT.TRANSFER.AGENCY` | `FsGaFrontOfficeAccount_TransferAgency` | TField |  | Transfer Agency Multifonds DB Column is TA. |
| 9 | `FS.GA.FRONT.OFFICE.ACCOUNT.THIRD.PARTY.ADMINISTRATOR` | `FsGaFrontOfficeAccount_ThirdPartyAdministrator` | TField |  | Third Party Administrator Multifonds DB Column is TPA. |
| 10 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED10` | `FsGaFrontOfficeAccount_Reserved10` | TField |  |  |
| 11 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED9` | `FsGaFrontOfficeAccount_Reserved9` | TField |  |  |
| 12 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED8` | `FsGaFrontOfficeAccount_Reserved8` | TField |  |  |
| 13 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED7` | `FsGaFrontOfficeAccount_Reserved7` | TField |  |  |
| 14 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED6` | `FsGaFrontOfficeAccount_Reserved6` | TField |  |  |
| 15 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED5` | `FsGaFrontOfficeAccount_Reserved5` | TField |  |  |
| 16 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED4` | `FsGaFrontOfficeAccount_Reserved4` | TField |  |  |
| 17 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED3` | `FsGaFrontOfficeAccount_Reserved3` | TField |  |  |
| 18 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED2` | `FsGaFrontOfficeAccount_Reserved2` | TField |  |  |
| 19 | `FS.GA.FRONT.OFFICE.ACCOUNT.RESERVED1` | `FsGaFrontOfficeAccount_Reserved1` | TField |  |  |
| 20 | `FS.GA.FRONT.OFFICE.ACCOUNT.LOCAL.REF` | `FsGaFrontOfficeAccount_LocalRef` |  |  |  |
| 21 | `FS.GA.FRONT.OFFICE.ACCOUNT.OVERRIDE` | `FsGaFrontOfficeAccount_Override` |  |  |  |
| 22 | `FS.GA.FRONT.OFFICE.ACCOUNT.RECORD.STATUS` | `FsGaFrontOfficeAccount_RecordStatus` | String |  |  |
| 23 | `FS.GA.FRONT.OFFICE.ACCOUNT.CURR.NO` | `FsGaFrontOfficeAccount_CurrNo` | String |  |  |
| 24 | `FS.GA.FRONT.OFFICE.ACCOUNT.INPUTTER` | `FsGaFrontOfficeAccount_Inputter` |  |  |  |
| 25 | `FS.GA.FRONT.OFFICE.ACCOUNT.DATE.TIME` | `FsGaFrontOfficeAccount_DateTime` |  |  |  |
| 26 | `FS.GA.FRONT.OFFICE.ACCOUNT.AUTHORISER` | `FsGaFrontOfficeAccount_Authoriser` | String |  |  |
| 27 | `FS.GA.FRONT.OFFICE.ACCOUNT.CO.CODE` | `FsGaFrontOfficeAccount_CoCode` | String |  |  |
| 28 | `FS.GA.FRONT.OFFICE.ACCOUNT.DEPT.CODE` | `FsGaFrontOfficeAccount_DeptCode` | String |  |  |
| 29 | `FS.GA.FRONT.OFFICE.ACCOUNT.AUDITOR.CODE` | `FsGaFrontOfficeAccount_AuditorCode` | String |  |  |
| 30 | `FS.GA.FRONT.OFFICE.ACCOUNT.AUDIT.DATE.TIME` | `FsGaFrontOfficeAccount_AuditDateTime` | String |  |  |
