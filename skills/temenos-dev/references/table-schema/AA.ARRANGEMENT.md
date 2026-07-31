# AA.ARRANGEMENT — Table Schema

> Source: `INSERTS/I_F.AA.ARRANGEMENT` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ARR.CUSTOMER` | `AaArrangement_Customer` |  |  |  |
| 2 | `AA.ARR.CUSTOMER.ROLE` | `AaArrangement_CustomerRole` |  |  |  |
| 3 | `AA.ARR.CR.OPPORTUNITY` | `AaArrangement_CrOpportunity` | TField |  |  |
| 4 | `AA.ARR.ALTERNATE.ID` | `AaArrangement_AlternateId` |  |  |  |
| 5 | `AA.ARR.SOURCE.REFERENCE` | `AaArrangement_SourceReference` |  |  |  |
| 6 | `AA.ARR.MAINTAIN.LIMIT.BALANCE` | `AaArrangement_MaintainLimitBalance` | TField |  | The value in this field indicates the arrangement which acts as master for the arrangement being created. When an arrangement is created by specifying an arrangement in the MASTER.ARRANGEMENT field of the application AA.ARRANGEMENT.ACTIVITY/AA.SIMULATION.CAPTURE, the new arrangement is treated as Sub-Arrangement of the Master Arrangement |
| 7 | `AA.ARR.POOL.DATE` | `AaArrangement_PoolDate` | TField |  | Used to store the date on which the arrangement thas been restructured to move to another pool. Any activity beyond this date will not be allowed. |
| 8 | `AA.ARR.CURRENCY` | `AaArrangement_Currency` | TField |  | This field denotes the currency of the Arrangement contract. Arrangement contract can be in both local currency or foreign currency. This field is used to specify in which currency the asset/liability is held. 3 character length, standard currency field. |
| 9 | `AA.ARR.CO.CODE` | `AaArrangement_CoCode` | String |  | Indicates the company on which this arrangement was created. |
| 10 | `AA.ARR.CHANNEL` | `AaArrangement_Channel` |  |  |  |
| 11 | `AA.ARR.ARR.STATUS` | `AaArrangement_ArrStatus` | TField |  | This field indicates the status of the Arrangement during the life cycle of the contract. The status can be standard statuses like, UNAUTH - The arrangement has been input and not Authorised yet. AUTH - The arrangement has been Authorised and LIVE. AUTH-FWD (Forward) - At this stage the Arrangement is not active and will be active on a future date. CURRENT - The arrangement has begun disbursement. Even if partial disbursement happens, this field would hold the same value. MATURED - Arrangement contract has matured and ALL DUES on this arrangement has been cleared. EXPIRED - Arrangement contract has gone past its final payment date. But it still has some dues left unsettled. But no-more disbursement can happen after status has reached MATURED or EXPIRED. REVERSED - The arrangement contract has been reversed. CANCELLED - Arrangement contract has been Cancelled(Only for Deposits) CLOSE - Arrangement contract has been Closed RESTORE-AUTH - Closed Arrangement is restored PENDING.CLOSURE - Arrangement contract is ready for closure. |
| 12 | `AA.ARR.START.DATE` | `AaArrangement_StartDate` | TField |  | This field indicates the creation or start date of the arrangement contract. Date on which the arrangement or service arrangement becomes active. Standard date field. |
| 13 | `AA.ARR.LINKED.APPL` | `AaArrangement_LinkedAppl` |  |  |  |
| 14 | `AA.ARR.LINKED.APPL.ID` | `AaArrangement_LinkedApplId` |  |  |  |
| 15 | `AA.ARR.PRODUCT.LINE` | `AaArrangement_ProductLine` | TField |  | Identifies the Product Line (AA.PRODUCT.LINE) of the arrangement contract. It is not possible to change the product line of the arrangement after it is active. |
| 16 | `AA.ARR.PRODUCT.GROUP` | `AaArrangement_ProductGroup` | TField |  | Identifies the Product Group (AA.PRODUCT.GROUP) of the arrangement contract. It is not possible to change the product group of the arrangement after the contract is authorized (or active). |
| 17 | `AA.ARR.PRODUCT` | `AaArrangement_Product` |  |  |  |
| 18 | `AA.ARR.PROD.EFF.DATE` | `AaArrangement_ProdEffDate` |  |  |  |
| 19 | `AA.ARR.PRODUCT.STATUS` | `AaArrangement_ProductStatus` |  |  |  |
| 20 | `AA.ARR.PROPERTY` | `AaArrangement_Property` |  |  |  |
| 21 | `AA.ARR.INHERITANCE.PROPERTY` | `AaArrangement_InheritanceProperty` |  |  |  |
| 22 | `AA.ARR.VARIATION.EFF.DATE` | `AaArrangement_VariationEffDate` |  |  |  |
| 23 | `AA.ARR.VARIATION` | `AaArrangement_Variation` |  |  |  |
| 24 | `AA.ARR.ORIG.CONTRACT.DATE` | `AaArrangement_OrigContractDate` | TField |  |  |
| 25 | `AA.ARR.LINK.DATE` | `AaArrangement_LinkDate` |  |  |  |
| 26 | `AA.ARR.LINK.TYPE` | `AaArrangement_LinkType` |  |  |  |
| 27 | `AA.ARR.LINK.ARRANGEMENT` | `AaArrangement_LinkArrangement` |  |  |  |
| 28 | `AA.ARR.LINK.PROPERTY` | `AaArrangement_LinkProperty` |  |  |  |
| 29 | `AA.ARR.LINKED.BALANCE.TYPE` | `AaArrangement_LinkedBalanceType` |  |  |  |
| 30 | `AA.ARR.LINKED.SOURCE.CALC.TYPE` | `AaArrangement_LinkedSourceCalcType` |  |  |  |
| 31 | `AA.ARR.LINKED.MAX.OFFSET` | `AaArrangement_LinkedMaxOffset` |  |  |  |
| 32 | `AA.ARR.ARRANGEMENT.TYPE` | `AaArrangement_ArrangementType` |  |  |  |
| 33 | `AA.ARR.RELATIONSHIP.DATE` | `AaArrangement_RelationshipDate` |  |  |  |
| 34 | `AA.ARR.RELATIONSHIP.PLAN` | `AaArrangement_RelationshipPlan` |  |  |  |
| 35 | `AA.ARR.RELATIONSHIP.ARR` | `AaArrangement_RelationshipArr` |  |  |  |
| 36 | `AA.ARR.RESERVED.5` | `AaArrangement_Reserved5` |  |  |  |
| 37 | `AA.ARR.PLAN.SELECT.METHOD` | `AaArrangement_PlanSelectMethod` | TField |  | Indicates the Selection method applied on the arrangement for determining the pricing. It could be AUTOMATIC, MANUAL and AUTOMATIC.OR.MANUAL |
| 38 | `AA.ARR.ELIGIBILITY.REVIEW` | `AaArrangement_EligibilityReview` | TField |  | Indicates whether the pricing was selected as a Manual process or Automatically by the system. If the field has MANUAL, then there would be no further review of pricing on this arrangement unless this is changed to AUTOMATIC. |
| 39 | `AA.ARR.LAST.REVIEW.DATE` | `AaArrangement_LastReviewDate` |  |  |  |
| 40 | `AA.ARR.AGENT.ID` | `AaArrangement_AgentId` |  |  |  |
| 41 | `AA.ARR.AGENT.ARR.ID` | `AaArrangement_AgentArrId` |  |  |  |
| 42 | `AA.ARR.AGENT.ROLE` | `AaArrangement_AgentRole` |  |  |  |
| 43 | `AA.ARR.REWARDS.ARR.ID` | `AaArrangement_RewardsArrId` | TField |  | Hold the Rewards�s arrangement ID, based on which rewards have to be calculated. |
| 44 | `AA.ARR.CLOSURE.REASON` | `AaArrangement_ClosureReason` | TField |  | This field holds the reason for closing the account This field is linked to the virtual table EB.LOOKUP. All values must have an existing code in the EB.LOOKUP table with ID as CLOSURE.REASON. EB.LOOKUP will be used to provide a general description of the closure code and same will be displayed on screen as an enrichment to the closure reason code. |
| 45 | `AA.ARR.CLOSURE.NOTES` | `AaArrangement_ClosureNotes` |  |  |  |
| 46 | `AA.ARR.ACTIVE.PRODUCT` | `AaArrangement_ActiveProduct` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 47 | `AA.ARR.EARLY.PROCESSING` | `AaArrangement_EarlyProcessing` | TField |  | Denotes if the arrangement is scheduled for early processing or the usual COB processing. When input in ACCOUNT PC the same value gets defaulted here. |
| 48 | `AA.ARR.MASTER.ARRANGEMENT` | `AaArrangement_MasterArrangement` | TField |  |  |
| 49 | `AA.ARR.SUB.ARRANGEMENT` | `AaArrangement_SubArrangement` |  |  |  |
| 50 | `AA.ARR.ARRANGEMENT.LINK.TYPE` | `AaArrangement_ArrangementLinkType` | TField |  | Field to capture the inheritance type of the target arrangement |
| 51 | `AA.ARR.TGT.TARGET.PROPERTY` | `AaArrangement_TgtTargetProperty` |  |  |  |
| 52 | `AA.ARR.TGT.SOURCE.LINK.DATE` | `AaArrangement_TgtSourceLinkDate` |  |  |  |
| 53 | `AA.ARR.TGT.SOURCE.ARRANGEMENT` | `AaArrangement_TgtSourceArrangement` |  |  |  |
| 54 | `AA.ARR.TGT.SOURCE.PROPERTY` | `AaArrangement_TgtSourceProperty` |  |  |  |
| 55 | `AA.ARR.TGT.ARR.LINK.TYPE` | `AaArrangement_TgtArrLinkType` |  |  |  |
| 56 | `AA.ARR.RESERVED.6` | `AaArrangement_Reserved6` |  |  |  |
| 57 | `AA.ARR.RESERVED.7` | `AaArrangement_Reserved7` |  |  |  |
| 58 | `AA.ARR.SRC.SOURCE.PROPERTY` | `AaArrangement_SrcSourceProperty` |  |  |  |
| 59 | `AA.ARR.SRC.LINK.DATE` | `AaArrangement_SrcLinkDate` |  |  |  |
| 60 | `AA.ARR.RESERVED.8` | `AaArrangement_Reserved8` |  |  |  |
| 61 | `AA.ARR.RESERVED.9` | `AaArrangement_Reserved9` |  |  |  |
| 62 | `AA.ARR.SRC.LINK.KEY` | `AaArrangement_SrcLinkKey` |  |  |  |
| 63 | `AA.ARR.SRC.TARGET.ARRANGEMENT` | `AaArrangement_SrcTargetArrangement` |  |  |  |
| 64 | `AA.ARR.SRC.TARGET.PROPERTY` | `AaArrangement_SrcTargetProperty` |  |  |  |
| 65 | `AA.ARR.RESERVED.10` | `AaArrangement_Reserved10` |  |  |  |
| 66 | `AA.ARR.RESERVED.11` | `AaArrangement_Reserved11` |  |  |  |
| 67 | `AA.ARR.INHERITANCE.DATE` | `AaArrangement_InheritanceDate` |  |  |  |
| 68 | `AA.ARR.INHERITANCE.CHILD` | `AaArrangement_InheritanceChild` |  |  |  |
| 69 | `AA.ARR.RESERVED.12` | `AaArrangement_Reserved12` |  |  |  |
| 70 | `AA.ARR.RESERVED.13` | `AaArrangement_Reserved13` |  |  |  |
| 71 | `AA.ARR.REMARKS` | `AaArrangement_Remarks` | TField |  | This field stores any valuable information like role, department as given by the user during arrangement creation |
| 72 | `AA.ARR.BUNDLE.LINK.DATE` | `AaArrangement_BundleLinkDate` | TField |  | Stores the date on which the account is linked to the bundle specified in Bundle Arrangement Id. |
| 73 | `AA.ARR.BUNDLE.LINK.TYPE` | `AaArrangement_BundleLinkType` | TField |  | Stores the Link(LINK/DELINK) type whether the account is linked(LINK) or delinked (DELINK) from the Bundle arrangement. |
| 74 | `AA.ARR.BUNDLE.ARR.ID` | `AaArrangement_BundleArrId` | TField |  | Stores the Bundle Arrangement Id to which the account is linked to. |
| 75 | `AA.ARR.POOL.EVENT.DATE` | `AaArrangement_PoolEventDate` |  |  |  |
| 76 | `AA.ARR.POOL.EVENT` | `AaArrangement_PoolEvent` |  |  |  |
| 77 | `AA.ARR.RESERVED.14` | `AaArrangement_Reserved14` |  |  |  |
| 78 | `AA.ARR.ACTIVE.BRANCH` | `AaArrangement_ActiveBranch` | TField |  | Denotes the branch in which the arrangement currently exist. This gets updated when a new arrangement is created by capturing the Branch and also at the time of arrangement being moved from one Branch to another. |
| 79 | `AA.ARR.ACTIVE.LINE.OF.BUSINESS` | `AaArrangement_ActiveLineOfBusiness` | TField |  | Denotes the current line of business of arrangement. |
| 80 | `AA.ARR.BRANCH` | `AaArrangement_Branch` |  |  |  |
| 81 | `AA.ARR.LINE.OF.BUSINESS` | `AaArrangement_LineOfBusiness` |  |  |  |
| 82 | `AA.ARR.ACTIVE.CHANNEL` | `AaArrangement_ActiveChannel` | TField |  | The value in this field denotes the current channel of the arrangement. |
| 83 | `AA.ARR.PROPERTY.CONTROL.PROP` | `AaArrangement_PropertyControlProp` |  |  |  |
| 84 | `AA.ARR.PROPERTY.CONTROL.PROP.DATE` | `AaArrangement_PropertyControlPropDate` |  |  |  |
| 85 | `AA.ARR.MASTER.TYPE` | `AaArrangement_MasterType` | TField |  | This field specifies the Product Line of the master arrangement, if the arrangement has a master. For example: On creation of a loan arrangement (drawings) under a facility, its AA.ARRANGEMENT record will be updated with FACILITY Product Line in MASTER.TYPE field. On creation of a accounts arrangement under a multiccyaccount, its AA.ARRANGEMENT record will be updated with MULTI.CCY.ACCOUNT Product Line in MASTER.TYPE field. |
| 86 | `AA.ARR.GROUP.LEVEL` | `AaArrangement_GroupLevel` | TField |  | This field specifies if the arrangement is a Deal or Facility or Guarantees arrangement For example: On creation of a arrangement under a facility which has Group Level as DEAL at product, it will be updated with DEAL. For example: On creation of a arrangement under a facility which has Group Level as NULL at product and MasterArrangement of Deal type, it will be updated with FACILITY. For example: On creation of a arrangement which belongs to the Guarantees product line the field will have value as CONTINGENT.LIABILITY. |
| 87 | `AA.ARR.OFFSET.TYPE` | `AaArrangement_OffsetType` | TField |  | This field represents the original contract date of the arrangement taken over from the legacy system. This value in this field can less than today but it should not be greater than the effective date or the start date of the arrangement in T24 Validation rule Standard date format |
| 88 | `AA.ARR.ALT.ID.TYPE` | `AaArrangement_AltIdType` |  |  |  |
| 89 | `AA.ARR.BALANCE.TREATMENT` | `AaArrangement_BalanceTreatment` | TField |  | Specifies if the account is off-balance or on-balance. Off-balance accounts maintain principal balance in CUR&lt;&lt;ACCOUNT&gt;&gt;INF balance type as opposed to CUR&lt;&lt;ACCOUNT&gt;&gt; balance type. Valid options are: PARTICIPATION - When this option is set, it means that the loan is funded by consortium of banks including the owning bank acting as an agent or participant. So multiple Contract Balances records will be maintained under a loan contract for Borrower(Global), Participant wise and Own Share. Borrower Balances: - Balances will be held under Borrower Contract balance record(Record ID : LOAN.ACCT.NO). - Balance will be of Internal type(Memo). Participant-wise balances: - Balance will be held under participant contract balance record (Record ID : LOAN.ACCT.NO*PART.CUST.NO) - Balance can be either Internal(Memo) or contingent (off-balance). Own Bank balances: - Balances will be held under Owning Bank contract balance record (Record ID : LOAN.ACCT.NO*BORROWER.CUST.NO) - It will be Non-Contingent(on-balance). |
| 90 | `AA.ARR.SYSTEM.REFERENCE` | `AaArrangement_SystemReference` | TField |  | The original contract�s system reference is stored |
| 91 | `AA.ARR.BASE.CONTRACT.REFERENCE` | `AaArrangement_BaseContractReference` | TField |  | This is the contract reference number in the original system which is mainatined in the system reference field |
| 92 | `AA.ARR.POSTING.RESTRICT` | `AaArrangement_PostingRestrict` |  |  |  |
| 93 | `AA.ARR.COMPANY.REFERENCE` | `AaArrangement_CompanyReference` | TField |  | Field is updated with the opportunity linked to a new arrangement. |
| 94 | `AA.ARR.MASTER.CCY` | `AaArrangement_MasterCcy` | TField |  | This field holds the currency of the master arrangement. |
| 95 | `AA.ARR.SUB.ARRANGEMENT.CCY` | `AaArrangement_SubArrangementCcy` |  |  |  |
| 96 | `AA.ARR.NOTICE.ACCOUNT` | `AaArrangement_NoticeAccount` | TField |  | This field will get update as 'YES' when NOTICE.ACCOUNT field in balance availability is 'YES' . |
| 97 | `AA.ARR.LINKED.DATE` | `AaArrangement_LinkedDate` |  |  |  |
| 98 | `AA.ARR.LINKED.ARRANGEMENT.TYPE` | `AaArrangement_LinkedArrangementType` |  |  |  |
| 99 | `AA.ARR.LINKED.TYPE` | `AaArrangement_LinkedType` |  |  |  |
| 100 | `AA.ARR.LINKED.ARRANGEMENT` | `AaArrangement_LinkedArrangement` |  |  |  |
| 101 | `AA.ARR.LINKED.RESERVED.2` | `AaArrangement_LinkedReserved2` |  |  |  |
| 102 | `AA.ARR.LINKED.RESERVED.1` | `AaArrangement_LinkedReserved1` |  |  |  |
| 103 | `AA.ARR.PROCESS.ONLINE` | `AaArrangement_ProcessOnline` |  |  |  |
| 104 | `AA.ARR.PROMO.ARR.ID` | `AaArrangement_PromoArrId` |  |  |  |
| 105 | `AA.ARR.PROMO.PRODUCT` | `AaArrangement_PromoProduct` |  |  |  |
| 106 | `AA.ARR.PROMO.EFFECTIVE.DATE` | `AaArrangement_PromoEffectiveDate` |  |  |  |
| 107 | `AA.ARR.PROMO.NAME` | `AaArrangement_PromoName` |  |  |  |
| 108 | `AA.ARR.PROMO.BENEFIT.TYPE` | `AaArrangement_PromoBenefitType` |  |  |  |
| 109 | `AA.ARR.RULE.PROCESS.TYPE` | `AaArrangement_RuleProcessType` |  |  |  |
| 110 | `AA.ARR.EPP.PRODUCT.LINE` | `AaArrangement_EppProductLine` | TField |  | This is a multi valued field. Specifies the EPP Product line for which Balance definition is done. Validation Rules: Either EPP Product Line or Epp Product Group or Product must be specified |
| 111 | `AA.ARR.EPP.PRODUCT.GROUP` | `AaArrangement_EppProductGroup` | TField |  | This is a multi valued field. Specifies the EPP Product Group for which Balance definition is done. Validation Rules: Either EPP Product Line or Epp Product Group or Product must be specified |
| 112 | `AA.ARR.CRA.CUSTOMER` | `AaArrangement_CraCustomer` |  |  |  |
| 113 | `AA.ARR.CLOSURE.TYPE` | `AaArrangement_ClosureType` | TField |  | To indicate whether the Sub account closure as part of Multi currency account's Combined closure |
| 114 | `AA.ARR.TRANSACTION.PROPERTY` | `AaArrangement_TransactionProperty` |  |  |  |
| 115 | `AA.ARR.LIMIT.CHARGE.ACCOUNT` | `AaArrangement_LimitChargeAccount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 116 | `AA.ARR.LEASE.TYPE` | `AaArrangement_LeaseType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 117 | `AA.ARR.RESERVED.15` | `AaArrangement_Reserved15` | TField |  |  |
