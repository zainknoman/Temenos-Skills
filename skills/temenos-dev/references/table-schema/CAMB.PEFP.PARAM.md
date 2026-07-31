# CAMB.PEFP.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.PEFP.PARAM` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEFP.PARAM.TRHOLD.AMOUNT` | `CambPefpParam_TrholdAmount` | TField |  | This field is used to define the threshold amount above which the FT and TT record will be considered for PEFP.Eg 100,000The threshold of aggregation of CAD 100,000 per transaction will be considered for PEFP reporting. |
| 2 | `PEFP.PARAM.RPT.FILE.NAME` | `CambPefpParam_RptFileName` | TField |  | The field is used to define the file name for PEFP extract.Eg. COMPLEXT_001_OUT.DATFile name will be 20180101:COMPLEXT_001_OUT.DATas--&gt; 20180101 is the date of the extract.--&gt; COMPLEXT_001_OUT.DAT - static value from this field.--&gt; DAT - file format |
| 3 | `PEFP.PARAM.LC.DIR` | `CambPefpParam_LcDir` | TField |  | The field is used to define the directory/path for PEFP file generation. |
| 4 | `PEFP.PARAM.OFS.SOURCE.ID` | `CambPefpParam_OfsSourceId` | TField |  | This field is used to define the OFS.SOURCE for CUSTOMER PEFP UpdateValidation.- Valid record of OFS.SOURCEDuring the batch process of PEFP reporting, system updates the CUSTOMER &gt; CAMB.PEFP viaOFS source |
| 5 | `PEFP.PARAM.VERSION` | `CambPefpParam_Version` | TField |  | Field used to define the customer Version, which system uses for PEFP Update.Valid VERSION recordDuring the batch process of PEFP reporting, system updates the CUSTOMER &gt; CAMB.PEFP via OFS source using the version defined in this field. |
| 6 | `PEFP.PARAM.DEST.IP.ADD` | `CambPefpParam_DestIpAdd` | TField |  | Field to define the Destination IP address for PEFP extract. |
| 7 | `PEFP.PARAM.DEST.DIR` | `CambPefpParam_DestDir` | TField |  | Field to define the valid log directory for PEFP extract. |
| 8 | `PEFP.PARAM.OUTWARD.FT.TXN` | `CambPefpParam_OutwardFtTxn` |  |  |  |
| 9 | `PEFP.PARAM.REMOTE.USER` | `CambPefpParam_RemoteUser` | TField |  | Remote ID used to place the extract in the path defined in LC.DIR |
| 10 | `PEFP.PARAM.RMT.PASSWORD` | `CambPefpParam_RmtPassword` | TField |  | Remote Password used to place the extract in the path defined in LC.DIR |
| 11 | `PEFP.PARAM.OFS.USER` | `CambPefpParam_OfsUser` | TField |  | This field is used to define the USER which system will use for CUSTOMER PEFP UpdateValidation: Valid USER recordDuring the batch process of PEFP reporting, system updates the CUSTOMER &gt; CAMB.PEFP via OFSOFS user id defined in this field is used to pass the USER ID in OFS for the udpate in Customer table. |
| 12 | `PEFP.PARAM.OFS.PASSWORD` | `CambPefpParam_OfsPassword` | TField |  | This field is used to define the USER Password which system will use for CUSTOMER PEFP UpdateValidation: Valid USER Password.During the batch process of PEFP reporting, system updates the CUSTOMER &gt; CAMB.PEFP via OFSOFS Password defined in this field is used to pass the PASSWORD OFS for the udpate in Customer table. |
| 13 | `PEFP.PARAM.INWARD.FT.TXN` | `CambPefpParam_InwardFtTxn` |  |  |  |
| 14 | `PEFP.PARAM.CUS.TYPE` | `CambPefpParam_CusType` |  |  |  |
| 15 | `PEFP.PARAM.CUSTOMER.SINCE` | `CambPefpParam_CustomerSince` | TField |  | This field is used to define the date after which the customer is to be selected for reporting.Field in Date format.Validations - CUSTOMER &gt; CUSTOMER.SINCE field will be compared with this field.CUSTOMER &gt; CUSTOMER.SINCE greater than this field will be considered for PEFP reporting.eg. 11 july 2015. Customer record with date greater than 11 july 2015 will be considered for PEFP reporting. |
| 16 | `PEFP.PARAM.OUTWARD.TT.TXN` | `CambPefpParam_OutwardTtTxn` |  |  |  |
| 17 | `PEFP.PARAM.INWARD.TT.TXN` | `CambPefpParam_InwardTtTxn` |  |  |  |
| 18 | `PEFP.PARAM.RECORD.STATUS` | `CambPefpParam_RecordStatus` | String |  |  |
| 19 | `PEFP.PARAM.CURR.NO` | `CambPefpParam_CurrNo` | String |  |  |
| 20 | `PEFP.PARAM.INPUTTER` | `CambPefpParam_Inputter` |  |  |  |
| 21 | `PEFP.PARAM.DATE.TIME` | `CambPefpParam_DateTime` |  |  |  |
| 22 | `PEFP.PARAM.AUTHORISER` | `CambPefpParam_Authoriser` | String |  |  |
| 23 | `PEFP.PARAM.CO.CODE` | `CambPefpParam_CoCode` | String |  |  |
| 24 | `PEFP.PARAM.DEPT.CODE` | `CambPefpParam_DeptCode` | String |  |  |
| 25 | `PEFP.PARAM.AUDITOR.CODE` | `CambPefpParam_AuditorCode` | String |  |  |
| 26 | `PEFP.PARAM.AUDIT.DATE.TIME` | `CambPefpParam_AuditDateTime` | String |  |  |
