# DE.CUSTOMER.PREFERENCES — Table Schema

> Source: `INSERTS/I_F.DE.CUSTOMER.PREFERENCES` in `PF_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.CUSPR.MESSAGE.GROUP` | `DeCustomerPreferences_MessageGroup` |  |  |  |
| 2 | `DE.CUSPR.COPY.CUSTOMER` | `DeCustomerPreferences_CopyCustomer` |  |  |  |
| 3 | `DE.CUSPR.CARRIER` | `DeCustomerPreferences_Carrier` |  |  |  |
| 4 | `DE.CUSPR.REQUIRED` | `DeCustomerPreferences_Required` |  |  |  |
| 5 | `DE.CUSPR.ADDRESS` | `DeCustomerPreferences_Address` |  |  |  |
| 6 | `DE.CUSPR.FORMAT` | `DeCustomerPreferences_Format` |  |  |  |
| 7 | `DE.CUSPR.COPIES` | `DeCustomerPreferences_Copies` |  |  |  |
| 8 | `DE.CUSPR.LANGUAGE` | `DeCustomerPreferences_Language` |  |  |  |
| 9 | `DE.CUSPR.HOLD.OUTPUT` | `DeCustomerPreferences_HoldOutput` |  |  |  |
| 10 | `DE.CUSPR.HOLD.MAIL.START` | `DeCustomerPreferences_HoldMailStart` |  |  |  |
| 11 | `DE.CUSPR.HOLD.MAIL.END` | `DeCustomerPreferences_HoldMailEnd` |  |  |  |
| 12 | `DE.CUSPR.HOLD.MAIL.OPT` | `DeCustomerPreferences_HoldMailOpt` |  |  |  |
| 13 | `DE.CUSPR.START.DATE` | `DeCustomerPreferences_StartDate` |  |  |  |
| 14 | `DE.CUSPR.END.DATE` | `DeCustomerPreferences_EndDate` |  |  |  |
| 15 | `DE.CUSPR.RESERVED.8` | `DeCustomerPreferences_Reserved8` |  |  |  |
| 16 | `DE.CUSPR.RESERVED.9` | `DeCustomerPreferences_Reserved9` |  |  |  |
| 17 | `DE.CUSPR.RESERVED.10` | `DeCustomerPreferences_Reserved10` |  |  |  |
| 18 | `DE.CUSPR.DE.PRODUCT.ID` | `DeCustomerPreferences_DeProductId` |  |  |  |
| 19 | `DE.CUSPR.PRD.ID.REBUILD` | `DeCustomerPreferences_PrdIdRebuild` | TField |  | Flag to force the rebuild of the DE.PRODUCT keys updated in Customer preferences DE.PRODUCT.ID keys will be generated based on Message type defined in DE.MESSAGE.GROUP When DE.MESSAGE.GROUP is modified ,then corresponding Customer Preferences record need to be rebuild. Validation Rules: 1) Tick box field. |
| 20 | `DE.CUSPR.SMS.ADDRESS` | `DeCustomerPreferences_SmsAddress` |  |  |  |
| 21 | `DE.CUSPR.BLACKOUT.START` | `DeCustomerPreferences_BlackoutStart` |  |  |  |
| 22 | `DE.CUSPR.BLACKOUT.END` | `DeCustomerPreferences_BlackoutEnd` |  |  |  |
| 23 | `DE.CUSPR.OFFSET` | `DeCustomerPreferences_Offset` | TField |  | Holds the time zone differences between the customers Home time zone and UST (Universal Standard Time). Validation rules: Entered in PLUS HH:MM or MINUS HH:MM format , Example, Customer in Paris will enter +01:00 hours and Customer in Central America will enter -06:00 hours denoting time difference with UST |
| 24 | `DE.CUSPR.DEFAULT.STMT.FQU1` | `DeCustomerPreferences_DefaultStmtFqu1` | TField |  | Validation rules: Must be a valid Date Frequency At the time of Creating the new Arrangements, the system would default Statement Frequency 1 |
| 25 | `DE.CUSPR.PRINT.ATTR.NAME` | `DeCustomerPreferences_PrintAttrName` |  |  |  |
| 26 | `DE.CUSPR.PRINT.ATTR.VALUE` | `DeCustomerPreferences_PrintAttrValue` |  |  |  |
| 27 | `DE.CUSPR.OTHER.MSG.HOLD.OUTPUT` | `DeCustomerPreferences_OtherMsgHoldOutput` |  |  |  |
| 28 | `DE.CUSPR.OTHER.MSG.HOLD.MAIL.START` | `DeCustomerPreferences_OtherMsgHoldMailStart` |  |  |  |
| 29 | `DE.CUSPR.OTHER.MSG.HOLD.MAIL.END` | `DeCustomerPreferences_OtherMsgHoldMailEnd` |  |  |  |
| 30 | `DE.CUSPR.OTHER.MSG.HOLD.MAIl.OPT` | `DeCustomerPreferences_OtherMsgHoldMailOpt` |  |  |  |
| 31 | `DE.CUSPR.OTHER.MSG.START.DATE` | `DeCustomerPreferences_OtherMsgStartDate` |  |  |  |
| 32 | `DE.CUSPR.OTHER.MSG.END.DATE` | `DeCustomerPreferences_OtherMsgEndDate` |  |  |  |
| 33 | `DE.CUSPR.OTHER.MSG.DE.PROD.ID` | `DeCustomerPreferences_OtherMsgDeProdId` |  |  |  |
| 34 | `DE.CUSPR.LOCAL.REF` | `DeCustomerPreferences_LocalRef` |  |  |  |
| 35 | `DE.CUSPR.OVERRIDE` | `DeCustomerPreferences_Override` |  |  |  |
| 36 | `DE.CUSPR.RECORD.STATUS` | `DeCustomerPreferences_RecordStatus` | String |  |  |
| 37 | `DE.CUSPR.CURR.NO` | `DeCustomerPreferences_CurrNo` | String |  |  |
| 38 | `DE.CUSPR.INPUTTER` | `DeCustomerPreferences_Inputter` |  |  |  |
| 39 | `DE.CUSPR.DATE.TIME` | `DeCustomerPreferences_DateTime` |  |  |  |
| 40 | `DE.CUSPR.AUTHORISER` | `DeCustomerPreferences_Authoriser` | String |  |  |
| 41 | `DE.CUSPR.CO.CODE` | `DeCustomerPreferences_CoCode` | String |  |  |
| 42 | `DE.CUSPR.DEPT.CODE` | `DeCustomerPreferences_DeptCode` | String |  |  |
| 43 | `DE.CUSPR.AUDITOR.CODE` | `DeCustomerPreferences_AuditorCode` | String |  |  |
| 44 | `DE.CUSPR.AUDIT.DATE.TIME` | `DeCustomerPreferences_AuditDateTime` | String |  |  |
| 45 | `DE.CUSPR.ROLE` | `DeCustomerPreferences_Role` |  |  |  |
| 46 | `DE.CUSPR.APPLY.OTHER.MSG` | `DeCustomerPreferences_ApplyOtherMsgs` | TField |  | Identifies the customer preferences for receiving any message group for which specific preferences have not been defined. It will be either blank or YES. |
| 47 | `DE.CUSPR.OTHER.MSG.ROLE` | `DeCustomerPreferences_OtherMsgRole` | TField |  | Specifies the role of the customer for the APPLY TO OTHER MESSAGES. Validation Rule: Applicable if AA is installed and must be a valid record in AA.CUSTOMER.ROLE |
| 48 | `DE.CUSPR.OTHER.MSG.COPY.CUST` | `DeCustomerPreferences_OtherMsgCopyCust` |  |  |  |
| 49 | `DE.CUSPR.OTHER.MSG.CARRIER` | `DeCustomerPreferences_OtherMsgCarrier` |  |  |  |
| 50 | `DE.CUSPR.OTHER.MSG.REQD` | `DeCustomerPreferences_OtherMsgReqd` |  |  |  |
| 51 | `DE.CUSPR.OTHER.MSG.ADDRESS` | `DeCustomerPreferences_OtherMsgAddress` |  |  |  |
| 52 | `DE.CUSPR.OTHER.MSG.FORMAT` | `DeCustomerPreferences_OtherMsgFormat` |  |  |  |
| 53 | `DE.CUSPR.OTHER.MSG.COPIES` | `DeCustomerPreferences_OtherMsgCopies` |  |  |  |
| 54 | `DE.CUSPR.OTHER.MSG.LANG` | `DeCustomerPreferences_OtherMsgLang` |  |  |  |
| 55 | `DE.CUSPR.CUSTOMER.REFERENCE` | `DeCustomerPreferences_CusprCustomerReference` |  |  |  |
| 56 | `DE.CUSPR.ACCOUNT.REFERENCE` | `DeCustomerPreferences_CusprAccountReference` |  |  |  |
| 57 | `DE.CUSPR.PORTFOLIO.REFERENCE` | `DeCustomerPreferences_CusprPortfolioReference` |  |  |  |
| 58 | `DE.CUSPR.PREFERENCE.TYPE` | `DeCustomerPreferences_CusprPreferenceType` |  |  |  |
| 59 | `DE.CUSPR.OTHER.RECIPIENT.REFERENCE` | `DeCustomerPreferences_CusprOtherRecipientReference` |  |  |  |
