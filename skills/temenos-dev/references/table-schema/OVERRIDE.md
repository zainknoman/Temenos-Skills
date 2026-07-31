# OVERRIDE — Table Schema

> Source: `INSERTS/I_F.OVERRIDE` in `EB_OverrideProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.OR.MESSAGE` | `Override_Message` |  |  |  |
| 2 | `EB.OR.TYPE` | `Override_Type` |  |  |  |
| 3 | `EB.OR.CHANNEL` | `Override_Channel` |  |  |  |
| 4 | `EB.OR.APPROVE.METHOD` | `Override_ApproveMethod` |  |  |  |
| 5 | `EB.OR.OVERRIDE.ACTION` | `Override_OverrideAction` |  |  |  |
| 6 | `EB.OR.RAISE.EVENT` | `Override_RaiseEvent` |  |  |  |
| 7 | `EB.OR.RESERVED13` | `Override_Reserved13` |  |  |  |
| 8 | `EB.OR.RESERVED14` | `Override_Reserved14` |  |  |  |
| 9 | `EB.OR.RESERVED15` | `Override_Reserved15` |  |  |  |
| 10 | `EB.OR.RESERVED16` | `Override_Reserved16` |  |  |  |
| 11 | `EB.OR.PREV.MESSAGE` | `Override_PrevMessage` |  |  |  |
| 12 | `EB.OR.NUMERIC.ID` | `Override_NumericId` | TField |  | This field is the key identification number for override message. Validation Rules: System generated field |
| 13 | `EB.OR.RESERVED03` | `Override_Reserved03` | TField |  |  |
| 14 | `EB.OR.APPLICATION` | `Override_Application` |  |  |  |
| 15 | `EB.OR.CLASS` | `Override_Class` |  |  |  |
| 16 | `EB.OR.DETAIL` | `Override_Detail` |  |  |  |
| 17 | `EB.OR.DISPO` | `Override_Dispo` |  |  |  |
| 18 | `EB.OR.CON.OVERRIDE` | `Override_ConOverride` |  |  |  |
| 19 | `EB.OR.TRANSACTION.IND` | `Override_TransactionInd` |  |  |  |
| 20 | `EB.OR.PRECEDENCE` | `Override_Precedence` |  |  |  |
| 21 | `EB.OR.RESERVED.4` | `Override_Reserved4` |  |  |  |
| 22 | `EB.OR.RESERVED.5` | `Override_Reserved5` |  |  |  |
| 23 | `EB.OR.DISPO.OFFICER` | `Override_DispoOfficer` |  |  |  |
| 24 | `EB.OR.HELP.TYPE` | `Override_HelpType` | TField |  | Defines the format of the help message associated with this override. Validation Rules: Must be either TEXT , HTML or RICHTEXT |
| 25 | `EB.OR.HELPTEXT` | `Override_Helptext` |  |  |  |
| 26 | `EB.OR.LEVEL` | `Override_Level` | TField |  | This field determines the order that the Dispo Transactions will be displayed in on the application DISPO.ITEMS. 1 representing the highest level 99 the lowest, thus in DISPO.ITEMS the transactions with a LEVEL of 1 will be displayed ahead of transactions with a level of 2 and so on up to a level of 999. Validation Rules: Numeric input, three characters. Giving a range of 1-999. |
| 27 | `EB.OR.DISPO.ALLOWED` | `Override_DispoAllowed` | TField |  | YES - Specify whether DISPO is allowed for this override message. This entry, which cannot be input on site, DISPO, DISPO.OFFICER FORCE - Enforce DISPO items for this override message specially for external DDA systems Cannot be input on site APPLICATION, DISPO and DISPO.OFFICER need not be set up for this FORCE type Validation Rules: "YES" or FORCE or blank Cannot be input on site. |
| 28 | `EB.OR.CREATE.OVE.LIST` | `Override_CreateOveList` |  |  |  |
| 29 | `EB.OR.OVE.SUPPRESSION` | `Override_OveSuppression` |  |  |  |
| 30 | `EB.OR.EXACT.MATCH` | `Override_ExactMatch` | TField |  | When checking if an OVERRIDE message has already been accepted, the system needs to know how to match the OVERRIDE message. YES - The OVERRIDE suppression programs will check the message exactly, including all values in the message. If any of the values do not match then the OVERRIDE will be shown. If the OVERRIDE message is exactly the same as the one stored in the EB.OVERRIDE.APPROVED file then the OVERRIDE message will be suppressed. NO - The OVERRIDE suppression programs will only check the Internal ID of the OVERRIDE, therefore if any of the text changes in the OVERRIDE the message will still be suppressed. E.g. If the OVERRIDE CASH.FLOW.OVERDRAFT creates the message "15/01/02 18599 CASH FLOW OVERDRAFT GBP -2234.99" has already been created in a previous application but the application we are in creates the same OVERRIDE with the message "15/01/02 18599 CASH FLOW OVERDRAFT GBP With EXACT.MATCH set to "NO" the system will compare the two OVERRIDE message ID's which are both CASH.FLOW.OVERDRAFT &amp; therefore suppress the message. With EXACT.MATCH set to "YES" not only are the message ID's checked but also the text. In this example the ID's match but the text is different because the overdraft amount has changed. Therefore this message will not be suppressed &amp; will be displayed. Validation Rules: YES or NO Cannot be input unless the SC product is installed. |
| 31 | `EB.OR.OFS.SOURCE` | `Override_OfsSource` |  |  |  |
| 32 | `EB.OR.APP.VERSION` | `Override_AppVersion` |  |  |  |
| 33 | `EB.OR.SUBROUTINE` | `Override_Subroutine` |  |  |  |
| 34 | `EB.OR.VALIDATION` | `Override_Validation` |  |  |  |
| 35 | `EB.OR.CONDITION` | `Override_Condition` |  |  |  |
| 36 | `EB.OR.DATA.POSN` | `Override_DataPosn` |  |  |  |
| 37 | `EB.OR.OPERATOR` | `Override_Operator` |  |  |  |
| 38 | `EB.OR.VALUE` | `Override_Value` |  |  |  |
| 39 | `EB.OR.SEPARATOR` | `Override_Separator` |  |  |  |
| 40 | `EB.OR.ACTION` | `Override_Action` |  |  |  |
| 41 | `EB.OR.INFO` | `Override_Info` |  |  |  |
| 42 | `EB.OR.SYSTEM` | `Override_System` | TField |  | This determines if the Override message is part of the T24 core software &amp; not user defined. Validation Rules: This field cannot be input on site. |
| 43 | `EB.OR.SUSP.APPLN` | `Override_SuspAppln` |  |  |  |
| 44 | `EB.OR.SUSP.COND.RTN` | `Override_SuspCondRtn` |  |  |  |
| 45 | `EB.OR.FWD.ACCT.MODE` | `Override_FwdAcctMode` |  |  |  |
| 46 | `EB.OR.LOCAL.REF` | `Override_LocalRef` |  |  |  |
| 47 | `EB.OR.RESERVED01` | `Override_Reserved01` | TField |  |  |
| 48 | `EB.OR.RECORD.STATUS` | `Override_RecordStatus` | String |  |  |
| 49 | `EB.OR.CURR.NO` | `Override_CurrNo` | String |  |  |
| 50 | `EB.OR.INPUTTER` | `Override_Inputter` |  |  |  |
| 51 | `EB.OR.DATE.TIME` | `Override_DateTime` |  |  |  |
| 52 | `EB.OR.AUTHORISER` | `Override_Authoriser` | String |  |  |
| 53 | `EB.OR.CO.CODE` | `Override_CoCode` | String |  |  |
| 54 | `EB.OR.DEPT.CODE` | `Override_DeptCode` | String |  |  |
| 55 | `EB.OR.AUDITOR.CODE` | `Override_AuditorCode` | String |  |  |
| 56 | `EB.OR.AUDIT.DATE.TIME` | `Override_AuditDateTime` | String |  |  |
