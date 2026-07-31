# PM.SC.PARAM — Table Schema

> Source: `INSERTS/I_F.PM.SC.PARAM` in `PM_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.SP.DESCRIPTION` | `PmScParam_Description` |  |  |  |
| 2 | `PM.SP.SHORT.NAME` | `PmScParam_ShortName` |  |  |  |
| 3 | `PM.SP.PORTFOLIO.ID` | `PmScParam_PortfolioId` |  |  |  |
| 4 | `PM.SP.PORTFOLIO.TYPE` | `PmScParam_PortfolioType` |  |  |  |
| 5 | `PM.SP.OVERNIGHT.PROC` | `PmScParam_OvernightProc` |  |  |  |
| 6 | `PM.SP.R2` | `PmScParam_R2` |  |  |  |
| 7 | `PM.SP.ASSET.TYPE` | `PmScParam_AssetType` |  |  |  |
| 8 | `PM.SP.PERIOD.ID` | `PmScParam_PeriodId` |  |  |  |
| 9 | `PM.SP.DEFAULT.MAT` | `PmScParam_DefaultMat` |  |  |  |
| 10 | `PM.SP.INT.GAP.YTM` | `PmScParam_IntGapYtm` |  |  |  |
| 11 | `PM.SP.DEFAULT.INT` | `PmScParam_DefaultInt` |  |  |  |
| 12 | `PM.SP.R6` | `PmScParam_R6` |  |  |  |
| 13 | `PM.SP.R7` | `PmScParam_R7` |  |  |  |
| 14 | `PM.SP.INCL.REDEEM.PRI` | `PmScParam_InclRedeemPri` | TField |  | Provides an option for the usage of the field Redeem Price in SECURITY.MASTER in Position Management projections . with regard to the following on account of a bond. 1.The maturity Value of a Bond in Cash Flow Report. 2.Calculation to derive Yield to Maturity (YTM) Rate shown in Interest Rate Gap report. The redeem price will be considered only for Investment portfolios of a bond provided the field INT.YTM.GAP in PM.SC.PARAM is set to. a) No for CAS record. b) Yes for GAP record. Validation Rules: Allowed values are YES, NO, NULL. When set to YES, the maturity cash flow and Yield to maturity for Interest rate Gap will be arrived by considering the Redeem Price. When set to NO, the redemption price is always considered same as the face value of the bond. |
| 15 | `PM.SP.BOND.YTM.GAP` | `PmScParam_BondYtmGap` | TField |  | This field holds the name of the user exit routine that can be triggered during close of business, to amend the values calculated by the CORE position management system for transactions from the SEC.TRADE application. This subroutine needs to have the following arguments, Incoming Arguments : R.STP -a dynamic array holding the SC.TRADING.POSITION record. PM.USR.POSN.CLASS - holds the name of position class in position PM.MA.POSN.CLASS. Outgoing Arguments : PM.USR.POSN.CLASS - Information about position class. PROCESSED - a flag to indicate whether the user exit routine has manipulated the YTM and amount. RESERVED.1 - to be passed as Null. RESERVED.2 - to be passed as Null. PM.USR.POSN.CLASS needs to be a dynamic array holding the following structure. PM.USR.POSN.CLASS&lt;1, PM.MA.ASST.LIAB.CD&gt; - to be passed as Null. PM.USR.POSN.CLASS &lt;1, PM.MA.POSN.CLASS&gt; - Name of Position Class. PM.USR.POSN.CLASS &lt;1, PM.MA.CCY.AMT&gt;- Acquired Amount. PM.USR.POSN.CLASS&lt;1, PM.MA.RATE&gt; - Yield to Maturity rate. PM.USR.POSN.CLASS &lt;1, PM.MA.VALUE.DATE&gt; - to be passed as Null. The details such as rate and amount that is updated in PM.TRAN.ACTIVITY / PM.DLY.POSN.CLASS can be modified as per the requirement of the bank. For example: The user exit routine modifies the Amount and rate for SCGSM by fetching the details from SC.TRADING.POSITION. The rate is the Yield to Maturity, which is referred from V.DATED.YLD.TO.MAT and amount is the acquired cost which is obtained by adding AMORTISED.AMOUNT with V.DATE.COST.OF.POS.The formed Position Classes and its details are returned to the calling routine. The calling routine modifies the built position classes with the values returned from the user exit routine based on the PROCESSED argument and the position management files PM.TRAN.ACTIVITY , PM.DLY.POSN.CLASS are built accordingly. The calling routines ignores the values returned from the user exit routine when PROCESSED argument is returned as null. Validation Rules: The routine name should contain a maximum of 25 characters and it should be a valid entry in EB.API application. |
| 16 | `PM.SP.RESERVED.7` | `PmScParam_Reserved7` | TField |  |  |
| 17 | `PM.SP.RESERVED.6` | `PmScParam_Reserved6` | TField |  |  |
| 18 | `PM.SP.RESERVED.5` | `PmScParam_Reserved5` | TField |  |  |
| 19 | `PM.SP.RESERVED.4` | `PmScParam_Reserved4` | TField |  |  |
| 20 | `PM.SP.RESERVED.3` | `PmScParam_Reserved3` | TField |  |  |
| 21 | `PM.SP.RESERVED.2` | `PmScParam_Reserved2` | TField |  |  |
| 22 | `PM.SP.RESERVED.1` | `PmScParam_Reserved1` | TField |  |  |
| 23 | `PM.SP.LOCAL.REF` | `PmScParam_LocalRef` |  |  |  |
| 24 | `PM.SP.RECORD.STATUS` | `PmScParam_RecordStatus` | String |  |  |
| 25 | `PM.SP.CURR.NO` | `PmScParam_CurrNo` | String |  |  |
| 26 | `PM.SP.INPUTTER` | `PmScParam_Inputter` |  |  |  |
| 27 | `PM.SP.DATE.TIME` | `PmScParam_DateTime` |  |  |  |
| 28 | `PM.SP.AUTHORISER` | `PmScParam_Authoriser` | String |  |  |
| 29 | `PM.SP.CO.CODE` | `PmScParam_CoCode` | String |  |  |
| 30 | `PM.SP.DEPT.CODE` | `PmScParam_DeptCode` | String |  |  |
| 31 | `PM.SP.AUDITOR.CODE` | `PmScParam_AuditorCode` | String |  |  |
| 32 | `PM.SP.AUDIT.DATE.TIME` | `PmScParam_AuditDateTime` | String |  |  |
