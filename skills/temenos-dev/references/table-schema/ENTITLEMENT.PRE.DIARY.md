# ENTITLEMENT.PRE.DIARY — Table Schema

> Source: `INSERTS/I_F.ENTITLEMENT.PRE.DIARY` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.EPD.PORTFOLIO.NO` | `EntitlementPreDiary_PortfolioNo` | TField |  | Portfolio number associated with the position for which the record is built. Enriched by the Account Name field from the SEC.ACC.MASTER file. Validation Rules: This is NOINPUT field. |
| 2 | `SC.EPD.SECURITY.NO` | `EntitlementPreDiary_SecurityNo` | TField |  | Security Master ID of the event/original security. Updated from the originating SC.PRE.DIARY record. Enriched by the Short description of the Security from Security Master file. Validation Rules: This is NOINPUT field. |
| 3 | `SC.EPD.DEPOSITORY` | `EntitlementPreDiary_Depository` | TField |  | The Depository number associated with the position. Enriched by short description from CUSTOMER.SECURITY file. Validation Rules: This is NOINPUT field. |
| 4 | `SC.EPD.NOMINEE` | `EntitlementPreDiary_Nominee` | TField |  | Unique reference which identifies the Nominee Company record. Validation Rules: This is NOINPUT field |
| 5 | `SC.EPD.SUB.ACCOUNT` | `EntitlementPreDiary_SubAccount` | TField |  | The Depository sub account of the position. It is defaulted from the ENTITLEMENT.PRE.DIARY key. Validation Rules: This is NOINPUT field |
| 6 | `SC.EPD.QUALIFY.HOLDING` | `EntitlementPreDiary_QualifyHolding` | TField |  | Portfolio's holding in the original security eligible for the event. The calculation is similar to Entitlement Validation Rules: This is NOINPUT field |
| 7 | `SC.EPD.EVENT.NOMINAL` | `EntitlementPreDiary_EventNominal` | TField |  | This is the total nominal involved in the event. Validation Rules: This is NOINPUT field |
| 8 | `SC.EPD.CURRENCY` | `EntitlementPreDiary_Currency` | TField |  | Currency in which ENTITLEMENT.AMT is calculated.If CURRENCY in Diary is a non-restricted Currency, then thecurrency will be defaultedfrom the CURRENCY field on the original SC.PRE.DIARY record. Enriched by the short description from the CURRENCY file. Validation Rules: This is NOINPUT field |
| 9 | `SC.EPD.OPTION.DESC` | `EntitlementPreDiary_OptionDesc` |  |  |  |
| 10 | `SC.EPD.GROSS.RATE` | `EntitlementPreDiary_GrossRate` |  |  |  |
| 11 | `SC.EPD.NET.RATE` | `EntitlementPreDiary_NetRate` |  |  |  |
| 12 | `SC.EPD.GROSS.OR.NET` | `EntitlementPreDiary_GrossOrNet` |  |  |  |
| 13 | `SC.EPD.ENTITLEMENT.AMT` | `EntitlementPreDiary_EntitlementAmt` |  |  |  |
| 14 | `SC.EPD.NEW.SECURITY` | `EntitlementPreDiary_NewSecurity` |  |  |  |
| 15 | `SC.EPD.NOMINAL` | `EntitlementPreDiary_Nominal` |  |  |  |
| 16 | `SC.EPD.RATIO` | `EntitlementPreDiary_Ratio` |  |  |  |
| 17 | `SC.EPD.ADDL.NARRATIVE` | `EntitlementPreDiary_AddlNarrative` |  |  |  |
| 18 | `SC.EPD.PRE.ADV.DATE` | `EntitlementPreDiary_PreAdvDate` | TField |  | Holds the date on which Pre-advice/notification is generated for the first time Validation Rules: This is NOINPUT field. |
| 19 | `SC.EPD.DATE.TIME` | `EntitlementPreDiary_DateTime` |  |  |  |
| 20 | `SC.EPD.MSG.FUNC` | `EntitlementPreDiary_MsgFunc` | TField |  | Holds the Current Function of the message (MT564) defined in SC.PRE.DIARY record Validation Rules: This is NOINPUT field. |
| 21 | `SC.EPD.PROC.STATUS` | `EntitlementPreDiary_ProcStatus` | TField |  | Holds the Current processing Status (from MT564) defined in SC.PRE.DIARY record Validation Rules: This is NOINPUT field. |
| 22 | `SC.EPD.ACTIVITY.CODE` | `EntitlementPreDiary_ActivityCode` |  |  |  |
| 23 | `SC.EPD.MESSAGE.TYPE` | `EntitlementPreDiary_MessageType` |  |  |  |
| 24 | `SC.EPD.DELIVERY.REF` | `EntitlementPreDiary_DeliveryRef` |  |  |  |
