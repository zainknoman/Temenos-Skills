# CAPL.H.MAX.CARD.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.MAX.CARD.PARAM` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PARAM.MAX.NOS` | `CaplHMaxCardParam_MaxNos` | TField |  | Field is used to store the maximum number of cards to be issued for this card type per Customers..Vaidations- Numeric and allowed till 999eg. 100Maximum 100 cards shall be issued for the ID card type for a Customer. |
| 2 | `CAPL.PARAM.MAX.PSN` | `CaplHMaxCardParam_MaxPsn` | TField |  | The maximum number of replacement of card, before placing a new orderField used to store the maximum number of Replacement Cards can be issued before replacing a new order for a particular card.Vaidations- Numeric and allowed till 999Applicable - only for MAIL replaements.eg. 9Maximum replacement of 9 times is allowed for the ID card type and on card expiring at 10th time, a new card will be ordered and replaced. |
| 3 | `CAPL.PARAM.EXPIRY.OFFSET` | `CaplHMaxCardParam_ExpiryOffset` | TField |  | Field to store the maximum number of days before the card expiry/renewal, new card to be ordered.Vaidations- Numeric and allowed till 999eg. 15New card reorder will trigger 15 days before the card expiry/renewal date. |
| 4 | `CAPL.PARAM.MAX.WATCH.DAYS` | `CaplHMaxCardParam_MaxWatchDays` | TField |  | Field to store the maximum number of days, the card status to be in WATCH status.Vaidations- Numeric and allowed till 99999eg. 9After 9 days, the cards with WATCH status is cancelled and moved to cancel status. |
| 5 | `CAPL.PARAM.MAX.ISSUED.DAYS` | `CaplHMaxCardParam_MaxIssuedDays` | TField |  | Field to store the maximum number of days to make a card inactive, if card is not used or activated after the card issuance.Vaidations- Numeric and allowed till 99999eg. 5After 5 days from the date of card issuance, the card will be deactivated and move to INACTIVE status. |
| 6 | `CAPL.PARAM.SOLE.PROP.SECTOR` | `CaplHMaxCardParam_SolePropSector` |  |  |  |
| 7 | `CAPL.PARAM.RESERVED.1` | `CaplHMaxCardParam_Reserved1` | TField |  |  |
| 8 | `CAPL.PARAM.RESERVED.2` | `CaplHMaxCardParam_Reserved2` | TField |  |  |
| 9 | `CAPL.PARAM.RESERVED.3` | `CaplHMaxCardParam_Reserved3` | TField |  |  |
| 10 | `CAPL.PARAM.RESERVED.4` | `CaplHMaxCardParam_Reserved4` | TField |  |  |
| 11 | `CAPL.PARAM.RESERVED.5` | `CaplHMaxCardParam_Reserved5` | TField |  |  |
| 12 | `CAPL.PARAM.RESERVED.6` | `CaplHMaxCardParam_Reserved6` | TField |  |  |
| 13 | `CAPL.PARAM.RESERVED.7` | `CaplHMaxCardParam_Reserved7` | TField |  |  |
| 14 | `CAPL.PARAM.RESERVED.8` | `CaplHMaxCardParam_Reserved8` | TField |  |  |
| 15 | `CAPL.PARAM.RESERVED.10` | `CaplHMaxCardParam_Reserved10` | TField |  |  |
| 16 | `CAPL.PARAM.LOCAL.REF` | `CaplHMaxCardParam_LocalRef` |  |  |  |
| 17 | `CAPL.PARAM.OVERRIDES` | `CaplHMaxCardParam_Overrides` |  |  |  |
| 18 | `CAPL.PARAM.RECORD.STATUS` | `CaplHMaxCardParam_RecordStatus` | String |  |  |
| 19 | `CAPL.PARAM.CURR.NO` | `CaplHMaxCardParam_CurrNo` | String |  |  |
| 20 | `CAPL.PARAM.INPUTTER` | `CaplHMaxCardParam_Inputter` |  |  |  |
| 21 | `CAPL.PARAM.DATE.TIME` | `CaplHMaxCardParam_DateTime` |  |  |  |
| 22 | `CAPL.PARAM.AUTHORISER` | `CaplHMaxCardParam_Authoriser` | String |  |  |
| 23 | `CAPL.PARAM.CO.CODE` | `CaplHMaxCardParam_CoCode` | String |  |  |
| 24 | `CAPL.PARAM.DEPT.CODE` | `CaplHMaxCardParam_DeptCode` | String |  |  |
| 25 | `CAPL.PARAM.AUDITOR.CODE` | `CaplHMaxCardParam_AuditorCode` | String |  |  |
| 26 | `CAPL.PARAM.AUDIT.DATE.TIME` | `CaplHMaxCardParam_AuditDateTime` | String |  |  |
