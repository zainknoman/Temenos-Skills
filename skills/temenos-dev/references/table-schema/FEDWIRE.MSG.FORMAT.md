# FEDWIRE.MSG.FORMAT — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.MSG.FORMAT` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWMF.DESC` | `FedwireMsgFormat_Desc` |  |  |  |
| 2 | `FWMF.MSG.TYPE` | `FedwireMsgFormat_MsgType` | TField |  | Indicator to determine the type of message. Possible values are: VALUE - Message that results in accounting entries and are originated/processed by T24 payment system. NON-VALUE - Message that does NOT result in accounting entries, such as SVC messages. |
| 3 | `FWMF.MT.KEY.TAG.ELEMENT` | `FedwireMsgFormat_MtKeyTagElement` | TField |  | Tag element from the incoming/outgoing message that is used to determine the key to FEWIRE.MESSAGE.TRACKER. Must be a valid entry in FEDWIRE.TAG.ELEMENT |
| 4 | `FWMF.TAG` | `FedwireMsgFormat_Tag` |  |  |  |
| 5 | `FWMF.EDIT.PROPERTY` | `FedwireMsgFormat_EditProperty` |  |  |  |
| 6 | `FWMF.TAG.VALUE` | `FedwireMsgFormat_TagValue` |  |  |  |
| 7 | `FWMF.DEF.VALUE` | `FedwireMsgFormat_DefValue` |  |  |  |
| 8 | `FWMF.RESERVED.20` | `FedwireMsgFormat_Reserved20` |  |  |  |
| 9 | `FWMF.RESERVED.19` | `FedwireMsgFormat_Reserved19` |  |  |  |
| 10 | `FWMF.RESERVED.18` | `FedwireMsgFormat_Reserved18` |  |  |  |
| 11 | `FWMF.RESERVED.17` | `FedwireMsgFormat_Reserved17` |  |  |  |
| 12 | `FWMF.RESERVED.16` | `FedwireMsgFormat_Reserved16` |  |  |  |
| 13 | `FWMF.PH.TXN` | `FedwireMsgFormat_PhTxn` | TField |  | Flag to determine whether the message is processed by PH Possible values are: YES NO |
| 14 | `FWMF.APP.NAME` | `FedwireMsgFormat_AppName` | TField | Yes | The Source/Destination application in T24 where data is mapped by the Fedwire inbound/outbound service. Mandatory input. |
| 15 | `FWMF.POST.PROCESS.API` | `FedwireMsgFormat_PostProcessApi` | TField |  | A user-defined API that will be triggered on processing of all TAG and can be used perform additional updates to on the constructed message before being posted. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record USRTGS.POST.PROCESS.API.HOOK This field supports the Fedwire.getTagOutputData() method. The Fedwire Class is in the hook.countrymodelbank.usa.Fedwire package which is in USRTGS_FedwireHook.jar shipped with T24. |
| 16 | `FWMF.OFAC.SCREENING.REQD` | `FedwireMsgFormat_OfacScreeningReqd` | TField |  | OFAC Screening Required field to Enable/Disable OFAC Screening. YES - Enable OFAC Screening Null - Disable OFAC Screening |
| 17 | `FWMF.RESERVED.14` | `FedwireMsgFormat_Reserved14` | TField |  |  |
| 18 | `FWMF.RESERVED.13` | `FedwireMsgFormat_Reserved13` | TField |  |  |
| 19 | `FWMF.RESERVED.12` | `FedwireMsgFormat_Reserved12` | TField |  |  |
| 20 | `FWMF.RESERVED.11` | `FedwireMsgFormat_Reserved11` | TField |  |  |
| 21 | `FWMF.RESERVED.10` | `FedwireMsgFormat_Reserved10` | TField |  |  |
| 22 | `FWMF.RESERVED.9` | `FedwireMsgFormat_Reserved9` | TField |  |  |
| 23 | `FWMF.RESERVED.8` | `FedwireMsgFormat_Reserved8` | TField |  |  |
| 24 | `FWMF.RESERVED.7` | `FedwireMsgFormat_Reserved7` | TField |  |  |
| 25 | `FWMF.RESERVED.6` | `FedwireMsgFormat_Reserved6` | TField |  |  |
| 26 | `FWMF.RESERVED.5` | `FedwireMsgFormat_Reserved5` | TField |  |  |
| 27 | `FWMF.RESERVED.4` | `FedwireMsgFormat_Reserved4` | TField |  |  |
| 28 | `FWMF.RESERVED.3` | `FedwireMsgFormat_Reserved3` | TField |  |  |
| 29 | `FWMF.RESERVED.2` | `FedwireMsgFormat_Reserved2` | TField |  |  |
| 30 | `FWMF.RESERVED.1` | `FedwireMsgFormat_Reserved1` | TField |  |  |
| 31 | `FWMF.RECORD.STATUS` | `FedwireMsgFormat_RecordStatus` | String |  |  |
| 32 | `FWMF.CURR.NO` | `FedwireMsgFormat_CurrNo` | String |  |  |
| 33 | `FWMF.INPUTTER` | `FedwireMsgFormat_Inputter` |  |  |  |
| 34 | `FWMF.DATE.TIME` | `FedwireMsgFormat_DateTime` |  |  |  |
| 35 | `FWMF.AUTHORISER` | `FedwireMsgFormat_Authoriser` | String |  |  |
| 36 | `FWMF.CO.CODE` | `FedwireMsgFormat_CoCode` | String |  |  |
| 37 | `FWMF.DEPT.CODE` | `FedwireMsgFormat_DeptCode` | String |  |  |
| 38 | `FWMF.AUDITOR.CODE` | `FedwireMsgFormat_AuditorCode` | String |  |  |
| 39 | `FWMF.AUDIT.DATE.TIME` | `FedwireMsgFormat_AuditDateTime` | String |  |  |
