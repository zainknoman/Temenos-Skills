# PX.PYT.RESOURCE — Table Schema

> Source: `INSERTS/I_F.PX.PYT.RESOURCE` in `PX_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PX.PYT.TPP.GLOBAL.URN` | `PxPytResource_TppGlobalUrn` | TField | Yes | Field to hold the Global URN of the TPP to which the consent is linked to based on an API call. This can be alsoa registered TPP in PZ.OPEN.BANKING.DIR if OBD management is within Temenos. Validation Rules: Alpha Numeric Nochange and Mandatory Field. |
| 2 | `PX.PYT.CUSTOMER.ID` | `PxPytResource_CustomerId` | TField |  | Field to hold the Transact customer Id of the online banking user who is authenticated. It is updated after theuser completes SCA. Validation Rules: A valid Transact Customer Id |
| 3 | `PX.PYT.SCA.HINT` | `PxPytResource_ScaHint` | TField |  |  |
| 4 | `PX.PYT.PAYMENT.STATUS` | `PxPytResource_PaymentStatus` | TField |  | Field to hold the status of the payment. The status is dependent on the information pushed from the User Agent. It is not directly linked to the internal Temenos Transact status of the payment record. The following statuses can be applied: 1.RCVD - Initial status of the payment when the request is received. 2.RJCT - When the payment is rejected for any reason. 3.PATC - When the user approves the payment and receives one authorisation and pending additional approvals. 4.ACSP/ACWP � When the user approves the payment and all authorisations have been met for the payment. 5.ANC � When the user cancels the payment. |
| 5 | `PX.PYT.SCA.STATUS` | `PxPytResource_ScaStatus` | TField | Yes | Field to hold overall SCA status of the payment. Mandatory field. Allowed values are - NULL, received, scaMethodSelected, psuAuthenticated, finalised (SCA is completed by theuser). 1.received - An authorisation or cancellation authorisation resource has been created successfully. 2.psuAuthenticated - The PSU related to the authorisation or cancellation-authorisation resource has beenidentified and authenticated e.g. by a password or by an access token. 3.scaMethodSelected - The PSU/TPP has selected the related SCA routine. If the SCA method is chosen implicitlysince only one SCA method is available, then this is the first status to be reported instead of 'received'. 4.finalised - The SCA routine has been finalised successfully. |
| 6 | `PX.PYT.TPP.REDIRECT.URL.DEFAULT` | `PxPytResource_TppRedirectUrlDefault` | TField |  | This field holds the redirection URL to the TPP. This URL can be used to redirect PSU from PSD2 User Agent to theTPP post Payment confirmation/rejection. However this field is not used in the current flows. |
| 7 | `PX.PYT.TPP.REDIRECT.URL.SUCCESS` | `PxPytResource_TppRedirectUrlSuccess` | TField |  |  |
| 8 | `PX.PYT.TPP.REDIRECT.URL.FAILURE` | `PxPytResource_TppRedirectUrlFailure` | TField |  |  |
| 9 | `PX.PYT.EXT.PYMT.STATUS` | `PxPytResource_ExtPymtStatus` | TField |  | The field specifies the payment status for externally initiated payments. |
| 10 | `PX.PYT.EXT.STATUS.REASON` | `PxPytResource_ExtStatusReason` | TField |  | The field denotes the reason for the payment status for externally initiated payments. |
| 11 | `PX.PYT.TRUSTED.BENEFICIARY` | `PxPytResource_TrustedBeneficiary` | TField |  | Field to identify whether the User who has logged in is the owning customer of a Beneficiary number matching thecredit account number in the payment. Validation Rule: Allowed Values - TRUE or FALSE. TRUE - means the system identifies that the creditor of the payment is a beneficiary of the logged in User. FALSE - means the system identifies that the creditor of the payment is NOT a beneficiary of the logged in User. Only stored for informational purposes in Temenos Transact without validations or logic. |
| 12 | `PX.PYT.SUB.RES.ID` | `PxPytResource_SubResId` |  |  |  |
| 13 | `PX.PYT.SUB.RES.SCA.STATUS` | `PxPytResource_SubResScaStatus` |  |  |  |
| 14 | `PX.PYT.SUB.RES.CAPTURE.METHOD` | `PxPytResource_SubResCaptureMethod` |  |  |  |
| 15 | `PX.PYT.SUB.RES.REQUEST.ID` | `PxPytResource_SubResRequestId` |  |  |  |
| 16 | `PX.PYT.SCA.EXEMPT` | `PxPytResource_ScaExempt` | TField |  | Field to hold the response from an external source, if the payment is exempted from SCA or not. No coreprocessing is performed based on the content of this field. Possible values - YES or NO. |
| 17 | `PX.PYT.AUTHORISATION` | `PxPytResource_AuthorisationKey` |  |  |  |
| 18 | `PX.PYT.CERTIFICATE` | `PxPytResource_Certificate` | TField |  | Field to hold the certificate from the SCA provider where an SCA hook is enabled in the PSD2 User Agent and isonly updated as part of local integration. |
| 19 | `PX.PYT.TPP.NAME` | `PxPytResource_TppName` | TField |  | Field to hold the name of the TPP to which the payment is linked to based on an API call. |
| 20 | `PX.PYT.RESERVED.42` | `PxPytResource_Reserved42` | TField |  |  |
| 21 | `PX.PYT.RESERVED.41` | `PxPytResource_Reserved41` | TField |  |  |
| 22 | `PX.PYT.RESERVED.40` | `PxPytResource_Reserved40` | TField |  |  |
| 23 | `PX.PYT.RESERVED.39` | `PxPytResource_Reserved39` | TField |  |  |
| 24 | `PX.PYT.RESERVED.38` | `PxPytResource_Reserved38` | TField |  |  |
| 25 | `PX.PYT.RESERVED.37` | `PxPytResource_Reserved37` | TField |  |  |
| 26 | `PX.PYT.RESERVED.36` | `PxPytResource_Reserved36` | TField |  |  |
| 27 | `PX.PYT.RESERVED.35` | `PxPytResource_Reserved35` | TField |  |  |
| 28 | `PX.PYT.RESERVED.34` | `PxPytResource_Reserved34` | TField |  |  |
| 29 | `PX.PYT.RESERVED.33` | `PxPytResource_Reserved33` | TField |  |  |
| 30 | `PX.PYT.RESERVED.32` | `PxPytResource_Reserved32` | TField |  |  |
| 31 | `PX.PYT.RESERVED.31` | `PxPytResource_Reserved31` | TField |  |  |
| 32 | `PX.PYT.RESERVED.30` | `PxPytResource_Reserved30` | TField |  |  |
| 33 | `PX.PYT.RESERVED.29` | `PxPytResource_Reserved29` | TField |  |  |
| 34 | `PX.PYT.RESERVED.28` | `PxPytResource_Reserved28` | TField |  |  |
| 35 | `PX.PYT.RESERVED.27` | `PxPytResource_Reserved27` | TField |  |  |
| 36 | `PX.PYT.RESERVED.26` | `PxPytResource_Reserved26` | TField |  |  |
| 37 | `PX.PYT.RESERVED.25` | `PxPytResource_Reserved25` | TField |  |  |
| 38 | `PX.PYT.RESERVED.24` | `PxPytResource_Reserved24` | TField |  |  |
| 39 | `PX.PYT.RESERVED.23` | `PxPytResource_Reserved23` | TField |  |  |
| 40 | `PX.PYT.RESERVED.22` | `PxPytResource_Reserved22` | TField |  |  |
| 41 | `PX.PYT.RESERVED.21` | `PxPytResource_Reserved21` | TField |  |  |
| 42 | `PX.PYT.RESERVED.20` | `PxPytResource_Reserved20` | TField |  |  |
| 43 | `PX.PYT.RESERVED.19` | `PxPytResource_Reserved19` | TField |  |  |
| 44 | `PX.PYT.RESERVED.18` | `PxPytResource_Reserved18` | TField |  |  |
| 45 | `PX.PYT.RESERVED.17` | `PxPytResource_Reserved17` | TField |  |  |
| 46 | `PX.PYT.RESERVED.16` | `PxPytResource_Reserved16` | TField |  |  |
| 47 | `PX.PYT.RESERVED.15` | `PxPytResource_Reserved15` | TField |  |  |
| 48 | `PX.PYT.RESERVED.14` | `PxPytResource_Reserved14` | TField |  |  |
| 49 | `PX.PYT.RESERVED.13` | `PxPytResource_Reserved13` | TField |  |  |
| 50 | `PX.PYT.RESERVED.12` | `PxPytResource_Reserved12` | TField |  |  |
| 51 | `PX.PYT.RESERVED.11` | `PxPytResource_Reserved11` | TField |  |  |
| 52 | `PX.PYT.RESERVED.10` | `PxPytResource_Reserved10` | TField |  |  |
| 53 | `PX.PYT.RESERVED.09` | `PxPytResource_Reserved09` | TField |  |  |
| 54 | `PX.PYT.RESERVED.08` | `PxPytResource_Reserved08` | TField |  |  |
| 55 | `PX.PYT.RESERVED.07` | `PxPytResource_Reserved07` | TField |  |  |
| 56 | `PX.PYT.RESERVED.06` | `PxPytResource_Reserved06` | TField |  |  |
| 57 | `PX.PYT.RESERVED.05` | `PxPytResource_Reserved05` | TField |  |  |
| 58 | `PX.PYT.RESERVED.04` | `PxPytResource_Reserved04` | TField |  |  |
| 59 | `PX.PYT.RESERVED.03` | `PxPytResource_Reserved03` | TField |  |  |
| 60 | `PX.PYT.RESERVED.02` | `PxPytResource_Reserved02` | TField |  |  |
| 61 | `PX.PYT.RESERVED.01` | `PxPytResource_Reserved01` | TField |  |  |
| 62 | `PX.PYT.LOCAL.REF` | `PxPytResource_LocalRef` |  |  |  |
| 63 | `PX.PYT.OVERRIDE` | `PxPytResource_Override` |  |  |  |
| 64 | `PX.PYT.RECORD.STATUS` | `PxPytResource_RecordStatus` | String |  |  |
| 65 | `PX.PYT.CURR.NO` | `PxPytResource_CurrNo` | String |  |  |
| 66 | `PX.PYT.INPUTTER` | `PxPytResource_Inputter` |  |  |  |
| 67 | `PX.PYT.DATE.TIME` | `PxPytResource_DateTime` |  |  |  |
| 68 | `PX.PYT.AUTHORISER` | `PxPytResource_Authoriser` | String |  |  |
| 69 | `PX.PYT.CO.CODE` | `PxPytResource_CoCode` | String |  |  |
| 70 | `PX.PYT.DEPT.CODE` | `PxPytResource_DeptCode` | String |  |  |
| 71 | `PX.PYT.AUDITOR.CODE` | `PxPytResource_AuditorCode` | String |  |  |
| 72 | `PX.PYT.AUDIT.DATE.TIME` | `PxPytResource_AuditDateTime` | String |  |  |
