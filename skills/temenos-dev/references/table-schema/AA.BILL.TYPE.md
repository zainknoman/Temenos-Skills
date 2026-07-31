# AA.BILL.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.BILL.TYPE` in `AA_PaymentSchedule.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BT.DESCRIPTION` | `AaBillType_Description` |  |  |  |
| 2 | `AA.BT.SYS.BILL.TYPE` | `AaBillType_SysBillType` | TField |  | This field links the user Bill Type to the system maintained Bill Type. Valid options are, PAYMENT, EXPECTED, ACT.CHARGE, PR.CHARGE, DEF.CHARGE, INFO, DISBURSEMENT, COMMISSION and EXTERNAL EXTERNAL - This Sys Bill type is applicable only if Info type of Charge is attached in Payment schedule condition INTERNAL - This Sys Bill type is applicable only for Non Customer type charges. COMMITMENT - This is used to decrease Facility's commitment as per payment schedules. The related property for this bill type must be Term Amount in AA.PAYMENT.TYPE. |
| 3 | `AA.BT.RESERVED.5` | `AaBillType_Reserved5` |  |  |  |
| 4 | `AA.BT.RESERVED.4` | `AaBillType_Reserved4` | TField |  |  |
| 5 | `AA.BT.RESERVED.3` | `AaBillType_Reserved3` | TField |  |  |
| 6 | `AA.BT.RESERVED.2` | `AaBillType_Reserved2` | TField |  |  |
| 7 | `AA.BT.RESERVED.1` | `AaBillType_Reserved1` | TField |  |  |
| 8 | `AA.BT.RECORD.STATUS` | `AaBillType_RecordStatus` | String |  |  |
| 9 | `AA.BT.CURR.NO` | `AaBillType_CurrNo` | String |  |  |
| 10 | `AA.BT.INPUTTER` | `AaBillType_Inputter` |  |  |  |
| 11 | `AA.BT.DATE.TIME` | `AaBillType_DateTime` |  |  |  |
| 12 | `AA.BT.AUTHORISER` | `AaBillType_Authoriser` | String |  |  |
| 13 | `AA.BT.CO.CODE` | `AaBillType_CoCode` | String |  |  |
| 14 | `AA.BT.DEPT.CODE` | `AaBillType_DeptCode` | String |  |  |
| 15 | `AA.BT.AUDITOR.CODE` | `AaBillType_AuditorCode` | String |  |  |
| 16 | `AA.BT.AUDIT.DATE.TIME` | `AaBillType_AuditDateTime` | String |  |  |
