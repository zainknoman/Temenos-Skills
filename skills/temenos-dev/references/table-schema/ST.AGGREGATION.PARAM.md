# ST.AGGREGATION.PARAM — Table Schema

> Source: `INSERTS/I_F.ST.AGGREGATION.PARAM` in `RT_BalanceAggregation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.AGP.RELATION.LEVEL` | `StAggregationParam_RelationLevel` | TField | Yes | Field to define the relation for balance aggregation process. The relationship can be defined at Customer Level (CUSTOMER) or account level (ACCOUNT) or Customer Relationship level (CUSTOMER.RELATIONSHIP) If the relationships are defined at customer level in T24 CUSTOMER, the field has to be set as CUSTOMER. It will be assumed that all the accounts are jointly held and the balance of all the accounts will be attributed to all the joint holders. If the field is set to ACCOUNT, the relationships will be checked at individual account level and only the balances of accounts that are held jointly will be attributed to all the joint holders. CUSTOMER.RELATIONSHIP - This is to respect relationships defined in CUSTOMER.RELATIONSHIP table Validation rules Mandatory field Allowed values are 'CUSTOMER' or 'ACCOUNT' or 'CUSTOMER.RELATIONSHIP' |
| 2 | `ST.AGP.RELATION.CODE` | `StAggregationParam_RelationCode` |  |  |  |
| 3 | `ST.AGP.EXCLD.FOR.ACCT.AGG` | `StAggregationParam_ExcldForAcctAgg` |  |  |  |
| 4 | `ST.AGP.EXC.RULE.APPL` | `StAggregationParam_ExcRuleAppl` |  |  |  |
| 5 | `ST.AGP.EXC.RULE.FIELD` | `StAggregationParam_ExcRuleField` |  |  |  |
| 6 | `ST.AGP.EXC.RULE.OPERAND` | `StAggregationParam_ExcRuleOperand` |  |  |  |
| 7 | `ST.AGP.EXC.RULE.VALUE` | `StAggregationParam_ExcRuleValue` |  |  |  |
| 8 | `ST.AGP.ENT.CUST.FIELD` | `StAggregationParam_EntCustField` |  |  |  |
| 9 | `ST.AGP.ENT.CUST.OPERAND` | `StAggregationParam_EntCustOperand` |  |  |  |
| 10 | `ST.AGP.ENT.CUST.VALUE` | `StAggregationParam_EntCustValue` |  |  |  |
| 11 | `ST.AGP.ACCT.AGGR.RTN` | `StAggregationParam_AcctAggrRtn` | TField |  | A local routine can be attached here which will be called during balance aggregation batch jobs. This routine will take two arguments, first argument is the customer number, second one is ST.AGGREGATE.BALANCES record. This routine can be used to consider additional positions for balance aggregation. Customer number is the input argument and aggregate balance record is both input/output argument. Validation rules Should have a valid EB.API record. |
| 12 | `ST.AGP.BALANCE.BUILD.RTN` | `StAggregationParam_BalanceBuildRtn` | TField |  | A local routine can be attached here which will be called during balance aggregation batch jobs. This routine provides the flexibility to build the customer balances record which is the input for the balance aggregation process. Contains three arguments, first argument is the customer number, second argument is the id's separated by field marker and the third argument is the array containing the respective customer information separated by field marker. It can be the customer position record. Validation rules Should have a valid EB.API record. |
| 13 | `ST.AGP.INIT.AGGR.LOGIC` | `StAggregationParam_InitAggrLogic` | TField |  | Indicate the method based on which balances has to be aggregated for the first time. EFFECTIVE- The balances will be aggregated as of the date (EFFECTIVE.DATE in CRS.PARAMETER minus 1 calendar day). IMPLEMENTATION - The balances will be aggregated as of the date (Date on which the service ST.BUILD.AGGR.BALANCE is run minus 1 calendar day). This set up is applicable only for first time balance aggregation. Validation rules Should have either EFFECTIVE/IMPLEMENTATION. When no set up is done by default IMPLEMENTATION option will be considered during aggregation. |
| 14 | `ST.AGP.CUS.REL.ROLE` | `StAggregationParam_CusRelRole` |  |  |  |
| 15 | `ST.AGP.CUS.REL.GROUP` | `StAggregationParam_CusRelGroup` |  |  |  |
| 16 | `ST.AGP.AGGR.BAL.FILE` | `StAggregationParam_AggrBalFile` | TField |  | This field represents the file which will be selected for balance aggregation processing. If CCSI is chosen then balance will be aggregated for customers having CRS.CUST.SUPP.INFO record. If REPORTABLE.STATUS is chosen balance will be aggregated only for the customers with CRS.CUST.SUPP.INFO, who is having their CRS.STATUS as REPORTABLE. If nothing is selected then balance will be aggregated as usual for all customers. Validation Rules: Input allowed: CCSI or REPORTABLE STATUS. |
| 17 | `ST.AGP.EXTERNAL.ARRANGEMENTS` | `StAggregationParam_ExternalArrangements` | TField |  | This field specifies if contracts from EXTERNAL.ARRANGEMENT.FILE needs to be included in the balance aggregation processing. Validation Rules: YES or NO |
| 18 | `ST.AGP.INCL.EX.JOINT.HOLDER` | `StAggregationParam_InclExJointHolder` | TField |  | This field is to instruct the system to store the details of former joint owners or related customers and to include them in the year-end report. Allowed values - YES,NO,NULL YES - When set to YES, whenever a customer is removed from an arrangement(AA.ARRANGEMENT.ACTIVITY>CUSTOMER) or a related customer is removed from customer CUSTOMER>RELATION.CUSTOMER, the details will be stored in CRS.CSI.CUSTOMER.STATUS and this information will be used in the year-end report. NO, Blank- If set to NO or blank then ex-joint holder details will not be stored or included in the year-end report. Validation Rules: Field value can be changed from NO to YES only once. Once set as YES, this cannot be changed back to NO/NULL. By default, this field is set to NO. |
| 19 | `ST.AGP.RESERVED.04` | `StAggregationParam_Reserved04` |  |  |  |
| 20 | `ST.AGP.RESERVED.03` | `StAggregationParam_Reserved03` | TField |  |  |
| 21 | `ST.AGP.LOCAL.REF` | `StAggregationParam_LocalRef` |  |  |  |
| 22 | `ST.AGP.OVERRIDE` | `StAggregationParam_Override` |  |  |  |
| 23 | `ST.AGP.RECORD.STATUS` | `StAggregationParam_RecordStatus` | String |  |  |
| 24 | `ST.AGP.CURR.NO` | `StAggregationParam_CurrNo` | String |  |  |
| 25 | `ST.AGP.INPUTTER` | `StAggregationParam_Inputter` |  |  |  |
| 26 | `ST.AGP.DATE.TIME` | `StAggregationParam_DateTime` |  |  |  |
| 27 | `ST.AGP.AUTHORISER` | `StAggregationParam_Authoriser` | String |  |  |
| 28 | `ST.AGP.CO.CODE` | `StAggregationParam_CoCode` | String |  |  |
| 29 | `ST.AGP.DEPT.CODE` | `StAggregationParam_DeptCode` | String |  |  |
| 30 | `ST.AGP.AUDITOR.CODE` | `StAggregationParam_AuditorCode` | String |  |  |
| 31 | `ST.AGP.AUDIT.DATE.TIME` | `StAggregationParam_AuditDateTime` | String |  |  |
