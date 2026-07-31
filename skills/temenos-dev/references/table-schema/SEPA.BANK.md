# SEPA.BANK — Table Schema

> Source: `INSERTS/I_F.SEPA.BANK` in `EP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.BNK.DESCRIPTION` | `SepaBank_Description` |  |  |  |
| 2 | `SEP.BNK.ADDRESS` | `SepaBank_Address` |  |  |  |
| 3 | `SEP.BNK.BANK.NAME` | `SepaBank_BankName` | A (Alphanumeric) |  | This field is specified with a Valid Bank name Validation Rules Value upto 90 type A(Alphanumeric) |
| 4 | `SEP.BNK.ROUTING.SCT` | `SepaBank_RoutingSct` | A (Alphanumeric) |  | This field holds the Value for routing SCT Validation Rules Value upto 2 type A(Alphanumeric) |
| 5 | `SEP.BNK.SRVC.FLAG.SCT` | `SepaBank_SrvcFlagSct` | A (Alphanumeric) |  | This field holds the Flag value for SCT Validation Rules Value upto 1 type A(Alphanumeric) |
| 6 | `SEP.BNK.ROUTING.SDD` | `SepaBank_RoutingSdd` | A (Alphanumeric) |  | This field holds the Value for routing SDD Validation Rules Value upto 2 type A(Alphanumeric) |
| 7 | `SEP.BNK.SRVC.FLAG.SDD` | `SepaBank_SrvcFlagSdd` | A (Alphanumeric) |  | This field holds the Flag value for SDD Validation Rules Value upto 1 type A(Alphanumeric) |
| 8 | `SEP.BNK.ROUTING.B2B` | `SepaBank_RoutingB2b` | A (Alphanumeric) |  | This field holds the Value for routing B2B Validation Rules Value upto 2 type A(Alphanumeric) |
| 9 | `SEP.BNK.SRVC.FLAG.B2B` | `SepaBank_SrvcFlagB2b` | A (Alphanumeric) |  | This field holds the Flag value for SDD-B2B Validation Rules Value upto 1 type A(Alphanumeric) |
| 10 | `SEP.BNK.IMP.FILE.NAME` | `SepaBank_ImpFileName` | A (Alphanumeric) |  | This Field specifies the File name in which the file gets stored in the path specified for routing directory Validation Rules Value upto 25 type A(Alphanumeric) |
| 11 | `SEP.BNK.PRODUCT` | `SepaBank_Product` |  |  |  |
| 12 | `SEP.BNK.VALID.FROM` | `SepaBank_ValidFrom` |  |  |  |
| 13 | `SEP.BNK.VALID.TO` | `SepaBank_ValidTo` |  |  |  |
| 14 | `SEP.BNK.CUT.OFF.TIME` | `SepaBank_CutOffTime` |  |  |  |
| 15 | `SEP.BNK.VERSION` | `SepaBank_Version` |  |  |  |
| 16 | `SEP.BNK.STATUS` | `SepaBank_Status` | A (Alphanumeric) |  | This field holds the status of the record Validation Rules Value upto 10 type A(Alphanumeric) |
| 17 | `SEP.BNK.ADM.PROFILE` | `SepaBank_AdmProfile` | A (Alphanumeric) |  | This field holds the Admission Profile. Allowed values are provided below Validation Rules Value upto 10 type A(Alphanumeric) CAD(The Bank is both Debtor and Creditor Agent and can send AND receive Direct Debit)� CRD(The Bank is a Creditor Agent only and can only send Direct Debit. The creditor bank should never be able to receive a Payment Cancellation Request or Reversal) DEB(The Bank is a Debtor Agent only and can only receive Direct Debit. The debtor bank should never be able to receive a Refund/Return or a Reject/Refusal) |
| 18 | `SEP.BNK.DP.BIC` | `SepaBank_DpBic` | A (Alphanumeric) |  | This fields holds the direct participant BIC Validation Rules Value upto 11 type A(Alphanumeric) |
| 19 | `SEP.BNK.TYPE.ALLOW` | `SepaBank_TypeAllow` |  |  |  |
| 20 | `SEP.BNK.RESERVED.4` | `SepaBank_Reserved4` | TField |  |  |
| 21 | `SEP.BNK.RESERVED.3` | `SepaBank_Reserved3` | TField |  |  |
| 22 | `SEP.BNK.RESERVED.2` | `SepaBank_Reserved2` | TField |  |  |
| 23 | `SEP.BNK.RESERVED.1` | `SepaBank_Reserved1` | TField |  |  |
| 24 | `SEP.BNK.LOCAL.REF` | `SepaBank_LocalRef` |  |  |  |
| 25 | `SEP.BNK.RECORD.STATUS` | `SepaBank_RecordStatus` | String |  |  |
| 26 | `SEP.BNK.CURR.NO` | `SepaBank_CurrNo` | String |  |  |
| 27 | `SEP.BNK.INPUTTER` | `SepaBank_Inputter` |  |  |  |
| 28 | `SEP.BNK.DATE.TIME` | `SepaBank_DateTime` |  |  |  |
| 29 | `SEP.BNK.AUTHORISER` | `SepaBank_Authoriser` | String |  |  |
| 30 | `SEP.BNK.CO.CODE` | `SepaBank_CoCode` | String |  |  |
| 31 | `SEP.BNK.DEPT.CODE` | `SepaBank_DeptCode` | String |  |  |
| 32 | `SEP.BNK.AUDITOR.CODE` | `SepaBank_AuditorCode` | String |  |  |
| 33 | `SEP.BNK.AUDIT.DATE.TIME` | `SepaBank_AuditDateTime` | String |  |  |
