# CAPL.H.ENCRYPTION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.H.ENCRYPTION.PARAMETER` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENC.PARM.SHORT.DESCRP` | `CaplHEncryptionParameter_ShortDescrp` |  |  |  |
| 2 | `ENC.PARM.DESCRIPTION` | `CaplHEncryptionParameter_Description` |  |  |  |
| 3 | `ENC.PARM.RCL.VMAC.REQ.MAPPING` | `CaplHEncryptionParameter_RclVmacReqMapping` | TField |  | This field used to define a request mapping record id to form the VMAC request to HSM device.Validation: It should be a valid record from DFE.MAPPING tableEverlink:Eg: FX0010003.EVRDCP:Eg: FX0010003 |
| 4 | `ENC.PARM.RCL.VMAC.RES.MAPPING` | `CaplHEncryptionParameter_RclVmacResMapping` | TField |  | This field used to define a request mapping record id to form the VMAC response from HSM device.Validation: It should be a valid record from DFE.MAPPING table.Everlink:Eg: FX0010004.EVRDCP:Eg: FX0010004 |
| 5 | `ENC.PARM.RCL.GMAC.REQ.MAPPING` | `CaplHEncryptionParameter_RclGmacReqMapping` | TField |  | This field used to define a request mapping record id to form the GMAC request to HSM device.Validation: It should be a valid record from DFE.MAPPING tableEg: FX0010005.EVR |
| 6 | `ENC.PARM.RCL.GMAC.RES.MAPPING` | `CaplHEncryptionParameter_RclGmacResMapping` | TField |  | This field used to define a request mapping record id to form the GMAC response from HSM device.Validation: It should be a valid record from DFE.MAPPING tableEverlink:Eg: FX0010006.EVRDCP:Eg: FX0010006 |
| 7 | `ENC.PARM.ERR.FLD.MAP` | `CaplHEncryptionParameter_ErrFldMap` |  |  |  |
| 8 | `ENC.PARM.ERR.FLD.DESC` | `CaplHEncryptionParameter_ErrFldDesc` |  |  |  |
| 9 | `ENC.PARM.HOST.IP` | `CaplHEncryptionParameter_HostIp` | TField |  | For future use |
| 10 | `ENC.PARM.PORT` | `CaplHEncryptionParameter_Port` | TField |  | For future use |
| 11 | `ENC.PARM.TIMEOUT` | `CaplHEncryptionParameter_Timeout` | TField |  |  |
| 12 | `ENC.PARM.DIRECTION` | `CaplHEncryptionParameter_Direction` | TField |  | For future use |
| 13 | `ENC.PARM.LOC.REF` | `CaplHEncryptionParameter_LocRef` |  |  |  |
| 14 | `ENC.PARM.RESERVED.10` | `CaplHEncryptionParameter_Reserved10` |  |  |  |
| 15 | `ENC.PARM.RESERVED.9` | `CaplHEncryptionParameter_Reserved9` |  |  |  |
| 16 | `ENC.PARM.RESERVED.8` | `CaplHEncryptionParameter_Reserved8` |  |  |  |
| 17 | `ENC.PARM.RESERVED.7` | `CaplHEncryptionParameter_Reserved7` |  |  |  |
| 18 | `ENC.PARM.RESERVED.6` | `CaplHEncryptionParameter_Reserved6` |  |  |  |
| 19 | `ENC.PARM.RESERVED.5` | `CaplHEncryptionParameter_Reserved5` |  |  |  |
| 20 | `ENC.PARM.RESERVED.4` | `CaplHEncryptionParameter_Reserved4` |  |  |  |
| 21 | `ENC.PARM.RESERVED.3` | `CaplHEncryptionParameter_Reserved3` |  |  |  |
| 22 | `ENC.PARM.RESERVED.2` | `CaplHEncryptionParameter_Reserved2` |  |  |  |
| 23 | `ENC.PARM.RESERVED.1` | `CaplHEncryptionParameter_Reserved1` |  |  |  |
| 24 | `ENC.PARM.OVERRIDE` | `CaplHEncryptionParameter_Override` |  |  |  |
| 25 | `ENC.PARM.RECORD.STATUS` | `CaplHEncryptionParameter_RecordStatus` | String |  |  |
| 26 | `ENC.PARM.CURR.NO` | `CaplHEncryptionParameter_CurrNo` | String |  |  |
| 27 | `ENC.PARM.INPUTTER` | `CaplHEncryptionParameter_Inputter` |  |  |  |
| 28 | `ENC.PARM.DATE.TIME` | `CaplHEncryptionParameter_DateTime` |  |  |  |
| 29 | `ENC.PARM.AUTHORISER` | `CaplHEncryptionParameter_Authoriser` | String |  |  |
| 30 | `ENC.PARM.CO.CODE` | `CaplHEncryptionParameter_CoCode` | String |  |  |
| 31 | `ENC.PARM.DEPT.CODE` | `CaplHEncryptionParameter_DeptCode` | String |  |  |
| 32 | `ENC.PARM.AUDITOR.CODE` | `CaplHEncryptionParameter_AuditorCode` | String |  |  |
| 33 | `ENC.PARM.AUDIT.DATE.TIME` | `CaplHEncryptionParameter_AuditDateTime` | String |  |  |
