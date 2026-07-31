# TNFCOP.FORM.APPLICATION — Table Schema

> Source: `INSERTS/I_F.TNFCOP.FORM.APPLICATION` in `TNFCOP_F1F2AuthorizationSheet.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.TYPE` | `TnfcopFormApplication_Type` | TField |  | This field is to store the type of the form which is created to submit the Central Bank for authorisation. Allowed values are 71 (F1) and 72 (F2) |
| 2 | `TNFCOP.DATE.SUBMISSION` | `TnfcopFormApplication_DateSubmission` | TField |  | Date on which the form is created to submit to the Central Bank |
| 3 | `TNFCOP.REQUEST.REASON` | `TnfcopFormApplication_RequestReason` | TField |  | This field stores the detail of the reason for which the F1/F2 request is raised |
| 4 | `TNFCOP.DEST.COUNTRY.CODE` | `TnfcopFormApplication_DestCountryCode` | TField |  | This field stores the destination country code, where the funds are goods are transferred |
| 5 | `TNFCOP.CCY.CODE` | `TnfcopFormApplication_CcyCode` | TField |  | This field stores the Currency code in which the Form is created |
| 6 | `TNFCOP.REQUEST.AMOUNT` | `TnfcopFormApplication_RequestAmount` | TField |  | This field stores the amount which is being requested to the Central Bank for the approval |
| 7 | `TNFCOP.CUST.ACCOUNT` | `TnfcopFormApplication_CustAccount` | TField |  | This field is to store the account number of the customer for whom the application is raised. This should be a valid T24 account and should not be closed/inactive |
| 8 | `TNFCOP.APPLICANT.NAME` | `TnfcopFormApplication_ApplicantName` | TField |  | This field denotes the name of the applicant, who is submitting the document to process the transaction on behalf of another customer |
| 9 | `TNFCOP.BENEFICIARY.NAME` | `TnfcopFormApplication_BeneficiaryName` | TField |  | This field denotes the name of the beneficiary, who is the end beneficiary of the trade or Financial transaction |
| 10 | `TNFCOP.BP.CODE` | `TnfcopFormApplication_BpCode` | TField |  | This field is to store the code of the Balance Payment, which is used for the transaction |
| 11 | `TNFCOP.LINKED.REFERENCE` | `TnfcopFormApplication_LinkedReference` | TField |  | This field denotes the Reference which is linked to the application. Validation: only F2 application can be linked |
| 12 | `TNFCOP.FILE.STATUS` | `TnfcopFormApplication_FileStatus` | TField |  | This field denotes the status of the application:(1) CBT Authorization(2) CBT Authorization Partial(3) Return for further information by CBT(4) CBT Rejection(5) Cancelled(6) Sent to CBT for approval(7)Additional information requested by Regulatory control(8)Rejected by Regulatory Control(9)File sent to Regulatory control for review |
| 13 | `TNFCOP.DATE.SENT.CBT` | `TnfcopFormApplication_DateSentCbt` | TField |  | This field denotes the date related to sending to the CBT |
| 14 | `TNFCOP.CBT.RESPONSE.DATE` | `TnfcopFormApplication_CbtResponseDate` |  |  |  |
| 15 | `TNFCOP.CBT.RESP.REF` | `TnfcopFormApplication_CbtRespRef` |  |  |  |
| 16 | `TNFCOP.ADDITIONAL.INFO` | `TnfcopFormApplication_AdditionalInfo` |  |  |  |
| 17 | `TNFCOP.REJECT.REASON` | `TnfcopFormApplication_RejectReason` | TField |  | This field stores the details of the reason for which the application is being rejected |
| 18 | `TNFCOP.VALIDITY.DATE` | `TnfcopFormApplication_ValidityDate` | TField |  | This field denotes the maturity date of the authorised application |
| 19 | `TNFCOP.APPROVED.AMOUNT` | `TnfcopFormApplication_ApprovedAmount` | TField |  | This field denotes the amount which is approved by the Central Bank for the application. It may be the full amount applied or less than what is applied |
| 20 | `TNFCOP.APPROVED.CCY` | `TnfcopFormApplication_ApprovedCcy` | TField |  | This field stores the Currency in which the approval is being given by the Central bank |
| 21 | `TNFCOP.APPROVED.CCY.AMT` | `TnfcopFormApplication_ApprovedCcyAmt` | TField |  | This field stores the approved amount in the approved currency by the Central Bank |
| 22 | `TNFCOP.RESUBMISSION.DATE` | `TnfcopFormApplication_ResubmissionDate` |  |  |  |
| 23 | `TNFCOP.RESUBMISSION.INFO` | `TnfcopFormApplication_ResubmissionInfo` |  |  |  |
| 24 | `TNFCOP.TRANSACTION.REF` | `TnfcopFormApplication_TransactionRef` |  |  |  |
| 25 | `TNFCOP.RESERVATION.DATE` | `TnfcopFormApplication_ReservationDate` |  |  |  |
| 26 | `TNFCOP.RESERVATION.CCY` | `TnfcopFormApplication_ReservationCcy` |  |  |  |
| 27 | `TNFCOP.RESERVED.AMOUNT` | `TnfcopFormApplication_ReservedAmount` |  |  |  |
| 28 | `TNFCOP.RELEASE.RES.DATE` | `TnfcopFormApplication_ReleaseResDate` |  |  |  |
| 29 | `TNFCOP.RELEASE.AMOUNT` | `TnfcopFormApplication_ReleaseAmount` |  |  |  |
| 30 | `TNFCOP.RESERVE.REF` | `TnfcopFormApplication_ReserveRef` |  |  |  |
| 31 | `TNFCOP.SETT.TRANS.REF` | `TnfcopFormApplication_SettTransRef` |  |  |  |
| 32 | `TNFCOP.SETTLEMENT.CCY` | `TnfcopFormApplication_SettlementCcy` |  |  |  |
| 33 | `TNFCOP.SETTLEMENT.AMOUNT` | `TnfcopFormApplication_SettlementAmount` |  |  |  |
| 34 | `TNFCOP.SETTLEMENT.DATE` | `TnfcopFormApplication_SettlementDate` |  |  |  |
| 35 | `TNFCOP.CANCELLATION.DATE` | `TnfcopFormApplication_CancellationDate` | TField |  | This field denotes the date on when the application is cancelled |
| 36 | `TNFCOP.CBT.CANC.REF` | `TnfcopFormApplication_CbtCancRef` | TField |  | This field denotes the Reference number of the cencellation received from Central Bank |
| 37 | `TNFCOP.CANC.REASON` | `TnfcopFormApplication_CancReason` | TField |  | This field denotes the reason for which the application is cancelled by the Central Bank |
| 38 | `TNFCOP.CHARGE.ACCOUNT` | `TnfcopFormApplication_ChargeAccount` | TField |  | This field Should be to store the account which is to be charged, it should pick CUST.ACCT and should be editable |
| 39 | `TNFCOP.CHARGE.TYPE` | `TnfcopFormApplication_ChargeType` |  |  |  |
| 40 | `TNFCOP.CHARGE.AMT` | `TnfcopFormApplication_ChargeAmt` |  |  |  |
| 41 | `TNFCOP.TRF.ELIGIBLE` | `TnfcopFormApplication_TrfEligible` | TField |  | This field is to store Yes or NO values. A value of YES indicates that the indicated title code is eligible for transfer |
| 42 | `TNFCOP.REMARKS` | `TnfcopFormApplication_Remarks` | TField |  | This field is used to store the reasons/remarks for the operations carried out by Branch or Regulatory |
| 43 | `TNFCOP.RESERVED.3` | `TnfcopFormApplication_Reserved3` | TField |  | Reserved for future use |
| 44 | `TNFCOP.RESERVED.2` | `TnfcopFormApplication_Reserved2` | TField |  | Reserved for future use |
| 45 | `TNFCOP.RESERVED.1` | `TnfcopFormApplication_Reserved1` | TField |  | Reserved for future use |
| 46 | `TNFCOP.LOCAL.REF` | `TnfcopFormApplication_LocalRef` |  |  |  |
| 47 | `TNFCOP.OVERRIDE` | `TnfcopFormApplication_Override` |  |  |  |
| 48 | `TNFCOP.RECORD.STATUS` | `TnfcopFormApplication_RecordStatus` | String |  |  |
| 49 | `TNFCOP.CURR.NO` | `TnfcopFormApplication_CurrNo` | String |  |  |
| 50 | `TNFCOP.INPUTTER` | `TnfcopFormApplication_Inputter` |  |  |  |
| 51 | `TNFCOP.DATE.TIME` | `TnfcopFormApplication_DateTime` |  |  |  |
| 52 | `TNFCOP.AUTHORISER` | `TnfcopFormApplication_Authoriser` | String |  |  |
| 53 | `TNFCOP.CO.CODE` | `TnfcopFormApplication_CoCode` | String |  |  |
| 54 | `TNFCOP.DEPT.CODE` | `TnfcopFormApplication_DeptCode` | String |  |  |
| 55 | `TNFCOP.AUDITOR.CODE` | `TnfcopFormApplication_AuditorCode` | String |  |  |
| 56 | `TNFCOP.AUDIT.DATE.TIME` | `TnfcopFormApplication_AuditDateTime` | String |  |  |
| 57 | `TNFCOP.AUTO.RESERVE.IND` | `TnfcopFormApplication_AutoReserveInd` |  |  |  |
| 58 | `TNFCOP.AUTO.SETT.IND` | `TnfcopFormApplication_AutoSettInd` |  |  |  |
