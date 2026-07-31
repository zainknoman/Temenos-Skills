# CA.CLEARING.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.CA.CLEARING.DIRECTORY` in `CA_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.CDR.EXTERNAL.RECORD.KEY` | `CaClearingDirectory_ExternalRecordKey` |  |  |  |
| 2 | `CA.CDR.MODIFICATION.FLAG` | `CaClearingDirectory_ModificationFlag` | TField |  | This field is used to hold the type of change indicated by the external source in a Delta file. |
| 3 | `CA.CDR.PAYMENT.CHANNEL` | `CaClearingDirectory_PaymentChannel` | TField |  | This field is used to hold the clearing channel through which the beneficiary institution is reachable. |
| 4 | `CA.CDR.BIC` | `CaClearingDirectory_Bic` | TField |  | This field holds the BIC of the financial institution reachable through the payment channel. |
| 5 | `CA.CDR.NATIONAL.CLR.CODE` | `CaClearingDirectory_NationalClrCode` | TField |  | This field is used to store the National Clearing Code of the participant. |
| 6 | `CA.CDR.ISO.NCC` | `CaClearingDirectory_IsoNcc` | TField |  |  |
| 7 | `CA.CDR.INSTITUTION.NAME` | `CaClearingDirectory_InstitutionName` | TField |  | This field is used to store the name of the financial institution. |
| 8 | `CA.CDR.CITY` | `CaClearingDirectory_City` | TField |  | This field is used to store the name of the city where the financial institution is located. |
| 9 | `CA.CDR.COUNTRY` | `CaClearingDirectory_Country` | TField |  | This field is used to store the country code where the financial institution is located. |
| 10 | `CA.CDR.SCHEME` | `CaClearingDirectory_Scheme` | TField |  | This field is used to define the scheme for which the Bank is reachable. Eg: SCT* SDD B2B* SDD CORE BACS |
| 11 | `CA.CDR.ADHERANCE.BIC` | `CaClearingDirectory_AdheranceBic` | TField |  | This field is used to hold the BIC that (according to the financial institution that provided routing data to SWIFT) appears in the EPC Adherence Register, if available. For future purpose. |
| 12 | `CA.CDR.ADHERANCE.START.DATE` | `CaClearingDirectory_AdheranceStartDate` | TField |  | This field is used to hold the date from which, according to the EPC Adherence Register, the institution will be ready for operating the scheme. For future purpose. |
| 13 | `CA.CDR.ADHERANCE.STOP.DATE` | `CaClearingDirectory_AdheranceStopDate` | TField |  | This field is used to hold the date after which, according to the EPC Adherence Register, the institution will cease scheme operations. For future purpose. |
| 14 | `CA.CDR.PREFERRED.CHANNEL` | `CaClearingDirectory_PreferredChannel` | TField |  | This flag indicates if the payment channel is the preferred payment channel of the beneficiary institution for receiving payment. Possible values: P(if Preferred) or Blank |
| 15 | `CA.CDR.REACHABILITY.TYPE` | `CaClearingDirectory_ReachabilityType` | TField |  | This field indicates the beneficiary institution's direct or indirect reachability through the payment channel. Possible values: D or I or B If "I" (Indirect), then the field "INTERMEDIARY INSTITUTION BIC" identifies the institution that will route the payment If 'B'(Both direct and Indirect), then the field "INTERMEDIARY INSTITUTION BIC" identifies the institution that will route the payment If 'R'(Indirect and DEBIT only), then the field "INTERMEDIARY INSTITUTION BIC" identifies the institution that will route the payment |
| 16 | `CA.CDR.INTERMEDIARY.INST.BIC` | `CaClearingDirectory_IntermediaryInstBic` | TField |  | This field holds the BIC of the Intermediary Institution through which the bank is reachable in the payment channel. |
| 17 | `CA.CDR.INTERMEDIARY.NCC` | `CaClearingDirectory_IntermediaryNcc` | TField |  | This field holds the national clearing code of the intermediary participant. |
| 18 | `CA.CDR.INTER.ISO.NCC` | `CaClearingDirectory_InterIsoNcc` | TField |  | This field holds the ISO national clearing code of the intermediary participant. |
| 19 | `CA.CDR.SETTLEMENT.BIC` | `CaClearingDirectory_SettlementBic` | TField |  | This field holds the BIC which will be used for settlement. |
| 20 | `CA.CDR.STATUS` | `CaClearingDirectory_Status` | TField |  | This field holds the status of the BIC. Some Clearings will provide status for reachability.Others are just indicating the product for which the BIC is reachable |
| 21 | `CA.CDR.START.DATE` | `CaClearingDirectory_StartDate` | TField |  | This field holds the date from which the institution becomes reachable through this payment channel. |
| 22 | `CA.CDR.END.DATE` | `CaClearingDirectory_EndDate` | TField |  | This field holds the date after which the institution is no longer reachable through this payment channel. |
| 23 | `CA.CDR.ADMISSION.PROFILE` | `CaClearingDirectory_AdmissionProfile` | TField |  | This field is reserved for future purpose. |
| 24 | `CA.CDR.AOS` | `CaClearingDirectory_Aos` |  |  |  |
| 25 | `CA.CDR.FIELD_A` | `CaClearingDirectory_Field_a` |  |  |  |
| 26 | `CA.CDR.FIELD_B` | `CaClearingDirectory_Field_b` |  |  |  |
| 27 | `CA.CDR.PREFERRED` | `CaClearingDirectory_Preferred` | TField |  | This field is used to indicate that this entry should take precedence over the recently uploaded ones Possible Values: YES or NO |
| 28 | `CA.CDR.PURGE.ELIGIBILITY` | `CaClearingDirectory_PurgeEligibility` | TField |  | This field is used to store the name of the most recent uploaded file. Possible Values: YES or NO. |
| 29 | `CA.CDR.ALTERNATE.KEY` | `CaClearingDirectory_AlternateKey` |  |  |  |
| 30 | `CA.CDR.CLEARING.PARAMETER` | `CaClearingDirectory_ClearingParameter` | TField |  | This field holds the ID of the record in Clearing Parameter table through which the record has been uploaded/manually added. |
| 31 | `CA.CDR.UPLOAD.DATE` | `CaClearingDirectory_UploadDate` | TField |  | This field holds the date when the file which created this record has been uploaded. For records created manually this will be the date when the records has been created. |
| 32 | `CA.CDR.EFFECTIVE.DATE` | `CaClearingDirectory_EffectiveDate` | TField |  | This field is used to store the effective date of the file through which the records has been created. For records created manually this will be manually input. |
| 33 | `CA.CDR.UPLOAD.FILE.NAME` | `CaClearingDirectory_UploadFileName` | TField |  | This field is used to store the name of the file via which the record has been uploaded. For records created manually this will be blank. |
| 34 | `CA.CDR.LOCAL.REF` | `CaClearingDirectory_LocalRef` |  |  |  |
| 35 | `CA.CDR.CONTEXT.NAME` | `CaClearingDirectory_ContextName` |  |  |  |
| 36 | `CA.CDR.CONTEXT.VALUE` | `CaClearingDirectory_ContextValue` |  |  |  |
| 37 | `CA.CDR.CURRENCY` | `CaClearingDirectory_Currency` | TField | No | Optional Field Valid Currency Code |
| 38 | `CA.CDR.MAXIMUM.AMOUNT` | `CaClearingDirectory_MaximumAmount` | TField |  | Contains the maximum amount limit till which the party is reachable via the specific clearing. |
| 39 | `CA.CDR.RESERVED.6` | `CaClearingDirectory_Reserved6` | TField |  |  |
| 40 | `CA.CDR.RESERVED.5` | `CaClearingDirectory_Reserved5` | TField |  |  |
| 41 | `CA.CDR.RESERVED.4` | `CaClearingDirectory_Reserved4` | TField |  |  |
| 42 | `CA.CDR.RESERVED.3` | `CaClearingDirectory_Reserved3` | TField |  |  |
| 43 | `CA.CDR.RESERVED.2` | `CaClearingDirectory_Reserved2` | TField |  |  |
| 44 | `CA.CDR.RESERVED.1` | `CaClearingDirectory_Reserved1` | TField |  |  |
| 45 | `CA.CDR.OVERRIDE` | `CaClearingDirectory_Override` |  |  |  |
| 46 | `CA.CDR.RECORD.STATUS` | `CaClearingDirectory_RecordStatus` | String |  |  |
| 47 | `CA.CDR.CURR.NO` | `CaClearingDirectory_CurrNo` | String |  |  |
| 48 | `CA.CDR.INPUTTER` | `CaClearingDirectory_Inputter` |  |  |  |
| 49 | `CA.CDR.DATE.TIME` | `CaClearingDirectory_DateTime` |  |  |  |
| 50 | `CA.CDR.AUTHORISER` | `CaClearingDirectory_Authoriser` | String |  |  |
| 51 | `CA.CDR.CO.CODE` | `CaClearingDirectory_CoCode` | String |  |  |
| 52 | `CA.CDR.DEPT.CODE` | `CaClearingDirectory_DeptCode` | String |  |  |
| 53 | `CA.CDR.AUDITOR.CODE` | `CaClearingDirectory_AuditorCode` | String |  |  |
| 54 | `CA.CDR.AUDIT.DATE.TIME` | `CaClearingDirectory_AuditDateTime` | String |  |  |
