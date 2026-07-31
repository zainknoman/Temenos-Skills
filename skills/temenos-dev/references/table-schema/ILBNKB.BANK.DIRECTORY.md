# ILBNKB.BANK.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.ILBNKB.BANK.DIRECTORY` in `CMBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BANK.DIR.BANK.CODE` | `IlbnkbBankDirectory_BankCode` | TField |  |  |
| 2 | `BANK.DIR.BANK.NAME` | `IlbnkbBankDirectory_BankName` |  |  |  |
| 3 | `BANK.DIR.BRANCH.CODE` | `IlbnkbBankDirectory_BranchCode` | TField |  |  |
| 4 | `BANK.DIR.BRANCH.NAME` | `IlbnkbBankDirectory_BranchName` |  |  |  |
| 5 | `BANK.DIR.ADDRESS` | `IlbnkbBankDirectory_Address` |  |  |  |
| 6 | `BANK.DIR.CITY` | `IlbnkbBankDirectory_City` |  |  |  |
| 7 | `BANK.DIR.ZIP.CODE` | `IlbnkbBankDirectory_ZipCode` | TField |  |  |
| 8 | `BANK.DIR.POST.OFFICE.BOX` | `IlbnkbBankDirectory_PostOfficeBox` | TField |  |  |
| 9 | `BANK.DIR.TELEPHONE` | `IlbnkbBankDirectory_Telephone` | TField |  |  |
| 10 | `BANK.DIR.FAX` | `IlbnkbBankDirectory_Fax` | TField |  |  |
| 11 | `BANK.DIR.FREE.TELEPHONE` | `IlbnkbBankDirectory_FreeTelephone` | TField |  |  |
| 12 | `BANK.DIR.HANDICAP.ACCESS` | `IlbnkbBankDirectory_HandicapAccess` | TField |  |  |
| 13 | `BANK.DIR.DAY.CLOSED` | `IlbnkbBankDirectory_DayClosed` | TField |  |  |
| 14 | `BANK.DIR.OPEN.DATE` | `IlbnkbBankDirectory_OpenDate` | TField |  |  |
| 15 | `BANK.DIR.CLOSE.DATE` | `IlbnkbBankDirectory_CloseDate` | TField |  |  |
| 16 | `BANK.DIR.DATE.OF.MODIFICATION` | `IlbnkbBankDirectory_DateOfModification` | TField |  |  |
| 17 | `BANK.DIR.TIME.OF.MODIFICATION` | `IlbnkbBankDirectory_TimeOfModification` | TField |  |  |
| 18 | `BANK.DIR.SETTLEMENT.DATE.START` | `IlbnkbBankDirectory_SettlementDateStart` | TField |  |  |
| 19 | `BANK.DIR.SETTLEMENT.DATE.END` | `IlbnkbBankDirectory_SettlementDateEnd` | TField |  |  |
| 20 | `BANK.DIR.ACTIVE.ENTITY` | `IlbnkbBankDirectory_ActiveEntity` | TField |  |  |
| 21 | `BANK.DIR.TYPE.OF.ACTION` | `IlbnkbBankDirectory_TypeOfAction` | TField |  |  |
| 22 | `BANK.DIR.LEGAL.ID` | `IlbnkbBankDirectory_LegalId` | TField |  |  |
| 23 | `BANK.DIR.NATIONAL.CLR.CODE` | `IlbnkbBankDirectory_NationalClrCode` | TField |  |  |
| 24 | `BANK.DIR.SCHEME` | `IlbnkbBankDirectory_Scheme` | TField |  |  |
| 25 | `BANK.DIR.INTERMEDIARY.NCC` | `IlbnkbBankDirectory_IntermediaryNcc` | TField |  |  |
| 26 | `BANK.DIR.COUNTRY` | `IlbnkbBankDirectory_Country` | TField |  |  |
| 27 | `BANK.DIR.ENTITY.TYPE` | `IlbnkbBankDirectory_EntityType` | TField |  |  |
| 28 | `BANK.DIR.RESERVED.5` | `IlbnkbBankDirectory_Reserved5` | TField |  |  |
| 29 | `BANK.DIR.RESERVED.4` | `IlbnkbBankDirectory_Reserved4` | TField |  |  |
| 30 | `BANK.DIR.RESERVED.3` | `IlbnkbBankDirectory_Reserved3` | TField |  |  |
| 31 | `BANK.DIR.RESERVED.2` | `IlbnkbBankDirectory_Reserved2` | TField |  |  |
| 32 | `BANK.DIR.RESERVED.1` | `IlbnkbBankDirectory_Reserved1` | TField |  |  |
| 33 | `BANK.DIR.LOCAL.REF` | `IlbnkbBankDirectory_LocalRef` |  |  |  |
| 34 | `BANK.DIR.OVERRIDE` | `IlbnkbBankDirectory_Override` |  |  |  |
| 35 | `BANK.DIR.RECORD.STATUS` | `IlbnkbBankDirectory_RecordStatus` | String |  |  |
| 36 | `BANK.DIR.CURR.NO` | `IlbnkbBankDirectory_CurrNo` | String |  |  |
| 37 | `BANK.DIR.INPUTTER` | `IlbnkbBankDirectory_Inputter` |  |  |  |
| 38 | `BANK.DIR.DATE.TIME` | `IlbnkbBankDirectory_DateTime` |  |  |  |
| 39 | `BANK.DIR.AUTHORISER` | `IlbnkbBankDirectory_Authoriser` | String |  |  |
| 40 | `BANK.DIR.CO.CODE` | `IlbnkbBankDirectory_CoCode` | String |  |  |
| 41 | `BANK.DIR.DEPT.CODE` | `IlbnkbBankDirectory_DeptCode` | String |  |  |
| 42 | `BANK.DIR.AUDITOR.CODE` | `IlbnkbBankDirectory_AuditorCode` | String |  |  |
| 43 | `BANK.DIR.AUDIT.DATE.TIME` | `IlbnkbBankDirectory_AuditDateTime` | String |  |  |
