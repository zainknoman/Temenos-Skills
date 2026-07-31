# PP.FILTERING.PAYMENTS — Table Schema

> Source: `INSERTS/I_F.PP.FILTERING.PAYMENTS` in `PP_FilteringService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FPY.CompanyID` | `PpFilteringPayments_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field 'CompanyID' in PP.COMPANY. |
| 2 | `PP.FPY.Ranking` | `PpFilteringPayments_Ranking` |  |  |  |
| 3 | `PP.FPY.OutputChannel` | `PpFilteringPayments_Outputchannel` |  |  |  |
| 4 | `PP.FPY.OutgoingMessageType` | `PpFilteringPayments_Outgoingmessagetype` |  |  |  |
| 5 | `PP.FPY.SkipFilterIndicator` | `PpFilteringPayments_Skipfilterindicator` |  |  |  |
| 6 | `PP.FPY.ActionOnHit` | `PpFilteringPayments_Actiononhit` |  |  |  |
| 7 | `PP.FPY.ActionOnSeizeFunds` | `PpFilteringPayments_Actiononseizefunds` |  |  |  |
| 8 | `PP.FPY.ActionOnTimeOut` | `PpFilteringPayments_Actionontimeout` |  |  |  |
| 9 | `PP.FPY.DateTypeForTimeOut` | `PpFilteringPayments_Datetypefortimeout` |  |  |  |
| 10 | `PP.FPY.CutOffForTimeOut` | `PpFilteringPayments_Cutofffortimeout` |  |  |  |
| 11 | `PP.FPY.LOCAL.REF` | `PpFilteringPayments_LocalRef` |  |  |  |
| 12 | `PP.FPY.OVERRIDE` | `PpFilteringPayments_Override` |  |  |  |
| 13 | `PP.FPY.RECORD.STATUS` | `PpFilteringPayments_RecordStatus` | String |  |  |
| 14 | `PP.FPY.CURR.NO` | `PpFilteringPayments_CurrNo` | String |  |  |
| 15 | `PP.FPY.INPUTTER` | `PpFilteringPayments_Inputter` |  |  |  |
| 16 | `PP.FPY.DATE.TIME` | `PpFilteringPayments_DateTime` |  |  |  |
| 17 | `PP.FPY.AUTHORISER` | `PpFilteringPayments_Authoriser` | String |  |  |
| 18 | `PP.FPY.CO.CODE` | `PpFilteringPayments_CoCode` | String |  |  |
| 19 | `PP.FPY.DEPT.CODE` | `PpFilteringPayments_DeptCode` | String |  |  |
| 20 | `PP.FPY.AUDITOR.CODE` | `PpFilteringPayments_AuditorCode` | String |  |  |
| 21 | `PP.FPY.AUDIT.DATE.TIME` | `PpFilteringPayments_AuditDateTime` | String |  |  |
| 22 | `PP.FPY.PaymentDetailsToEmit` | `PpFilteringPayments_Paymentdetailstoemit` | TField |  | When Sanction Screening is enabled for a payment, TPH emits the payment information to an AML system. User can configure in this field how much information needs to be sent to the AML system. If user configures PaymentDetailsToEmit as 'Complete' then the entire payment information will be sent to the external system. If user configures PaymentDetailsToEmit as 'Blank' then only limited set of information will be sent to the AML system. The information that is being sent to AML can be viewed in table IF.INTEGRATION.FLOW.CATALOG for the record 'TPSAMLIntegration-TPSFlow' in field 'Imported schema'. Possible Values: Complete Blank Default value must be 'Blank' |
| 23 | `PP.FPY.ActionOnPossibleHit` | `PpFilteringPayments_ActionOnPossibleHit` |  |  |  |
