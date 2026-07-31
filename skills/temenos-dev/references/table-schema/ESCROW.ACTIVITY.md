# ESCROW.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.ESCROW.ACTIVITY` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.ACT.DESCRIPTION` | `EscrowActivity_Description` |  |  |  |
| 2 | `ESCROW.ACT.FULL.DESC` | `EscrowActivity_FullDesc` |  |  |  |
| 3 | `ESCROW.ACT.ACTIVITY.TYPE` | `EscrowActivity_ActivityType` |  |  |  |
| 4 | `ESCROW.ACT.BATCH.NAME` | `EscrowActivity_BatchName` |  |  |  |
| 5 | `ESCROW.ACT.BATCH.SEQ` | `EscrowActivity_BatchSeq` |  |  |  |
| 6 | `ESCROW.ACT.RESERVED.25` | `EscrowActivity_Reserved25` |  |  |  |
| 7 | `ESCROW.ACT.RESERVED.24` | `EscrowActivity_Reserved24` |  |  |  |
| 8 | `ESCROW.ACT.RESERVED.23` | `EscrowActivity_Reserved23` |  |  |  |
| 9 | `ESCROW.ACT.RESERVED.22` | `EscrowActivity_Reserved22` |  |  |  |
| 10 | `ESCROW.ACT.RESERVED.21` | `EscrowActivity_Reserved21` |  |  |  |
| 11 | `ESCROW.ACT.RESERVED.20` | `EscrowActivity_Reserved20` |  |  |  |
| 12 | `ESCROW.ACT.ACTION.RTN` | `EscrowActivity_ActionRtn` | TField | Yes | Action routine configured by Temenos will be invoked after the VALIDATION.RTN when this activity is triggered. Mandatory input. Application vetting to EB.API |
| 13 | `ESCROW.ACT.ADVICE.NO` | `EscrowActivity_AdviceNo` | TField | No | Delivery advice to be generated. Optional input. Application vetting to EB.ADVICES table. |
| 14 | `ESCROW.ACT.SEND.MESSAGE` | `EscrowActivity_SendMessage` | TField | Yes | Whether a delivery advice is required when this activity is processed Possible values: Y � Yes N � No (default values) Mandatory input |
| 15 | `ESCROW.ACT.RESERVED.19` | `EscrowActivity_Reserved19` | TField |  |  |
| 16 | `ESCROW.ACT.RESERVED.18` | `EscrowActivity_Reserved18` | TField |  |  |
| 17 | `ESCROW.ACT.RESERVED.17` | `EscrowActivity_Reserved17` | TField |  |  |
| 18 | `ESCROW.ACT.RESERVED.16` | `EscrowActivity_Reserved16` | TField |  |  |
| 19 | `ESCROW.ACT.RESERVED.15` | `EscrowActivity_Reserved15` | TField |  |  |
| 20 | `ESCROW.ACT.RESERVED.14` | `EscrowActivity_Reserved14` | TField |  |  |
| 21 | `ESCROW.ACT.RESERVED.13` | `EscrowActivity_Reserved13` | TField |  |  |
| 22 | `ESCROW.ACT.RESERVED.12` | `EscrowActivity_Reserved12` | TField |  |  |
| 23 | `ESCROW.ACT.RESERVED.11` | `EscrowActivity_Reserved11` | TField |  |  |
| 24 | `ESCROW.ACT.RESERVED.10` | `EscrowActivity_Reserved10` | TField |  |  |
| 25 | `ESCROW.ACT.RESERVED.9` | `EscrowActivity_Reserved9` | TField |  |  |
| 26 | `ESCROW.ACT.RESERVED.8` | `EscrowActivity_Reserved8` | TField |  |  |
| 27 | `ESCROW.ACT.RESERVED.7` | `EscrowActivity_Reserved7` | TField |  |  |
| 28 | `ESCROW.ACT.RESERVED.6` | `EscrowActivity_Reserved6` | TField |  |  |
| 29 | `ESCROW.ACT.RESERVED.5` | `EscrowActivity_Reserved5` | TField |  |  |
| 30 | `ESCROW.ACT.RESERVED.4` | `EscrowActivity_Reserved4` | TField |  |  |
| 31 | `ESCROW.ACT.RESERVED.3` | `EscrowActivity_Reserved3` | TField |  |  |
| 32 | `ESCROW.ACT.RESERVED.2` | `EscrowActivity_Reserved2` | TField |  |  |
| 33 | `ESCROW.ACT.RESERVED.1` | `EscrowActivity_Reserved1` | TField |  |  |
| 34 | `ESCROW.ACT.VALIDATION.RTN` | `EscrowActivity_ValidationRtn` | TField | No | User defined routine that will be invoked prior to the ACTION.RTN Optional input. Application vetting to EB.API |
| 35 | `ESCROW.ACT.RECORD.STATUS` | `EscrowActivity_RecordStatus` | String |  |  |
| 36 | `ESCROW.ACT.CURR.NO` | `EscrowActivity_CurrNo` | String |  |  |
| 37 | `ESCROW.ACT.INPUTTER` | `EscrowActivity_Inputter` |  |  |  |
| 38 | `ESCROW.ACT.DATE.TIME` | `EscrowActivity_DateTime` |  |  |  |
| 39 | `ESCROW.ACT.AUTHORISER` | `EscrowActivity_Authoriser` | String |  |  |
| 40 | `ESCROW.ACT.CO.CODE` | `EscrowActivity_CoCode` | String |  |  |
| 41 | `ESCROW.ACT.DEPT.CODE` | `EscrowActivity_DeptCode` | String |  |  |
| 42 | `ESCROW.ACT.AUDITOR.CODE` | `EscrowActivity_AuditorCode` | String |  |  |
| 43 | `ESCROW.ACT.AUDIT.DATE.TIME` | `EscrowActivity_AuditDateTime` | String |  |  |
