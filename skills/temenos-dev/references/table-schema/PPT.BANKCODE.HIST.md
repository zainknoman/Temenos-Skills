# PPT.BANKCODE.HIST — Table Schema

> Source: `INSERTS/I_F.PPT.BANKCODE.HIST` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCDH.BankCodeID` | `PptBankcodeHist_Bankcodeid` |  |  |  |
| 2 | `PPBCDH.CompanyID` | `PptBankcodeHist_Companyid` |  |  |  |
| 3 | `PPBCDH.CountryCode` | `PptBankcodeHist_Countrycode` |  |  |  |
| 4 | `PPBCDH.NationalID` | `PptBankcodeHist_Nationalid` |  |  |  |
| 5 | `PPBCDH.StartDateBankCode` | `PptBankcodeHist_Startdatebankcode` |  |  |  |
| 6 | `PPBCDH.BICCode` | `PptBankcodeHist_Biccode` |  |  |  |
| 7 | `PPBCDH.FinancialInstitutionName` | `PptBankcodeHist_Financialinstitutionname` |  |  |  |
| 8 | `PPBCDH.ZIPCode` | `PptBankcodeHist_Zipcode` |  |  |  |
| 9 | `PPBCDH.CityName` | `PptBankcodeHist_Cityname` |  |  |  |
| 10 | `PPBCDH.CheckDigitMethod` | `PptBankcodeHist_Checkdigitmethod` |  |  |  |
| 11 | `PPBCDH.OverrideThroughUpload` | `PptBankcodeHist_Overridethroughupload` |  |  |  |
| 12 | `PPBCDH.SourceKey` | `PptBankcodeHist_Sourcekey` |  |  |  |
| 13 | `PPBCDH.OriginatingSource` | `PptBankcodeHist_Originatingsource` |  |  |  |
| 14 | `PPBCDH.IBANBIC` | `PptBankcodeHist_Ibanbic` |  |  |  |
| 15 | `PPBCDH.IBANCountryCode` | `PptBankcodeHist_Ibancountrycode` |  |  |  |
| 16 | `PPBCDH.IBANNationalID` | `PptBankcodeHist_Ibannationalid` |  |  |  |
| 17 | `PPBCDH.EndDateBankCode` | `PptBankcodeHist_Enddatebankcode` |  |  |  |
| 18 | `PPBCDH.RACBankCode` | `PptBankcodeHist_Racbankcode` |  |  |  |
| 19 | `PPBCDH.RSCBankCode` | `PptBankcodeHist_Rscbankcode` |  |  |  |
| 20 | `PPBCDH.EntryUserID` | `PptBankcodeHist_Entryuserid` |  |  |  |
| 21 | `PPBCDH.EntryDateTime` | `PptBankcodeHist_Entrydatetime` |  |  |  |
| 22 | `PPBCDH.ApproverUserID` | `PptBankcodeHist_Approveruserid` |  |  |  |
| 23 | `PPBCDH.ApprovedDateTime` | `PptBankcodeHist_Approveddatetime` |  |  |  |
| 24 | `PPBCDH.OfficeType` | `PptBankcodeHist_Officetype` |  |  |  |
| 25 | `PPBCDH.GroupType` | `PptBankcodeHist_Grouptype` |  |  |  |
