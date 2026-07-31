# PP.PAYMENT.SUBFLOW.CONFIG — Table Schema

> Source: `INSERTS/I_F.PP.PAYMENT.SUBFLOW.CONFIG` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PSF.CompanyID` | `PpPaymentSubflowConfig_Companyid` |  |  |  |
| 2 | `PP.PSF.SubFlowID` | `PpPaymentSubflowConfig_Subflowid` |  |  |  |
| 3 | `PP.PSF.NumberOfServices` | `PpPaymentSubflowConfig_Numberofservices` |  |  |  |
| 4 | `PP.PSF.SelectSize` | `PpPaymentSubflowConfig_Selectsize` |  |  |  |
| 5 | `PP.PSF.RAC` | `PpPaymentSubflowConfig_Rac` |  |  |  |
| 6 | `PP.PSF.RSC` | `PpPaymentSubflowConfig_Rsc` |  |  |  |
| 7 | `PP.PSF.OldID` | `PpPaymentSubflowConfig_Oldid` |  |  |  |
| 8 | `PP.PSF.CurrentID` | `PpPaymentSubflowConfig_Currentid` |  |  |  |
| 9 | `PP.PSF.Action` | `PpPaymentSubflowConfig_Action` |  |  |  |
| 10 | `PP.PSF.OVERRIDE` | `PpPaymentSubflowConfig_Override` |  |  |  |
| 11 | `PP.PSF.RECORD.STATUS` | `PpPaymentSubflowConfig_RecordStatus` |  |  |  |
| 12 | `PP.PSF.CURR.NO` | `PpPaymentSubflowConfig_CurrNo` |  |  |  |
| 13 | `PP.PSF.INPUTTER` | `PpPaymentSubflowConfig_Inputter` |  |  |  |
| 14 | `PP.PSF.DATE.TIME` | `PpPaymentSubflowConfig_DateTime` |  |  |  |
| 15 | `PP.PSF.AUTHORISER` | `PpPaymentSubflowConfig_Authoriser` |  |  |  |
| 16 | `PP.PSF.CO.CODE` | `PpPaymentSubflowConfig_CoCode` |  |  |  |
| 17 | `PP.PSF.DEPT.CODE` | `PpPaymentSubflowConfig_DeptCode` |  |  |  |
| 18 | `PP.PSF.AUDITOR.CODE` | `PpPaymentSubflowConfig_AuditorCode` |  |  |  |
| 19 | `PP.PSF.AUDIT.DATE.TIME` | `PpPaymentSubflowConfig_AuditDateTime` |  |  |  |
