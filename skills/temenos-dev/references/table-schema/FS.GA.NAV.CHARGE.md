# FS.GA.NAV.CHARGE — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CHARGE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CHARGE.PARENT.REF.ID` | `FsGaNavCharge_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CHARGE.ORA.ROWID` | `FsGaNavCharge_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CHARGE.CHARGE.CODE` | `FsGaNavCharge_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 4 | `FS.GA.NAV.CHARGE.DESCRIPTION` | `FsGaNavCharge_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 5 | `FS.GA.NAV.CHARGE.CALC.CODE` | `FsGaNavCharge_CalcCode` | TField |  | Select one of the two calculation codes as follows: 01 A a a Before NAV sub-total, 02 A a a After NAV sub-total, 03 A a a After NAV sub-total Multifonds DB Column is CD_CALC. |
| 6 | `FS.GA.NAV.CHARGE.FEE.TYPE` | `FsGaNavCharge_FeeType` | TField |  | Type of charge parameterized in multifonds Multifonds DB Column is TCHARGE. |
| 7 | `FS.GA.NAV.CHARGE.AMOUNT.OR.PERCENT` | `FsGaNavCharge_AmountOrPercent` | TField |  | Enter the percentage or amount of the fee Multifonds DB Column is MNTPRT. |
| 8 | `FS.GA.NAV.CHARGE.LOCAL.CURRENCY` | `FsGaNavCharge_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 9 | `FS.GA.NAV.CHARGE.METHOD.CODE` | `FsGaNavCharge_MethodCode` | TField |  | Defines how the number of days in a period will be calculated. Interest day-count algorithms may be used in conjunction with the method codes. Multifonds DB Column is CMETHODE. |
| 10 | `FS.GA.NAV.CHARGE.FREQUENCY.CODE` | `FsGaNavCharge_FrequencyCode` | TField |  | The frequency code corresponds to the expected number of payments to be done within a year. Multifonds DB Column is CPPRT. |
| 11 | `FS.GA.NAV.CHARGE.EX.DATE` | `FsGaNavCharge_ExDate` | TField |  | Execution date for Dividend announcement and Corporate Action Multifonds DB Column is DPAYMNT. |
| 12 | `FS.GA.NAV.CHARGE.OPERATION.CODE` | `FsGaNavCharge_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 13 | `FS.GA.NAV.CHARGE.NUMB.OF.DAYS` | `FsGaNavCharge_NumbOfDays` | TField |  | Number of day&apos;s between deposit&apos;s value date to maturity date, number of a fixed number of days or number of NAVs as at which fees will be accrued for. Multifonds DB Column is NB_JOURS. |
| 14 | `FS.GA.NAV.CHARGE.TYPE.OF.AMOUNT` | `FsGaNavCharge_TypeOfAmount` | TField |  | The type of amountA can be defined as the amount used as basis for fees calculation Multifonds DB Column is TYPE_MNT. |
| 15 | `FS.GA.NAV.CHARGE.SCALE.CODE` | `FsGaNavCharge_ScaleCode` | TField |  | If the fee type is equal to &quot;5 - Scale&quot;, a scale code needs to be entered. Note that scales must have been created before via the button scale Multifonds DB Column is CBAREME. |
| 16 | `FS.GA.NAV.CHARGE.OFFICIAL.OR.UNOFFICIAL` | `FsGaNavCharge_OfficialOrUnofficial` | TField |  | Official / Unofficial. Do not use this function. Do not flag this box Multifonds DB Column is OFF_INOFF. |
| 17 | `FS.GA.NAV.CHARGE.DAY.COUNT.CONVENTION` | `FsGaNavCharge_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 18 | `FS.GA.NAV.CHARGE.GL.ACCOUNT` | `FsGaNavCharge_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 19 | `FS.GA.NAV.CHARGE.VAT.CODE` | `FsGaNavCharge_VatCode` | TField |  | The VAT incidence can be taken into consideration independently of the principal of the comm in the respect of the conditions of the agreement among the fund and the 3rd party initiating the fee. Multifonds DB Column is FLAG_TVA. |
| 20 | `FS.GA.NAV.CHARGE.CORRESPONDENT` | `FsGaNavCharge_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 21 | `FS.GA.NAV.CHARGE.GROUP.MULTICLASS` | `FsGaNavCharge_GroupMulticlass` | TField |  | In case of a fund having multiple share classes and if the fee is linked to a particular share class, hence the multi-class group code must be entered in this field Multifonds DB Column is CODE_GRP_MULTICLASS. |
| 22 | `FS.GA.NAV.CHARGE.MANAGER.CODE` | `FsGaNavCharge_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 23 | `FS.GA.NAV.CHARGE.GROUP.ACCOUNT` | `FsGaNavCharge_GroupAccount` | TField |  | The user has the possibility to insert a code number which corresponds to the code he has created by clicking on the button &apos;GRP ACC&apos; Multifonds DB Column is GROUPE_NRUB. |
| 24 | `FS.GA.NAV.CHARGE.LINKING.FEE.CODE` | `FsGaNavCharge_LinkingFeeCode` | TField |  | This field is not used Multifonds DB Column is LINK_NOFRAIS. |
| 25 | `FS.GA.NAV.CHARGE.RELIEF.CALCULATION` | `FsGaNavCharge_ReliefCalculation` | TField |  | Relief calculation flag Multifonds DB Column is FLG_RELIEF. |
| 26 | `FS.GA.NAV.CHARGE.ALL.IN.ONE` | `FsGaNavCharge_AllInOne` | TField |  | If &apos;Y&apos; is selected, the expense is calculated for all managers within the fund structure. In this case, the &apos;Manager&apos; field must be blank. If &apos;N&apos; is selected, the standard functionality is used. Multifonds DB Column is NS_PORTFOLIO_CALC_FLG. |
| 27 | `FS.GA.NAV.CHARGE.MANAGER.CODE.ID` | `FsGaNavCharge_ManagerCodeId` | TField |  | Enter a manager code in this field Multifonds DB Column is NS_PORTFOLIO_CODE. |
| 28 | `FS.GA.NAV.CHARGE.VAT.CODE.2` | `FsGaNavCharge_VatCode2` | TField |  | The field &apos;VAT code 2&apos; enables to parameterize one more tax on expense accrual (case of GST and PST on expenses) Multifonds DB Column is FLAG_TVA_2. |
| 29 | `FS.GA.NAV.CHARGE.EXCLUDE.SECURITY` | `FsGaNavCharge_ExcludeSecurity` | TField |  | It allows creating a group of fee codes for which the markt value of the sec linked to one of those fee codes will be excluded from the based amt for the calc of the charges Multifonds DB Column is EXCL_SEC. |
| 30 | `FS.GA.NAV.CHARGE.GROUP.GTI` | `FsGaNavCharge_GroupGti` | TField |  | The &apos;Grp. GTI&apos; field and &apos;GRP_GTI&apos; button enable to create Groups of GTI&apos;s which allow users linking GTI&apos;s to be included in the based amount for the Korean evaluation fee accrual. Multifonds DB Column is CGTI_GRP. |
| 31 | `FS.GA.NAV.CHARGE.ROUNDING.FIELD` | `FsGaNavCharge_RoundingField` | TField |  | The &apos;Rounding&apos; field enables to trunk down at 10 the fee amount. This is used in the context of Korean bond evaluation fees. Multifonds DB Column is FEE_ARRONDI. |
| 32 | `FS.GA.NAV.CHARGE.CYCLICAL.ID` | `FsGaNavCharge_CyclicalId` | TField | Yes | cyclical ID will be parameterized for controlling charge. Field cycl. ID is mandatory for the charges with fee type 18. Multifonds DB Column is CYCL_ID. |
| 33 | `FS.GA.NAV.CHARGE.MGMT.COMPANY` | `FsGaNavCharge_MgmtCompany` | TField |  | To manage the rebate by management company Multifonds DB Column is MNGT_COMPANY. |
| 34 | `FS.GA.NAV.CHARGE.ROR.CODE` | `FsGaNavCharge_RorCode` | TField |  | ROR code is required for user to define the ROR and management fee rate parameter Multifonds DB Column is CROR. |
| 35 | `FS.GA.NAV.CHARGE.DEPOSIT.GROUP` | `FsGaNavCharge_DepositGroup` | TField |  | deposit group to include in the local custodian calculation Multifonds DB Column is NDEPOSI_GRP. |
| 36 | `FS.GA.NAV.CHARGE.WEEKEND.CALCULATION` | `FsGaNavCharge_WeekendCalculation` | TField |  | Weekend Calculation functionality enables calculation of fees for weekend and holidays Multifonds DB Column is WEEKEND_CALC. |
| 37 | `FS.GA.NAV.CHARGE.TW.ROUNDING` | `FsGaNavCharge_TwRounding` | TField |  | A flag to decide whether each tier fee to be rounded or unrounded separately in each cylindrical cycle Multifonds DB Column is FLG_TW_RDG. |
| 38 | `FS.GA.NAV.CHARGE.REBATE.CODE` | `FsGaNavCharge_RebateCode` | TField |  | Rebate code for specific security. System will look for the same rebate code defined in security position FDPOT01. It supports up to 2 digits (i.e. 01-99). Please see the example for detail Multifonds DB Column is REBATE_CODE. |
| 39 | `FS.GA.NAV.CHARGE.VALUATION.MODEL` | `FsGaNavCharge_ValuationModel` | TField |  | Valuation report configuration code Multifonds DB Column is NESTI. |
| 40 | `FS.GA.NAV.CHARGE.FX.CODE` | `FsGaNavCharge_FxCode` | TField |  | FX code is used to define the NAV code of unrealized G/L generated with the non-fund base fee accrual. This is also linked with A a A Group MulticlassA a A and determine which class level should be posted Multifonds DB Column is FX_CODE. |
| 41 | `FS.GA.NAV.CHARGE.APM.EX.IN.HOUSE.FEE` | `FsGaNavCharge_ApmExInHouseFee` | TField |  | User will not be allowed to attach a charge with AP8 amount type if already APM charge is attached in the cyclical group and Vice versa. User should input a APM fee with this flag checked Multifonds DB Column is FLG_APM_EX_FEE. |
| 42 | `FS.GA.NAV.CHARGE.RESERVED10` | `FsGaNavCharge_Reserved10` | TField |  |  |
| 43 | `FS.GA.NAV.CHARGE.RESERVED9` | `FsGaNavCharge_Reserved9` | TField |  |  |
| 44 | `FS.GA.NAV.CHARGE.RESERVED8` | `FsGaNavCharge_Reserved8` | TField |  |  |
| 45 | `FS.GA.NAV.CHARGE.RESERVED7` | `FsGaNavCharge_Reserved7` | TField |  |  |
| 46 | `FS.GA.NAV.CHARGE.RESERVED6` | `FsGaNavCharge_Reserved6` | TField |  |  |
| 47 | `FS.GA.NAV.CHARGE.RESERVED5` | `FsGaNavCharge_Reserved5` | TField |  |  |
| 48 | `FS.GA.NAV.CHARGE.RESERVED4` | `FsGaNavCharge_Reserved4` | TField |  |  |
| 49 | `FS.GA.NAV.CHARGE.RESERVED3` | `FsGaNavCharge_Reserved3` | TField |  |  |
| 50 | `FS.GA.NAV.CHARGE.RESERVED2` | `FsGaNavCharge_Reserved2` | TField |  |  |
| 51 | `FS.GA.NAV.CHARGE.RESERVED1` | `FsGaNavCharge_Reserved1` | TField |  |  |
| 52 | `FS.GA.NAV.CHARGE.LOCAL.REF` | `FsGaNavCharge_LocalRef` |  |  |  |
| 53 | `FS.GA.NAV.CHARGE.OVERRIDE` | `FsGaNavCharge_Override` |  |  |  |
| 54 | `FS.GA.NAV.CHARGE.RECORD.STATUS` | `FsGaNavCharge_RecordStatus` | String |  |  |
| 55 | `FS.GA.NAV.CHARGE.CURR.NO` | `FsGaNavCharge_CurrNo` | String |  |  |
| 56 | `FS.GA.NAV.CHARGE.INPUTTER` | `FsGaNavCharge_Inputter` |  |  |  |
| 57 | `FS.GA.NAV.CHARGE.DATE.TIME` | `FsGaNavCharge_DateTime` |  |  |  |
| 58 | `FS.GA.NAV.CHARGE.AUTHORISER` | `FsGaNavCharge_Authoriser` | String |  |  |
| 59 | `FS.GA.NAV.CHARGE.CO.CODE` | `FsGaNavCharge_CoCode` | String |  |  |
| 60 | `FS.GA.NAV.CHARGE.DEPT.CODE` | `FsGaNavCharge_DeptCode` | String |  |  |
| 61 | `FS.GA.NAV.CHARGE.AUDITOR.CODE` | `FsGaNavCharge_AuditorCode` | String |  |  |
| 62 | `FS.GA.NAV.CHARGE.AUDIT.DATE.TIME` | `FsGaNavCharge_AuditDateTime` | String |  |  |
