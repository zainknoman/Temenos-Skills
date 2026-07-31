# CAMB.H.ADDR.RIGHT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.H.ADDR.RIGHT.PARAM` in `CAADRT_AddressRight.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ADD.RIG.DESCRIPTION` | `CambHAddrRightParam_Description` | TField |  | Free text to define the description of the interface parameter. |
| 2 | `CAMB.ADD.RIG.EXC.CUST.STATUS` | `CambHAddrRightParam_ExcCustStatus` |  |  |  |
| 3 | `CAMB.ADD.RIG.EXC.CUST.SECTOR` | `CambHAddrRightParam_ExcCustSector` |  |  |  |
| 4 | `CAMB.ADD.RIG.INC.CUST.COUNTRY` | `CambHAddrRightParam_IncCustCountry` |  |  |  |
| 5 | `CAMB.ADD.RIG.EXT.PATH` | `CambHAddrRightParam_ExtPath` | TField |  | Field to define the Path where the Address file will be generated |
| 6 | `CAMB.ADD.RIG.EXT.FILE.NAME` | `CambHAddrRightParam_ExtFileName` | TField |  | Field used to define the File name of the customer address |
| 7 | `CAMB.ADD.RIG.UPD.PATH` | `CambHAddrRightParam_UpdPath` | TField |  | This Field is used to define the directory where the corrected Address extract file from the Canada post (3rd party) will be placed for updating the customer address in T24.3 files such as Valid Address file , Invalid address file and Corrected Address file will be receiving from a third party (eg street sweeper) to respective customer record and the alternate addresses. modified |
| 8 | `CAMB.ADD.RIG.UPD.FILE.NAME` | `CambHAddrRightParam_UpdFileName` | TField |  | Field used to define address files name for upload process.3 Address files (Valid Address file , Invalid address file and Corrected Address file) will be receiving from a third party (eg street sweeper) to respective customer record and the alternate addresses. comment not able to view |
| 9 | `CAMB.ADD.RIG.ARCH.PATH` | `CambHAddrRightParam_ArchPath` | TField |  | This field is mainly used to define the Path where the uploaded corrected file will be stored for audit purpose.Once the corrected Address file is uploaded in system, System will remove the corrected file from the path mentioned in UPD.PATH and move to the path defined in this field for audit purposes.Note : File name will be appended with date time modified |
| 10 | `CAMB.ADD.RIG.DEADDRESS.VERSION` | `CambHAddrRightParam_DeaddressVersion` | TField |  | This field is used to define the version name of APPLICATION DE.ADDRESS, that will be used by system to correct the customer address based on the file received from 3rd party.Validation: Valid VERSION record. Author:please validate, I see lot of fields missing or the field name is not correct. Please revalidateSrividya - added |
| 11 | `CAMB.ADD.RIG.OFS.SOURCE.RECORD` | `CambHAddrRightParam_OfsSourceRecord` | TField |  | This field is used to define the OFS Source id using which System will post OFS message to correct the customer address based on the file received from 3rd party.Validation: Valid OFS.SOURCE.ID |
| 12 | `CAMB.ADD.RIG.INC.BAD.ADDRESS` | `CambHAddrRightParam_IncBadAddress` | TField |  | Purpose of this field to indicate whether the customer with bad address flag to be considered for Address extraction or not.Inputs allowed - YES/NO--&gt; YES - Customer with bad address will be included in extracts.--&gt; NO - Customer with bad address will be excluded from extracts.Note: Bad address is mapped to CUSTOMER &gt; BAD.ADDRESS and DE.ADDRESS&gt;RETURN.MAIL) modified |
| 13 | `CAMB.ADD.RIG.INC.ADDR.STATUS` | `CambHAddrRightParam_IncAddrStatus` |  |  |  |
| 14 | `CAMB.ADD.RIG.OVERRIDE` | `CambHAddrRightParam_Override` |  |  |  |
| 15 | `CAMB.ADD.RIG.RESERVED.4` | `CambHAddrRightParam_Reserved4` | TField |  |  |
| 16 | `CAMB.ADD.RIG.RESERVED.3` | `CambHAddrRightParam_Reserved3` | TField |  |  |
| 17 | `CAMB.ADD.RIG.RESERVED.2` | `CambHAddrRightParam_Reserved2` | TField |  |  |
| 18 | `CAMB.ADD.RIG.RESERVED.1` | `CambHAddrRightParam_Reserved1` | TField |  |  |
| 19 | `CAMB.ADD.RIG.RECORD.STATUS` | `CambHAddrRightParam_RecordStatus` | String |  |  |
| 20 | `CAMB.ADD.RIG.CURR.NO` | `CambHAddrRightParam_CurrNo` | String |  |  |
| 21 | `CAMB.ADD.RIG.INPUTTER` | `CambHAddrRightParam_Inputter` |  |  |  |
| 22 | `CAMB.ADD.RIG.DATE.TIME` | `CambHAddrRightParam_DateTime` |  |  |  |
| 23 | `CAMB.ADD.RIG.AUTHORISER` | `CambHAddrRightParam_Authoriser` | String |  |  |
| 24 | `CAMB.ADD.RIG.CO.CODE` | `CambHAddrRightParam_CoCode` | String |  |  |
| 25 | `CAMB.ADD.RIG.DEPT.CODE` | `CambHAddrRightParam_DeptCode` | String |  |  |
| 26 | `CAMB.ADD.RIG.AUDITOR.CODE` | `CambHAddrRightParam_AuditorCode` | String |  |  |
| 27 | `CAMB.ADD.RIG.AUDIT.DATE.TIME` | `CambHAddrRightParam_AuditDateTime` | String |  |  |
