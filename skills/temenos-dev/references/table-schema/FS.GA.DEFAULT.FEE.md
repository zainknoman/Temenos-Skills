# FS.GA.DEFAULT.FEE — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEFAULT.FEE` in `FS_Fee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEFAULT.FEE.PARENT.REF.ID` | `FsGaDefaultFee_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEFAULT.FEE.ORA.ROWID` | `FsGaDefaultFee_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEFAULT.FEE.FUND.ID` | `FsGaDefaultFee_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEFAULT.FEE.SHARE.CLASS.CODE` | `FsGaDefaultFee_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.DEFAULT.FEE.TRANSACTION.CODE` | `FsGaDefaultFee_TransactionCode` | TField |  | Select an appropriate operation code which indicates the type of transaction Multifonds DB Column is CTYP. |
| 6 | `FS.GA.DEFAULT.FEE.FEE.CODE` | `FsGaDefaultFee_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 7 | `FS.GA.DEFAULT.FEE.FEES.RATE` | `FsGaDefaultFee_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 8 | `FS.GA.DEFAULT.FEE.LOWEST` | `FsGaDefaultFee_Lowest` | TField |  | Enter the minimum scale amount Multifonds DB Column is MNT_MIN. |
| 9 | `FS.GA.DEFAULT.FEE.HIGHEST` | `FsGaDefaultFee_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 10 | `FS.GA.DEFAULT.FEE.MINIMUM` | `FsGaDefaultFee_Minimum` | TField |  | Enter the minimum fee amount to be charged. The minimum will apply if the amount calculated on the basis of the scales does not reach such minimum Multifonds DB Column is COM_MIN. |
| 11 | `FS.GA.DEFAULT.FEE.MAXIMUM` | `FsGaDefaultFee_Maximum` | TField |  | Enter the maximum fee to be charged. The maximum will apply if the amount calculated on the basis of the scales exceeds such maximum Multifonds DB Column is COM_MAX. |
| 12 | `FS.GA.DEFAULT.FEE.TRANSFER` | `FsGaDefaultFee_Transfer` | TField |  | If set, means that this fee can be used in transfer agent module Multifonds DB Column is FLAG_TA. |
| 13 | `FS.GA.DEFAULT.FEE.TA.COMMISSION` | `FsGaDefaultFee_TaCommission` | TField |  | B for Calculate on Gross amount, N for calculate on Net amount. Multifonds DB Column is CODE_COMMISSION. |
| 14 | `FS.GA.DEFAULT.FEE.CAL.CODE` | `FsGaDefaultFee_CalCode` | TField |  | The values for this field are: 0- Sub-red fee calculated, 1- Sub-red fee calculated/added/subtracted, 2- Sub-red fee calculated/added/subtracted/booked, 3- Dual pricing for series fund Multifonds DB Column is FEE_TYPE. |
| 15 | `FS.GA.DEFAULT.FEE.SEC.TYPE.PERCENT.OR.AMOUNT` | `FsGaDefaultFee_SecTypePercentOrAmount` | TField |  | Enter a value in percentage or amount according to the sec.type specified before Multifonds DB Column is SEC_MNT. |
| 16 | `FS.GA.DEFAULT.FEE.SEC.TYPE` | `FsGaDefaultFee_SecType` | TField |  | Allows user to define security type Multifonds DB Column is SEC_TYPE. |
| 17 | `FS.GA.DEFAULT.FEE.TRUST` | `FsGaDefaultFee_Trust` | TField |  | Trust identifier if the correspondent is linked to a wider trust group. Multifonds DB Column is NCORRESP_TRUST. |
| 18 | `FS.GA.DEFAULT.FEE.MANAGER.CODE` | `FsGaDefaultFee_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 19 | `FS.GA.DEFAULT.FEE.COMPANY.OR.EMPLOYEE` | `FsGaDefaultFee_CompanyOrEmployee` | TField |  | select appropriate fee code Multifonds DB Column is COM_TYPE. |
| 20 | `FS.GA.DEFAULT.FEE.RETRO.COMMISSION.CURRENCY` | `FsGaDefaultFee_RetroCommissionCurrency` | TField |  | Retro Commission Currency Multifonds DB Column is RETRO_CCY. |
| 21 | `FS.GA.DEFAULT.FEE.DELAY.DAYS` | `FsGaDefaultFee_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 22 | `FS.GA.DEFAULT.FEE.BUSINESS.DAY` | `FsGaDefaultFee_BusinessDay` | TField |  | Allows the settling of broker fees either on a calendar day or a business day Multifonds DB Column is BUS_DAY. |
| 23 | `FS.GA.DEFAULT.FEE.RESERVED10` | `FsGaDefaultFee_Reserved10` | TField |  |  |
| 24 | `FS.GA.DEFAULT.FEE.RESERVED9` | `FsGaDefaultFee_Reserved9` | TField |  |  |
| 25 | `FS.GA.DEFAULT.FEE.RESERVED8` | `FsGaDefaultFee_Reserved8` | TField |  |  |
| 26 | `FS.GA.DEFAULT.FEE.RESERVED7` | `FsGaDefaultFee_Reserved7` | TField |  |  |
| 27 | `FS.GA.DEFAULT.FEE.RESERVED6` | `FsGaDefaultFee_Reserved6` | TField |  |  |
| 28 | `FS.GA.DEFAULT.FEE.RESERVED5` | `FsGaDefaultFee_Reserved5` | TField |  |  |
| 29 | `FS.GA.DEFAULT.FEE.RESERVED4` | `FsGaDefaultFee_Reserved4` | TField |  |  |
| 30 | `FS.GA.DEFAULT.FEE.RESERVED3` | `FsGaDefaultFee_Reserved3` | TField |  |  |
| 31 | `FS.GA.DEFAULT.FEE.RESERVED2` | `FsGaDefaultFee_Reserved2` | TField |  |  |
| 32 | `FS.GA.DEFAULT.FEE.RESERVED1` | `FsGaDefaultFee_Reserved1` | TField |  |  |
| 33 | `FS.GA.DEFAULT.FEE.LOCAL.REF` | `FsGaDefaultFee_LocalRef` |  |  |  |
| 34 | `FS.GA.DEFAULT.FEE.OVERRIDE` | `FsGaDefaultFee_Override` |  |  |  |
| 35 | `FS.GA.DEFAULT.FEE.RECORD.STATUS` | `FsGaDefaultFee_RecordStatus` | String |  |  |
| 36 | `FS.GA.DEFAULT.FEE.CURR.NO` | `FsGaDefaultFee_CurrNo` | String |  |  |
| 37 | `FS.GA.DEFAULT.FEE.INPUTTER` | `FsGaDefaultFee_Inputter` |  |  |  |
| 38 | `FS.GA.DEFAULT.FEE.DATE.TIME` | `FsGaDefaultFee_DateTime` |  |  |  |
| 39 | `FS.GA.DEFAULT.FEE.AUTHORISER` | `FsGaDefaultFee_Authoriser` | String |  |  |
| 40 | `FS.GA.DEFAULT.FEE.CO.CODE` | `FsGaDefaultFee_CoCode` | String |  |  |
| 41 | `FS.GA.DEFAULT.FEE.DEPT.CODE` | `FsGaDefaultFee_DeptCode` | String |  |  |
| 42 | `FS.GA.DEFAULT.FEE.AUDITOR.CODE` | `FsGaDefaultFee_AuditorCode` | String |  |  |
| 43 | `FS.GA.DEFAULT.FEE.AUDIT.DATE.TIME` | `FsGaDefaultFee_AuditDateTime` | String |  |  |
