# AC.BALANCE.TYPE — Table Schema

> Source: `INSERTS/I_F.AC.BALANCE.TYPE` in `AC_SoftAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.BT.DESCRIPTION` | `AcBalanceType_Description` |  |  |  |
| 2 | `AC.BT.REPORTING.TYPE` | `AcBalanceType_ReportingType` | TField |  | Defines how this balance should be used with respect to reporting.? Fields from PRODUCT.LINE to ABSOLUTE.VALUE can be entered only when the REPORTING.TYPE is BUNDLE or CRA or Facility Validation Rules: CONTINGENT � reported as a contingent NON-CONTINGENT � on balance sheet type INTERNAL � not to be used in reporting VIRTUAL � is used to allow balances to be summed together for enquiry purposes and is an aggregation of balance types BUNDLE � Option to specify whether the total balance to be calculated will be based on all CRA or all Bundle participants arrangements CRA � Option to specify whether the total balance to be calculated will be based on all CRA or all Bundle participants arrangements FACILITY � option to specify whether the balance should be calculated for facility arrangement and all the underlying drawings arrangements |
| 3 | `AC.BT.FIN.SYSTEM` | `AcBalanceType_FinSystem` | TField |  | This field for future use, should be a valid id to EB.FIN.SYSTEM No input field. |
| 4 | `AC.BT.LINKED.LIVE.TYPE` | `AcBalanceType_LinkedLiveType` | TField |  | CONTINGENT balance types can be designated as a forward type. When value dated accounting is used and a forward movement is raised the live type specified here will be changed automatically to the record balance type(as the record balance type is a forward balance type). On authorisation of the record, the FWD.LINKED.TYPE field for the balance type specified here will be updated with ID of the record being authorised. Validation Rules: Should be a valid Balance.Type. Type specified must be a NON-CONTINGENT type. Should not be allowed to define a balance type which has it�s own LINKED.LIVE.TYPE or a FWD.LINKED.TYPE. |
| 5 | `AC.BT.FWD.LINKED.TYPE` | `AcBalanceType_FwdLinkedType` | TField |  | Indicates this record as being the LINKED.LIVE.TYPE to forward type displayed here. It is automatically updated on authorisation of the forward type. Validation Rules: A valid Balance Type No input field. |
| 6 | `AC.BT.SELF.BALANCING` | `AcBalanceType_SelfBalancing` | TField |  | Self balancing is an option allowed for contingent type that will cause the accounting system to automatically raise self balancing entries. |
| 7 | `AC.BT.VIRTUAL.BAL` | `AcBalanceType_VirtualBal` |  |  |  |
| 8 | `AC.BT.SUSPEND.BALANCE` | `AcBalanceType_SuspendBalance` | TField |  | Indicates if the balance type can be suspensed (e.g. contract moves to NAB). Validation Rules: Y_NO Only allowed for Contingent and Non-Contingent types. If Suspend Balance is set to Y a balance type with an "SP" suffix must exist. |
| 9 | `AC.BT.ACTIVITY.UPDATE` | `AcBalanceType_ActivityUpdate` | TField |  | Specifies whether a dated balance file (ACCT.ACTIVITY) should be updated when this balance type is updated. For some types of balance (e.g. accruals) there is no need to maintain a dated history. Validation Rules: Y_NO Not allowed for Virtual. |
| 10 | `AC.BT.SUB.TYPE.ALLOWED` | `AcBalanceType_SubTypeAllowed` | TField |  | Identifies that the balance stored should be decomposed according to the sub-type supplied by the application. If set to Y the balance type stored in EB.CONTRACT.BALANCES will be in the format Balance Type.Sub type. Validation Rules: Y_NO |
| 11 | `AC.BT.SUB.TYPE.ACTIVITY` | `AcBalanceType_SubTypeActivity` | TField |  | If the balance is to be stored by sub-type in SUB.TYPE.ALLOWED, this option allows the activity to be recorded by sub type too. This field can be set to �Y� only if SUB.TYPE.ALLOWED is set to �Y�. Validation Rules: Y_NO |
| 12 | `AC.BT.MOVEMENT.SUPPRESS` | `AcBalanceType_MovementSuppress` | TField |  | For internal movements the entry records can be suppressed. If Reporting.Type is defined as �INTERNAL� and if this field is set to �Y� then no accounting entries will be raised for the Balance.Type record. Validation Rules: Y_NO |
| 13 | `AC.BT.MIS.UPDATE` | `AcBalanceType_MisUpdate` | TField |  | To specify whether BALANCE.MOVEMENT record should update or not. Validation Rules: Valid options Y or NO |
| 14 | `AC.BT.ENTRY.TYPE` | `AcBalanceType_EntryType` | TField |  | The type of entry (STMT or SPECIAL) to be generated. |
| 15 | `AC.BT.SIGNED.TYPE` | `AcBalanceType_SignedType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `AC.BT.EXCLUDE.CR.CHECK` | `AcBalanceType_ExcludeCrCheck` | TField |  | To specify whether entries with this balance type should be excluded from the credit check processing. Validation Rules: Option field, Allowed Values are YES or NO or Blank The blank value will be considered as NO, by default the movement will do a credit check and update limit. The credit check will be excluded only when the value is set as YES. This will be a No change field. |
| 17 | `AC.BT.LOCAL.REF` | `AcBalanceType_LocalRef` |  |  |  |
| 18 | `AC.BT.OVERRIDE` | `AcBalanceType_Override` |  |  |  |
| 19 | `AC.BT.RECORD.STATUS` | `AcBalanceType_RecordStatus` | String |  |  |
| 20 | `AC.BT.CURR.NO` | `AcBalanceType_CurrNo` | String |  |  |
| 21 | `AC.BT.INPUTTER` | `AcBalanceType_Inputter` |  |  |  |
| 22 | `AC.BT.DATE.TIME` | `AcBalanceType_DateTime` |  |  |  |
| 23 | `AC.BT.AUTHORISER` | `AcBalanceType_Authoriser` | String |  |  |
| 24 | `AC.BT.CO.CODE` | `AcBalanceType_CoCode` | String |  |  |
| 25 | `AC.BT.DEPT.CODE` | `AcBalanceType_DeptCode` | String |  |  |
| 26 | `AC.BT.AUDITOR.CODE` | `AcBalanceType_AuditorCode` | String |  |  |
| 27 | `AC.BT.AUDIT.DATE.TIME` | `AcBalanceType_AuditDateTime` | String |  |  |
| 28 | `AC.BT.PRODUCT.LINE` | `AcBalanceType_ProductLine` |  |  |  |
| 29 | `AC.BT.PRODUCT.GROUP` | `AcBalanceType_ProductGroup` |  |  |  |
| 30 | `AC.BT.PRODUCT` | `AcBalanceType_Product` |  |  |  |
| 31 | `AC.BT.EXCLUDE` | `AcBalanceType_Exclude` |  |  |  |
| 32 | `AC.BT.BALANCE.TYPE` | `AcBalanceType_BalanceType` |  |  |  |
| 33 | `AC.BT.ABSOLUTE.VALUE` | `AcBalanceType_AbsoluteValue` |  |  |  |
| 34 | `AC.BT.REDUCE.LIMIT` | `AcBalanceType_ReduceLimit` | TField |  | This should be an one time configuration to avoid the balance mismatches. Default value is NULL NULL - Current behaviour i.e., Entries will be included for Netting. If the result of the Netting is credit, each credit will reduce the limit. YES - The entry will not be included for Netting. Credits will REDUCE the limit, Debits will INCREASE the outstanding on Limit i.e. a debit will increase the available (unutilized) amount of the limit and not the limit. NO - Entries will not be included for Netting. Credits will NOT REDUCE the limit, Debits will INCREASE outstanding (available) on limit. Validation Rules: This field can be configured only for balance types corresponding to STMT entries. Reduce Limit cannot be configured as YES if Exclude Credit Check is YES and vice-versa Amendment to this field should be avoided since balances will become out of sync. Other balance types must be set accordingly |
| 35 | `AC.BT.IFP.BALANCE` | `AcBalanceType_IfpBalance` | TField |  | To specify whether the balances available under this Balance Type for an Account are to be considered for Credit CHECK. Validation Rules: Option field, Allowed Values are YES or NO or Blank. The credit check will be included only when the value is set as YES. This will be a No change field. Option YES will be allowed only when the field REPORTING.TYPE is set to INTERNAL and ENTRY.TYPE is set to SPECIAL. |
| 36 | `AC.BT.EVENT.BALANCE.NAME` | `AcBalanceType_EventBalanceName` | TField |  | This field is used to map individual balance types to standard Enterprise pricing balance types Contents should be defined in EB.LOOKUP of EPP.PROPERTY |
| 37 | `AC.BT.SIGN.RESTRICTED` | `AcBalanceType_SignRestricted` | TField | No | Decides if the balance under the balance type can move from credit to debit or debit to credit. System will raise a warning based on setup Validation rules: Optional field. Valid values are: CREDITS.ONLY/DEBITS.ONLY/NULL. CREDITS.ONLY - The balance under this balance type can only be credit DEBITS.ONLY - The balance under this balance type can only be debit NULL - The balance under this balance type can be in credit or debit |
| 38 | `AC.BT.EPP.PRODUCT.LINE` | `AcBalanceType_EppProductLine` |  |  |  |
| 39 | `AC.BT.EPP.PRODUCT.GROUP` | `AcBalanceType_EppProductGroup` |  |  |  |
