# CARD.ISSUE.RESTRICT — Table Schema

> Source: `INSERTS/I_F.CARD.ISSUE.RESTRICT` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAIS.REST.DESCRIPTION` | `CardIssueRestrict_Description` |  |  |  |
| 2 | `CAIS.REST.APPL.FLD` | `CardIssueRestrict_ApplFld` |  |  |  |
| 3 | `CAIS.REST.APPL.OPR` | `CardIssueRestrict_ApplOpr` |  |  |  |
| 4 | `CAIS.REST.FR.APPL.VALUE` | `CardIssueRestrict_FrApplValue` |  |  |  |
| 5 | `CAIS.REST.TO.APPL.VALUE` | `CardIssueRestrict_ToApplValue` |  |  |  |
| 6 | `CAIS.REST.RESERVED.15` | `CardIssueRestrict_Reserved15` |  |  |  |
| 7 | `CAIS.REST.RESERVED.14` | `CardIssueRestrict_Reserved14` |  |  |  |
| 8 | `CAIS.REST.RESERVED.13` | `CardIssueRestrict_Reserved13` |  |  |  |
| 9 | `CAIS.REST.RESERVED.12` | `CardIssueRestrict_Reserved12` |  |  |  |
| 10 | `CAIS.REST.RESERVED.11` | `CardIssueRestrict_Reserved11` |  |  |  |
| 11 | `CAIS.REST.CUSTOM.RTN` | `CardIssueRestrict_CustomRtn` | TField |  | The purpose of this field is to attach customized routine to perform validation. Either APPL.FLD or CUSTOM.RTN should be defined . The CUSTOM.RTN can have 3 arguments. 1st Argument as incoming of Application record id (ex if @id as CUSTOMER then Customer Id as incoming argument) and 2nd argument for future use. 3rd argument as outgoing argument should have Yes or No value. If it returning as Yes then system will raise the override/error for card issue restrict Validation Rules: Length 50 Type A |
| 12 | `CAIS.REST.ELG.CUS.FLDS` | `CardIssueRestrict_ElgCusFlds` |  |  |  |
| 13 | `CAIS.REST.ELG.DOR.STAT` | `CardIssueRestrict_ElgDorStat` |  |  |  |
| 14 | `CAIS.REST.DORMANCY.CHECK` | `CardIssueRestrict_DormancyCheck` | TField |  | The purpose of this field is used to validate whether the account is in dormancy status during card reordering.Note: This is applicable only for SYSTEM record in CARD.ISSUE.RESTRICT table.Allowed values are:ALL.ACCOUNT - If all account is set then system will check all the account dormancy status and if all the accounts are dormant system will restrict the card reorder with an override.SINGLE.ACCOUNT - If single account is set then system will check the accounts of the customer and if anyone account is dormancy status. System will restrict the card reorder with an override. |
| 15 | `CAIS.REST.CHANNEL.FOR.REORDER` | `CardIssueRestrict_ChannelForReorder` | TField |  | This field has valid record from CARD.INTERFACE.TABLE. If the field is configured with any interface value during COB reorder, accounts under the configured interfacewill be taken into consideration for dormancy check. If no value is defined all the accounts of the card will be validated for dormancy. |
| 16 | `CAIS.REST.RESERVED.8` | `CardIssueRestrict_Reserved8` | TField |  |  |
| 17 | `CAIS.REST.RESERVED.7` | `CardIssueRestrict_Reserved7` | TField |  |  |
| 18 | `CAIS.REST.RESERVED.6` | `CardIssueRestrict_Reserved6` | TField |  |  |
| 19 | `CAIS.REST.RESERVED.5` | `CardIssueRestrict_Reserved5` | TField |  |  |
| 20 | `CAIS.REST.RESERVED.4` | `CardIssueRestrict_Reserved4` | TField |  |  |
| 21 | `CAIS.REST.RESERVED.3` | `CardIssueRestrict_Reserved3` | TField |  |  |
| 22 | `CAIS.REST.RESERVED.2` | `CardIssueRestrict_Reserved2` | TField |  |  |
| 23 | `CAIS.REST.RESERVED.1` | `CardIssueRestrict_Reserved1` | TField |  |  |
| 24 | `CAIS.REST.LOCAL.REF` | `CardIssueRestrict_LocalRef` |  |  |  |
| 25 | `CAIS.REST.OVERRIDE` | `CardIssueRestrict_Override` |  |  |  |
| 26 | `CAIS.REST.RECORD.STATUS` | `CardIssueRestrict_RecordStatus` | String |  |  |
| 27 | `CAIS.REST.CURR.NO` | `CardIssueRestrict_CurrNo` | String |  |  |
| 28 | `CAIS.REST.INPUTTER` | `CardIssueRestrict_Inputter` |  |  |  |
| 29 | `CAIS.REST.DATE.TIME` | `CardIssueRestrict_DateTime` |  |  |  |
| 30 | `CAIS.REST.AUTHORISER` | `CardIssueRestrict_Authoriser` | String |  |  |
| 31 | `CAIS.REST.CO.CODE` | `CardIssueRestrict_CoCode` | String |  |  |
| 32 | `CAIS.REST.DEPT.CODE` | `CardIssueRestrict_DeptCode` | String |  |  |
| 33 | `CAIS.REST.AUDITOR.CODE` | `CardIssueRestrict_AuditorCode` | String |  |  |
| 34 | `CAIS.REST.AUDIT.DATE.TIME` | `CardIssueRestrict_AuditDateTime` | String |  |  |
