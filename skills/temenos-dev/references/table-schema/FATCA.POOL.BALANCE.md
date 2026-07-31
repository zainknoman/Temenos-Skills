# FATCA.POOL.BALANCE — Table Schema

> Source: `INSERTS/I_F.FATCA.POOL.BALANCE` in `FE_FatcaReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FE.FPB.STATUS.TYPE` | `FatcaPoolBalance_StatusType` | TField |  | Extracted and defaulted from the Record ID of this application. |
| 2 | `FE.FPB.YEAR` | `FatcaPoolBalance_Year` | TField |  | The year to which the aggregated balance pertains to. |
| 3 | `FE.FPB.NO.COUNT` | `FatcaPoolBalance_NoCount` | TField |  | This field denotes the number of accounts under the above status type. The Count will be by number of clients. |
| 4 | `FE.FPB.ACC.BALANCE` | `FatcaPoolBalance_AccBalance` | TField |  | The balance is aggregated from FATCA.TAX.BASE and is represented in USD currency. |
| 5 | `FE.FPB.GIIN` | `FatcaPoolBalance_Giin` | TField |  | The GIIN of the non-participating financial institution updated from FATCA TAX BASE. |
| 6 | `FE.FPB.TRANS.COUNTRY` | `FatcaPoolBalance_TransCountry` | TField |  | The field will be Update from FATCA.TAX.BASE record. This will be mapped from the LOCAL COUNTRY field of the COMPANY to which the ACCOUNT belongs to. |
| 7 | `FE.FPB.REC.COUNTRY` | `FatcaPoolBalance_RecCountry` | TField |  | This fields will be Update from FATCA.TAX.BASE record. If the STATUS in FATCA PARAMETER is IGA1, then the receiving country will be the same as the TransmittingCountryelse it will be �US�. |
| 8 | `FE.FPB.MSG.REF.ID` | `FatcaPoolBalance_MsgRefId` | TField |  | The field will be updated as FATCA.POOL.BALANCE.ID.SEQ.NO (seq.no will be 1 for the new record). It will appended with FATCA.POOL.BALANCE.ID.SEQ.NO.FI value seperated by '*'. This information is mapped to ReportingFI section in a pool report. |
| 9 | `FE.FPB.CRCTD.MSG.REF.ID` | `FatcaPoolBalance_CrctdMsgRefId` | TField |  | The field is used for updating the amended message reference. |
| 10 | `FE.FPB.STATUS.DATE` | `FatcaPoolBalance_StatusDate` | TField |  | This fields will be Update from FATCA.TAX.BASE record. Date on which the base file is updated |
| 11 | `FE.FPB.TIMESTAMP` | `FatcaPoolBalance_Timestamp` | TField |  | Time of the request for generating xml will be updated. |
| 12 | `FE.FPB.COM.NAME` | `FatcaPoolBalance_ComName` | TField |  | The field will be updated from the field COMPANY.NAME in COMPANY record. |
| 13 | `FE.FPB.COM.ADDRESS` | `FatcaPoolBalance_ComAddress` |  |  |  |
| 14 | `FE.FPB.COM.TIN` | `FatcaPoolBalance_ComTin` | TField |  | The field will be updated from the field EIN in FATCA.PARAMETER record. |
| 15 | `FE.FPB.REPORT.TYPE` | `FatcaPoolBalance_ReportType` | TField |  | On Authorising the FATCA.XML.REQUEST the field will be updated as FATCA1 = New FATCA2 = Corrected FATCA3 = Void FATCA4 = Amended |
| 16 | `FE.FPB.POOL.REPORT.TYPE` | `FatcaPoolBalance_PoolReportType` | TField |  | Based on the FATCA.TAX.BASE STATUS.TYPE AND INDICAT STATUS FIELD Below will be updated . FATCA201 = Recalcitrant account holders with US Indicia FATCA202 = Recalcitrant account holders without US Indicia FATCA203 = Dormant Accounts FATCA204 = Non-participating foreign financial institutions |
| 17 | `FE.FPB.FI.RETURN.REF` | `FatcaPoolBalance_FiReturnRef` | TField |  | The field used to define the reference ID. ID format will be like FATCAID/Reporting period/jurisdiction. |
| 18 | `FE.FPB.FI.RETURN.ACTION` | `FatcaPoolBalance_FiReturnAction` | TField |  | The field used to define the valid value of New, Replacement and variation. |
| 19 | `FE.FPB.DUE.DILIGENCE.IND` | `FatcaPoolBalance_DueDiligenceInd` | TField |  | The field used to define whether an account is a Reportable Account or an account held by a Non-participatingFinancial Institution. |
| 20 | `FE.FPB.THRESHOLD.IND` | `FatcaPoolBalance_ThresholdInd` | TField |  | The field used to define the thresholds in the due diligence process. |
| 21 | `FE.FPB.FI.REGISTER.ID` | `FatcaPoolBalance_FiRegisterId` | TField |  | The field used to define the first three digits of the FI's (Financial Institution) name. |
| 22 | `FE.FPB.FATCA.USER.ID` | `FatcaPoolBalance_FatcaUserId` | TField |  | The field used to define the FATCA.ID which is populated from FATCA.REPORTING.PARAMETER |
| 23 | `FE.FPB.FILER.CATEGORY` | `FatcaPoolBalance_FilerCategory` | TField |  | The field will be updated from the field FILER.CATEGORY in FATCA.REPORTING.PARAMETER record. The field contains the category of reporting financial institution to be reported in FATCA XML report. |
| 24 | `FE.FPB.DOC.REF.ID` | `FatcaPoolBalance_DocRefId` | TField |  | The field specified the pool report reference. It is updated as FATCA.POOL.BALANCE.ID.SEQ.NO.PR (seq.no will be 1 for the new record). The corrected document reference status is also stored here seperated by '*' |
