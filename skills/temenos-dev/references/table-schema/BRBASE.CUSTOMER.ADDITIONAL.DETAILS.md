# BRBASE.CUSTOMER.ADDITIONAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.BRBASE.CUSTOMER.ADDITIONAL.DETAILS` in `BRBASE_CustomerCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BR.ACD.WEBSITE` | `BrbaseCustomerAdditionalDetails_Website` | TField |  | Field that hold information about borough of an especific CEP code. |
| 2 | `BR.ACD.WTF.REGIME` | `BrbaseCustomerAdditionalDetails_WtfRegime` | TField | Yes | Tax Regime For purposes of withholding tax. The allowed values are Immune, Exempt, Taxed. If �Taxed� is selected RFB.REGIME is mandatory. |
| 3 | `BR.ACD.RFB.REGIME` | `BrbaseCustomerAdditionalDetails_RfbRegime` | TField |  | Taxation Regime According to RFB. The allowed values are Simple, Presumed and Real. |
| 4 | `BR.ACD.BOUND.PERSON` | `BrbaseCustomerAdditionalDetails_BoundPerson` | TField |  | Field that hold information if the customer is bound person. The allowed values are YES and NO. |
| 5 | `BR.ACD.FORM.OF.CONSTITUTION` | `BrbaseCustomerAdditionalDetails_FormOfConstitution` | TField |  | Dropdown field that hold information about the form of constitution. |
| 6 | `BR.ACD.MAIN.ACTIVITY` | `BrbaseCustomerAdditionalDetails_MainActivity` | TField |  | Field that holds information about the customer main activity. |
| 7 | `BR.ACD.QUALIFICATION` | `BrbaseCustomerAdditionalDetails_Qualification` | TField |  | Field that hold the information about the qualification. |
| 8 | `BR.ACD.DIRECT.CONTROL.ENTITY` | `BrbaseCustomerAdditionalDetails_DirectControlEntity` |  |  |  |
| 9 | `BR.ACD.DIRECT.CONTROL.CNPJ.CPF` | `BrbaseCustomerAdditionalDetails_DirectControlCnpjCpf` |  |  |  |
| 10 | `BR.ACD.DIRECT.CONTROL.COUNTRY` | `BrbaseCustomerAdditionalDetails_DirectControlCountry` |  |  |  |
| 11 | `BR.ACD.DIRECT.CONTROL.TIN` | `BrbaseCustomerAdditionalDetails_DirectControlTin` |  |  |  |
| 12 | `BR.ACD.DIRECT.CONTROL.DATE` | `BrbaseCustomerAdditionalDetails_DirectControlDate` |  |  |  |
| 13 | `BR.ACD.DIRECT.CONTROL.HOLD` | `BrbaseCustomerAdditionalDetails_DirectControlHold` |  |  |  |
| 14 | `BR.ACD.EMPLOYMENT.UF` | `BrbaseCustomerAdditionalDetails_EmploymentUf` | TField |  | Field that hold Employment UF. |
| 15 | `BR.ACD.EMPLOYMENT.STREET` | `BrbaseCustomerAdditionalDetails_EmploymentStreet` | TField |  | Field that hold Employment Street. |
| 16 | `BR.ACD.EMPLOYMENT.TOWN.COUNTRY` | `BrbaseCustomerAdditionalDetails_EmploymentTownCountry` | TField |  | Field that hold Employment Town Country. |
| 17 | `BR.ACD.EMPLOYMENT.POSTAL.CODE` | `BrbaseCustomerAdditionalDetails_EmploymentPostalCode` | TField |  | Field that hold Employment Postal Code. |
| 18 | `BR.ACD.EMPLOYMENT.CITY` | `BrbaseCustomerAdditionalDetails_EmploymentCity` | TField |  | Field that hold Employment City. |
| 19 | `BR.ACD.EMPLOYMENT.EMAIL` | `BrbaseCustomerAdditionalDetails_EmploymentEmail` | TField |  | Field that hold Employment Email. |
| 20 | `BR.ACD.EMPLOYMENT.BOROUGH` | `BrbaseCustomerAdditionalDetails_EmploymentBorough` | TField |  | Field that hold Employment Borough. |
| 21 | `BR.ACD.EMPLOYMENT.COUNTRY` | `BrbaseCustomerAdditionalDetails_EmploymentCountry` | TField |  | Field that hold Employment Country. |
| 22 | `BR.ACD.FATCA.NAME` | `BrbaseCustomerAdditionalDetails_FatcaName` | TField |  | Field that hold if Fatca is required. The allowed values are YES and NO. |
| 23 | `BR.ACD.US.ASSOCIATES` | `BrbaseCustomerAdditionalDetails_UsAssociates` | TField |  | Field that hold infomation about if the customer has US citizens as partners or beneficiaries. The allowed values are YES and NO. |
| 24 | `BR.ACD.US.LAW` | `BrbaseCustomerAdditionalDetails_UsLaw` | TField |  | Field that hold infomation about if the company is behing US law. The allowed values are YES and NO. |
| 25 | `BR.ACD.CONTROL.ENTITY` | `BrbaseCustomerAdditionalDetails_ControlEntity` |  |  |  |
| 26 | `BR.ACD.INDIRECT.CNPJ.CPF` | `BrbaseCustomerAdditionalDetails_IndirectCnpjCpf` |  |  |  |
| 27 | `BR.ACD.INDIRECT.COUNTRY` | `BrbaseCustomerAdditionalDetails_IndirectCountry` |  |  |  |
| 28 | `BR.ACD.INDIRECT.TIN` | `BrbaseCustomerAdditionalDetails_IndirectTin` |  |  |  |
| 29 | `BR.ACD.INDIRECT.DATE` | `BrbaseCustomerAdditionalDetails_IndirectDate` |  |  |  |
| 30 | `BR.ACD.INDIRECT.HOLD` | `BrbaseCustomerAdditionalDetails_IndirectHold` |  |  |  |
| 31 | `BR.ACD.MARRIAGE.REGIME` | `BrbaseCustomerAdditionalDetails_MarriageRegime` | TField |  | Field that hold Marriage Regime. Values provided from MARRIAGE.REGIME eblookup. |
| 32 | `BR.ACD.TAX.EXEMPTION` | `BrbaseCustomerAdditionalDetails_TaxExemption` | TField |  | Field that hold information if the customer is tax exempted. The allowed values are YES and NO. |
| 33 | `BR.ACD.TAX.START.DATE` | `BrbaseCustomerAdditionalDetails_TaxStartDate` | TField |  | Field that hold information about tax exempted start date. |
| 34 | `BR.ACD.TAX.END.DATE` | `BrbaseCustomerAdditionalDetails_TaxEndDate` | TField |  | Field that hold information about tax exempted end date. |
| 35 | `BR.ACD.INJUNCTION.NUMBER` | `BrbaseCustomerAdditionalDetails_InjunctionNumber` | TField |  | Field that hold information about injunction number. |
| 36 | `BR.ACD.DATE.INJUNCTION` | `BrbaseCustomerAdditionalDetails_DateInjunction` | TField |  | Field that hold information about date injunction. |
| 37 | `BR.ACD.DATE.SUSPENSION` | `BrbaseCustomerAdditionalDetails_DateSuspension` | TField |  | Field that hold information about date suspension. |
| 38 | `BR.ACD.EMANCIPATION` | `BrbaseCustomerAdditionalDetails_Emancipation` | TField |  | Field that hold information about emancipation. Values provided from EMANCIPATION eblookup. |
| 39 | `BR.ACD.TAX.EXEMPTION.FIN` | `BrbaseCustomerAdditionalDetails_TaxExemptionFin` | TField |  | Field that hold information about Exemption from taxes on financial transactions. The allowed values are YES and NO. |
| 40 | `BR.ACD.INJUNCTION.NOTE` | `BrbaseCustomerAdditionalDetails_InjunctionNote` | TField |  | Field that hold information about Injunction note. |
| 41 | `BR.ACD.SUSPENSION.REASON` | `BrbaseCustomerAdditionalDetails_SuspensionReason` | TField |  | Field that hold information about suspension reason. |
| 42 | `BR.ACD.POLITICALLY.EXPOSED.RELATED` | `BrbaseCustomerAdditionalDetails_PoliticallyExposedRelated` | TField |  | Field that hold information if the customer is related to a politically exposed person. The allowed values are YES and NO. |
| 43 | `BR.ACD.POLITICALLY.EXPOSED.NAME` | `BrbaseCustomerAdditionalDetails_PoliticallyExposedName` |  |  |  |
| 44 | `BR.ACD.POLITICALLY.EXPOSED.ID` | `BrbaseCustomerAdditionalDetails_PoliticallyExposedId` |  |  |  |
| 45 | `BR.ACD.POLITICALLY.EXPOSED.COUNTRY` | `BrbaseCustomerAdditionalDetails_PoliticallyExposedCountry` |  |  |  |
| 46 | `BR.ACD.CHANGES` | `BrbaseCustomerAdditionalDetails_Changes` | TField |  | Field for internal purpose. No user input. |
| 47 | `BR.ACD.RESERVED.15` | `BrbaseCustomerAdditionalDetails_Reserved15` | TField |  | Reserved field - This is used for future purpose |
| 48 | `BR.ACD.RESERVED.14` | `BrbaseCustomerAdditionalDetails_Reserved14` | TField |  | Reserved field - This is used for future purpose |
| 49 | `BR.ACD.RESERVED.13` | `BrbaseCustomerAdditionalDetails_Reserved13` | TField |  | Reserved field - This is used for future purpose |
| 50 | `BR.ACD.RESERVED.12` | `BrbaseCustomerAdditionalDetails_Reserved12` | TField |  | Reserved field - This is used for future purpose |
| 51 | `BR.ACD.RESERVED.11` | `BrbaseCustomerAdditionalDetails_Reserved11` | TField |  | Reserved field - This is used for future purpose |
| 52 | `BR.ACD.RESERVED.10` | `BrbaseCustomerAdditionalDetails_Reserved10` | TField |  | Reserved field - This is used for future purpose |
| 53 | `BR.ACD.RESERVED.9` | `BrbaseCustomerAdditionalDetails_Reserved9` | TField |  | Reserved field - This is used for future purpose |
| 54 | `BR.ACD.RESERVED.8` | `BrbaseCustomerAdditionalDetails_Reserved8` | TField |  | Reserved field - This is used for future purpose |
| 55 | `BR.ACD.RESERVED.7` | `BrbaseCustomerAdditionalDetails_Reserved7` | TField |  | Reserved field - This is used for future purpose |
| 56 | `BR.ACD.RESERVED.6` | `BrbaseCustomerAdditionalDetails_Reserved6` | TField |  | Reserved field - This is used for future purpose |
| 57 | `BR.ACD.RESERVED.5` | `BrbaseCustomerAdditionalDetails_Reserved5` | TField |  | Reserved field - This is used for future purpose |
| 58 | `BR.ACD.RESERVED.4` | `BrbaseCustomerAdditionalDetails_Reserved4` | TField |  | Reserved field - This is used for future purpose |
| 59 | `BR.ACD.RESERVED.3` | `BrbaseCustomerAdditionalDetails_Reserved3` | TField |  | Reserved field - This is used for future purpose |
| 60 | `BR.ACD.RESERVED.2` | `BrbaseCustomerAdditionalDetails_Reserved2` | TField |  | Reserved field - This is used for future purpose |
| 61 | `BR.ACD.RESERVED.1` | `BrbaseCustomerAdditionalDetails_Reserved1` | TField |  | Reserved field - This is used for future purpose |
| 62 | `BR.ACD.LOCAL.REF` | `BrbaseCustomerAdditionalDetails_LocalRef` |  |  |  |
| 63 | `BR.ACD.OVERRIDE` | `BrbaseCustomerAdditionalDetails_Override` |  |  |  |
| 64 | `BR.ACD.RECORD.STATUS` | `BrbaseCustomerAdditionalDetails_RecordStatus` | String |  |  |
| 65 | `BR.ACD.CURR.NO` | `BrbaseCustomerAdditionalDetails_CurrNo` | String |  |  |
| 66 | `BR.ACD.INPUTTER` | `BrbaseCustomerAdditionalDetails_Inputter` |  |  |  |
| 67 | `BR.ACD.DATE.TIME` | `BrbaseCustomerAdditionalDetails_DateTime` |  |  |  |
| 68 | `BR.ACD.AUTHORISER` | `BrbaseCustomerAdditionalDetails_Authoriser` | String |  |  |
| 69 | `BR.ACD.CO.CODE` | `BrbaseCustomerAdditionalDetails_CoCode` | String |  |  |
| 70 | `BR.ACD.DEPT.CODE` | `BrbaseCustomerAdditionalDetails_DeptCode` | String |  |  |
| 71 | `BR.ACD.AUDITOR.CODE` | `BrbaseCustomerAdditionalDetails_AuditorCode` | String |  |  |
| 72 | `BR.ACD.AUDIT.DATE.TIME` | `BrbaseCustomerAdditionalDetails_AuditDateTime` | String |  |  |
