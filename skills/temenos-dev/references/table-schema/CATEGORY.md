# CATEGORY — Table Schema

> Source: `INSERTS/I_F.CATEGORY` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CAT.DESCRIPTION` | `Category_Description` |  |  |  |
| 2 | `EB.CAT.SHORT.NAME` | `Category_ShortName` |  |  |  |
| 3 | `EB.CAT.SYSTEM.IND` | `Category_SystemInd` | TField | Yes | Identifies the System to which the Category code belongs. This field identifies the System to which the Category code relates. This indicator enables T24 to ensure that a transaction is not assigned a Category code which is totally irrelevant to the business operation. The Codes are defined as follows: AC = Account AR = Asset Register BD = Bonds (not available) DG = Disagio FD = Fiduciaries FF = Financial Futures(not available) FR = Forward Rate Agreement FX = Foreign Exchange LC = Letters of Credit LD = Loans and Deposits MD = Miscellaneous Deals MG = Mortgage Loans MM = Money Market PD = Past Due Payments PL = Profit and Loss SC = Securities SL = Syndicated Loans (not available) SW = SWAPS LNTRAD = LOAN.TRADE Note : At the present time the codes defined above are the only inputs allowed for this field, but these will be updated as required to include other system codes. Validation Rules: 2/6 type SSS (uppercase alpha) character System code: AC, AR, BD, DG, FD, FF, FR, FX, LC, LD, MD, MG, MM, PD, PL, SC, SL, SW, LNTRAD Mandatory input PL Category 50000-69999 only |
| 4 | `EB.CAT.MI.CATEG.GROUP` | `Category_MiCategGroup` | TField | No | This field is used to specify the MI.CATEG.GROUP to which this category code belongs and is used within the MI module to make analysis simpler and more efficient. Validation Rules: Up to 6 alphanumeric characters. Must be a valid record on the MI.CATEG.GROUP file. This field cannot be input if MI is not installed as a product, otherwise optional input. |
| 5 | `EB.CAT.MI.ENTRY.TYPE.DFT` | `Category_MiEntryTypeDft` | TField | No | The default MI.ENTRY.TYPE for the category is specified in this field. MI.ENTRY.TYPEs are used within the MI module to identify the type of profit and loss entry being processed. The value in this field will be used as the default entry type within the MI.ENTRY, MI.AUTO.ENTRY and CATEG.ENTRY applications. Validation Rules: Must be a valid record on the MI.ENTRY.TYPE file. Input only allowed for profit and loss categories, i.e. category codes greater than 49999. This field c annot be input if MI is not installed as a product, otherwise optional. |
| 6 | `EB.CAT.MI.PL.ALLOC2.ID` | `Category_MiPlAlloc2Id` |  |  |  |
| 7 | `EB.CAT.MNEMONIC` | `Category_Mnemonic` | TField | No | Specifies an alternative easy means of referencing the Category. Any value can be entered in this field with the exception that the first character must be alpha. Like the ID, the Mnemonic must be unique across T24. Note : For each Category, the System will automatically update the internal file "MNEMONIC.CATEGORY" which allows the User to display the CATEGORY codes in Mnemonic sequence instead. Validation Rules: 3-10 type MNE (Uppercase alpha or numeric, first character alpha, or ".") characters. Optional input. |
| 8 | `EB.CAT.AC.CONTINGENT` | `Category_AcContingent` | TField |  | This field is populated by the ACCOUNT application when the account record is authorised. Possible defaulted values are CONTINGENT NON.CONTINGENT Validation Rules: At the time of setting up contingent categories in ACCOUNT.PARAMETER none of the Category codes within the ranges should have value NON.CONTINGENT |
| 9 | `EB.CAT.CONSOLIDATE.ENT` | `Category_ConsolidateEnt` | TField |  | If entries are to be consolidated the field CONSOLIDATE.ENT should contain the id to the AC.CONSOLIDATE.COND record that describes rules for consolidation. This must be set for consolidating entries raised for PL category. Then categ entries will be consolidated by the following consolidation criteria: Entry Type P&amp;L category Currency System Id Transaction Code Value Date Exposure Date Reversal Marker Currency Market Suspense Category Terminal Number Account Officer (P&amp;L only) Product Category (P&amp;L only) Plus any additional elements defined in AC.CONSOLIDATE.COND The combined key is structured as follows, the ! character is used as a delimeter: S!12345678!GBP!FT!210!20021126!!!1!!89 Validation Rules: |
| 10 | `EB.CAT.POSITION.TYPE` | `Category_PositionType` | TField |  | The position that accounts related to the category fall within. If not set will be designated as TR, for multi-gaap the position type would be the value of the reporting method used (IA, IF etc). Only used for internal account category range. Once set it cannot be changed if any account has been created using the category. Validation Rules: Only valid for range 10000 - 19999 No change if category has an account using it. Must be a valid FX.POS.TYPE record |
| 11 | `EB.CAT.LOSS.GIVEN.DEFT` | `Category_LossGivenDeft` | TField |  | Invalid Field Name. Hence not allowed to input |
| 12 | `EB.CAT.RESERVED.6` | `Category_Reserved6` | TField |  |  |
| 13 | `EB.CAT.RESERVED.5` | `Category_Reserved5` | TField |  |  |
| 14 | `EB.CAT.RESERVED.4` | `Category_Reserved4` | TField |  |  |
| 15 | `EB.CAT.RESERVED.3` | `Category_Reserved3` | TField |  |  |
| 16 | `EB.CAT.RESERVED.2` | `Category_Reserved2` | TField |  |  |
| 17 | `EB.CAT.RESERVED.1` | `Category_Reserved1` | TField |  |  |
| 18 | `EB.CAT.LOCAL.REF` | `Category_LocalRef` |  |  |  |
| 19 | `EB.CAT.RECORD.STATUS` | `Category_RecordStatus` | String |  |  |
| 20 | `EB.CAT.CURR.NO` | `Category_CurrNo` | String |  |  |
| 21 | `EB.CAT.INPUTTER` | `Category_Inputter` |  |  |  |
| 22 | `EB.CAT.DATE.TIME` | `Category_DateTime` |  |  |  |
| 23 | `EB.CAT.AUTHORISER` | `Category_Authoriser` | String |  |  |
| 24 | `EB.CAT.CO.CODE` | `Category_CoCode` | String |  |  |
| 25 | `EB.CAT.DEPT.CODE` | `Category_DeptCode` | String |  |  |
| 26 | `EB.CAT.AUDITOR.CODE` | `Category_AuditorCode` | String |  |  |
| 27 | `EB.CAT.AUDIT.DATE.TIME` | `Category_AuditDateTime` | String |  |  |
