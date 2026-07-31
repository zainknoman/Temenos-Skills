# SC.ORDER.SESSION — Table Schema

> Source: `INSERTS/I_F.SC.ORDER.SESSION` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.OR.CUSTOMER` | `ScOrderSession_Customer` | TField |  | Customer to which the PORTFOLIO belongs to. Validation Rules 1. Should be a valid CUSTOMER ID |
| 2 | `SC.OR.PORTFOLIO` | `ScOrderSession_Portfolio` | TField | Yes | Portfolio for which checks are to be performed. Validation Rules 1. Should be a valid SEC.ACC.MASTER ID 2. This is a mandatory field. |
| 3 | `SC.OR.SECURITY.MASTER` | `ScOrderSession_SecurityMaster` |  |  |  |
| 4 | `SC.OR.CONTRACT.MASTER` | `ScOrderSession_ContractMaster` |  |  |  |
| 5 | `SC.OR.ACCOUNT` | `ScOrderSession_Account` |  |  |  |
| 6 | `SC.OR.CONTRACT.TYPE` | `ScOrderSession_ContractType` |  |  |  |
| 7 | `SC.OR.CALL.PUT.IND` | `ScOrderSession_CallPutInd` |  |  |  |
| 8 | `SC.OR.MATURITY` | `ScOrderSession_Maturity` |  |  |  |
| 9 | `SC.OR.BOUGHT.CCY` | `ScOrderSession_BoughtCcy` |  |  |  |
| 10 | `SC.OR.SOLD.CCY` | `ScOrderSession_SoldCcy` |  |  |  |
| 11 | `SC.OR.MKT.VALUE.CCY` | `ScOrderSession_MktValueCcy` |  |  |  |
| 12 | `SC.OR.MARKET.VALUE` | `ScOrderSession_MarketValue` |  |  |  |
| 13 | `SC.OR.MARGIN.VALUE` | `ScOrderSession_MarginValue` |  |  |  |
| 14 | `SC.OR.RESERVED1` | `ScOrderSession_Reserved1` |  |  |  |
| 15 | `SC.OR.RESERVED2` | `ScOrderSession_Reserved2` |  |  |  |
| 16 | `SC.OR.RESERVED3` | `ScOrderSession_Reserved3` |  |  |  |
| 17 | `SC.OR.RESERVED4` | `ScOrderSession_Reserved4` |  |  |  |
| 18 | `SC.OR.RESERVED5` | `ScOrderSession_Reserved5` |  |  |  |
| 19 | `SC.OR.RESERVED6` | `ScOrderSession_Reserved6` |  |  |  |
| 20 | `SC.OR.RESERVED7` | `ScOrderSession_Reserved7` |  |  |  |
| 21 | `SC.OR.RESERVED8` | `ScOrderSession_Reserved8` |  |  |  |
| 22 | `SC.OR.RESERVED9` | `ScOrderSession_Reserved9` |  |  |  |
| 23 | `SC.OR.RESERVED10` | `ScOrderSession_Reserved10` |  |  |  |
| 24 | `SC.OR.INIT.MKT.VALUE` | `ScOrderSession_InitMktValue` | TField |  |  |
| 25 | `SC.OR.INIT.MGN.VALUE` | `ScOrderSession_InitMgnValue` | TField |  | The initial margin value for the portfolio before considering the new orders from this session. |
| 26 | `SC.OR.INIT.LIAB.POS` | `ScOrderSession_InitLiabPos` | TField |  | The initial liability value for the portfolio before considering the new orders from this session. |
| 27 | `SC.OR.INIT.COLL.SURPLUS.DEF` | `ScOrderSession_InitCollSurplusDef` | TField |  | Collateral Surplus before considering the new orders from this session.Difference between Initial Margin value and intial liabilty position |
| 28 | `SC.OR.NEW.MKT.VALUE` | `ScOrderSession_NewMktValue` | TField |  | The market value for the portfolio after considering the new orders from this session. |
| 29 | `SC.OR.NEW.MGN.VALUE` | `ScOrderSession_NewMgnValue` | TField |  | The margin value for the portfolio after considering the new orders from this session. |
| 30 | `SC.OR.NEW.LIAB.POS` | `ScOrderSession_NewLiabPos` | TField |  | The liability value for the portfolio after considering the new orders from this session. |
| 31 | `SC.OR.COLL.SURPLUS.DEF` | `ScOrderSession_CollSurplusDef` | TField |  | Collateral Surplus after considering the new orders from this session.Difference between new margin value and new liability position |
| 32 | `SC.OR.CREDIT.CHECK` | `ScOrderSession_CreditCheck` | TField |  | If Collateral Surplus Deficit is positive,this field will be set to YES.Else,it will be set to NO. |
| 33 | `SC.OR.COLLATERAL.CHECK` | `ScOrderSession_CollateralCheck` | TField |  | This field is used to indicate whether the current positions in this order session has to be checked for collateral breach or not. If the field is set to Yes and if the portfolio is linked as collateral, then the Margin value of the Portfolio will be simulated with the Positions in this Order Session and potential impact in Limit will be calculated and reported in BREACH.INFO field. Validation Rules: If 'CO' module is installed and COLL.CHECK field in COLLATERAL.PARAMETER is set to Yes, this Field can be set to YES. Else, it will be a No Input field. |
| 34 | `SC.OR.BREACH.INFO` | `ScOrderSession_BreachInfo` |  |  |  |
| 35 | `SC.OR.RESERVED13` | `ScOrderSession_Reserved13` | TField |  |  |
| 36 | `SC.OR.RESERVED14` | `ScOrderSession_Reserved14` | TField |  |  |
| 37 | `SC.OR.RESERVED15` | `ScOrderSession_Reserved15` | TField |  |  |
| 38 | `SC.OR.RESERVED16` | `ScOrderSession_Reserved16` | TField |  |  |
| 39 | `SC.OR.RESERVED17` | `ScOrderSession_Reserved17` | TField |  |  |
| 40 | `SC.OR.RESERVED18` | `ScOrderSession_Reserved18` | TField |  |  |
| 41 | `SC.OR.RESERVED19` | `ScOrderSession_Reserved19` | TField |  |  |
| 42 | `SC.OR.RESERVED20` | `ScOrderSession_Reserved20` | TField |  |  |
| 43 | `SC.OR.LOCAL.REF` | `ScOrderSession_LocalRef` |  |  |  |
| 44 | `SC.OR.OVERRIDE` | `ScOrderSession_Override` | TField |  |  |
| 45 | `SC.OR.RECORD.STATUS` | `ScOrderSession_RecordStatus` | String |  |  |
| 46 | `SC.OR.CURR.NO` | `ScOrderSession_CurrNo` | String |  |  |
| 47 | `SC.OR.INPUTTER` | `ScOrderSession_Inputter` |  |  |  |
| 48 | `SC.OR.DATE.TIME` | `ScOrderSession_DateTime` |  |  |  |
| 49 | `SC.OR.AUTHORISER` | `ScOrderSession_Authoriser` | String |  |  |
| 50 | `SC.OR.CO.CODE` | `ScOrderSession_CoCode` | String |  |  |
| 51 | `SC.OR.DEPT.CODE` | `ScOrderSession_DeptCode` | String |  |  |
| 52 | `SC.OR.AUDITOR.CODE` | `ScOrderSession_AuditorCode` | String |  |  |
| 53 | `SC.OR.AUDIT.DATE.TIME` | `ScOrderSession_AuditDateTime` | String |  |  |
