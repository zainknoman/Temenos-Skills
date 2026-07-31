# HUTXNF.ATM.RESERVATION.HISTORY — Table Schema

> Source: `INSERTS/I_F.HUTXNF.ATM.RESERVATION.HISTORY` in `HUTXNF_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUTRES.LOCKED.EVENT.REF` | `HutxnfAtmReservationHistory_LockedEventRef` |  |  |  |
| 2 | `HUTRES.DATE` | `HutxnfAtmReservationHistory_Date` |  |  |  |
| 3 | `HUTRES.TRANSACTION.AMOUNT` | `HutxnfAtmReservationHistory_TransactionAmount` |  |  |  |
| 4 | `HUTRES.ACTIVITY.ID` | `HutxnfAtmReservationHistory_ActivityId` |  |  |  |
| 5 | `HUTRES.AC.INWARD.ENTRY.REF` | `HutxnfAtmReservationHistory_AcInwardEntryRef` |  |  |  |
| 6 | `HUTRES.SETTLE.STATUS` | `HutxnfAtmReservationHistory_SettleStatus` |  |  |  |
| 7 | `HUTRES.RESERVED.10` | `HutxnfAtmReservationHistory_Reserved10` | TField |  | Reserved for future use. |
| 8 | `HUTRES.RESERVED.9` | `HutxnfAtmReservationHistory_Reserved9` | TField |  | Reserved for future use. |
| 9 | `HUTRES.RESERVED.8` | `HutxnfAtmReservationHistory_Reserved8` | TField |  | Reserved for future use. |
| 10 | `HUTRES.RESERVED.7` | `HutxnfAtmReservationHistory_Reserved7` | TField |  | Reserved for future use. |
| 11 | `HUTRES.RESERVED.6` | `HutxnfAtmReservationHistory_Reserved6` | TField |  | Reserved for future use. |
| 12 | `HUTRES.RESERVED.5` | `HutxnfAtmReservationHistory_Reserved5` | TField |  | Reserved for future use. |
| 13 | `HUTRES.RESERVED.4` | `HutxnfAtmReservationHistory_Reserved4` | TField |  | Reserved for future use. |
| 14 | `HUTRES.RESERVED.3` | `HutxnfAtmReservationHistory_Reserved3` | TField |  | Reserved for future use. |
| 15 | `HUTRES.RESERVED.2` | `HutxnfAtmReservationHistory_Reserved2` | TField |  | Reserved for future use. |
| 16 | `HUTRES.RESERVED.1` | `HutxnfAtmReservationHistory_Reserved1` | TField |  | Reserved for future use. |
| 17 | `HUTRES.LOCAL.REF` | `HutxnfAtmReservationHistory_LocalRef` |  |  |  |
