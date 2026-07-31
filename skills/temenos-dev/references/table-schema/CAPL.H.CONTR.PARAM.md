# CAPL.H.CONTR.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CONTR.PARAM` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CON.PARAM.RECEIPT.NUMBER` | `CaplHContrParam_ReceiptNumber` | TField |  | Receipt number |
| 2 | `CAPL.CON.PARAM.FILER.NUMBER` | `CaplHContrParam_FilerNumber` | TField |  | Filer number assigned by CRA |
| 3 | `CAPL.CON.PARAM.ISSUER.NAME.1` | `CaplHContrParam_IssuerName1` | TField |  | Field is used to store the name of issuer.Ideally Company name. |
| 4 | `CAPL.CON.PARAM.ISSUER.NAME.2` | `CaplHContrParam_IssuerName2` | TField |  | Field is used to store the name of issuer.Ideally Company name. |
| 5 | `CAPL.CON.PARAM.ISSUER.NAME.3` | `CaplHContrParam_IssuerName3` | TField |  | Field is used to store the name of issuer.Ideally Company name. |
| 6 | `CAPL.CON.PARAM.ISSUER.ADR.1` | `CaplHContrParam_IssuerAdr1` | TField |  | Field is used to store the address of the issuer.Ideally Company address |
| 7 | `CAPL.CON.PARAM.ISSUER.ADR.2` | `CaplHContrParam_IssuerAdr2` | TField |  | Field is used to store the address of the issuer.Ideally Company address |
| 8 | `CAPL.CON.PARAM.ISSUER.CITY` | `CaplHContrParam_IssuerCity` | TField |  | Field is used to store the address of the issuer to store the city details. |
| 9 | `CAPL.CON.PARAM.ISSUER.PROVINCE` | `CaplHContrParam_IssuerProvince` | TField |  | Field is used to store the address of the issuer to store province details. |
| 10 | `CAPL.CON.PARAM.ISSUER.COUNTRY` | `CaplHContrParam_IssuerCountry` | TField |  | Field is used to store the address of the issuer to store country details.Issuer Country by CRA |
| 11 | `CAPL.CON.PARAM.ISSUER.POSTAL` | `CaplHContrParam_IssuerPostal` | TField |  | Field is used to store the address of the issuer to store postal details.Issuer Country by CRA |
| 12 | `CAPL.CON.PARAM.CONTACT.NAME` | `CaplHContrParam_ContactName` | TField |  | Field is used to store the contact details for CRA |
| 13 | `CAPL.CON.PARAM.CONTACT.TEL.AREA` | `CaplHContrParam_ContactTelArea` | TField |  | Field is used to store the Telephone area code details for CRA |
| 14 | `CAPL.CON.PARAM.CONTACT.PHONE` | `CaplHContrParam_ContactPhone` | TField |  | Field is used to store the contact details (phone number) for CRAShould be in the format NNN-NNNN. |
| 15 | `CAPL.CON.PARAM.CONTACT.EXT` | `CaplHContrParam_ContactExt` | TField |  | Field is used to store the Contact Telephone Extension number |
| 16 | `CAPL.CON.PARAM.RESTRICT.PRINT.FROM` | `CaplHContrParam_RestrictPrintFrom` | TField |  | Field is used to store the date from which the contra prints to be processed.Valid date format field. |
| 17 | `CAPL.CON.PARAM.RESTRICT.PRINT.TO` | `CaplHContrParam_RestrictPrintTo` | TField |  | Field is used to store the date till which the contra prints to be processed.Valid date format field. |
| 18 | `CAPL.CON.PARAM.RECEIPT.DAYS` | `CaplHContrParam_ReceiptDays` | TField |  | Field used to store the number of days that the contribution done within can allocate to previous year. |
| 19 | `CAPL.CON.PARAM.DEAL.SLIP.ID` | `CaplHContrParam_DealSlipId` | TField |  | field is used to store the format to be considered for deal slip process.Validation - Link to DEAL.SLIP.FORMAT. |
| 20 | `CAPL.CON.PARAM.HANDOFF.ID` | `CaplHContrParam_HandoffId` | TField |  | field is used to store the handoff message to be considered for deal slip process.Link to DE.MAPPING. |
| 21 | `CAPL.CON.PARAM.XML.SCHEMA` | `CaplHContrParam_XmlSchema` | TField |  | Field is used to store the interface id used to XML extract.Link to GIT.INTERFACE.OUT |
| 22 | `CAPL.CON.PARAM.BUISNESS.NO` | `CaplHContrParam_BuisnessNo` | TField |  |  |
| 23 | `CAPL.CON.PARAM.SPLIT.RSP.XML` | `CaplHContrParam_SplitRspXml` | TField |  | The Purpose of this field is define how the RRSP contribution XML to be generated for "Managed" and "Self-Directed" Plans.Allowed Inputs are Yes, No, None'YES' - XML Files will be produced separately for "RRSP" and "SDRPS" based on the unique specimen number available in SAM. If specimen number is not available in SAM, XML files will be produced based on the Specimen number configured in CAPL.PLAN.TYPE for the corresponding plan typeFile naming convention will be *Specimen.No*-*O or A or C*.xml based on the Action selected while processing contribution'No'/'None' - For both "RRSP" and "SDRSP" only one XML file will be generated based on the file name configured in the parameter table 'CAPL.H.TX.XML.PARMS' irrespective of different specimen numberFile naming convention will be *Out File* configured in CAPL.H.TX.XML.PARMS for RRSP slips |
| 24 | `CAPL.CON.PARAM.SPECIMEN.NO` | `CaplHContrParam_SpecimenNo` | TField |  | This field is used to configure the specimen number of the plan types.Alphanumeric and 35 in lengthThe specimen number configured here will be mapped in the specimen number tag(*rrsp_spcmn_nbr*) while generating contribution receipts. This field value will be mapped to the Summary section in T4RSP xml. |
| 25 | `CAPL.CON.PARAM.RESERVED.7` | `CaplHContrParam_Reserved7` |  |  |  |
| 26 | `CAPL.CON.PARAM.RESERVED.6` | `CaplHContrParam_Reserved6` |  |  |  |
| 27 | `CAPL.CON.PARAM.RESERVED.5` | `CaplHContrParam_Reserved5` |  |  |  |
| 28 | `CAPL.CON.PARAM.RESERVED.4` | `CaplHContrParam_Reserved4` |  |  |  |
| 29 | `CAPL.CON.PARAM.RESERVED.3` | `CaplHContrParam_Reserved3` |  |  |  |
| 30 | `CAPL.CON.PARAM.RESERVED.2` | `CaplHContrParam_Reserved2` |  |  |  |
| 31 | `CAPL.CON.PARAM.RESERVED.1` | `CaplHContrParam_Reserved1` |  |  |  |
| 32 | `CAPL.CON.PARAM.RECORD.STATUS` | `CaplHContrParam_RecordStatus` | String |  |  |
| 33 | `CAPL.CON.PARAM.CURR.NO` | `CaplHContrParam_CurrNo` | String |  |  |
| 34 | `CAPL.CON.PARAM.INPUTTER` | `CaplHContrParam_Inputter` |  |  |  |
| 35 | `CAPL.CON.PARAM.DATE.TIME` | `CaplHContrParam_DateTime` |  |  |  |
| 36 | `CAPL.CON.PARAM.AUTHORISER` | `CaplHContrParam_Authoriser` | String |  |  |
| 37 | `CAPL.CON.PARAM.CO.CODE` | `CaplHContrParam_CoCode` | String |  |  |
| 38 | `CAPL.CON.PARAM.DEPT.CODE` | `CaplHContrParam_DeptCode` | String |  |  |
| 39 | `CAPL.CON.PARAM.AUDITOR.CODE` | `CaplHContrParam_AuditorCode` | String |  |  |
| 40 | `CAPL.CON.PARAM.AUDIT.DATE.TIME` | `CaplHContrParam_AuditDateTime` | String |  |  |
