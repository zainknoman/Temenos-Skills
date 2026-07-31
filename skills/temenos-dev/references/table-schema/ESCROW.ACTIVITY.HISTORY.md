# ESCROW.ACTIVITY.HISTORY — Table Schema

> Source: `INSERTS/I_F.ESCROW.ACTIVITY.HISTORY` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.AH.ACTIVITY.DATE` | `EscrowActivityHistory_ActivityDate` |  |  |  |
| 2 | `ESCROW.AH.ACTIVITY.NAME` | `EscrowActivityHistory_ActivityName` |  |  |  |
| 3 | `ESCROW.AH.DATE.TIME` | `EscrowActivityHistory_DateTime` |  |  |  |
| 4 | `ESCROW.AH.AAA.REF` | `EscrowActivityHistory_AaaRef` |  |  |  |
| 5 | `ESCROW.AH.TRANS.REF` | `EscrowActivityHistory_TransRef` |  |  |  |
| 6 | `ESCROW.AH.BILL.REF` | `EscrowActivityHistory_BillRef` |  |  |  |
| 7 | `ESCROW.AH.ACTIVITY.AMT` | `EscrowActivityHistory_ActivityAmt` |  |  |  |
| 8 | `ESCROW.AH.INITIATION.TYPE` | `EscrowActivityHistory_InitiationType` |  |  |  |
| 9 | `ESCROW.AH.PAYEE.ID` | `EscrowActivityHistory_PayeeId` |  |  |  |
| 10 | `ESCROW.AH.REFERENCE.NO` | `EscrowActivityHistory_ReferenceNo` |  |  |  |
| 11 | `ESCROW.AH.DELIVERY.REF` | `EscrowActivityHistory_DeliveryRef` |  |  |  |
| 12 | `ESCROW.AH.ERROR.MSG` | `EscrowActivityHistory_ErrorMsg` |  |  |  |
| 13 | `ESCROW.AH.ACT.STATUS` | `EscrowActivityHistory_ActStatus` |  |  |  |
| 14 | `ESCROW.AH.RESERVED.18` | `EscrowActivityHistory_Reserved18` |  |  |  |
| 15 | `ESCROW.AH.RESERVED.17` | `EscrowActivityHistory_Reserved17` |  |  |  |
| 16 | `ESCROW.AH.RESERVED.16` | `EscrowActivityHistory_Reserved16` |  |  |  |
| 17 | `ESCROW.AH.RESERVED.15` | `EscrowActivityHistory_Reserved15` |  |  |  |
| 18 | `ESCROW.AH.RESERVED.14` | `EscrowActivityHistory_Reserved14` |  |  |  |
| 19 | `ESCROW.AH.RESERVED.13` | `EscrowActivityHistory_Reserved13` |  |  |  |
| 20 | `ESCROW.AH.RESERVED.12` | `EscrowActivityHistory_Reserved12` |  |  |  |
| 21 | `ESCROW.AH.RESERVED.11` | `EscrowActivityHistory_Reserved11` |  |  |  |
| 22 | `ESCROW.AH.RESERVED.10` | `EscrowActivityHistory_Reserved10` | TField |  |  |
| 23 | `ESCROW.AH.RESERVED.9` | `EscrowActivityHistory_Reserved9` | TField |  |  |
| 24 | `ESCROW.AH.RESERVED.8` | `EscrowActivityHistory_Reserved8` | TField |  |  |
| 25 | `ESCROW.AH.RESERVED.7` | `EscrowActivityHistory_Reserved7` | TField |  |  |
| 26 | `ESCROW.AH.RESERVED.6` | `EscrowActivityHistory_Reserved6` | TField |  |  |
| 27 | `ESCROW.AH.RESERVED.5` | `EscrowActivityHistory_Reserved5` | TField |  |  |
| 28 | `ESCROW.AH.RESERVED.4` | `EscrowActivityHistory_Reserved4` | TField |  |  |
| 29 | `ESCROW.AH.RESERVED.3` | `EscrowActivityHistory_Reserved3` | TField |  |  |
| 30 | `ESCROW.AH.RESERVED.2` | `EscrowActivityHistory_Reserved2` | TField |  |  |
| 31 | `ESCROW.AH.RESERVED.1` | `EscrowActivityHistory_Reserved1` | TField |  |  |
