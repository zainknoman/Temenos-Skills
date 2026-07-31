# CARD.TYPE.IDENTIFIER — Table Schema

> Source: `INSERTS/I_F.CARD.TYPE.IDENTIFIER` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CARD.TYP.ID.SHORT.DESCRP` | `CardTypeIdentifier_ShortDescrp` |  |  |  |
| 2 | `CARD.TYP.ID.DESCRIPTION` | `CardTypeIdentifier_Description` |  |  |  |
| 3 | `CARD.TYP.ID.PATTERN` | `CardTypeIdentifier_Pattern` |  |  |  |
| 4 | `CARD.TYP.ID.CARD.TYPE` | `CardTypeIdentifier_CardType` |  |  |  |
| 5 | `CARD.TYP.ID.TRANSFER.TYPE` | `CardTypeIdentifier_TransferType` |  |  |  |
| 6 | `CARD.TYP.ID.MIN.DB.LIMIT` | `CardTypeIdentifier_MinDbLimit` |  |  |  |
| 7 | `CARD.TYP.ID.MAX.DB.LIMIT` | `CardTypeIdentifier_MaxDbLimit` |  |  |  |
| 8 | `CARD.TYP.ID.MIN.CR.LIMIT` | `CardTypeIdentifier_MinCrLimit` |  |  |  |
| 9 | `CARD.TYP.ID.MAX.CR.LIMIT` | `CardTypeIdentifier_MaxCrLimit` |  |  |  |
| 10 | `CARD.TYP.ID.DAILY.DB.LIMIT` | `CardTypeIdentifier_DailyDbLimit` |  |  |  |
| 11 | `CARD.TYP.ID.DAILY.CR.LIMIT` | `CardTypeIdentifier_DailyCrLimit` |  |  |  |
| 12 | `CARD.TYP.ID.LEGACY.CARD.LEN` | `CardTypeIdentifier_LegacyCardLen` | TField |  | Field to store the length of the legacy card.Allowed upto - 2 digits. 0-99 |
| 13 | `CARD.TYP.ID.CREATION.VERSION` | `CardTypeIdentifier_CreationVersion` |  |  |  |
| 14 | `CARD.TYP.ID.RENEWAL.VERSION` | `CardTypeIdentifier_RenewalVersion` |  |  |  |
| 15 | `CARD.TYP.ID.LIMIT.CHANGE.VERSION` | `CardTypeIdentifier_LimitChangeVersion` |  |  |  |
| 16 | `CARD.TYP.ID.ATM.ACC.DESC` | `CardTypeIdentifier_AtmAccDesc` | TField |  |  |
| 17 | `CARD.TYP.ID.EXP.STATUS.CHK` | `CardTypeIdentifier_ExpStatusChk` |  |  |  |
| 18 | `CARD.TYP.ID.EXP.STATUS.CODE` | `CardTypeIdentifier_ExpStatusCode` | TField |  | Field to store the code which is to be considered for expired cards.Eg. 9 |
| 19 | `CARD.TYP.ID.ATM.CUSTOMER` | `CardTypeIdentifier_AtmCustomer` | TField |  | Field to indicate the customer to be accepted for ATM during card issuance.Allowed inputs: CIF/CONTAINERATM card is assigned to CIF, and will have the access to all the related accounts.Note: while issuing a card, DEF.MEMBER field to be a CIF or blank.CONTAINER - ATM card is assigned to CONTAINER and will have the access to only Container Accounts.Note: while issuing a card, DEF.MEMBER field to be MEMBER and not to be blank |
| 20 | `CARD.TYP.ID.CARD.CANCEL.STATUS` | `CardTypeIdentifier_CardCancelStatus` |  |  |  |
| 21 | `CARD.TYP.ID.TCIB.CARD.TYPE` | `CardTypeIdentifier_TcibCardType` | TField |  | Field to define the card type to be used for TCIB.Valid record of CARD.TYPE |
| 22 | `CARD.TYP.ID.CARD.BFR.ACTIVE.STATUS` | `CardTypeIdentifier_CardBfrActiveStatus` |  |  |  |
| 23 | `CARD.TYP.ID.CARD.ACTIVE.STATUS` | `CardTypeIdentifier_CardActiveStatus` | TField |  | Purpose of the field to store the status of the card to be moved after activation.Valid record of CARD.STATUS without Hold response code.Validation - If HRC is available in Card Status, user will be thrown with an override.Eg. 5During card activation, only if the card status matches with the field CARD.BFR.ACTIVE.STATUS, card gets activated and moved to status defined in CARD.ACTIVE.STATUS |
| 24 | `CARD.TYP.ID.EX.ARR.STATUS` | `CardTypeIdentifier_ExArrStatus` |  |  |  |
| 25 | `CARD.TYP.ID.CARD.BFR.ACTIVE.STATUS.TRAN` | `CardTypeIdentifier_CardBfrActiveStatusTran` |  |  |  |
| 26 | `CARD.TYP.ID.CARD.REPLACE.VERSION` | `CardTypeIdentifier_CardReplaceVersion` |  |  |  |
| 27 | `CARD.TYP.ID.T24.UPGRADE.DATE` | `CardTypeIdentifier_T24UpgradeDate` | TField |  | The purpose of this field is used to define the T24 upgrade date which will considered for card ordering.If the T24 date is less than T24.UPGRADE.DATE, then system will select the cards from CARD.ISSUE with status equals "2".If the T24 dateis greater than T24.UPGRADE.DATE, then system will fetch the cards from CARD.ISSUE.ORDER.ID.LIST table.Allowed value is valid t24 date. |
| 28 | `CARD.TYP.ID.CARD.BLOCK.STATUS` | `CardTypeIdentifier_CardBlockStatus` |  |  |  |
| 29 | `CARD.TYP.ID.CARD.BLOCK.ERROR` | `CardTypeIdentifier_CardBlockError` |  |  |  |
| 30 | `CARD.TYP.ID.RESERVED.4` | `CardTypeIdentifier_Reserved4` |  |  |  |
| 31 | `CARD.TYP.ID.RESERVED.3` | `CardTypeIdentifier_Reserved3` | TField |  |  |
| 32 | `CARD.TYP.ID.RESERVED.2` | `CardTypeIdentifier_Reserved2` | TField |  |  |
| 33 | `CARD.TYP.ID.RESERVED.1` | `CardTypeIdentifier_Reserved1` | TField |  |  |
| 34 | `CARD.TYP.ID.LOCAL.REF` | `CardTypeIdentifier_LocalRef` |  |  |  |
| 35 | `CARD.TYP.ID.OVERRIDE` | `CardTypeIdentifier_Override` |  |  |  |
| 36 | `CARD.TYP.ID.RECORD.STATUS` | `CardTypeIdentifier_RecordStatus` | String |  |  |
| 37 | `CARD.TYP.ID.CURR.NO` | `CardTypeIdentifier_CurrNo` | String |  |  |
| 38 | `CARD.TYP.ID.INPUTTER` | `CardTypeIdentifier_Inputter` |  |  |  |
| 39 | `CARD.TYP.ID.DATE.TIME` | `CardTypeIdentifier_DateTime` |  |  |  |
| 40 | `CARD.TYP.ID.AUTHORISER` | `CardTypeIdentifier_Authoriser` | String |  |  |
| 41 | `CARD.TYP.ID.CO.CODE` | `CardTypeIdentifier_CoCode` | String |  |  |
| 42 | `CARD.TYP.ID.DEPT.CODE` | `CardTypeIdentifier_DeptCode` | String |  |  |
| 43 | `CARD.TYP.ID.AUDITOR.CODE` | `CardTypeIdentifier_AuditorCode` | String |  |  |
| 44 | `CARD.TYP.ID.AUDIT.DATE.TIME` | `CardTypeIdentifier_AuditDateTime` | String |  |  |
