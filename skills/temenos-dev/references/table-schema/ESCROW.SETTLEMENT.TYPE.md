# ESCROW.SETTLEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.ESCROW.SETTLEMENT.TYPE` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.ST.DESCRIPTION` | `EscrowSettlementType_Description` |  |  |  |
| 2 | `ESCROW.ST.SETTLEMENT.METHOD` | `EscrowSettlementType_SettlementMethod` | TField |  | Determines the channel through which payment will be routed on settlement from payee wash account to the actual payee account. Possible values are PAYMENT.ORDER, MANUAL. If PAYMENT.ORDER is selected, the funds are settled automatically based on the PAYMENT.ORDER.PRD used. It MANUAL is selected, the funds has to be debited from the escrow wash account using a transaction like FT/TT |
| 3 | `ESCROW.ST.SETTLEMENT.TYPE` | `EscrowSettlementType_SettlementType` | TField |  | Determines the level at which the disbursement should be considered for settlement processing Possible values: INDIVIDUAL � Represents individual disbursement from escrow account towards the payee. BULK � Represents collective disbursement from all escrow accounts |
| 4 | `ESCROW.ST.PAYMENT.ORDER.PRD` | `EscrowSettlementType_PaymentOrderPrd` | TField |  | Id of PAYMENT.ORDER.PRODUCT associated with this settlement type. |
| 5 | `ESCROW.ST.LEAD.DAYS` | `EscrowSettlementType_LeadDays` | TField |  | This field allows the bank to opt advance settlement process. Possible values are Yes, No and Null. This is a NOCHANGE field. If left blank or null then system will throw override to intimate user that same day settlement would take place for the escrow account disbursements. |
| 6 | `ESCROW.ST.RESERVED.24` | `EscrowSettlementType_Reserved24` | TField |  |  |
| 7 | `ESCROW.ST.RESERVED.23` | `EscrowSettlementType_Reserved23` | TField |  |  |
| 8 | `ESCROW.ST.RESERVED.22` | `EscrowSettlementType_Reserved22` | TField |  |  |
| 9 | `ESCROW.ST.RESERVED.21` | `EscrowSettlementType_Reserved21` | TField |  |  |
| 10 | `ESCROW.ST.RESERVED.20` | `EscrowSettlementType_Reserved20` | TField |  |  |
| 11 | `ESCROW.ST.RESERVED.19` | `EscrowSettlementType_Reserved19` | TField |  |  |
| 12 | `ESCROW.ST.RESERVED.18` | `EscrowSettlementType_Reserved18` | TField |  |  |
| 13 | `ESCROW.ST.RESERVED.17` | `EscrowSettlementType_Reserved17` | TField |  |  |
| 14 | `ESCROW.ST.RESERVED.16` | `EscrowSettlementType_Reserved16` | TField |  |  |
| 15 | `ESCROW.ST.RESERVED.15` | `EscrowSettlementType_Reserved15` | TField |  |  |
| 16 | `ESCROW.ST.RESERVED.14` | `EscrowSettlementType_Reserved14` | TField |  |  |
| 17 | `ESCROW.ST.RESERVED.13` | `EscrowSettlementType_Reserved13` | TField |  |  |
| 18 | `ESCROW.ST.RESERVED.12` | `EscrowSettlementType_Reserved12` | TField |  |  |
| 19 | `ESCROW.ST.RESERVED.11` | `EscrowSettlementType_Reserved11` | TField |  |  |
| 20 | `ESCROW.ST.RESERVED.10` | `EscrowSettlementType_Reserved10` | TField |  |  |
| 21 | `ESCROW.ST.RESERVED.9` | `EscrowSettlementType_Reserved9` | TField |  |  |
| 22 | `ESCROW.ST.RESERVED.8` | `EscrowSettlementType_Reserved8` | TField |  |  |
| 23 | `ESCROW.ST.RESERVED.7` | `EscrowSettlementType_Reserved7` | TField |  |  |
| 24 | `ESCROW.ST.RESERVED.6` | `EscrowSettlementType_Reserved6` | TField |  |  |
| 25 | `ESCROW.ST.RESERVED.5` | `EscrowSettlementType_Reserved5` | TField |  |  |
| 26 | `ESCROW.ST.RESERVED.4` | `EscrowSettlementType_Reserved4` | TField |  |  |
| 27 | `ESCROW.ST.RESERVED.3` | `EscrowSettlementType_Reserved3` | TField |  |  |
| 28 | `ESCROW.ST.RESERVED.2` | `EscrowSettlementType_Reserved2` | TField |  |  |
| 29 | `ESCROW.ST.OVERRIDE` | `EscrowSettlementType_Override` |  |  |  |
| 30 | `ESCROW.ST.RECORD.STATUS` | `EscrowSettlementType_RecordStatus` | String |  |  |
| 31 | `ESCROW.ST.CURR.NO` | `EscrowSettlementType_CurrNo` | String |  |  |
| 32 | `ESCROW.ST.INPUTTER` | `EscrowSettlementType_Inputter` |  |  |  |
| 33 | `ESCROW.ST.DATE.TIME` | `EscrowSettlementType_DateTime` |  |  |  |
| 34 | `ESCROW.ST.AUTHORISER` | `EscrowSettlementType_Authoriser` | String |  |  |
| 35 | `ESCROW.ST.CO.CODE` | `EscrowSettlementType_CoCode` | String |  |  |
| 36 | `ESCROW.ST.DEPT.CODE` | `EscrowSettlementType_DeptCode` | String |  |  |
| 37 | `ESCROW.ST.AUDITOR.CODE` | `EscrowSettlementType_AuditorCode` | String |  |  |
| 38 | `ESCROW.ST.AUDIT.DATE.TIME` | `EscrowSettlementType_AuditDateTime` | String |  |  |
