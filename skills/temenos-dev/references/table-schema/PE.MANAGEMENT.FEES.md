# PE.MANAGEMENT.FEES — Table Schema

> Source: `INSERTS/I_F.PE.MANAGEMENT.FEES` in `SC_ScPeFunds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PE.MGMT.CUST.PORT` | `PeManagementFees_CustPort` | TField |  | This field holds the value of SEC.ACC.MASTER id i.e: Customer Portfolio who has subscribed for PE fund This field will be blank for the PE Management Fees record that corresponds to the issuer of the fund Validation Rules: Value this field will be a valid record in SEC.ACC.MASTER |
| 2 | `SC.PE.MGMT.COMMITMENT.AMT` | `PeManagementFees_CommitmentAmt` | TField |  | This field holds the Committed capital of this customer towards the PE fund Validation Rules: Standard T24 Amount field |
| 3 | `SC.PE.MGMT.MGMT.FEES` | `PeManagementFees_MgmtFees` | TField |  | This field holds the management Fees amount for the customer who subscribed for the PE Fund This fees is calculated based on the commitment amount and the management fee code defined in PE.PRODUCT.EVENTS for the fund and this can be amended by the user Validation Rules: Standard T24 Amount field |
| 4 | `SC.PE.MGMT.ACCOUNT` | `PeManagementFees_Account` | TField |  | This field holds the customer's account who subscribed for the PE fund This account is used to debit the management fees amount Validation Rules: Standard T24 Account field |
| 5 | `SC.PE.MGMT.DELIVERY.REF` | `PeManagementFees_DeliveryRef` | TField |  | This Field is to hold the delivery Reference of the fee advice generated and sent to the customer when PE.MANAGEMENT.FEES record is authorised Validation Rules: System updated field |
| 6 | `SC.PE.MGMT.VALUE.DATE` | `PeManagementFees_ValueDate` | TField |  | This Field holds the value date of accounting entries generated for PE Management Fees Value of this field will be calculated based on MGMT.FEE.OFFSET in PE.PRODUCT.EVENTS for the management fees Validation Rules: Standard T24 Date Field |
| 7 | `SC.PE.MGMT.TOTAL.CUST.FEES` | `PeManagementFees_TotalCustFees` | TField |  | This Field holds the fees amount for each customer. For the issuer record, this would be sum of all the management fees of the investors Validation Rules: Standard T24 Amount Field Noinput, System updated Field |
| 8 | `SC.PE.MGMT.FEES.TO.ISSUER` | `PeManagementFees_FeesToIssuer` | TField |  | This Field holds the management fees that is to be paid to the issuer Validation Rules: Standard T24 Amount Field Noinput, System updated Field |
| 9 | `SC.PE.MGMT.POSTING.STATUS` | `PeManagementFees_PostingStatus` | TField |  | This Field holds the status of the Management fees record automatically created The accounting entries for the management fees will be generated when this field is set to COMPLETED, thus the user can review the calculated fees and set it to complete for the accounting entries to be posted.The user needs to update the status in the issuer record Validation Rules: Option field, allowed value is COMPLETED A new service PE.UPDATE.MGMT.FEES will automatically mark the status field as COMPLETED of each customer record |
| 10 | `SC.PE.MGMT.CURRENCY` | `PeManagementFees_Currency` | TField |  | This Field holds the currency of the PE fund This field value is mapped from CURRENCY field of PE.CUSTOMER.TXN Validation Rules: Standard T24 Currency Field Input not allowed, system updated field |
| 11 | `SC.PE.MGMT.ISSUER.ACCOUNT` | `PeManagementFees_IssuerAccount` | TField |  | This Field holds the Fund issuer's account which will be mapped in the accounting entries for Management fees This field will be blank for the PE Management Fees record that corresponds to the issuer of the fund This field will be defaulted from the ISSUER.ACCOUNT field of PE.CUSTOMER.TXN Validation Rules: Standard T24 Account Field |
| 12 | `SC.PE.MGMT.ISSUER` | `PeManagementFees_Issuer` | TField |  | This Field holds the Fund issuer's id This field will be defaulted from the Issuer of the fund from PE.PRODUCT.EVENTS when the record is amended Validation Rules: Standard T24 Customer Field Noinput Field |
| 13 | `SC.PE.MGMT.PE.FUND` | `PeManagementFees_PeFund` | TField |  | This Field identifies the PE fund for which the management fees is created This field will be defaulted from the SECURITY.MASTER id for which the Management fees was set up Validation Rules: Noinput Field |
| 14 | `SC.PE.MGMT.FEE.DATE` | `PeManagementFees_FeeDate` | TField |  | This Field identifies the date on which the management fees is processed and created This field will be defaulted from the date part of id Validation Rules: Noinput , system updated field |
| 15 | `SC.PE.MGMT.RESERVED4` | `PeManagementFees_Reserved4` | TField |  |  |
| 16 | `SC.PE.MGMT.RESERVED5` | `PeManagementFees_Reserved5` | TField |  |  |
| 17 | `SC.PE.MGMT.RESERVED6` | `PeManagementFees_Reserved6` | TField |  |  |
| 18 | `SC.PE.MGMT.RESERVED7` | `PeManagementFees_Reserved7` | TField |  |  |
| 19 | `SC.PE.MGMT.RESERVED8` | `PeManagementFees_Reserved8` | TField |  |  |
| 20 | `SC.PE.MGMT.RESERVED9` | `PeManagementFees_Reserved9` | TField |  |  |
| 21 | `SC.PE.MGMT.RESERVED10` | `PeManagementFees_Reserved10` | TField |  |  |
| 22 | `SC.PE.MGMT.RESERVED11` | `PeManagementFees_Reserved11` | TField |  |  |
| 23 | `SC.PE.MGMT.RESERVED12` | `PeManagementFees_Reserved12` | TField |  |  |
| 24 | `SC.PE.MGMT.RESERVED13` | `PeManagementFees_Reserved13` | TField |  |  |
| 25 | `SC.PE.MGMT.RESERVED14` | `PeManagementFees_Reserved14` | TField |  |  |
| 26 | `SC.PE.MGMT.RESERVED15` | `PeManagementFees_Reserved15` | TField |  |  |
| 27 | `SC.PE.MGMT.RESERVED16` | `PeManagementFees_Reserved16` | TField |  |  |
| 28 | `SC.PE.MGMT.RESERVED17` | `PeManagementFees_Reserved17` | TField |  |  |
| 29 | `SC.PE.MGMT.RESERVED18` | `PeManagementFees_Reserved18` | TField |  |  |
| 30 | `SC.PE.MGMT.RESERVED19` | `PeManagementFees_Reserved19` | TField |  |  |
| 31 | `SC.PE.MGMT.RESERVED20` | `PeManagementFees_Reserved20` | TField |  |  |
| 32 | `SC.PE.MGMT.LOCAL.REF` | `PeManagementFees_LocalRef` |  |  |  |
| 33 | `SC.PE.MGMT.STMT.NOS` | `PeManagementFees_StmtNos` |  |  |  |
| 34 | `SC.PE.MGMT.OVERRIDE` | `PeManagementFees_Override` |  |  |  |
| 35 | `SC.PE.MGMT.RECORD.STATUS` | `PeManagementFees_RecordStatus` | String |  |  |
| 36 | `SC.PE.MGMT.CURR.NO` | `PeManagementFees_CurrNo` | String |  |  |
| 37 | `SC.PE.MGMT.INPUTTER` | `PeManagementFees_Inputter` |  |  |  |
| 38 | `SC.PE.MGMT.DATE.TIME` | `PeManagementFees_DateTime` |  |  |  |
| 39 | `SC.PE.MGMT.AUTHORISER` | `PeManagementFees_Authoriser` | String |  |  |
| 40 | `SC.PE.MGMT.CO.CODE` | `PeManagementFees_CoCode` | String |  |  |
| 41 | `SC.PE.MGMT.DEPT.CODE` | `PeManagementFees_DeptCode` | String |  |  |
| 42 | `SC.PE.MGMT.AUDITOR.CODE` | `PeManagementFees_AuditorCode` | String |  |  |
| 43 | `SC.PE.MGMT.AUDIT.DATE.TIME` | `PeManagementFees_AuditDateTime` | String |  |  |
