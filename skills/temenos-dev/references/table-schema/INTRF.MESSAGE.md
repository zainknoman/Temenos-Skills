# INTRF.MESSAGE — Table Schema

> Source: `INSERTS/I_F.INTRF.MESSAGE` in `ATMFRM_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INTRF.MSG.DESCRIPTION` | `IntrfMessage_Description` |  |  |  |
| 2 | `INTRF.MSG.TRACK.FILE.NAME` | `IntrfMessage_TrackFileName` | TField |  | Routine attached to this field will be called in the pre-processing routine to perform any additional processing on the ISO message before being processed by the pre-processing routine attached to OFS |
| 3 | `INTRF.MSG.INTRF.PRE.RTN` | `IntrfMessage_IntrfPreRtn` | TField |  | Routine that modifies the incoming ISO request. It receives incoming ISO request as first argument and returns the modified ISO request as second argument. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record INTRF.MSG.PRE.RTN.HOOK. This field supports the AtmMessageLifecycle.modifyRequestMessage() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 4 | `INTRF.MSG.MAPPING.ID` | `IntrfMessage_MappingId` |  |  |  |
| 5 | `INTRF.MSG.INTRF.HEAD.NAME` | `IntrfMessage_IntrfHeadName` |  |  |  |
| 6 | `INTRF.MSG.INTRF.HEAD.DELIM` | `IntrfMessage_IntrfHeadDelim` |  |  |  |
| 7 | `INTRF.MSG.INTRF.HEAD.POS` | `IntrfMessage_IntrfHeadPos` |  |  |  |
| 8 | `INTRF.MSG.INTRF.HEAD.LEN` | `IntrfMessage_IntrfHeadLen` |  |  |  |
| 9 | `INTRF.MSG.INTRF.HEAD.TYPE` | `IntrfMessage_IntrfHeadType` |  |  |  |
| 10 | `INTRF.MSG.INTRF.HEAD.S.M` | `IntrfMessage_IntrfHeadSM` |  |  |  |
| 11 | `INTRF.MSG.INTRF.HEAD.MAND` | `IntrfMessage_IntrfHeadMand` |  |  |  |
| 12 | `INTRF.MSG.INTRF.FLD.NAME` | `IntrfMessage_IntrfFldName` |  |  |  |
| 13 | `INTRF.MSG.INTRF.FLD.DELIM` | `IntrfMessage_IntrfFldDelim` |  |  |  |
| 14 | `INTRF.MSG.INTRF.FLD.POS` | `IntrfMessage_IntrfFldPos` |  |  |  |
| 15 | `INTRF.MSG.INTRF.FLD.LEN` | `IntrfMessage_IntrfFldLen` |  |  |  |
| 16 | `INTRF.MSG.INTRF.FLD.TYPE` | `IntrfMessage_IntrfFldType` |  |  |  |
| 17 | `INTRF.MSG.INTRF.FLD.S.M` | `IntrfMessage_IntrfFldSM` |  |  |  |
| 18 | `INTRF.MSG.INTRF.FLD.MAND` | `IntrfMessage_IntrfFldMand` |  |  |  |
| 19 | `INTRF.MSG.TXN.FIELD.POS` | `IntrfMessage_TxnFieldPos` |  |  |  |
| 20 | `INTRF.MSG.MV.RESERVED.5` | `IntrfMessage_MvReserved5` |  |  |  |
| 21 | `INTRF.MSG.MV.RESERVED.4` | `IntrfMessage_MvReserved4` |  |  |  |
| 22 | `INTRF.MSG.MV.RESERVED.3` | `IntrfMessage_MvReserved3` |  |  |  |
| 23 | `INTRF.MSG.MV.RESERVED.2` | `IntrfMessage_MvReserved2` |  |  |  |
| 24 | `INTRF.MSG.MV.RESERVED.1` | `IntrfMessage_MvReserved1` |  |  |  |
| 25 | `INTRF.MSG.INTRF.POST.RTN` | `IntrfMessage_IntrfPostRtn` | TField |  | This field hold routine name. Routine attached here should have one argument value passed. Customized hook routines can be attached here for post-mapping validations. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record INTRF.MSG.POST.RTN.HOOK. This field supports the AtmMessageLifecycle.updateResponseMessage() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 26 | `INTRF.MSG.MSG.FORMAT` | `IntrfMessage_MsgFormat` | TField |  | Indicates which type of transaction for which the record is created. i.e. ISO_BASE24_PHOENIX |
| 27 | `INTRF.MSG.WARMUP.API` | `IntrfMessage_WarmupApi` | TField |  | This field holds the routine name. Routine attached here should have two arguments (Incoming ISO message, Outgoing Warmup.Flag). If Warup flag is set by the API, then the ISO message will be treated like a WARMUP request and hence will not be processed by IN.MSG.RTN and OUT.MSG.RTN. |
| 28 | `INTRF.MSG.RESERVED.8` | `IntrfMessage_Reserved8` | TField |  |  |
| 29 | `INTRF.MSG.RESERVED.7` | `IntrfMessage_Reserved7` | TField |  |  |
| 30 | `INTRF.MSG.RESERVED.6` | `IntrfMessage_Reserved6` | TField |  |  |
| 31 | `INTRF.MSG.LOCAL.REF` | `IntrfMessage_LocalRef` |  |  |  |
| 32 | `INTRF.MSG.RESERVED.5` | `IntrfMessage_Reserved5` | TField |  |  |
| 33 | `INTRF.MSG.RESERVED.4` | `IntrfMessage_Reserved4` | TField |  |  |
| 34 | `INTRF.MSG.RESERVED.3` | `IntrfMessage_Reserved3` | TField |  |  |
| 35 | `INTRF.MSG.RESERVED.2` | `IntrfMessage_Reserved2` | TField |  |  |
| 36 | `INTRF.MSG.RESERVED.1` | `IntrfMessage_Reserved1` | TField |  |  |
| 37 | `INTRF.MSG.RECORD.STATUS` | `IntrfMessage_RecordStatus` | String |  |  |
| 38 | `INTRF.MSG.CURR.NO` | `IntrfMessage_CurrNo` | String |  |  |
| 39 | `INTRF.MSG.INPUTTER` | `IntrfMessage_Inputter` |  |  |  |
| 40 | `INTRF.MSG.DATE.TIME` | `IntrfMessage_DateTime` |  |  |  |
| 41 | `INTRF.MSG.AUTHORISER` | `IntrfMessage_Authoriser` | String |  |  |
| 42 | `INTRF.MSG.CO.CODE` | `IntrfMessage_CoCode` | String |  |  |
| 43 | `INTRF.MSG.DEPT.CODE` | `IntrfMessage_DeptCode` | String |  |  |
| 44 | `INTRF.MSG.AUDITOR.CODE` | `IntrfMessage_AuditorCode` | String |  |  |
| 45 | `INTRF.MSG.AUDIT.DATE.TIME` | `IntrfMessage_AuditDateTime` | String |  |  |
