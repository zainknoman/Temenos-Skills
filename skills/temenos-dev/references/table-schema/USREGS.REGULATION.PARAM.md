# USREGS.REGULATION.PARAM — Table Schema

> Source: `INSERTS/I_F.USREGS.REGULATION.PARAM` in `NACUST_CustomerHolds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.REG.PARAM.DESCRIPTION` | `UsregsRegulationParam_Description` |  |  |  |
| 2 | `US.REG.PARAM.CALENDAR` | `UsregsRegulationParam_Calendar` | TField | No | Should be a valid record id from the HOLIDAY application determining which calendar logic should be referred to determine the working /business days for hold condition. Validation Rules Optional input, Drop down values from the HOLIDAY table. |
| 3 | `US.REG.PARAM.EXPIRY.DATE` | `UsregsRegulationParam_ExpiryDate` | TField | No | This field helps to indicate the Expiry Date for the hold condition of an Account. Any hold placed for that Account after this expiry date will be considered as the new condition or it will default SYSTEM/ Customer hold condition. Validation Rules Optional input. Standard date format. |
| 4 | `US.REG.PARAM.NEW.ACCT.PERIOD` | `UsregsRegulationParam_NewAcctPeriod` | TField | No | Number of days till which the account is considered as a new account. Validation Rules 1-2 Numeric Characters, Optional Input. |
| 5 | `US.REG.PARAM.INPUT.DIR` | `UsregsRegulationParam_InputDir` | TField | Yes | Applicable only for TCPA Regulation. This field contains the "Do Not Call List" file upload directory path. Phone numbers in file(s) placed in path will be updated in USREGS.CONTACT.DETAILS on running the batch job USREGS.DNC.FILE.UPLOAD Validation Rules 65 Characters, Input must be a valid file path. Input mandatory for record id- TCPA |
| 6 | `US.REG.PARAM.RESERVED.09` | `UsregsRegulationParam_Reserved09` | TField |  |  |
| 7 | `US.REG.PARAM.AVAIL.AMOUNT` | `UsregsRegulationParam_AvailAmount` | TField | No | This field indicates the amount that will be available for immediate withdrawal for the customer. Validation Rules Up to 14 characters plus a decimal point (Standard Amount Format) - type AMT. (Optional input) |
| 8 | `US.REG.PARAM.AVAIL.METHOD` | `UsregsRegulationParam_AvailMethod` | TField |  | This field helps to choose the method of withdrawal for the Customer. If the value is selected as IMMEDIATE, then the amount given in the field AVAIL.AMOUNT will be immediately available to the Customer. If the value is selected as NEXTDAY, then the amount given in the field AVAIL.AMOUNT will be available next day to the Customer. Validation Rules Radio Button: Immediate, Next Day and Default Value - None. |
| 9 | `US.REG.PARAM.CHECK.TYPE` | `UsregsRegulationParam_CheckType` |  |  |  |
| 10 | `US.REG.PARAM.CURRENCY` | `UsregsRegulationParam_Currency` |  |  |  |
| 11 | `US.REG.PARAM.AMT.LESS.OR.EQ` | `UsregsRegulationParam_AmtLessOrEq` |  |  |  |
| 12 | `US.REG.PARAM.HOLD.DAYS1` | `UsregsRegulationParam_HoldDays1` |  |  |  |
| 13 | `US.REG.PARAM.AMOUNT.GREATER` | `UsregsRegulationParam_AmountGreater` |  |  |  |
| 14 | `US.REG.PARAM.HOLD.DAYS2` | `UsregsRegulationParam_HoldDays2` |  |  |  |
| 15 | `US.REG.PARAM.CCY.AVAIL.AMOUNT` | `UsregsRegulationParam_CcyAvailAmount` |  |  |  |
| 16 | `US.REG.PARAM.RESERVED.24` | `UsregsRegulationParam_Reserved24` |  |  |  |
| 17 | `US.REG.PARAM.RESERVED.23` | `UsregsRegulationParam_Reserved23` |  |  |  |
| 18 | `US.REG.PARAM.RESERVED.22` | `UsregsRegulationParam_Reserved22` |  |  |  |
| 19 | `US.REG.PARAM.RESERVED.21` | `UsregsRegulationParam_Reserved21` |  |  |  |
| 20 | `US.REG.PARAM.RESERVED.20` | `UsregsRegulationParam_Reserved20` |  |  |  |
| 21 | `US.REG.PARAM.RESERVED.19` | `UsregsRegulationParam_Reserved19` |  |  |  |
| 22 | `US.REG.PARAM.RESERVED.18` | `UsregsRegulationParam_Reserved18` |  |  |  |
| 23 | `US.REG.PARAM.RESERVED.17` | `UsregsRegulationParam_Reserved17` |  |  |  |
| 24 | `US.REG.PARAM.RESERVED.16` | `UsregsRegulationParam_Reserved16` |  |  |  |
| 25 | `US.REG.PARAM.RESERVED.15` | `UsregsRegulationParam_Reserved15` |  |  |  |
| 26 | `US.REG.PARAM.RESERVED.14` | `UsregsRegulationParam_Reserved14` |  |  |  |
| 27 | `US.REG.PARAM.RESERVED.13` | `UsregsRegulationParam_Reserved13` |  |  |  |
| 28 | `US.REG.PARAM.THRESHOLD.AMOUNT` | `UsregsRegulationParam_ThresholdAmount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `US.REG.PARAM.EXEMPT.PERIOD` | `UsregsRegulationParam_ExemptPeriod` | TField |  | Reserved for CTR development |
| 30 | `US.REG.PARAM.REL.CODE` | `UsregsRegulationParam_RelCode` |  |  |  |
| 31 | `US.REG.PARAM.W9.PERIOD` | `UsregsRegulationParam_W9Period` | TField | No | This field is used to indicate the number of days within which the form W9 has to be submitted for TIN/SSN certification. Validation Rules Optional Input, 1-4 numeric characters |
| 32 | `US.REG.PARAM.W8.BEN.PERIOD` | `UsregsRegulationParam_W8BenPeriod` | TField | No | This field denotes the allowed number of days for a foreign customer to be exempted from withholding the tax. Validation Rules Optional Input, 1-4 numeric characters |
| 33 | `US.REG.PARAM.BNOTICE.PERIOD` | `UsregsRegulationParam_BnoticePeriod` | TField | No | This field is used to indicate number of days within which the customer has to submit the revised TIN/SSN information received from the IRS department. The END.DATE will be defaulted in CUST.DOCUMENT application based on this field. Validation Rules Optional Input, 1-4 numeric characters |
| 34 | `US.REG.PARAM.SECTOR` | `UsregsRegulationParam_Sector` |  |  |  |
| 35 | `US.REG.PARAM.TRANSACTION` | `UsregsRegulationParam_Transaction` |  |  |  |
| 36 | `US.REG.PARAM.REGCC.CHECK.TYPE` | `UsregsRegulationParam_RegccCheckType` |  |  |  |
| 37 | `US.REG.PARAM.RESERVED.8` | `UsregsRegulationParam_Reserved8` |  |  |  |
| 38 | `US.REG.PARAM.RESERVED.7` | `UsregsRegulationParam_Reserved7` |  |  |  |
| 39 | `US.REG.PARAM.RESERVED.6` | `UsregsRegulationParam_Reserved6` |  |  |  |
| 40 | `US.REG.PARAM.CATEGORY` | `UsregsRegulationParam_Category` |  |  |  |
| 41 | `US.REG.PARAM.NOTES` | `UsregsRegulationParam_Notes` |  |  |  |
| 42 | `US.REG.PARAM.ALLOWED.SECTOR` | `UsregsRegulationParam_AllowedSector` |  |  |  |
| 43 | `US.REG.PARAM.EXCLUDED.SECTOR` | `UsregsRegulationParam_ExcludedSector` |  |  |  |
| 44 | `US.REG.PARAM.EXCL.AA.PRODUCT` | `UsregsRegulationParam_ExclAaProduct` |  |  |  |
| 45 | `US.REG.PARAM.POSTING.RESTRICT` | `UsregsRegulationParam_PostingRestrict` | TField |  | This field is used to define the valid Posting Restrict that should be used for Escheat Customer validation Rule : 1 to 4 numeric characters Posting Restriction code, based on EB.OBJECT Valid ID from POSTING.RESTRICT |
| 46 | `US.REG.PARAM.CUST.INACTIV.MONTHS` | `UsregsRegulationParam_CustInactivMonths` | TField |  |  |
| 47 | `US.REG.PARAM.PRIVACY.STATUS` | `UsregsRegulationParam_PrivacyStatus` | TField |  | To flag a customer whether to opt in for the Privacy status or not Validation Rules: It can be either Opt-In or Opt-Out |
| 48 | `US.REG.PARAM.PRE.NOTICE.DAYS` | `UsregsRegulationParam_PreNoticeDays` | TField |  | Define the No of Inactive months to set Customer to Escheat status Validation Rule: Numeric 1-15 digits |
| 49 | `US.REG.PARAM.INCL.AA.PRODUCT` | `UsregsRegulationParam_InclAaProduct` |  |  |  |
| 50 | `US.REG.PARAM.ROLES` | `UsregsRegulationParam_Roles` |  |  |  |
| 51 | `US.REG.PARAM.INCL.AA.PRODUCT.GROUP` | `UsregsRegulationParam_InclAaProductGroup` |  |  |  |
| 52 | `US.REG.PARAM.HOLD.PROCESS` | `UsregsRegulationParam_HoldProcess` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 53 | `US.REG.PARAM.LOOKBACK.MONTH` | `UsregsRegulationParam_LookbackMonth` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 54 | `US.REG.PARAM.HOLD.ON.RETURN` | `UsregsRegulationParam_HoldOnReturn` | TField |  | User can define whether hold must be placed upon check deposit based on breach of excessive returned deposited items. Validation Rules: YES or NO field |
| 55 | `US.REG.PARAM.THRESHOLD.DESC` | `UsregsRegulationParam_ThresholdDesc` |  |  |  |
| 56 | `US.REG.PARAM.THRESHOLD.TYPE` | `UsregsRegulationParam_ThresholdType` |  |  |  |
| 57 | `US.REG.PARAM.THRESHOLD.VALUE` | `UsregsRegulationParam_ThresholdValue` |  |  |  |
| 58 | `US.REG.PARAM.THRESHOLD.PERIOD` | `UsregsRegulationParam_ThresholdPeriod` |  |  |  |
| 59 | `US.REG.PARAM.RETENTION.PERIOD` | `UsregsRegulationParam_RetentionPeriod` |  |  |  |
| 60 | `US.REG.PARAM.ALLOWED.CATEGORY` | `UsregsRegulationParam_AllowedCategory` |  |  |  |
| 61 | `US.REG.PARAM.EXCLUDE.CATEGORY` | `UsregsRegulationParam_ExcludeCategory` |  |  |  |
| 62 | `US.REG.PARAM.RET.TRANSACTION.CODE` | `UsregsRegulationParam_RetTransactionCode` |  |  |  |
| 63 | `US.REG.PARAM.EVALUATION.CYCLE` | `UsregsRegulationParam_EvaluationCycle` |  |  |  |
| 64 | `US.REG.PARAM.VIOLATION.NUMBER` | `UsregsRegulationParam_ViolationNumber` |  |  |  |
| 65 | `US.REG.PARAM.VIOLATION.ACTION` | `UsregsRegulationParam_ViolationAction` |  |  |  |
| 66 | `US.REG.PARAM.REG.D.PRODUCT` | `UsregsRegulationParam_RegDProduct` |  |  |  |
| 67 | `US.REG.PARAM.REG.D.ACTIVITIES` | `UsregsRegulationParam_RegDActivities` |  |  |  |
| 68 | `US.REG.PARAM.OVERRIDE` | `UsregsRegulationParam_Override` |  |  |  |
| 69 | `US.REG.PARAM.RECORD.STATUS` | `UsregsRegulationParam_RecordStatus` | String |  |  |
| 70 | `US.REG.PARAM.CURR.NO` | `UsregsRegulationParam_CurrNo` | String |  |  |
| 71 | `US.REG.PARAM.INPUTTER` | `UsregsRegulationParam_Inputter` |  |  |  |
| 72 | `US.REG.PARAM.DATE.TIME` | `UsregsRegulationParam_DateTime` |  |  |  |
| 73 | `US.REG.PARAM.AUTHORISER` | `UsregsRegulationParam_Authoriser` | String |  |  |
| 74 | `US.REG.PARAM.CO.CODE` | `UsregsRegulationParam_CoCode` | String |  |  |
| 75 | `US.REG.PARAM.DEPT.CODE` | `UsregsRegulationParam_DeptCode` | String |  |  |
| 76 | `US.REG.PARAM.AUDITOR.CODE` | `UsregsRegulationParam_AuditorCode` | String |  |  |
| 77 | `US.REG.PARAM.AUDIT.DATE.TIME` | `UsregsRegulationParam_AuditDateTime` | String |  |  |
| 78 | `US.REG.PARAM.SWIFT.COUNTDOWN` | `UsregsRegulationParam_SwiftCountdown` | TField |  | Field to configure the swift countdown period. |
| 79 | `US.REG.PARAM.CONFIRM.EMAIL` | `UsregsRegulationParam_ConfirmEmail` | TField |  | Email address to send the confirmation. |
| 80 | `US.REG.PARAM.NOTIFICATION.EMAIL` | `UsregsRegulationParam_NotificationEmail` | TField |  | Email address to send the notification |
| 81 | `US.REG.PARAM.SWIFT.SECTOR.START` | `UsregsRegulationParam_SwiftSectorStart` |  |  |  |
| 82 | `US.REG.PARAM.SWIFT.SECTOR.END` | `UsregsRegulationParam_SwiftSectorEnd` |  |  |  |
| 83 | `US.REG.PARAM.AFFILIATE.MKT.PERIOD` | `UsregsRegulationParam_AffiliateMktPeriod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 84 | `US.REG.PARAM.SPLIT.TXN.TYPE` | `UsregsRegulationParam_SplitTxnType` | TField |  | This field is used to define the split deposit transaction type for placing the hold as per the priority order. When transaction type define in this field match witht he TFS transaction, system will placed the hodls considering the split transaction. Valid record from TFS.TRANSACTION table. Ex. SPLIT.DEPOSIT, CASH.IN |
| 85 | `US.REG.PARAM.CASH.OUT.TXN.TYPE` | `UsregsRegulationParam_CashOutTxnType` | TField |  | This field is used to define the cash out transaction that needs to be considered during the split deposit transaction processing. Validation: The cash out transaction type will be validated against this field, if the cash out amount is greater than the avail amount system will display an override message. Valid record from TFS.TRANSACTION table. Ex. CASH.OUT |
