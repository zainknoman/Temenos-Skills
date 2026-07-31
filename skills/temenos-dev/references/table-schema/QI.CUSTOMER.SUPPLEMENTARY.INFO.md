# QI.CUSTOMER.SUPPLEMENTARY.INFO — Table Schema

> Source: `INSERTS/I_F.QI.CUSTOMER.SUPPLEMENTARY.INFO` in `QI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QI.SI.CUSTOMER.TYPE` | `QiCustomerSupplementaryInfo_CustomerType` | TField |  | This is a system populated field and corresponds to the customer in the record ID, based on the rules configuredin the RT.REGULATORY.RULES application. Validation Rules: Allowed values are ENTITY,INDIVIDUAL |
| 2 | `QI.SI.TAX.RESIDENCE` | `QiCustomerSupplementaryInfo_TaxResidence` | TField |  | This field indicates the Tax Residence of a customer. The system auto-populates this field as per the rules ordata elements configured in RT.REGULATORY.RULES.If data elements such as the Domicile field in the CUSTOMER table are configured in RT.REGULATORY.RULES, the value inthe Domicile field is considered while populating a value in this field Validation Rules: Valid record in COUNTRY table |
| 3 | `QI.SI.LEGAL.RESIDENCE` | `QiCustomerSupplementaryInfo_LegalResidence` | TField |  | This field indicates the residence of a customer. It is updated by the system as per the rules or data elementsconfigured in RT.REGULATORY.RULES.If data elements such as the Residence field in the CUSTOMER table is configured in RT.REGULATORY.RULES, the value inthe Residence field is considered while populating a value in this field Validation Rules: Valid record in COUNTRY table |
| 4 | `QI.SI.CUS.APPLN.COUNTRY` | `QiCustomerSupplementaryInfo_CusApplnCountry` | TField |  | This field is referred in tax processing to apply tax rate. This logic is part of RT.REGULATORY.RULES and isamendable.If the Tax Residence is US, this field is updated with the value in Tax Residence field. If not, the value in theLegal Residence field is updated. Validation Rules: Valid record in COUNTRY table |
| 5 | `QI.SI.CUS.ADDRESS.CONFLICT.IND` | `QiCustomerSupplementaryInfo_CusAddressConflictInd` | TField |  | Address conflict indicator is one of the data elements considered in calculating a customer's QI status forNon-US individual customers. Rules and data elements to be considered in determining the Address conflict indicatorare user definable and configured in rules application RT.REGULATORY.RULES. The record id in RT.REGULATORY.RULESfor Address conflict(QI.ADDRESS.CONFLICT.INDICATOR) is then parameterized in QI.PARAMETER in order for the systemto perform the address conflict evaluation. The Address conflict evaluation by the system makes a comparison between : - Customer's Tax Residence against the Legal Residence residence - Legal ID document's issuing country against the customer's Tax Residence - country code in mailing address against Tax residence. This is a system populated field. Where the system evaluates and detects any address conflict, the value for thisfield is updated as Y. The bank will require to follow up with its customer for the submission of WDTT document bythe customer in order to resolve the address conflict. Further,on receipt of the document from the customer andencoding this information into the Document Management table within Transact i.e CUST.DOCUMENT, system willautomatically re-evaluate and populate N as a value into this field. |
| 6 | `QI.SI.CUS.QI.STATUS` | `QiCustomerSupplementaryInfo_CusQiStatus` | TField |  | This is a system populated value that automatically uses a logic that considers the rules and data elements configured in RT.REGULATORY.RULES for customer identification from QI perspective.The system logic also considers the address conflict indicator i.e rules and data elements defined in RT.REGULATORY.RULES (QI.ADDRESS.CONFLICT.INDICATOR) application in determining the status. The value in this field must be one of the record ids configured in the QI.STATUS.TYPE table. The value in this field must be one of the record ids configured in the QI.STATUS.TYPE table. |
| 7 | `QI.SI.CUS.QI.STATUS.LAST.UPD` | `QiCustomerSupplementaryInfo_CusQiStatusLastUpd` | TField |  | Date on when the Customer QI Status is updated. |
| 8 | `QI.SI.CUS.PREV.QI.STATUS` | `QiCustomerSupplementaryInfo_CusPrevQiStatus` |  |  |  |
| 9 | `QI.SI.CUS.PREV.QI.STATUS.LAST.UPD` | `QiCustomerSupplementaryInfo_CusPrevQiStatusLastUpd` |  |  |  |
| 10 | `QI.SI.RESERVED.25` | `QiCustomerSupplementaryInfo_Reserved25` |  |  |  |
| 11 | `QI.SI.RESERVED.24` | `QiCustomerSupplementaryInfo_Reserved24` |  |  |  |
| 12 | `QI.SI.RESERVED.23` | `QiCustomerSupplementaryInfo_Reserved23` |  |  |  |
| 13 | `QI.SI.RESERVED.22` | `QiCustomerSupplementaryInfo_Reserved22` |  |  |  |
| 14 | `QI.SI.RESERVED.21` | `QiCustomerSupplementaryInfo_Reserved21` |  |  |  |
| 15 | `QI.SI.CUS.DOC.RECD` | `QiCustomerSupplementaryInfo_CusDocRecd` | TField |  | This field is updated by the system based on the allowed set of document types configured in RT.REGULATORY.RULESapplication. The document's status is verified against the customer's CUST.DOCUMENT record while updating the valuein this field. Validation Rules: Valid record in DOCUMENT.TYPE table |
| 16 | `QI.SI.CUS.LIMITATION.ON.BENEFITS` | `QiCustomerSupplementaryInfo_CusLimitationOnBenefits` | TField |  | User can select any value from the dropdown list which was configured in EB.LOOKUP(CUS.LOB) table.This field denotes a customer is requested to apply a conventional tax rate by submitting a signed document. Validation Rules: if the field LMTN.BEN.APPLICABLE is Y in QI.STATUS.TYPE field for a CUS.QI.STATUS which is defaulted by systemand CUS.LIMITATION.ON.BENEFITS is not inputted and also Customer document is received,then system will generate Override |
| 17 | `QI.SI.RESERVED.20` | `QiCustomerSupplementaryInfo_Reserved20` | TField |  | Reserved for future use |
| 18 | `QI.SI.RESERVED.19` | `QiCustomerSupplementaryInfo_Reserved19` | TField |  | Reserved for future use |
| 19 | `QI.SI.RESERVED.18` | `QiCustomerSupplementaryInfo_Reserved18` | TField |  | Reserved for future use |
| 20 | `QI.SI.RESERVED.17` | `QiCustomerSupplementaryInfo_Reserved17` | TField |  | Reserved for future use |
| 21 | `QI.SI.RESERVED.16` | `QiCustomerSupplementaryInfo_Reserved16` | TField |  | Reserved for future use |
| 22 | `QI.SI.PORT.QI.STATUS` | `QiCustomerSupplementaryInfo_PortQiStatus` | TField |  | The user can enter a value in this field only if the customer is another QI or NQI.The allowed values are those configured in QI.STATUS.TYPE with the QI NQI Institution field set as Yes. If not, avalidation is raised.The system automatically defaults a status from the QI.STATUS.TYPE table when the selected QI status such as QIA, QIB,QIC, QID and NQI changes to invalid because the document supporting the status has expired. Validation Rules: Field allow to input only if a valid document is available for the respective PORT.QI.STATUS which is also defaulted inPORT.QI.DOC.RECD field. |
| 23 | `QI.SI.PORT.QI.DOC.RECD` | `QiCustomerSupplementaryInfo_PortQiDocRecd` | TField |  | This field is automatically defaulted from the QI.STATUS.TYPE record corresponding to the QI Status given in the PortQi Status field and checks for the existence and validity of the same.If the document is not received from the QI or NQI customer or is invalid, a validation is raised and user input isnot accepted. Validation Rules: - No input field. - valid record in DOCUMENT.TYPE table - On defaulting the value into this field,the system further validates the document status in CUST.DOCUMENT |
| 24 | `QI.SI.PORT.ID` | `QiCustomerSupplementaryInfo_PortId` |  |  |  |
| 25 | `QI.SI.PORT.STATUS` | `QiCustomerSupplementaryInfo_PortStatus` |  |  |  |
| 26 | `QI.SI.PORT.TAX.RATE.KEY` | `QiCustomerSupplementaryInfo_PortTaxRateKey` |  |  |  |
| 27 | `QI.SI.PORT.TAX.DOC.RECD` | `QiCustomerSupplementaryInfo_PortTaxDocRecd` |  |  |  |
| 28 | `QI.SI.PORT.COMPANY` | `QiCustomerSupplementaryInfo_PortCompany` |  |  |  |
| 29 | `QI.SI.RESERVED.14` | `QiCustomerSupplementaryInfo_Reserved14` |  |  |  |
| 30 | `QI.SI.RESERVED.13` | `QiCustomerSupplementaryInfo_Reserved13` |  |  |  |
| 31 | `QI.SI.RESERVED.12` | `QiCustomerSupplementaryInfo_Reserved12` |  |  |  |
| 32 | `QI.SI.RESERVED.11` | `QiCustomerSupplementaryInfo_Reserved11` |  |  |  |
| 33 | `QI.SI.QI.EMP.ID.NUM` | `QiCustomerSupplementaryInfo_QiEmpIdNum` | TField |  | Field denotes whether EIN is applicable for a given PORT.QI.STATUS or not. This can be defined in QI.STATUS.TYPE.For example, if the field EIN.REQUIRED is Y in QI.STATUS.TYPE field for a PORT.QI.STATUS which is inputted by userand QI.EMP.ID.NUM is not inputted,then system will generate Override |
| 34 | `QI.SI.HIST.DATE` | `QiCustomerSupplementaryInfo_HistDate` |  |  |  |
| 35 | `QI.SI.REMARKS` | `QiCustomerSupplementaryInfo_Remarks` | TField |  |  |
| 36 | `QI.SI.RESERVED.8` | `QiCustomerSupplementaryInfo_Reserved8` | TField |  | Reserved for future use |
| 37 | `QI.SI.RESERVED.7` | `QiCustomerSupplementaryInfo_Reserved7` | TField |  | Reserved for future use |
| 38 | `QI.SI.RESERVED.6` | `QiCustomerSupplementaryInfo_Reserved6` | TField |  | Reserved for future use |
| 39 | `QI.SI.RESERVED.5` | `QiCustomerSupplementaryInfo_Reserved5` | TField |  | Reserved for future use |
| 40 | `QI.SI.RESERVED.4` | `QiCustomerSupplementaryInfo_Reserved4` | TField |  | Reserved for future use |
| 41 | `QI.SI.RESERVED.3` | `QiCustomerSupplementaryInfo_Reserved3` | TField |  | Reserved for future use |
| 42 | `QI.SI.RESERVED.2` | `QiCustomerSupplementaryInfo_Reserved2` | TField |  | Reserved for future use |
| 43 | `QI.SI.RESERVED.1` | `QiCustomerSupplementaryInfo_Reserved1` | TField |  | Reserved for future use |
| 44 | `QI.SI.LOCAL.REF` | `QiCustomerSupplementaryInfo_LocalRef` |  |  |  |
| 45 | `QI.SI.OVERRIDE` | `QiCustomerSupplementaryInfo_Override` |  |  |  |
| 46 | `QI.SI.RECORD.STATUS` | `QiCustomerSupplementaryInfo_RecordStatus` | String |  | Status of the record |
| 47 | `QI.SI.CURR.NO` | `QiCustomerSupplementaryInfo_CurrNo` | String |  | Curr No |
| 48 | `QI.SI.INPUTTER` | `QiCustomerSupplementaryInfo_Inputter` |  |  |  |
| 49 | `QI.SI.DATE.TIME` | `QiCustomerSupplementaryInfo_DateTime` |  |  |  |
| 50 | `QI.SI.AUTHORISER` | `QiCustomerSupplementaryInfo_Authoriser` | String |  | Authoriser |
| 51 | `QI.SI.CO.CODE` | `QiCustomerSupplementaryInfo_CoCode` | String |  | Company code |
| 52 | `QI.SI.DEPT.CODE` | `QiCustomerSupplementaryInfo_DeptCode` | String |  | Department code |
| 53 | `QI.SI.AUDITOR.CODE` | `QiCustomerSupplementaryInfo_AuditorCode` | String |  | Auditor Code |
| 54 | `QI.SI.AUDIT.DATE.TIME` | `QiCustomerSupplementaryInfo_AuditDateTime` | String |  | Audit Date and time |
