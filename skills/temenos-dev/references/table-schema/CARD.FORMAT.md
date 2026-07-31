# CARD.FORMAT — Table Schema

> Source: `INSERTS/I_F.CARD.FORMAT` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAFO.SHORT.DESCRP` | `CardFormat_ShortDescrp` |  |  |  |
| 2 | `CAFO.DESCRIPTION` | `CardFormat_Description` |  |  |  |
| 3 | `CAFO.CRD.PGM.NAME` | `CardFormat_CrdPgmName` |  |  |  |
| 4 | `CAFO.CRD.PGM.ACT.DATE` | `CardFormat_CrdPgmActDate` |  |  |  |
| 5 | `CAFO.MOBILE.ACCESS` | `CardFormat_MobileAccess` |  |  |  |
| 6 | `CAFO.MOB.CARD.PGM.NAME` | `CardFormat_MobCardPgmName` |  |  |  |
| 7 | `CAFO.INTERAC.FLASH` | `CardFormat_InteracFlash` |  |  |  |
| 8 | `CAFO.RESERVED.24` | `CardFormat_Reserved24` |  |  |  |
| 9 | `CAFO.RESERVED.23` | `CardFormat_Reserved23` |  |  |  |
| 10 | `CAFO.RESERVED.22` | `CardFormat_Reserved22` |  |  |  |
| 11 | `CAFO.RESERVED.21` | `CardFormat_Reserved21` |  |  |  |
| 12 | `CAFO.RESERVED.20` | `CardFormat_Reserved20` |  |  |  |
| 13 | `CAFO.ORDER.TYPE` | `CardFormat_OrderType` |  |  |  |
| 14 | `CAFO.RESERVED.19` | `CardFormat_Reserved19` |  |  |  |
| 15 | `CAFO.RESERVED.18` | `CardFormat_Reserved18` |  |  |  |
| 16 | `CAFO.RESERVED.17` | `CardFormat_Reserved17` |  |  |  |
| 17 | `CAFO.RESERVED.16` | `CardFormat_Reserved16` |  |  |  |
| 18 | `CAFO.RESERVED.15` | `CardFormat_Reserved15` |  |  |  |
| 19 | `CAFO.EXTERNAL.ID` | `CardFormat_ExternalId` |  |  |  |
| 20 | `CAFO.MAILER.DESTINATION` | `CardFormat_MailerDestination` | TField |  | Field Indicates whether a new card should be mailed to the address specified for the cardholder (a value of 0) or to the Issuer contact address i.e. Branch Address (a value of 1). Default value will be "0". &lt;Blank&gt; must be considered as "0".Inputs Allowed - 0 and 1. |
| 21 | `CAFO.MAILER.DEST.CO` | `CardFormat_MailerDestCo` |  |  |  |
| 22 | `CAFO.MAG.CARD` | `CardFormat_MagCard` | TField |  | Reserved for future use. |
| 23 | `CAFO.ADDRESS.FLD` | `CardFormat_AddressFld` | TField |  | Field to store the valid address field from CUSTOMER. Used for validation while a card is issued to a customer. |
| 24 | `CAFO.RESERVED.10` | `CardFormat_Reserved10` | TField |  |  |
| 25 | `CAFO.RESERVED.9` | `CardFormat_Reserved9` | TField |  |  |
| 26 | `CAFO.RESERVED.8` | `CardFormat_Reserved8` | TField |  |  |
| 27 | `CAFO.RESERVED.7` | `CardFormat_Reserved7` | TField |  |  |
| 28 | `CAFO.RESERVED.6` | `CardFormat_Reserved6` | TField |  |  |
| 29 | `CAFO.RESERVED.5` | `CardFormat_Reserved5` | TField |  |  |
| 30 | `CAFO.RESERVED.4` | `CardFormat_Reserved4` | TField |  |  |
| 31 | `CAFO.RESERVED.3` | `CardFormat_Reserved3` | TField |  |  |
| 32 | `CAFO.RESERVED.2` | `CardFormat_Reserved2` | TField |  |  |
| 33 | `CAFO.RESERVED.1` | `CardFormat_Reserved1` | TField |  |  |
| 34 | `CAFO.LOCAL.REF` | `CardFormat_LocalRef` |  |  |  |
| 35 | `CAFO.OVERRIDE` | `CardFormat_Override` |  |  |  |
| 36 | `CAFO.RECORD.STATUS` | `CardFormat_RecordStatus` | String |  |  |
| 37 | `CAFO.CURR.NO` | `CardFormat_CurrNo` | String |  |  |
| 38 | `CAFO.INPUTTER` | `CardFormat_Inputter` |  |  |  |
| 39 | `CAFO.DATE.TIME` | `CardFormat_DateTime` |  |  |  |
| 40 | `CAFO.AUTHORISER` | `CardFormat_Authoriser` | String |  |  |
| 41 | `CAFO.CO.CODE` | `CardFormat_CoCode` | String |  |  |
| 42 | `CAFO.DEPT.CODE` | `CardFormat_DeptCode` | String |  |  |
| 43 | `CAFO.AUDITOR.CODE` | `CardFormat_AuditorCode` | String |  |  |
| 44 | `CAFO.AUDIT.DATE.TIME` | `CardFormat_AuditDateTime` | String |  |  |
