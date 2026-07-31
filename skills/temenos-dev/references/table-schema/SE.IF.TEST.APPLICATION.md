# SE.IF.TEST.APPLICATION — Table Schema

> Source: `INSERTS/I_F.SE.IF.TEST.APPLICATION` in `SE_TestOtherApplication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SITA.DESCRIPTION` | `SeIfTestApplication_Description` |  |  |  |
| 2 | `SITA.CUSTOMER` | `SeIfTestApplication_Customer` | TField |  |  |
| 3 | `SITA.ACCOUNT.OFFICER` | `SeIfTestApplication_AccountOfficer` |  |  |  |
| 4 | `SITA.CONTACT.NOTES` | `SeIfTestApplication_ContactNotes` |  |  |  |
| 5 | `SITA.ADDRESS` | `SeIfTestApplication_Address` |  |  |  |
| 6 | `SITA.START.DATE` | `SeIfTestApplication_StartDate` | TField |  |  |
| 7 | `SITA.NOTES` | `SeIfTestApplication_Notes` |  |  |  |
| 8 | `SITA.LEGAL.ID` | `SeIfTestApplication_LegalId` |  |  |  |
| 9 | `SITA.LEGAL.HOLDER.NAME` | `SeIfTestApplication_LegalHolderName` |  |  |  |
| 10 | `SITA.LEGAL.EXP.DATE` | `SeIfTestApplication_LegalExpDate` |  |  |  |
| 11 | `SITA.RELATION.CODE` | `SeIfTestApplication_RelationCode` |  |  |  |
| 12 | `SITA.REL.CUSTOMER` | `SeIfTestApplication_RelCustomer` |  |  |  |
| 13 | `SITA.ROLE` | `SeIfTestApplication_Role` |  |  |  |
| 14 | `SITA.ROLE.NOTES` | `SeIfTestApplication_RoleNotes` |  |  |  |
| 15 | `SITA.CONTRACT.TYPE` | `SeIfTestApplication_ContractType` |  |  |  |
| 16 | `SITA.CONTRACT.DESCRIPT` | `SeIfTestApplication_ContractDescript` |  |  |  |
| 17 | `SITA.START.CATEGORY` | `SeIfTestApplication_StartCategory` |  |  |  |
| 18 | `SITA.END.CATEGORY` | `SeIfTestApplication_EndCategory` |  |  |  |
| 19 | `SITA.FIELD.NAME` | `SeIfTestApplication_FieldName` |  |  |  |
| 20 | `SITA.SPLIT.INC.EXC` | `SeIfTestApplication_SplitIncExc` |  |  |  |
| 21 | `SITA.FIELD.DESCRIPTION` | `SeIfTestApplication_FieldDescription` |  |  |  |
| 22 | `SITA.THRESHOLD.DESC` | `SeIfTestApplication_ThresholdDesc` |  |  |  |
| 23 | `SITA.THRESHOLD.TYPE` | `SeIfTestApplication_ThresholdType` |  |  |  |
| 24 | `SITA.ALLOWED.CATEGORY` | `SeIfTestApplication_AllowedCategory` |  |  |  |
| 25 | `SITA.VIOLATION.NUMBER` | `SeIfTestApplication_ViolationNumber` |  |  |  |
| 26 | `SITA.VIOLATION.ACTION` | `SeIfTestApplication_ViolationAction` |  |  |  |
| 27 | `SITA.DRAFT.DETAILS` | `SeIfTestApplication_DraftDetails` |  |  |  |
| 28 | `SITA.DRAFT.DATE` | `SeIfTestApplication_DraftDate` |  |  |  |
| 29 | `SITA.DRAFT.NUMBER` | `SeIfTestApplication_DraftNumber` |  |  |  |
| 30 | `SITA.DRAFT.ISSUE.TO` | `SeIfTestApplication_DraftIssueTo` |  |  |  |
| 31 | `SITA.DRAFT.AMOUNT` | `SeIfTestApplication_DraftAmount` |  |  |  |
| 32 | `SITA.APP.NAME` | `SeIfTestApplication_AppName` |  |  |  |
| 33 | `SITA.APP.VALUE` | `SeIfTestApplication_AppValue` |  |  |  |
| 34 | `SITA.EXCEPTION` | `SeIfTestApplication_Exception` |  |  |  |
| 35 | `SITA.ISSUE.CUSTOMERS` | `SeIfTestApplication_IssueCustomers` |  |  |  |
| 36 | `SITA.EXCHANGE.RATE` | `SeIfTestApplication_ExchangeRate` |  |  |  |
| 37 | `SITA.OTHER.OFFICER` | `SeIfTestApplication_OtherOfficer` |  |  |  |
| 38 | `SITA.RESERVED.19` | `SeIfTestApplication_Reserved19` | TField |  |  |
| 39 | `SITA.RESERVED.18` | `SeIfTestApplication_Reserved18` | TField |  |  |
| 40 | `SITA.RESERVED.17` | `SeIfTestApplication_Reserved17` | TField |  |  |
| 41 | `SITA.RESERVED.16` | `SeIfTestApplication_Reserved16` | TField |  |  |
| 42 | `SITA.RESERVED.15` | `SeIfTestApplication_Reserved15` | TField |  |  |
| 43 | `SITA.RESERVED.14` | `SeIfTestApplication_Reserved14` | TField |  |  |
| 44 | `SITA.RESERVED.13` | `SeIfTestApplication_Reserved13` | TField |  |  |
| 45 | `SITA.RESERVED.12` | `SeIfTestApplication_Reserved12` | TField |  |  |
| 46 | `SITA.RESERVED.11` | `SeIfTestApplication_Reserved11` | TField |  |  |
| 47 | `SITA.RESERVED.10` | `SeIfTestApplication_Reserved10` | TField |  |  |
| 48 | `SITA.RESERVED.9` | `SeIfTestApplication_Reserved9` | TField |  |  |
| 49 | `SITA.RESERVED.8` | `SeIfTestApplication_Reserved8` | TField |  |  |
| 50 | `SITA.RESERVED.7` | `SeIfTestApplication_Reserved7` | TField |  |  |
| 51 | `SITA.RESERVED.6` | `SeIfTestApplication_Reserved6` | TField |  |  |
| 52 | `SITA.RESERVED.5` | `SeIfTestApplication_Reserved5` | TField |  |  |
| 53 | `SITA.RESERVED.4` | `SeIfTestApplication_Reserved4` | TField |  |  |
| 54 | `SITA.RESERVED.3` | `SeIfTestApplication_Reserved3` | TField |  |  |
| 55 | `SITA.RESERVED.2` | `SeIfTestApplication_Reserved2` | TField |  |  |
| 56 | `SITA.RESERVED.1` | `SeIfTestApplication_Reserved1` | TField |  |  |
| 57 | `SITA.LOCAL.REF` | `SeIfTestApplication_LocalRef` |  |  |  |
| 58 | `SITA.OVERRIDE` | `SeIfTestApplication_Override` |  |  |  |
| 59 | `SITA.RECORD.STATUS` | `SeIfTestApplication_RecordStatus` | String |  |  |
| 60 | `SITA.CURR.NO` | `SeIfTestApplication_CurrNo` | String |  |  |
| 61 | `SITA.INPUTTER` | `SeIfTestApplication_Inputter` |  |  |  |
| 62 | `SITA.DATE.TIME` | `SeIfTestApplication_DateTime` |  |  |  |
| 63 | `SITA.AUTHORISER` | `SeIfTestApplication_Authoriser` | String |  |  |
| 64 | `SITA.CO.CODE` | `SeIfTestApplication_CoCode` | String |  |  |
| 65 | `SITA.DEPT.CODE` | `SeIfTestApplication_DeptCode` | String |  |  |
| 66 | `SITA.AUDITOR.CODE` | `SeIfTestApplication_AuditorCode` | String |  |  |
| 67 | `SITA.AUDIT.DATE.TIME` | `SeIfTestApplication_AuditDateTime` | String |  |  |
