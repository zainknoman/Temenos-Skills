# PP.SOURCE.SETTING — Table Schema

> Source: `INSERTS/I_F.PP.SOURCE.SETTING` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SS.TransactionType` | `PpSourceSetting_Transactiontype` |  |  |  |
| 2 | `PP.SS.MessagePaymentType` | `PpSourceSetting_Messagepaymenttype` |  |  |  |
| 3 | `PP.SS.AutomatedCancelIndi` | `PpSourceSetting_Automatedcancelindi` |  |  |  |
| 4 | `PP.SS.CreateCustomerStatusMsg` | `PpSourceSetting_Createcustomerstatusmsg` |  |  |  |
| 5 | `PP.SS.CustomerStatusMsgType` | `PpSourceSetting_Customerstatusmsgtype` |  |  |  |
| 6 | `PP.SS.BatchFeeHoldIndicator` | `PpSourceSetting_Batchfeeholdindicator` |  |  |  |
| 7 | `PP.SS.MaxAllowedDays` | `PpSourceSetting_Maxalloweddays` |  |  |  |
| 8 | `PP.SS.BulkingMode` | `PpSourceSetting_Bulkingmode` | TField |  | Indicates the mode of bulking. ESB - The outgoing msg will be emitted through the ESB layer. NonESB - The outgoing msg will be emitted internally. |
| 9 | `PP.SS.SchemaFolder` | `PpSourceSetting_Schemafolder` | TField | Yes | Indicates the directory location of path to the xsd's. Validation Rules: - non mandatory field - it has to be a valid path This field can hold upto 260 alphanumeric characters. |
| 10 | `PP.SS.StylesheetFolder` | `PpSourceSetting_Stylesheetfolder` | TField | Yes | Indicates the directory location of path to the StyleSheet folder where xslt's are available. Validation Rules: - non mandatory field - it has to be a valid path This field can hold upto 260 alphanumeric characters. |
| 11 | `PP.SS.OutputFolder` | `PpSourceSetting_Outputfolder` | TField |  | Holds the folder name where the outgoing msg will be generated. |
| 12 | `PP.SS.ClearingNatureCode` | `PpSourceSetting_Clearingnaturecode` |  |  |  |
| 13 | `PP.SS.MandateVerificationInd` | `PpSourceSetting_Mandateverificationind` |  |  |  |
| 14 | `PP.SS.AutoRegisterMandateInd` | `PpSourceSetting_Autoregistermandateind` |  |  |  |
| 15 | `PP.SS.MandateAmendmentIndicator` | `PpSourceSetting_Mandateamendmentindicator` |  |  |  |
| 16 | `PP.SS.CompareMandateDetailsAPI` | `PpSourceSetting_Comparemandatedetailsapi` |  |  |  |
| 17 | `PP.SS.LOCAL.REF` | `PpSourceSetting_LocalRef` |  |  |  |
| 18 | `PP.SS.OVERRIDE` | `PpSourceSetting_Override` |  |  |  |
| 19 | `PP.SS.RECORD.STATUS` | `PpSourceSetting_RecordStatus` | String |  |  |
| 20 | `PP.SS.CURR.NO` | `PpSourceSetting_CurrNo` | String |  |  |
| 21 | `PP.SS.INPUTTER` | `PpSourceSetting_Inputter` |  |  |  |
| 22 | `PP.SS.DATE.TIME` | `PpSourceSetting_DateTime` |  |  |  |
| 23 | `PP.SS.AUTHORISER` | `PpSourceSetting_Authoriser` | String |  |  |
| 24 | `PP.SS.CO.CODE` | `PpSourceSetting_CoCode` | String |  |  |
| 25 | `PP.SS.DEPT.CODE` | `PpSourceSetting_DeptCode` | String |  |  |
| 26 | `PP.SS.AUDITOR.CODE` | `PpSourceSetting_AuditorCode` | String |  |  |
| 27 | `PP.SS.AUDIT.DATE.TIME` | `PpSourceSetting_AuditDateTime` | String |  |  |
| 28 | `PP.SS.CustomerStatusReportRejects` | `PpSourceSetting_Customerstatusreportrejects` |  |  |  |
| 29 | `PP.SS.EnrichOutMessgaeAPI` | `PpSourceSetting_Enrichoutmessgaeapi` | TField |  |  |
| 30 | `PP.SS.CustomerStatusReportReturns` | `PpSourceSetting_Customerstatusreportreturns` |  |  |  |
| 31 | `PP.SS.CustStatusRptOnSettlement` | `PpSourceSetting_Custstatusrptonsettlement` |  |  |  |
| 32 | `PP.SS.ErrorFolder` | `PpSourceSetting_Errorfolder` | TField |  | Allows the user to configure the path where the outward error messages needs to be stored. |
| 33 | `PP.SS.InterfaceAPI` | `PpSourceSetting_Interfaceapi` | TField |  | New field to configure the routine to achieve some additional functionality in addition to the product functionality. For bulk messages,logic to post the outward message in a queue needs to be developed in the Interface API |
| 34 | `PP.SS.CancelPaymentwithStatus` | `PpSourceSetting_Cancelpaymentwithstatus` |  |  |  |
| 35 | `PP.SS.InterimStatusInd` | `PpSourceSetting_Interimstatusind` | TField | No | Optional field. This field indicates that the Customer status report is enabled for Individual transactions parked in Interim status or Standalone status. Possible values: Immediate- Interim response must be sent immediately EOD- CSR must be generated at EOD (pre-COB) for latest interim status of the payment. Blank- CSR must not be generated for transactions in interim status. |
