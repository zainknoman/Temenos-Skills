# CAPL.H.TX.FORM.TYPE — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.FORM.TYPE` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.H.TX.FRMTYP.DESCRIPTION` | `CaplHTxFormType_Description` |  |  |  |
| 2 | `CAPL.H.TX.FRMTYP.MAP.FILE` | `CaplHTxFormType_MapFile` |  |  |  |
| 3 | `CAPL.H.TX.FRMTYP.SYSTEM.ID` | `CaplHTxFormType_SystemId` |  |  |  |
| 4 | `CAPL.H.TX.FRMTYP.ID.MAP.FLD` | `CaplHTxFormType_IdMapFld` |  |  |  |
| 5 | `CAPL.H.TX.FRMTYP.ID.ROUTINE` | `CaplHTxFormType_IdRoutine` |  |  |  |
| 6 | `CAPL.H.TX.FRMTYP.AMOUNT.CODE` | `CaplHTxFormType_AmountCode` |  |  |  |
| 7 | `CAPL.H.TX.FRMTYP.INC.CCY` | `CaplHTxFormType_IncCcy` |  |  |  |
| 8 | `CAPL.H.TX.FRMTYP.EXC.CCY` | `CaplHTxFormType_ExcCcy` |  |  |  |
| 9 | `CAPL.H.TX.FRMTYP.AMOUNT.TYPE` | `CaplHTxFormType_AmountType` |  |  |  |
| 10 | `CAPL.H.TX.FRMTYP.AMT.CDE.TXN` | `CaplHTxFormType_AmtCdeTxn` |  |  |  |
| 11 | `CAPL.H.TX.FRMTYP.TXN.SYS.ID` | `CaplHTxFormType_TxnSysId` |  |  |  |
| 12 | `CAPL.H.TX.FRMTYP.TXN.ROUTINE` | `CaplHTxFormType_TxnRoutine` |  |  |  |
| 13 | `CAPL.H.TX.FRMTYP.MAPP.PREV.YEAR` | `CaplHTxFormType_MappPrevYear` | TField |  | The purpose of the field is to define whether the previous year form to be included or not. If the previous yes is set to NO, then system will default to today.Possible values are "YES" or "NO" Each time this field is changed the system should generate override "Adjustment to previous year flag is changed" so only authorized users can update it. Validate in check field level. Modified |
| 14 | `CAPL.H.TX.FRMTYP.AMT.CDE.RES2` | `CaplHTxFormType_AmtCdeRes2` | TField |  | No input field |
| 15 | `CAPL.H.TX.FRMTYP.AMT.CDE.RES3` | `CaplHTxFormType_AmtCdeRes3` | TField |  | No input field |
| 16 | `CAPL.H.TX.FRMTYP.AMT.CDE.RES4` | `CaplHTxFormType_AmtCdeRes4` | TField |  | No input field |
| 17 | `CAPL.H.TX.FRMTYP.INC.CATEGORY` | `CaplHTxFormType_IncCategory` |  |  |  |
| 18 | `CAPL.H.TX.FRMTYP.CONDITION.RTN` | `CaplHTxFormType_ConditionRtn` | TField |  | This field is used to define the condition routine, where the entries will be filtered based on user conditions.Valid record from PGM.FILE table.E.g CAPL.TX.T5.NR4.COND.RTN Modified |
| 19 | `CAPL.H.TX.FRMTYP.VDATE.ADJUST` | `CaplHTxFormType_VdateAdjust` |  |  |  |
| 20 | `CAPL.H.TX.FRMTYP.VDAT.ADJ.TXN` | `CaplHTxFormType_VdatAdjTxn` |  |  |  |
| 21 | `CAPL.H.TX.FRMTYP.FORM.TEMPLATE` | `CaplHTxFormType_FormTemplate` | TField |  | This field is used to define the form template for the corresponding form type.Valid record form FILE.CONTROL table.E.g CAPL.TX.FORM.TEMPLATE Modified |
| 22 | `CAPL.H.TX.FRMTYP.EXC.CATEGORY` | `CaplHTxFormType_ExcCategory` |  |  |  |
| 23 | `CAPL.H.TX.FRMTYP.INC.AGC` | `CaplHTxFormType_IncAgc` |  |  |  |
| 24 | `CAPL.H.TX.FRMTYP.EXC.AGC` | `CaplHTxFormType_ExcAgc` |  |  |  |
| 25 | `CAPL.H.TX.FRMTYP.INC.APP` | `CaplHTxFormType_IncApp` |  |  |  |
| 26 | `CAPL.H.TX.FRMTYP.EXC.APP` | `CaplHTxFormType_ExcApp` |  |  |  |
| 27 | `CAPL.H.TX.FRMTYP.INC.RESIDENCE` | `CaplHTxFormType_IncResidence` |  |  |  |
| 28 | `CAPL.H.TX.FRMTYP.EXC.RESIDENCE` | `CaplHTxFormType_ExcResidence` |  |  |  |
| 29 | `CAPL.H.TX.FRMTYP.ROLE.CODE` | `CaplHTxFormType_RoleCode` |  |  |  |
| 30 | `CAPL.H.TX.FRMTYP.EXEMPT.AA.PROD` | `CaplHTxFormType_ExemptAaProd` |  |  |  |
| 31 | `CAPL.H.TX.FRMTYP.INCL.AA.PROD` | `CaplHTxFormType_InclAaProd` |  |  |  |
| 32 | `CAPL.H.TX.FRMTYP.INC.PROVINCE` | `CaplHTxFormType_IncProvince` |  |  |  |
| 33 | `CAPL.H.TX.FRMTYP.EXC.PROVINCE` | `CaplHTxFormType_ExcProvince` |  |  |  |
| 34 | `CAPL.H.TX.FRMTYP.INT.MIN.AMT` | `CaplHTxFormType_IntMinAmt` | TField |  | This field is used to define the minimum interest amount for the form type.T24 valid Amount |
| 35 | `CAPL.H.TX.FRMTYP.INT.MIN.FLD` | `CaplHTxFormType_IntMinFld` | TField |  | This field is used to define the INT.MIN.FLD for the tax form type.Validation:It should be AMOUNT.CODE.1 to AMOUNT.CODE.9 from CAPL.TX.FORM.TEMPLATE table field. Check for SS Record of the particular field. |
| 36 | `CAPL.H.TX.FRMTYP.TAX.OPERAND` | `CaplHTxFormType_TaxOperand` | TField |  | This field is used to define the operand which is to be used between minimum interest and minimum tax.Possible values are "AND/OR". |
| 37 | `CAPL.H.TX.FRMTYP.TAX.MIN.AMT` | `CaplHTxFormType_TaxMinAmt` | TField |  | This field is used to define the Minimum tax amt required for a slip to be printed.Valid T24 Amount. |
| 38 | `CAPL.H.TX.FRMTYP.TAX.MIN.FLD` | `CaplHTxFormType_TaxMinFld` | TField |  | Field is used to define he min tax field for the tax form type.Validation:It should be AMOUNT.CODE.1 to AMOUNT.CODE.9 from CAPL.TX.FORM.TEMPLATE table field. Check for SS Record of the particular field. |
| 39 | `CAPL.H.TX.FRMTYP.RELATION.CODES` | `CaplHTxFormType_RelationCodes` |  |  |  |
| 40 | `CAPL.H.TX.FRMTYP.NR.ACCOUNT.NO` | `CaplHTxFormType_NrAccountNo` | TField |  | Purpose of this field is to define theNon-resident Account number for the from type. |
| 41 | `CAPL.H.TX.FRMTYP.BUSINESS.NO` | `CaplHTxFormType_BusinessNo` | TField |  | This field is used to capture the CRA number. |
| 42 | `CAPL.H.TX.FRMTYP.FILER.ID.NO` | `CaplHTxFormType_FilerIdNo` | TField |  | Purpose of this field is used to define the Filer Identification no by CRA. This is used for filing of tax purpose.Freetext field 9 alphanumeric character. |
| 43 | `CAPL.H.TX.FRMTYP.BANK.TR.NO` | `CaplHTxFormType_BankTrNo` | TField |  | Field is used to define the Bank transit no for the tax filing.Freetext field 25 alphanumeric character. |
| 44 | `CAPL.H.TX.FRMTYP.SLIP.FORMAT` | `CaplHTxFormType_SlipFormat` | TField |  | This field is used to denote the deal slip format for the tax form to be printed.Valid record from DEAL.SLIP.FORMAT Table. |
| 45 | `CAPL.H.TX.FRMTYP.SLIP.NUMBER` | `CaplHTxFormType_SlipNumber` | TField |  |  |
| 46 | `CAPL.H.TX.FRMTYP.LOCAL.REF` | `CaplHTxFormType_LocalRef` |  |  |  |
| 47 | `CAPL.H.TX.FRMTYP.INC.SECTOR` | `CaplHTxFormType_IncSector` |  |  |  |
| 48 | `CAPL.H.TX.FRMTYP.EXC.SECTOR` | `CaplHTxFormType_ExcSector` |  |  |  |
| 49 | `CAPL.H.TX.FRMTYP.CERT.NO` | `CaplHTxFormType_CertNo` | TField |  | To define the certificate number for CRA reporting |
| 50 | `CAPL.H.TX.FRMTYP.SEQ.RL.NO` | `CaplHTxFormType_SeqRlNo` | TField |  | To define the sequence number position for R2 and R3 |
| 51 | `CAPL.H.TX.FRMTYP.PARTNER.ID` | `CaplHTxFormType_PartnerId` | TField | Yes | Holds the partner Id* Partner ID: RL Slips Partner Identifier Mandatory (Maximum of 16 alpha), the number that identifies the FI as a software developer and partner to the RL Slips and Information Slip field of activity. FI must have obtained this number from the "Direction des relations avec les partenaires et de la planification" before generating your test file. |
| 52 | `CAPL.H.TX.FRMTYP.PRODUCT.ID` | `CaplHTxFormType_ProductId` | TField | Yes | Holds the product id Note:* Product ID: RL Slips Product Identifier Mandatory (Maximum of 16 alpha), the identifier number of the product that is registered to the RL Slips and Information Slips field of activity. FI must have obtained this number from the "Direction des relations avec les partenaires et de la planification" before generating your test file. |
| 53 | `CAPL.H.TX.FRMTYP.TEST.CASE.NO` | `CaplHTxFormType_TestCaseNo` | TField | No | Holds the Test case Number for partner testing* Test case Number: Test Case Number Optional (Maximum of 25 alpha) This must only be used in the Partners Testing Environment to validate the test cases in order to obtain a certification number. Refer the SW-251-T guide for the list of test case numbers that can be used according to the type of RL slips. All the test cases must be executed in order.Applicable only for R2 and R3 |
| 54 | `CAPL.H.TX.FRMTYP.CIF.SECTOR` | `CaplHTxFormType_CifSector` |  |  |  |
| 55 | `CAPL.H.TX.FRMTYP.CIF.INDUSTRY` | `CaplHTxFormType_CifIndustry` |  |  |  |
| 56 | `CAPL.H.TX.FRMTYP.AUTH.NO` | `CaplHTxFormType_AuthNo` | TField |  | Field to indicate the authorization Number- to be part of the CRA Slip printed.Note: This field is only for information purpose. |
| 57 | `CAPL.H.TX.FRMTYP.SEQ.NO` | `CaplHTxFormType_SeqNo` | TField |  | Field to indicate the Sequential Number start range- to be part of the print slips.Note: This field is only for information purpose. |
| 58 | `CAPL.H.TX.FRMTYP.SEQ.NO.END` | `CaplHTxFormType_SeqNoEnd` | TField |  | Field to indicate the Sequential Number end range- to be part of the print slips.Note: This field is only for information purpose. |
| 59 | `CAPL.H.TX.FRMTYP.SLIP.NO.END` | `CaplHTxFormType_SlipNoEnd` | TField |  | Field Field to Hold the Slip Number Range provided by CRA.Note: Start range is defined in SLIP.NO, this field is to capture the slip send range.The slip number mentioned in this field should not be less than the actual SLIP.NUMBER field. |
| 60 | `CAPL.H.TX.FRMTYP.INC.PLANTYPE` | `CaplHTxFormType_IncPlantype` |  |  |  |
| 61 | `CAPL.H.TX.FRMTYP.EXC.PLANTYPE` | `CaplHTxFormType_ExcPlantype` |  |  |  |
| 62 | `CAPL.H.TX.FRMTYP.EXCLUDE.CUSTOMER` | `CaplHTxFormType_ExcludeCustomer` |  |  |  |
| 63 | `CAPL.H.TX.FRMTYP.DTH.SETTLE.PRE.YR` | `CaplHTxFormType_DthSettlePreYr` | TField |  | Applicable values YES/NOIf YES - if the death date of annuitant is in previous years, and settlement is done in current year, then DOD and DOD value will not be part of current year T4RSP and T4RIF xml.No - if the death date of annuitant is in previous years, and settlement is done in current year, then DOD and DOD value will be part of current year T4RSP and T4RIF xml. |
| 64 | `CAPL.H.TX.FRMTYP.RESERVED.8` | `CaplHTxFormType_Reserved8` |  |  |  |
| 65 | `CAPL.H.TX.FRMTYP.RESERVED.7` | `CaplHTxFormType_Reserved7` |  |  |  |
| 66 | `CAPL.H.TX.FRMTYP.RESERVED.6` | `CaplHTxFormType_Reserved6` |  |  |  |
| 67 | `CAPL.H.TX.FRMTYP.RESERVED.5` | `CaplHTxFormType_Reserved5` |  |  |  |
| 68 | `CAPL.H.TX.FRMTYP.RESERVED.4` | `CaplHTxFormType_Reserved4` |  |  |  |
| 69 | `CAPL.H.TX.FRMTYP.RESERVED.3` | `CaplHTxFormType_Reserved3` |  |  |  |
| 70 | `CAPL.H.TX.FRMTYP.RESERVED.2` | `CaplHTxFormType_Reserved2` | TField |  |  |
| 71 | `CAPL.H.TX.FRMTYP.RESERVED.1` | `CaplHTxFormType_Reserved1` | TField |  |  |
| 72 | `CAPL.H.TX.FRMTYP.OVERRIDE` | `CaplHTxFormType_Override` |  |  |  |
| 73 | `CAPL.H.TX.FRMTYP.RECORD.STATUS` | `CaplHTxFormType_RecordStatus` | String |  |  |
| 74 | `CAPL.H.TX.FRMTYP.CURR.NO` | `CaplHTxFormType_CurrNo` | String |  |  |
| 75 | `CAPL.H.TX.FRMTYP.INPUTTER` | `CaplHTxFormType_Inputter` |  |  |  |
| 76 | `CAPL.H.TX.FRMTYP.DATE.TIME` | `CaplHTxFormType_DateTime` |  |  |  |
| 77 | `CAPL.H.TX.FRMTYP.AUTHORISER` | `CaplHTxFormType_Authoriser` | String |  |  |
| 78 | `CAPL.H.TX.FRMTYP.CO.CODE` | `CaplHTxFormType_CoCode` | String |  |  |
| 79 | `CAPL.H.TX.FRMTYP.DEPT.CODE` | `CaplHTxFormType_DeptCode` | String |  |  |
| 80 | `CAPL.H.TX.FRMTYP.AUDITOR.CODE` | `CaplHTxFormType_AuditorCode` | String |  |  |
| 81 | `CAPL.H.TX.FRMTYP.AUDIT.DATE.TIME` | `CaplHTxFormType_AuditDateTime` | String |  |  |
