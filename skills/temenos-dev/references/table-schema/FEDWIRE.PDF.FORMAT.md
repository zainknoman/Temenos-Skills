# FEDWIRE.PDF.FORMAT — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.PDF.FORMAT` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWPDF.DESC` | `FedwirePdfFormat_Desc` |  |  |  |
| 2 | `FWPDF.DIRECTION` | `FedwirePdfFormat_Direction` | TField | Yes | Determines the direction of PDF message flow. Possible values: INWARD OUTWARD Mandatory input. |
| 3 | `FWPDF.IN.FMH.LEN` | `FedwirePdfFormat_InFmhLen` | TField |  | Inward Flash FMH header length. Input allowed only when ID is FLASH.FMH-i |
| 4 | `FWPDF.IN.FMH.FLD.NAME` | `FedwirePdfFormat_InFmhFldName` |  |  |  |
| 5 | `FWPDF.IN.FMH.FLD.LEN` | `FedwirePdfFormat_InFmhFldLen` |  |  |  |
| 6 | `FWPDF.RESERVED.25` | `FedwirePdfFormat_Reserved25` |  |  |  |
| 7 | `FWPDF.RESERVED.23` | `FedwirePdfFormat_Reserved23` |  |  |  |
| 8 | `FWPDF.RESERVED.22` | `FedwirePdfFormat_Reserved22` |  |  |  |
| 9 | `FWPDF.REQ.MID.ID` | `FedwirePdfFormat_ReqMidId` | TField | No | Contains the MID-ID of the request message for a solicited response received from FFS. Optional input. |
| 10 | `FWPDF.OUT.FLD.NAME` | `FedwirePdfFormat_OutFldName` |  |  |  |
| 11 | `FWPDF.OUT.FLD.LEN` | `FedwirePdfFormat_OutFldLen` |  |  |  |
| 12 | `FWPDF.OUT.FLD.FMT` | `FedwirePdfFormat_OutFldFmt` |  |  |  |
| 13 | `FWPDF.RESERVED.21` | `FedwirePdfFormat_Reserved21` |  |  |  |
| 14 | `FWPDF.RESERVED.20` | `FedwirePdfFormat_Reserved20` |  |  |  |
| 15 | `FWPDF.URC` | `FedwirePdfFormat_Urc` | TField | No | User Request Correlation is spaces on messages and files sent by FFS. Otherwise, it will be the same as in the corresponding request. Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 16 | `FWPDF.MSG.ID` | `FedwirePdfFormat_MsgId` | TField | No | Identifies the message/file description. A unique ID(across all applications, the first 2 characters should identify the originating application. Optional input. |
| 17 | `FWPDF.RELEASE.ID` | `FedwirePdfFormat_ReleaseId` | TField | No | Indicates the release number of the format corresponding to MSG-ID. Starting with &quot; 01 &quot; , it will be increment by 1 whenever the contents are significantly revised. Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 18 | `FWPDF.MSG.STAT.CD` | `FedwirePdfFormat_MsgStatCd` | TField | No | Identifies the reason and status of the output. A � sent by FFS as part of normal processing. E � sent by FFS as an error response to an input request. space - good response to an inquiry or service request. Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 19 | `FWPDF.PRINT.LN.SIZE` | `FedwirePdfFormat_PrintLnSize` | TField | No | The number of print/display characters per line (eg. �079� or �132�). It will be less than or equals to 132, not including LN-TYPE block(s) Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 20 | `FWPDF.MAX.NO.LINES` | `FedwirePdfFormat_MaxNoLines` | TField | No | The max. number of lines per page. It should be less than or equals to 66. Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 21 | `FWPDF.FILLER` | `FedwirePdfFormat_Filler` | TField | No | For future use. Filled with spaces. Optional input. Input must be of format Start Postion,End Position. For eg, 10,5 |
| 22 | `FWPDF.CNTRL.DATA.LEN` | `FedwirePdfFormat_CntrlDataLen` | TField | No | Total length of CTRNL-DATA block Optional input. |
| 23 | `FWPDF.CNTRL.DATA.API` | `FedwirePdfFormat_CntrlDataApi` | TField | No | API that should be invoked specific to control data block. Optional input. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record USRTGS.CNTRL.DATA.API.HOOK This field supports the Fedwire.updateControlData() method. The Fedwire Class is in the hook.countrymodelbank.usa.Fedwire package which is in USRTGS_FedwireHook.jar shipped with T24. |
| 24 | `FWPDF.LN.TYPE` | `FedwirePdfFormat_LnType` |  |  |  |
| 25 | `FWPDF.LN.FLD.NAME` | `FedwirePdfFormat_LnFldName` |  |  |  |
| 26 | `FWPDF.LN.FLD.LEN` | `FedwirePdfFormat_LnFldLen` |  |  |  |
| 27 | `FWPDF.RESERVED.19` | `FedwirePdfFormat_Reserved19` |  |  |  |
| 28 | `FWPDF.RESERVED.18` | `FedwirePdfFormat_Reserved18` |  |  |  |
| 29 | `FWPDF.LN.TYPE.API` | `FedwirePdfFormat_LnTypeApi` |  |  |  |
| 30 | `FWPDF.RESERVED.17` | `FedwirePdfFormat_Reserved17` |  |  |  |
| 31 | `FWPDF.RESERVED.16` | `FedwirePdfFormat_Reserved16` |  |  |  |
| 32 | `FWPDF.RESERVED.15` | `FedwirePdfFormat_Reserved15` | TField |  |  |
| 33 | `FWPDF.RESERVED.14` | `FedwirePdfFormat_Reserved14` | TField |  |  |
| 34 | `FWPDF.RESERVED.13` | `FedwirePdfFormat_Reserved13` | TField |  |  |
| 35 | `FWPDF.RESERVED.12` | `FedwirePdfFormat_Reserved12` | TField |  |  |
| 36 | `FWPDF.RESERVED.11` | `FedwirePdfFormat_Reserved11` | TField |  |  |
| 37 | `FWPDF.RESERVED.10` | `FedwirePdfFormat_Reserved10` | TField |  |  |
| 38 | `FWPDF.RESERVED.9` | `FedwirePdfFormat_Reserved9` | TField |  |  |
| 39 | `FWPDF.RESERVED.8` | `FedwirePdfFormat_Reserved8` | TField |  |  |
| 40 | `FWPDF.RESERVED.7` | `FedwirePdfFormat_Reserved7` | TField |  |  |
| 41 | `FWPDF.RESERVED.6` | `FedwirePdfFormat_Reserved6` | TField |  |  |
| 42 | `FWPDF.RESERVED.5` | `FedwirePdfFormat_Reserved5` | TField |  |  |
| 43 | `FWPDF.RESERVED.4` | `FedwirePdfFormat_Reserved4` | TField |  |  |
| 44 | `FWPDF.RESERVED.3` | `FedwirePdfFormat_Reserved3` | TField |  |  |
| 45 | `FWPDF.RESERVED.2` | `FedwirePdfFormat_Reserved2` | TField |  |  |
| 46 | `FWPDF.RESERVED.1` | `FedwirePdfFormat_Reserved1` | TField |  |  |
| 47 | `FWPDF.RECORD.STATUS` | `FedwirePdfFormat_RecordStatus` | String |  |  |
| 48 | `FWPDF.CURR.NO` | `FedwirePdfFormat_CurrNo` | String |  |  |
| 49 | `FWPDF.INPUTTER` | `FedwirePdfFormat_Inputter` |  |  |  |
| 50 | `FWPDF.DATE.TIME` | `FedwirePdfFormat_DateTime` |  |  |  |
| 51 | `FWPDF.AUTHORISER` | `FedwirePdfFormat_Authoriser` | String |  |  |
| 52 | `FWPDF.CO.CODE` | `FedwirePdfFormat_CoCode` | String |  |  |
| 53 | `FWPDF.DEPT.CODE` | `FedwirePdfFormat_DeptCode` | String |  |  |
| 54 | `FWPDF.AUDITOR.CODE` | `FedwirePdfFormat_AuditorCode` | String |  |  |
| 55 | `FWPDF.AUDIT.DATE.TIME` | `FedwirePdfFormat_AuditDateTime` | String |  |  |
