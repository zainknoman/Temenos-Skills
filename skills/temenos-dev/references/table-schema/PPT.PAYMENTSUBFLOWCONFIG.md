# PPT.PAYMENTSUBFLOWCONFIG — Table Schema

> Source: `INSERTS/I_F.PPT.PAYMENTSUBFLOWCONFIG` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPSF.CompanyID` | `PptPaymentsubflowconfig_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY Mandatory Field. |
| 2 | `PPPSF.SubFlowID` | `PptPaymentsubflowconfig_Subflowid` | TField | Yes | Predefined unique value assigned to each sub workflow configured in the payments hub. Possible values: 1 � WEIGHT.SUBFLOW 2 � STP.SUBFLOW.MAIN &amp; STP.SUBFLOW.BALANCE 3 � FILTER.SUBFLOW 4 � FEE.SUBFLOW 5 � POSTING.SUBFLOW 6 � PAYMENT.GENERATION.SUBFLOW Validation Rules: Mandatory Field. 2 numeric characters allowed. |
| 3 | `PPPSF.NumberOfServices` | `PptPaymentsubflowconfig_Numberofservices` | TField | Yes | Specifies the default number of agents to be used by the subflow services for each subflow. Validation Rules: Mandatory field. 3 numeric characters. |
| 4 | `PPPSF.SelectSize` | `PptPaymentsubflowconfig_Selectsize` | TField |  | Specifies the default number of records to be selected by each service of a subflow. Validation Rules: 3 numeric characters. |
| 5 | `PPPSF.RACSubflowConfig` | `PptPaymentsubflowconfig_Racsubflowconfig` | TField |  |  |
| 6 | `PPPSF.RSCSubflowConfig` | `PptPaymentsubflowconfig_Rscsubflowconfig` | TField |  |  |
| 7 | `PPPSF.EntryUserID` | `PptPaymentsubflowconfig_Entryuserid` | TField |  | User ID of the record creator |
| 8 | `PPPSF.EntryDateTime` | `PptPaymentsubflowconfig_Entrydatetime` | TField |  | Date and Time when the record was created in DD MON YYYY HH:MM:SS.MMM format |
| 9 | `PPPSF.ApproverUserID` | `PptPaymentsubflowconfig_Approveruserid` | TField |  | User ID of the record approver |
| 10 | `PPPSF.ApprovedDateTime` | `PptPaymentsubflowconfig_Approveddatetime` | TField |  | Date and Time when the record was approved in DD MON YYYY HH:MM:SS.MMM format |
