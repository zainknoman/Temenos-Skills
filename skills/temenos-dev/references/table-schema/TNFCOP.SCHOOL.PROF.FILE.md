# TNFCOP.SCHOOL.PROF.FILE — Table Schema

> Source: `INSERTS/I_F.TNFCOP.SCHOOL.PROF.FILE` in `TNFCOP_SchoolingProfessionalTraining.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.SPT.FILE.TYPE` | `TnfcopSchoolProfFile_FileType` | TField |  | This field stores the type of the file for which it is being created |
| 2 | `TNFCOP.SPT.CUSTOMER.ACCOUNT` | `TnfcopSchoolProfFile_CustomerAccount` | TField |  | This field stores the account number of the customer for which the file is created |
| 3 | `TNFCOP.SPT.DATE.SUBMISSION` | `TnfcopSchoolProfFile_DateSubmission` | TField |  | This field stores the date on when the file is submitted to the bank |
| 4 | `TNFCOP.SPT.BENEFICIARY.ID` | `TnfcopSchoolProfFile_BeneficiaryId` | TField |  | This field stores the Customer ID of the Beneficiary of the subject file |
| 5 | `TNFCOP.SPT.DEST.COUNTRY` | `TnfcopSchoolProfFile_DestCountry` | TField |  | This field stores the destination country where the money is being transferred to |
| 6 | `TNFCOP.SPT.PURPOSE.TYPE` | `TnfcopSchoolProfFile_PurposeType` | TField |  | This field stores the details of the purpose of applying for the file |
| 7 | `TNFCOP.SPT.FINAL.REGISTRATION` | `TnfcopSchoolProfFile_FinalRegistration` | TField |  | This field shows the registration status of the file whether it is pre-registration or final registration |
| 8 | `TNFCOP.SPT.BENEFICIARY.TYPE` | `TnfcopSchoolProfFile_BeneficiaryType` | TField |  | This field stores the type of the Beneficiary. Possible values are:(1) B (External Funding holder)(2) NB (Self Funding)(3) A (Approved by CBT) |
| 9 | `TNFCOP.SPT.EXT.FUNDING.CCY` | `TnfcopSchoolProfFile_ExtFundingCcy` | TField |  | This field stores the currency in which the external funding for the monthly expenses is provided to the beneficiary |
| 10 | `TNFCOP.SPT.EXT.FUNDING.MON.EXP` | `TnfcopSchoolProfFile_ExtFundingMonExp` | TField |  | This field stores the external funding for the monthly expenses provided to the beneficiary |
| 11 | `TNFCOP.SPT.STUDY.YEAR` | `TnfcopSchoolProfFile_StudyYear` |  |  |  |
| 12 | `TNFCOP.SPT.START.MONTH` | `TnfcopSchoolProfFile_StartMonth` |  |  |  |
| 13 | `TNFCOP.SPT.END.MONTH` | `TnfcopSchoolProfFile_EndMonth` |  |  |  |
| 14 | `TNFCOP.SPT.ALLOW.CARRYOVER` | `TnfcopSchoolProfFile_AllowCarryover` |  |  |  |
| 15 | `TNFCOP.SPT.TERM.AMT.CCY` | `TnfcopSchoolProfFile_TermAmtCcy` | TField |  | This field stores the Currency in which the term amount has to be transferred |
| 16 | `TNFCOP.SPT.FILE.TERM.AMT` | `TnfcopSchoolProfFile_FileTermAmt` | TField |  | This field stores the total term amount which has to be transferred |
| 17 | `TNFCOP.SPT.DOC.SUBMITTED` | `TnfcopSchoolProfFile_DocSubmitted` |  |  |  |
| 18 | `TNFCOP.SPT.FILE.STATUS` | `TnfcopSchoolProfFile_FileStatus` | TField |  | This field stores the status of the file |
| 19 | `TNFCOP.SPT.LINKED.REF` | `TnfcopSchoolProfFile_LinkedRef` | TField |  | This field stores the F2 reference which is linked to the file |
| 20 | `TNFCOP.SPT.CHARGE.ACCT` | `TnfcopSchoolProfFile_ChargeAcct` | TField |  | This field stores the account from which the charge has to be debited from the customer |
| 21 | `TNFCOP.SPT.CHARGE.TYPE` | `TnfcopSchoolProfFile_ChargeType` |  |  |  |
| 22 | `TNFCOP.SPT.CHARGE.AMT` | `TnfcopSchoolProfFile_ChargeAmt` |  |  |  |
| 23 | `TNFCOP.SPT.TAX.AMT` | `TnfcopSchoolProfFile_TaxAmt` |  |  |  |
| 24 | `TNFCOP.SPT.CHARGE.DETAIL` | `TnfcopSchoolProfFile_ChargeDetail` |  |  |  |
| 25 | `TNFCOP.SPT.CLOSURE.DATE` | `TnfcopSchoolProfFile_ClosureDate` | TField |  | This field stores the date on when the file is closed |
| 26 | `TNFCOP.SPT.CLOSURE.REASON` | `TnfcopSchoolProfFile_ClosureReason` | TField |  | This field stores the reason due to which the file is closed |
| 27 | `TNFCOP.SPT.REGULATORY` | `TnfcopSchoolProfFile_Regulatory` | TField |  | This field must be marked as YES to all the versions attached under regulatory menu |
| 28 | `TNFCOP.SPT.REMARKS` | `TnfcopSchoolProfFile_Remarks` | TField |  | This field is used to store the reasons/remarks for the operations carried out by Branch or Regulatory |
| 29 | `TNFCOP.SPT.RESERVED.3` | `TnfcopSchoolProfFile_Reserved3` | TField |  | Reserved for future use |
| 30 | `TNFCOP.SPT.RESERVED.2` | `TnfcopSchoolProfFile_Reserved2` | TField |  | Reserved for future use |
| 31 | `TNFCOP.SPT.RESERVED.1` | `TnfcopSchoolProfFile_Reserved1` | TField |  | Reserved for future use |
| 32 | `TNFCOP.SPT.LOCAL.REF` | `TnfcopSchoolProfFile_LocalRef` |  |  |  |
| 33 | `TNFCOP.SPT.OVERRIDE` | `TnfcopSchoolProfFile_Override` |  |  |  |
| 34 | `TNFCOP.SPT.RECORD.STATUS` | `TnfcopSchoolProfFile_RecordStatus` | String |  |  |
| 35 | `TNFCOP.SPT.CURR.NO` | `TnfcopSchoolProfFile_CurrNo` | String |  |  |
| 36 | `TNFCOP.SPT.INPUTTER` | `TnfcopSchoolProfFile_Inputter` |  |  |  |
| 37 | `TNFCOP.SPT.DATE.TIME` | `TnfcopSchoolProfFile_DateTime` |  |  |  |
| 38 | `TNFCOP.SPT.AUTHORISER` | `TnfcopSchoolProfFile_Authoriser` | String |  |  |
| 39 | `TNFCOP.SPT.CO.CODE` | `TnfcopSchoolProfFile_CoCode` | String |  |  |
| 40 | `TNFCOP.SPT.DEPT.CODE` | `TnfcopSchoolProfFile_DeptCode` | String |  |  |
| 41 | `TNFCOP.SPT.AUDITOR.CODE` | `TnfcopSchoolProfFile_AuditorCode` | String |  |  |
| 42 | `TNFCOP.SPT.AUDIT.DATE.TIME` | `TnfcopSchoolProfFile_AuditDateTime` | String |  |  |
