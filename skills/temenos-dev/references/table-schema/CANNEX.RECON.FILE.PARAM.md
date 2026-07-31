# CANNEX.RECON.FILE.PARAM — Table Schema

> Source: `INSERTS/I_F.CANNEX.RECON.FILE.PARAM` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.RFP.HEADER.REC.TYPE` | `CannexReconFileParam_HeaderRecType` | TField |  | This field will hold the value of the header record type of the GIC order event file (RECORD-TYPE field).E.g. HDR (Constant value) |
| 2 | `CANNEX.RFP.VERSION` | `CannexReconFileParam_Version` | TField |  | The field value will be displayed in the Header of the Recon file param.This field will hold the value of the current Version.E.g. 1.11j |
| 3 | `CANNEX.RFP.ORDER.REC.TYPE` | `CannexReconFileParam_OrderRecType` | TField |  | This field will hold the value of the Order record type of the GIC order event file (RECORD-TYPE field).E.g. DTL (Constant value) |
| 4 | `CANNEX.RFP.TRAILER.REC.TYPE` | `CannexReconFileParam_TrailerRecType` | TField |  | This field will hold the value of the Trailer record type of the GIC order event file (RECORD-TYPE field).E.g.TRL (Constant value) |
| 5 | `CANNEX.RFP.FILE.NAME` | `CannexReconFileParam_FileName` | TField | No | This field will hold the naming convention of the file.E.g: TERMR[Y]_YYYYMMDD_XXXX_AAAAAAAAAAAA_DD.{TXT,CSV}[Y] - an optional character with a value of "Y" to indicate that this file is for testing only.YYYYMMDD - the period ending date that the file was created for reconciling.XXXX - the IPNO the CANNEX Information Provider number - i.e. CANNEX Issuer Number), 4 character alpha-numeric value that CANNEX has uniquely assigned to each of the issuers.AAAAAAAAAAAA - the Agent Id assigned by the issuer for the AgentDD - The file sequence number (parameterized).{txt,csv} - The file extension to indicate whether the file is a fixed position format (.TXT) or a comma delimited format (.CSV). |
| 6 | `CANNEX.RFP.DIR.NAME` | `CannexReconFileParam_DirName` | TField |  |  |
| 7 | `CANNEX.RFP.COMP.CODE` | `CannexReconFileParam_CompCode` |  |  |  |
| 8 | `CANNEX.RFP.IPNO` | `CannexReconFileParam_Ipno` |  |  |  |
| 9 | `CANNEX.RFP.SEQ.NO` | `CannexReconFileParam_SeqNo` | TField |  | The value in the field is numeric character, which will hold the report sequence number, incremental for each new file generated for the specific period. |
| 10 | `CANNEX.RFP.ALT.ACCT.TYPE` | `CannexReconFileParam_AltAcctType` | TField |  | This field is to capture the ALT.ACCT.TYPE to fetch the alternate ID for certificate number in recon file. |
| 11 | `CANNEX.RFP.DEF.CERT.INSTR` | `CannexReconFileParam_DefCertInstr` | TField |  | This field is to store the default certificate instr for recon file.Value support NM and CP. |
| 12 | `CANNEX.RFP.DEFAULT.IPNO` | `CannexReconFileParam_DefaultIpno` | TField |  | This field is to store the default IPNO number of a company. |
| 13 | `CANNEX.RFP.BRNCH.CDE.FLD.NAME` | `CannexReconFileParam_BrnchCdeFldName` | TField |  | This Field captures the T24 field name which stores the cannex branch code |
| 14 | `CANNEX.RFP.DEF.BRANCH.CODE` | `CannexReconFileParam_DefBranchCode` | TField |  | Field to indicate the default branch code. Which will be prefixed with the BR.FLD.CO.CDE field in Account appliaction.Note: The ACCOUNT application field name will be defined in BRNCH.CDE.FLD.NAME field. |
| 15 | `CANNEX.RFP.RESERVED.9` | `CannexReconFileParam_Reserved9` | TField |  |  |
| 16 | `CANNEX.RFP.RESERVED.10` | `CannexReconFileParam_Reserved10` | TField |  |  |
| 17 | `CANNEX.RFP.RECORD.STATUS` | `CannexReconFileParam_RecordStatus` | String |  |  |
| 18 | `CANNEX.RFP.CURR.NO` | `CannexReconFileParam_CurrNo` | String |  |  |
| 19 | `CANNEX.RFP.INPUTTER` | `CannexReconFileParam_Inputter` |  |  |  |
| 20 | `CANNEX.RFP.DATE.TIME` | `CannexReconFileParam_DateTime` |  |  |  |
| 21 | `CANNEX.RFP.AUTHORISER` | `CannexReconFileParam_Authoriser` | String |  |  |
| 22 | `CANNEX.RFP.CO.CODE` | `CannexReconFileParam_CoCode` | String |  |  |
| 23 | `CANNEX.RFP.DEPT.CODE` | `CannexReconFileParam_DeptCode` | String |  |  |
| 24 | `CANNEX.RFP.AUDITOR.CODE` | `CannexReconFileParam_AuditorCode` | String |  |  |
| 25 | `CANNEX.RFP.AUDIT.DATE.TIME` | `CannexReconFileParam_AuditDateTime` | String |  |  |
