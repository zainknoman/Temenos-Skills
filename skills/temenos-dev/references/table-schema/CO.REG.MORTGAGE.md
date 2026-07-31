# CO.REG.MORTGAGE — Table Schema

> Source: `INSERTS/I_F.CO.REG.MORTGAGE` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.MTG.DESCRIPTION` | `CoRegMortgage_Description` |  |  |  |
| 2 | `CO.MTG.CLA.NUMBER` | `CoRegMortgage_ClaNumber` | TField |  | Conditional Loan Approval document number which is a support document needed for the mortgage. |
| 3 | `CO.MTG.CUSTOMER` | `CoRegMortgage_Customer` | TField |  | Owner of the Mortgage Collateral Validation Rules: Valid Customer record. |
| 4 | `CO.MTG.AGREEMENT.DATE` | `CoRegMortgage_AgreementDate` | TField |  | Date on which the Mortgage agreement is signed. |
| 5 | `CO.MTG.VALUE.DATE` | `CoRegMortgage_ValueDate` | TField |  | Date on which the mortgage is taken as Collateral. Validation Rules: 11 digit Date format field. Default value is today's date. |
| 6 | `CO.MTG.END.DATE` | `CoRegMortgage_EndDate` | TField | Yes | Date on which the mortgage will expire. Validation Rules: Mandatory field. Date cannot be earlier than the Value date. |
| 7 | `CO.MTG.PROPERTY.REF` | `CoRegMortgage_PropertyRef` |  |  |  |
| 8 | `CO.MTG.PROP.VAL.CCY` | `CoRegMortgage_PropValCcy` |  |  |  |
| 9 | `CO.MTG.PROP.DISTRICT` | `CoRegMortgage_PropDistrict` |  |  |  |
| 10 | `CO.MTG.RESERVED15` | `CoRegMortgage_Reserved15` |  |  |  |
| 11 | `CO.MTG.RESERVED14` | `CoRegMortgage_Reserved14` |  |  |  |
| 12 | `CO.MTG.RESERVED13` | `CoRegMortgage_Reserved13` |  |  |  |
| 13 | `CO.MTG.RESERVED12` | `CoRegMortgage_Reserved12` |  |  |  |
| 14 | `CO.MTG.RESERVED11` | `CoRegMortgage_Reserved11` |  |  |  |
| 15 | `CO.MTG.CURRENCY` | `CoRegMortgage_Currency` | TField |  | Currency of the Mortgage Collateral Validation Rules: Valid currency. |
| 16 | `CO.MTG.LAND.REG.DISTRICT` | `CoRegMortgage_LandRegDistrict` | TField |  | The district where the Mortgage is registered. |
| 17 | `CO.MTG.REGISTRATION.NO` | `CoRegMortgage_RegistrationNo` | TField |  | TThe ID/number for Mortgage registration. |
| 18 | `CO.MTG.CONTRACT.REF` | `CoRegMortgage_ContractRef` | TField |  | The assignment contract reference which the bank will update in case of transfer of mortgage. |
| 19 | `CO.MTG.REGISTER.DATE` | `CoRegMortgage_RegisterDate` | TField |  |  |
| 20 | `CO.MTG.REG.COMP.DATE` | `CoRegMortgage_RegCompDate` | TField |  | The date on which the mortgage registration took place at Registrar of Companies |
| 21 | `CO.MTG.MORTGAGE.RANK` | `CoRegMortgage_MortgageRank` | TField |  | Rank of the given mortgage, for information purpose |
| 22 | `CO.MTG.MARKET.VALUE` | `CoRegMortgage_MarketValue` | TField |  | Fair market value of a given Mortgage in the open market |
| 23 | `CO.MTG.INT.RATE` | `CoRegMortgage_IntRate` | TField |  | Interest Rate at which the Mortgage is given. |
| 24 | `CO.MTG.TOT.MARKET.VALUE.CUR` | `CoRegMortgage_TotMarketValueCur` | TField |  | The sum of the fair market value of all the underlying immovable properties under a given mortgage. |
| 25 | `CO.MTG.TOT.MARKET.VALUE.COMP` | `CoRegMortgage_TotMarketValueComp` | TField |  | The sum of the fair market value of all the underlying finished or completed immovable properties under a given mortgage. |
| 26 | `CO.MTG.FORCED.SALE.VALUE.CUR` | `CoRegMortgage_ForcedSaleValueCur` | TField |  | The estimated amount of the Mortgage during an unforeseen or uncontrollable event. |
| 27 | `CO.MTG.FORCED.SALE.VALUE.COMP` | `CoRegMortgage_ForcedSaleValueComp` | TField |  | The estimated amount of the Mortgage during an unforeseen or uncontrollable event after completion of any sort of construction of the Mortgage. |
| 28 | `CO.MTG.COEFFICIENT` | `CoRegMortgage_Coefficient` | TField | No | The Margin rate to be applicable on Mortgage. Validation Rules: Optional field. When left as blank, system will consider the rate as 100%. |
| 29 | `CO.MTG.ADJ.MARKET.VALUE` | `CoRegMortgage_AdjMarketValue` | TField |  | The adjusted Market value calculated by the sytem by applying Margin rate on the Market value. Validation Rules: NOINPUT field. Maintained by System. |
| 30 | `CO.MTG.SUG.ADJ.MARKET.VALUE` | `CoRegMortgage_SugAdjMarketValue` | TField | No | The Mortgage value given by the user. If not given, defaulted as Adj Market value. Validation Rules: Up to 19-digit numeric, inclusive decimal point (amount format). Optional input. |
| 31 | `CO.MTG.NOTES` | `CoRegMortgage_Notes` |  |  |  |
| 32 | `CO.MTG.COLLATERAL.TYPE` | `CoRegMortgage_CollateralType` | TField |  | The type of Collateral which will be updated from the Transact system when linked to Collateral. |
| 33 | `CO.MTG.COLLATERAL.ID` | `CoRegMortgage_CollateralId` | TField |  | The reference ID of Collateral to which this mortgage is attached. System maintained field. Validation Rules: NOINPUT field. Maintained by System. |
| 34 | `CO.MTG.RESERVED10` | `CoRegMortgage_Reserved10` | TField |  |  |
| 35 | `CO.MTG.RESERVED9` | `CoRegMortgage_Reserved9` | TField |  |  |
| 36 | `CO.MTG.RESERVED8` | `CoRegMortgage_Reserved8` | TField |  |  |
| 37 | `CO.MTG.RESERVED7` | `CoRegMortgage_Reserved7` | TField |  |  |
| 38 | `CO.MTG.RESERVED6` | `CoRegMortgage_Reserved6` | TField |  |  |
| 39 | `CO.MTG.RESERVED5` | `CoRegMortgage_Reserved5` | TField |  |  |
| 40 | `CO.MTG.RESERVED4` | `CoRegMortgage_Reserved4` | TField |  |  |
| 41 | `CO.MTG.RESERVED3` | `CoRegMortgage_Reserved3` | TField |  |  |
| 42 | `CO.MTG.RESERVED2` | `CoRegMortgage_Reserved2` | TField |  |  |
| 43 | `CO.MTG.RESERVED1` | `CoRegMortgage_Reserved1` | TField |  |  |
| 44 | `CO.MTG.LOCAL.REF` | `CoRegMortgage_LocalRef` |  |  |  |
| 45 | `CO.MTG.OVERRIDE` | `CoRegMortgage_Override` |  |  |  |
| 46 | `CO.MTG.RECORD.STATUS` | `CoRegMortgage_RecordStatus` | String |  |  |
| 47 | `CO.MTG.CURR.NO` | `CoRegMortgage_CurrNo` | String |  |  |
| 48 | `CO.MTG.INPUTTER` | `CoRegMortgage_Inputter` |  |  |  |
| 49 | `CO.MTG.DATE.TIME` | `CoRegMortgage_DateTime` |  |  |  |
| 50 | `CO.MTG.AUTHORISER` | `CoRegMortgage_Authoriser` | String |  |  |
| 51 | `CO.MTG.CO.CODE` | `CoRegMortgage_CoCode` | String |  |  |
| 52 | `CO.MTG.DEPT.CODE` | `CoRegMortgage_DeptCode` | String |  |  |
| 53 | `CO.MTG.AUDITOR.CODE` | `CoRegMortgage_AuditorCode` | String |  |  |
| 54 | `CO.MTG.AUDIT.DATE.TIME` | `CoRegMortgage_AuditDateTime` | String |  |  |
