# SC.STAPLING.ARRANGEMENT — Table Schema

> Source: `INSERTS/I_F.SC.STAPLING.ARRANGEMENT` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SSA.STAPLE.SECURITY` | `ScStaplingArrangement_StapleSecurity` | TField |  | Any Security defined as a Staple in SECURITY.MASTER Validation Rules: Must be defined as parent in SECURITY.MASTER Must contain SC.STAPLED.COMPONENT record for the security specified |
| 2 | `SC.SSA.CHILD.SECURITY` | `ScStaplingArrangement_ChildSecurity` |  |  |  |
| 3 | `SC.SSA.EFFECTIVE.DATE` | `ScStaplingArrangement_EffectiveDate` | TField |  | This field holds the Effective date |
| 4 | `SC.SSA.OPERATION.TYPE` | `ScStaplingArrangement_OperationType` | TField |  | This field indicates whether parent position needs to be created, removed or adjusted for cost Validation Rules: Allowed values : CREATE.PARENT, REMOVE.PARENT, ADJUST.COST, ADD.CHILD, REMOVE.CHILD ADD.CHILD , REMOVE.CHILD is allowed only when STAPLE.ALLOC.LEVEL is parent in CG.PARAMETER |
| 5 | `SC.SSA.TRANSFER.OUT.PRICE.TYPE` | `ScStaplingArrangement_TransferOutPriceType` | TField | Yes | When operation type is 'REMOVE.PARENT', the price of SECURITY.TRANSFER is determined by this field It can be either the avg cost of the holding for each portfolio or the market price or the price input in theapplication Validation Rules: Allowed values : AVG.COST, MARKET.PRICE, INPUT.PRICE Mandatory when operation type is 'REMOVE.PARENT' |
| 6 | `SC.SSA.TRANSFER.OUT.PRICE` | `ScStaplingArrangement_TransferOutPrice` | TField | Yes | Price field. Available for user input Validation Rules: Mandatory when TRANSFER.OUT.PRICE.TYPE is INPUT.PRICE |
| 7 | `SC.SSA.AUTH.TYPE` | `ScStaplingArrangement_AuthType` | TField |  | This will determine whether the transaction (SECURITY.TRANSFER or SC.BOOK.COST) will be created in AUTHORIZEDstatus or not. Validation Rules: Allowed values : UNAUTH, AUTH Defaulted to UNAUTH, when left blank |
| 8 | `SC.SSA.SEC.CR.TRANS.CODE` | `ScStaplingArrangement_SecCrTransCode` | TField |  | Holds the credit transaction code Validation Rules: Defaulted from CG.PARAMETER |
| 9 | `SC.SSA.SEC.DR.TRANS.CODE` | `ScStaplingArrangement_SecDrTransCode` | TField |  | Holds the debit transaction code Validation Rules: Defaulted from CG.PARAMETER |
| 10 | `SC.SSA.STATUS` | `ScStaplingArrangement_Status` | TField |  | This field indicates whether the record is processed or not Validation Rules: Possible value : PROCESSED |
| 11 | `SC.SSA.UPD.CHILD.SECURITY` | `ScStaplingArrangement_UpdChildSecurity` |  |  |  |
| 12 | `SC.SSA.RESERVED9` | `ScStaplingArrangement_Reserved9` | TField |  |  |
| 13 | `SC.SSA.RESERVED8` | `ScStaplingArrangement_Reserved8` | TField |  |  |
| 14 | `SC.SSA.RESERVED7` | `ScStaplingArrangement_Reserved7` | TField |  |  |
| 15 | `SC.SSA.RESERVED6` | `ScStaplingArrangement_Reserved6` | TField |  |  |
| 16 | `SC.SSA.RESERVED5` | `ScStaplingArrangement_Reserved5` | TField |  |  |
| 17 | `SC.SSA.RESERVED4` | `ScStaplingArrangement_Reserved4` | TField |  |  |
| 18 | `SC.SSA.RESERVED3` | `ScStaplingArrangement_Reserved3` | TField |  |  |
| 19 | `SC.SSA.RESERVED2` | `ScStaplingArrangement_Reserved2` | TField |  |  |
| 20 | `SC.SSA.RESERVED1` | `ScStaplingArrangement_Reserved1` | TField |  |  |
| 21 | `SC.SSA.LOCAL.REF` | `ScStaplingArrangement_LocalRef` |  |  |  |
| 22 | `SC.SSA.OVERRIDE` | `ScStaplingArrangement_Override` |  |  |  |
| 23 | `SC.SSA.RECORD.STATUS` | `ScStaplingArrangement_RecordStatus` | String |  |  |
| 24 | `SC.SSA.CURR.NO` | `ScStaplingArrangement_CurrNo` | String |  |  |
| 25 | `SC.SSA.INPUTTER` | `ScStaplingArrangement_Inputter` |  |  |  |
| 26 | `SC.SSA.DATE.TIME` | `ScStaplingArrangement_DateTime` |  |  |  |
| 27 | `SC.SSA.AUTHORISER` | `ScStaplingArrangement_Authoriser` | String |  |  |
| 28 | `SC.SSA.CO.CODE` | `ScStaplingArrangement_CoCode` | String |  |  |
| 29 | `SC.SSA.DEPT.CODE` | `ScStaplingArrangement_DeptCode` | String |  |  |
| 30 | `SC.SSA.AUDITOR.CODE` | `ScStaplingArrangement_AuditorCode` | String |  |  |
| 31 | `SC.SSA.AUDIT.DATE.TIME` | `ScStaplingArrangement_AuditDateTime` | String |  |  |
| 32 | `SC.SSA.DIARY.ID` | `ScStaplingArrangement_DiaryId` | TField |  | This field indicates only the parcels that participated in the DIARY are to be stapled. Validation Rules: Must be a valid Diary record Must be an in-specie dividend type The Child securities of the staple should be both the event security and the receivable security Allowed only when STAPLE.ALLOC.LEVEL in CG.PARAMETER is PARENT |
| 33 | `SC.SSA.INCLUDE.PORTFOLIO` | `ScStaplingArrangement_IncludePortfolio` |  |  |  |
| 34 | `SC.SSA.EXCLUDE.PORTFOLIO` | `ScStaplingArrangement_ExcludePortfolio` |  |  |  |
| 35 | `SC.SSA.EFFECTIVE.TIME` | `ScStaplingArrangement_EffectiveTime` | TField |  | This field will hold the time of the stapling event. This field can be used to sequence the events if multipleevents affects the CG.TXN.BASE at the same time. |
