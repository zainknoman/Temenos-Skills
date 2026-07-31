# DESCTX.ACCOUNT.STAGING — Table Schema

> Source: `INSERTS/I_F.DESCTX.ACCOUNT.STAGING` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DESCTX.TAX.FREE.AMOUNT` | `DesctxAccountStaging_TaxFreeAmount` | TField |  | Total tax free amount for the Arrangement activity reference before optimization/correction |
| 2 | `DESCTX.KIST.SIGN` | `DesctxAccountStaging_KistSign` | TField |  | Sign for LST amount. The possible values are P=Plus, M=Minus |
| 3 | `DESCTX.KIST.AMOUNT` | `DesctxAccountStaging_KistAmount` | TField |  | LST amount |
| 4 | `DESCTX.SOLIDARITY.SIGN` | `DesctxAccountStaging_SolidaritySign` | TField |  | Sign for solidarity surcharge. The possible values are P=Plus, M=Minus |
| 5 | `DESCTX.SOLIDARITY.AMOUNT` | `DesctxAccountStaging_SolidarityAmount` | TField |  | Solidarity surcharge amount |
| 6 | `DESCTX.TOTAL.CHURCH.TAX.SIGN` | `DesctxAccountStaging_TotalChurchTaxSign` | TField |  | Church Tx sign. The possible values are P=Plus, M=Minus |
| 7 | `DESCTX.TOTAL.CHURCH.TAX.AMOUNT` | `DesctxAccountStaging_TotalChurchTaxAmount` | TField |  | Total Church Tax amount |
| 8 | `DESCTX.CHURCH.PARTNER1.SIGN` | `DesctxAccountStaging_ChurchPartner1Sign` | TField |  | Sign for Church Tax Partner-1. The possible values are P=Plus, M=Minus |
| 9 | `DESCTX.CHURCH.PARTNER1.AMOUNT` | `DesctxAccountStaging_ChurchPartner1Amount` | TField |  | Church Tax amount for partner-1 |
| 10 | `DESCTX.CHURCH.PARTNER2.SIGN` | `DesctxAccountStaging_ChurchPartner2Sign` | TField |  | Sign for Church Tax Partner-2. The possible values are P=Plus, M=Minus |
| 11 | `DESCTX.CHURCH.PARTNER2.AMOUNT` | `DesctxAccountStaging_ChurchPartner2Amount` | TField |  | Church Tax amount for partner-2 |
| 12 | `DESCTX.CORRECTED.TRN` | `DesctxAccountStaging_CorrectedTrn` | TField |  | This field denotes the transaction reference of the corrected transaction |
| 13 | `DESCTX.STATUS.CODE` | `DesctxAccountStaging_StatusCode` | TField |  | It denotes the status of the transaction. Possible valuesre: 1�Transaction�Received 2 Ready�For�Processing 3�Objection�To�Tax Claims 4 Objection�To�Tax Claims Utilizing�Limit 5 Taxdjustment Raised to Suspense 6 Taxdjustment Not Raised 7 Cancelled 8 Taxdjustment Raised to Customer |
| 14 | `DESCTX.DETAIL.STATUS` | `DesctxAccountStaging_DetailStatus` | TField |  | This field indicates the additional information about transaction |
| 15 | `DESCTX.REQUEST.STRING` | `DesctxAccountStaging_RequestString` |  |  |  |
| 16 | `DESCTX.STATEMENT.DETAILS` | `DesctxAccountStaging_StatementDetails` |  |  |  |
| 17 | `DESCTX.LOCAL.REF` | `DesctxAccountStaging_LocalRef` |  |  |  |
| 18 | `DESCTX.POSTING.IDENTIFIER` | `DesctxAccountStaging_PostingIdentifier` | TField |  | This field containsn indicator for the booking transaction. Possible valuesre: OPT = optimization booking OPE = couple LCA consumption (egüVv) CO1 = correction booking initiated byutomatic Correction Process CO2 = correction booking initiated by Manual Correction Process CO3 = correction booking initiated by Delta Correction Process CLA =dditional claim booking initiated by Sectras due to negative LCA (Loss Consumptionccounts) VSI = Taxable virtual sale due to drop out of investment tax law PLS = Taxable preliminary lump sum If system parameter “Separate book keeping codes for businessssets / Separate Buchungsschlüssel für Betriebsvermögen�? (BOOKING_CODES_ BUSINESS_ASSET) is set true the posting identifiers will be expanded by B for businesssset BOPT = optimization booking BCO1 = correction booking initiated byutomatic Correction Process BCO2 = correction booking initiated by Manual Correction Process BCO3 = correction booking initiated by Delta Correction Process BCLA =dditional claim booking initiated by Sectras due to negative LCA (Loss Consumptionccounts) BVSI = Taxable virtual sale due to drop out of investment tax law BPLS = Taxable preliminary lump sum |
| 19 | `DESCTX.TAX.SETTLE.ACCOUNT` | `DesctxAccountStaging_TaxSettleAccount` | TField |  | This field contains theccount number specified for optimization/correction booking for the partner group. If noccount is specified, it should be zero |
| 20 | `DESCTX.PARTNER.1` | `DesctxAccountStaging_Partner1` | TField |  | This field contains the customer identification of partner 1 |
| 21 | `DESCTX.PARTNER.2` | `DesctxAccountStaging_Partner2` | TField |  | This field contains the customer identification number of Partner 2 |
| 22 | `DESCTX.EMP.INDI.1` | `DesctxAccountStaging_EmpIndi1` | TField |  | This field containsn employee indicator for customer identification number 1. Possible valuesre: Y = employee, N = non employee |
| 23 | `DESCTX.OVERRIDE` | `DesctxAccountStaging_Override` |  |  |  |
| 24 | `DESCTX.RECORD.STATUS` | `DesctxAccountStaging_RecordStatus` | String |  |  |
| 25 | `DESCTX.CURR.NO` | `DesctxAccountStaging_CurrNo` | String |  |  |
| 26 | `DESCTX.INPUTTER` | `DesctxAccountStaging_Inputter` |  |  |  |
| 27 | `DESCTX.DATE.TIME` | `DesctxAccountStaging_DateTime` |  |  |  |
| 28 | `DESCTX.AUTHORISER` | `DesctxAccountStaging_Authoriser` | String |  |  |
| 29 | `DESCTX.CO.CODE` | `DesctxAccountStaging_CoCode` | String |  |  |
| 30 | `DESCTX.DEPT.CODE` | `DesctxAccountStaging_DeptCode` | String |  |  |
| 31 | `DESCTX.AUDITOR.CODE` | `DesctxAccountStaging_AuditorCode` | String |  |  |
| 32 | `DESCTX.AUDIT.DATE.TIME` | `DesctxAccountStaging_AuditDateTime` | String |  |  |
| 33 | `DESCTX.EMP.INDI.2` | `DesctxAccountStaging_EmpIndi2` | TField |  | This field containsn employee indicator for customer identification number 2. Possible valuesre: Y = employee, N = non employee |
| 34 | `DESCTX.EXT.TXN.NO` | `DesctxAccountStaging_ExtTxnNo` | TField |  | This field contains the unique transaction number generated by Sectras |
| 35 | `DESCTX.DATE.OPT` | `DesctxAccountStaging_DateOpt` | TField |  | This field contains the optimization date (ex:20090315 or Empty) |
| 36 | `DESCTX.VALUE.DATE` | `DesctxAccountStaging_ValueDate` | TField |  | This field contains the value date(ex:20090315 or Empty) |
| 37 | `DESCTX.SEC.IDEN.TYPE` | `DesctxAccountStaging_SecIdenType` | TField |  | This field describes the type of securities identification. Valid codes: I = ISIN W = German securities identification number Dom 9690 |
| 38 | `DESCTX.SEC.IDENTIFIER` | `DesctxAccountStaging_SecIdentifier` | TField |  | This field contains in dependence on field SEC_CODE_TYPE either the security number or the ISIN. |
| 39 | `DESCTX.USER.IDEN.CORR` | `DesctxAccountStaging_UserIdenCorr` | TField |  | This field contains Identification of the user who triggers the correction |
| 40 | `DESCTX.TAX.FREE.AMT.BEFORE` | `DesctxAccountStaging_TaxFreeAmtBefore` | TField |  | FSA tax freemount before optimization/correction |
| 41 | `DESCTX.LCA.EQ.BEFORE` | `DesctxAccountStaging_LcaEqBefore` | TField |  | Totalmount of losses by shares before optimization/correction |
| 42 | `DESCTX.LCA.OTHERS.BEFORE` | `DesctxAccountStaging_LcaOthersBefore` | TField |  | Totalmount of losses by bonds before optimization/correction |
| 43 | `DESCTX.LCA.FR.WHT.TAX.BEFORE` | `DesctxAccountStaging_LcaFrWhtTaxBefore` | TField |  | Totalmount of not utilizedccountable foreign tax deductedt source before optimization/correction |
| 44 | `DESCTX.LCA.EQ.AFTER` | `DesctxAccountStaging_LcaEqAfter` | TField |  | Totalmount of losses by sharesfter optimization/correction |
| 45 | `DESCTX.LCA.OTHERS.AFTER` | `DesctxAccountStaging_LcaOthersAfter` | TField |  | Totalmount of losses by bondsfter optimization/correction |
| 46 | `DESCTX.LCA.FR.WHT.TAX.AFTER` | `DesctxAccountStaging_LcaFrWhtTaxAfter` | TField |  | Totalmount of not utilizedccountable foreign tax deductedt sourcefter optimization/correction |
| 47 | `DESCTX.FED.KEST.PAY.ADV` | `DesctxAccountStaging_FedKestPayAdv` | TField |  | This field contains the federal state for KeStdvice .SECTRAS Domain 16000 (BW-Berlin,BE-Baden-Wuerttemberg) |
| 48 | `DESCTX.REL.DENOM.PART.1` | `DesctxAccountStaging_RelDenomPart1` | TField |  | This field contains the religious denomination of the partner with the lower partner identification number.SECTRAS DOMAIN 9124 (rk) roman catholic) |
| 49 | `DESCTX.CHU.TAX.RATE.PART.1` | `DesctxAccountStaging_ChuTaxRatePart1` | TField |  | This field contains the church tax rate of the partner with the lower partner identification number |
| 50 | `DESCTX.REL.DENOM.PART.2` | `DesctxAccountStaging_RelDenomPart2` | TField |  | This field contains the religious denomination of the partner with the higher partner identification number.SECTRAS DOMAIN 9124 (rk) roman catholic) |
| 51 | `DESCTX.CHU.TAX.RATE.PART.2` | `DesctxAccountStaging_ChuTaxRatePart2` | TField |  | This field contains the church tax rate of the partner with the higher partner identification number |
| 52 | `DESCTX.CHU.TAX.CAL.IND.PART.1` | `DesctxAccountStaging_ChuTaxCalIndPart1` | TField |  | This field contains church tax calculation indicator of the partner with the lower partner identification number.SECTRAS DOMAIN 9720 (YES / NO) |
| 53 | `DESCTX.CHU.TAX.CAL.IND.PART.2` | `DesctxAccountStaging_ChuTaxCalIndPart2` | TField |  | This field contains church tax calculation indicator of the partner with the higher partner identification number |
| 54 | `DESCTX.NO.REBOOKING.BLOCKS` | `DesctxAccountStaging_NoRebookingBlocks` | TField |  | Counter repeating group rebooking |
| 55 | `DESCTX.TAX.COLL.ORG.1` | `DesctxAccountStaging_TaxCollOrg1` | TField |  | This field contains the numeric code of the tax collectable organization unit Partner 1 (with beginning of 2015). |
| 56 | `DESCTX.NAME.TAX.COLL.ORG.1` | `DesctxAccountStaging_NameTaxCollOrg1` |  |  |  |
| 57 | `DESCTX.TAX.COLL.ORG.2` | `DesctxAccountStaging_TaxCollOrg2` | TField |  | This field contains the numeric code of the tax collectable organization unit Partner 2 (with beginning of 2015). |
| 58 | `DESCTX.NAME.TAX.COLL.ORG.2` | `DesctxAccountStaging_NameTaxCollOrg2` |  |  |  |
| 59 | `DESCTX.INDI.REBOOK.BLOCK` | `DesctxAccountStaging_IndiRebookBlock` |  |  |  |
| 60 | `DESCTX.SIGN.KEST.REBOOK.FROM` | `DesctxAccountStaging_SignKestRebookFrom` |  |  |  |
| 61 | `DESCTX.KEST.REBOOK.FROM` | `DesctxAccountStaging_KestRebookFrom` |  |  |  |
| 62 | `DESCTX.SIGN.SOLIDARITY.FROM` | `DesctxAccountStaging_SignSolidarityFrom` |  |  |  |
| 63 | `DESCTX.SOLIDARITY.REBOOK.FROM` | `DesctxAccountStaging_SolidarityRebookFrom` |  |  |  |
| 64 | `DESCTX.FED.STATE.KEST.PAY.FROM` | `DesctxAccountStaging_FedStateKestPayFrom` |  |  |  |
| 65 | `DESCTX.SIGN.KEST.REBOOK.TO` | `DesctxAccountStaging_SignKestRebookTo` |  |  |  |
| 66 | `DESCTX.KEST.REBOOK.TO` | `DesctxAccountStaging_KestRebookTo` |  |  |  |
| 67 | `DESCTX.SIGN.SOLIDARITY.TO` | `DesctxAccountStaging_SignSolidarityTo` |  |  |  |
| 68 | `DESCTX.SOLIDARITY.REBOOK.TO` | `DesctxAccountStaging_SolidarityRebookTo` |  |  |  |
| 69 | `DESCTX.FED.STATE.KEST.PAY.TO` | `DesctxAccountStaging_FedStateKestPayTo` |  |  |  |
| 70 | `DESCTX.SIGN.CHU.TAX.PART.1.FROM` | `DesctxAccountStaging_SignChuTaxPart1From` |  |  |  |
| 71 | `DESCTX.CHU.TAX.PART.1.FROM` | `DesctxAccountStaging_ChuTaxPart1From` |  |  |  |
| 72 | `DESCTX.REL.DENOM.PART.1.FROM` | `DesctxAccountStaging_RelDenomPart1From` |  |  |  |
| 73 | `DESCTX.SIGN.CHU.TAX.PART.1.TO` | `DesctxAccountStaging_SignChuTaxPart1To` |  |  |  |
| 74 | `DESCTX.CHU.TAX.PART.1.TO` | `DesctxAccountStaging_ChuTaxPart1To` |  |  |  |
| 75 | `DESCTX.REL.DENOM.PART.1.TO` | `DesctxAccountStaging_RelDenomPart1To` |  |  |  |
| 76 | `DESCTX.SIGN.CHU.TAX.PART.2.FROM` | `DesctxAccountStaging_SignChuTaxPart2From` |  |  |  |
| 77 | `DESCTX.CHU.TAX.PART.2.FROM` | `DesctxAccountStaging_ChuTaxPart2From` |  |  |  |
| 78 | `DESCTX.REL.DENOM.PART.2.FROM` | `DesctxAccountStaging_RelDenomPart2From` |  |  |  |
| 79 | `DESCTX.SIGN.CHU.TAX.PART.2.TO` | `DesctxAccountStaging_SignChuTaxPart2To` |  |  |  |
| 80 | `DESCTX.CHU.TAX.PART.2.TO` | `DesctxAccountStaging_ChuTaxPart2To` |  |  |  |
| 81 | `DESCTX.REL.DENOM.PART.2.TO` | `DesctxAccountStaging_RelDenomPart2To` |  |  |  |
| 82 | `DESCTX.USER.NAME.CORR.TXN` | `DesctxAccountStaging_UserNameCorrTxn` |  |  |  |
| 83 | `DESCTX.TAX.COLL.ORG.PART.1.FROM` | `DesctxAccountStaging_TaxCollOrgPart1From` |  |  |  |
| 84 | `DESCTX.NAME.COLL.ORG.PART.1.FROM` | `DesctxAccountStaging_NameCollOrgPart1From` |  |  |  |
| 85 | `DESCTX.TAX.COLL.ORG.PART.1.TO` | `DesctxAccountStaging_TaxCollOrgPart1To` |  |  |  |
| 86 | `DESCTX.NAME.COLL.ORG.PART.1.TO` | `DesctxAccountStaging_NameCollOrgPart1To` |  |  |  |
| 87 | `DESCTX.TAX.COLL.ORG.PART.2.FROM` | `DesctxAccountStaging_TaxCollOrgPart2From` |  |  |  |
| 88 | `DESCTX.NAME.COLL.ORG.PART.2.FROM` | `DesctxAccountStaging_NameCollOrgPart2From` |  |  |  |
| 89 | `DESCTX.TAX.COLL.ORG.PART.2.TO` | `DesctxAccountStaging_TaxCollOrgPart2To` |  |  |  |
| 90 | `DESCTX.NAME.COLL.ORG.PART.2.TO` | `DesctxAccountStaging_NameCollOrgPart2To` |  |  |  |
| 91 | `DESCTX.STATUS.REMARKS` | `DesctxAccountStaging_StatusRemarks` |  |  |  |
| 92 | `DESCTX.DEBIT.ACCOUNT.NUMBER` | `DesctxAccountStaging_DebitAccountNumber` | TField |  | This will contain theccount, which has been Debited / Credited. Ifccount Mode is SAO,�this will be captured with the Tax Settlementccount Ifccount Mode is SSS,�this will be captured with the Suspenseccount as configured inCCOUNT.CLASS Ifccount Mode is SNP,�this will be Null |
