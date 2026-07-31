# TNACIN.CHEQUE.ELIGIBILITY — Table Schema

> Source: `INSERTS/I_F.TNACIN.CHEQUE.ELIGIBILITY` in `TNACIN_ChequeEligibility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHEQ.ELG.LEGAL.ID` | `TnacinChequeEligibility_LegalId` | TField |  | This field is to store the Legal ID number of the customer. |
| 2 | `CHEQ.ELG.DATE.OF.BIRTH` | `TnacinChequeEligibility_DateOfBirth` | TField |  | This field is to store the Date of Birth of the customer. Should be in format of DD/MM/YYYY. |
| 3 | `CHEQ.ELG.NO.OF.CHQ.AMNESTIES` | `TnacinChequeEligibility_NoOfChqAmnesties` | TField |  | This field stores the number of amnesty by the customer for cheque related transactions. |
| 4 | `CHEQ.ELG.NO.OF.CHQ.INCIDENTS` | `TnacinChequeEligibility_NoOfChqIncidents` | TField |  | This field denotes the number of times the cheque incidents by the customer. |
| 5 | `CHEQ.ELG.NO.OF.CHQ.REGULARISED` | `TnacinChequeEligibility_NoOfChqRegularised` | TField |  | This field denotes the number of times the regularized the issued cheque. |
| 6 | `CHEQ.ELG.CUSTOMER.NAME` | `TnacinChequeEligibility_CustomerName` | TField |  | This field stores the name of the customer for whom the eligibility is checked. |
| 7 | `CHEQ.ELG.DATE.INCIDENT` | `TnacinChequeEligibility_DateIncident` | TField |  | This field stores the date on when the cheque incident happened. |
| 8 | `CHEQ.ELG.FIRST.NAME` | `TnacinChequeEligibility_FirstName` | TField |  | This field stores the first name of the customer for whom the eligibility is checked. |
| 9 | `CHEQ.ELG.ERROR.CODE` | `TnacinChequeEligibility_ErrorCode` | TField |  | This field is to store the Error code received. |
| 10 | `CHEQ.ELG.ERROR.DESC` | `TnacinChequeEligibility_ErrorDesc` | TField |  | This field is to store the description of the Error received. |
| 11 | `CHEQ.ELG.REQUEST.USER` | `TnacinChequeEligibility_RequestUser` | TField |  | This field stores the user detail who has requested for the cheque book eligibility. |
| 12 | `CHEQ.ELG.REQUEST.DATE` | `TnacinChequeEligibility_RequestDate` | TField |  | This field stores the date on when the cheque book request is raised by the user. |
