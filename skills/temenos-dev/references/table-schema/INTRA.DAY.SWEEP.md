# INTRA.DAY.SWEEP — Table Schema

> Source: `INSERTS/I_F.INTRA.DAY.SWEEP` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IDS.DESCRIPTION` | `IntraDaySweep_Description` | TField | Yes | Free text field that contains meaningful description of the record. When the INTRA.DAY.SWEEP record is automatically created by the system, the value defaults from the description field of the AC.CP.GROUP.PARAM application. When multiple sweep is to be executed, this record is to be amended and authorized for which the user is allowed to make changes to the description field. Validation Rules: Mandatory Field |
| 2 | `AC.IDS.SWEEP.TIME` | `IntraDaySweep_SweepTime` |  |  |  |
| 3 | `AC.IDS.PH.END.TIME` | `IntraDaySweep_PhEndTime` | TField |  | This has the latest time on which the phantom got executed for the time specified for this Group. Note this field is updated only when the group has scheduled date as today and scheduled time less than or equal to system time. Validation Rules: No input -Updated by System. |
| 4 | `AC.IDS.PH.USER` | `IntraDaySweep_PhUser` | TField |  | This has the user-id relevant to the phantom process. Validation Rules: No Input-Updated by System. |
| 5 | `AC.IDS.CHARGE.CODE` | `IntraDaySweep_ChargeCode` | TField | No | Defines the charge that is to be collected for executing an intraday sweep.. Accepts valid record ID of FT.CHARGE.TYPE/FT.COMMISSION.TYPE. Care must be taken to define a fixed charge amount in FT.CHARGE.TYPE/FT.COMMISSION.TYPE. Otherwise, charge amount must be mandatorily input. Optional field. |
| 6 | `AC.IDS.CHARGE.AMOUNT` | `IntraDaySweep_ChargeAmount` | TField |  | Defines the fixed charge amount associated with the CHARGE.CODE field. |
| 7 | `AC.IDS.CHARGE.ACCOUNT` | `IntraDaySweep_ChargeAccount` | TField |  | Defines the Account from which the charge is to be debited. |
| 8 | `AC.IDS.TAX.AMOUNT` | `IntraDaySweep_TaxAmount` | TField |  |  |
| 9 | `AC.IDS.RESERVED.1` | `IntraDaySweep_Reserved1` | TField |  |  |
| 10 | `AC.IDS.LOCAL.REF` | `IntraDaySweep_LocalRef` |  |  |  |
| 11 | `AC.IDS.SW.DATE.TIME` | `IntraDaySweep_SwDateTime` |  |  |  |
| 12 | `AC.IDS.MASTER.COMPANY.TIME` | `IntraDaySweep_MasterCompanyTime` | TField |  |  |
| 13 | `AC.IDS.RESERVED.13` | `IntraDaySweep_Reserved13` | TField |  |  |
| 14 | `AC.IDS.RESERVED.12` | `IntraDaySweep_Reserved12` | TField |  |  |
| 15 | `AC.IDS.RESERVED.11` | `IntraDaySweep_Reserved11` | TField |  |  |
| 16 | `AC.IDS.STMT.NOS` | `IntraDaySweep_StmtNos` |  |  |  |
| 17 | `AC.IDS.OVERRIDE` | `IntraDaySweep_Override` |  |  |  |
| 18 | `AC.IDS.RECORD.STATUS` | `IntraDaySweep_RecordStatus` | String |  |  |
| 19 | `AC.IDS.CURR.NO` | `IntraDaySweep_CurrNo` | String |  |  |
| 20 | `AC.IDS.INPUTTER` | `IntraDaySweep_Inputter` |  |  |  |
| 21 | `AC.IDS.DATE.TIME` | `IntraDaySweep_DateTime` |  |  |  |
| 22 | `AC.IDS.AUTHORISER` | `IntraDaySweep_Authoriser` | String |  |  |
| 23 | `AC.IDS.CO.CODE` | `IntraDaySweep_CoCode` | String |  |  |
| 24 | `AC.IDS.DEPT.CODE` | `IntraDaySweep_DeptCode` | String |  |  |
| 25 | `AC.IDS.AUDITOR.CODE` | `IntraDaySweep_AuditorCode` | String |  |  |
| 26 | `AC.IDS.AUDIT.DATE.TIME` | `IntraDaySweep_AuditDateTime` | String |  |  |
