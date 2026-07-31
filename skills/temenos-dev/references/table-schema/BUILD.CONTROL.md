# BUILD.CONTROL — Table Schema

> Source: `INSERTS/I_F.BUILD.CONTROL` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BCON.DESC` | `BuildControl_Desc` |  |  |  |
| 2 | `BCON.MNEMONIC` | `BuildControl_Mnemonic` | TField |  |  |
| 3 | `BCON.ACTION` | `BuildControl_Action` | TField |  |  |
| 4 | `BCON.BCON.PRODUCT` | `BuildControl_BconProduct` | TField |  |  |
| 5 | `BCON.SAVE.PATH` | `BuildControl_SavePath` | TField |  |  |
| 6 | `BCON.RELEASE.PATH` | `BuildControl_ReleasePath` | TField |  |  |
| 7 | `BCON.PROGRAM.BP` | `BuildControl_ProgramBp` |  |  |  |
| 8 | `BCON.SELECT.CMD` | `BuildControl_SelectCmd` |  |  |  |
| 9 | `BCON.MV.RESERVED.9` | `BuildControl_MvReserved9` |  |  |  |
| 10 | `BCON.RELEASE.BP` | `BuildControl_ReleaseBp` |  |  |  |
| 11 | `BCON.JBCDEV.LIB` | `BuildControl_JbcdevLib` |  |  |  |
| 12 | `BCON.JBCDEV.BIN` | `BuildControl_JbcdevBin` |  |  |  |
| 13 | `BCON.OBJ.NAME` | `BuildControl_ObjName` | TField |  |  |
| 14 | `BCON.DEPENDENCY` | `BuildControl_Dependency` |  |  |  |
| 15 | `BCON.OUR.REFERENCE` | `BuildControl_OurReference` |  |  |  |
| 16 | `BCON.THEIR.REFERENCE` | `BuildControl_TheirReference` |  |  |  |
| 17 | `BCON.ISSUE.DESC` | `BuildControl_IssueDesc` |  |  |  |
| 18 | `BCON.OFS.SOURCE.ID` | `BuildControl_OfsSourceId` | TField |  |  |
| 19 | `BCON.DL.DEFINE` | `BuildControl_DlDefine` |  |  |  |
| 20 | `BCON.FROM.COMPANY` | `BuildControl_FromCompany` |  |  |  |
| 21 | `BCON.TO.COMPANY` | `BuildControl_ToCompany` |  |  |  |
| 22 | `BCON.LOC.REF.TABLE` | `BuildControl_LocRefTable` |  |  |  |
| 23 | `BCON.LOCAL.TABLE` | `BuildControl_LocalTable` |  |  |  |
| 24 | `BCON.TABLE.ASSOC` | `BuildControl_TableAssoc` |  |  |  |
| 25 | `BCON.SS.APPL.NAME` | `BuildControl_SsApplName` |  |  |  |
| 26 | `BCON.USR.FIELD.NAME` | `BuildControl_UsrFieldName` |  |  |  |
| 27 | `BCON.USR.TYPE` | `BuildControl_UsrType` |  |  |  |
| 28 | `BCON.USR.FIELD.NO` | `BuildControl_UsrFieldNo` |  |  |  |
| 29 | `BCON.USR.VAL.PROG` | `BuildControl_UsrValProg` |  |  |  |
| 30 | `BCON.USR.CONVERSION` | `BuildControl_UsrConversion` |  |  |  |
| 31 | `BCON.USR.DISPLAY.FMT` | `BuildControl_UsrDisplayFmt` |  |  |  |
| 32 | `BCON.USR.ALT.INDEX` | `BuildControl_UsrAltIndex` |  |  |  |
| 33 | `BCON.USR.IDX.FILE` | `BuildControl_UsrIdxFile` |  |  |  |
| 34 | `BCON.USR.INDEX.NULLS` | `BuildControl_UsrIndexNulls` |  |  |  |
| 35 | `BCON.USR.SINGLE.MULT` | `BuildControl_UsrSingleMult` |  |  |  |
| 36 | `BCON.USR.LANG.FIELD` | `BuildControl_UsrLangField` |  |  |  |
| 37 | `BCON.USR.CNV.TYPE` | `BuildControl_UsrCnvType` |  |  |  |
| 38 | `BCON.USR.REL.FILE` | `BuildControl_UsrRelFile` |  |  |  |
| 39 | `BCON.SS.RESVD.39` | `BuildControl_SsResvd39` |  |  |  |
| 40 | `BCON.SS.RESVD.40` | `BuildControl_SsResvd40` |  |  |  |
| 41 | `BCON.SS.RESVD.41` | `BuildControl_SsResvd41` |  |  |  |
| 42 | `BCON.SS.RESVD.42` | `BuildControl_SsResvd42` |  |  |  |
| 43 | `BCON.BUILD.NEW.DICT` | `BuildControl_BuildNewDict` |  |  |  |
| 44 | `BCON.WS.FILE.NAME` | `BuildControl_WsFileName` |  |  |  |
| 45 | `BCON.WS.RECORD.NAME` | `BuildControl_WsRecordName` |  |  |  |
| 46 | `BCON.GEN.INSTALL.DOC` | `BuildControl_GenInstallDoc` | TField |  |  |
| 47 | `BCON.RESERVED.47` | `BuildControl_Reserved47` | TField |  |  |
| 48 | `BCON.RESERVED.48` | `BuildControl_Reserved48` | TField |  |  |
| 49 | `BCON.UPD.TABLE.NAME` | `BuildControl_UpdTableName` |  |  |  |
| 50 | `BCON.UPD.COMPANY` | `BuildControl_UpdCompany` |  |  |  |
| 51 | `BCON.UPD.RECORD` | `BuildControl_UpdRecord` |  |  |  |
| 52 | `BCON.UPD.FIELD` | `BuildControl_UpdField` |  |  |  |
| 53 | `BCON.SV.RESVD.53` | `BuildControl_SvResvd53` |  |  |  |
| 54 | `BCON.SV.RESVD.54` | `BuildControl_SvResvd54` |  |  |  |
| 55 | `BCON.SV.RESVD.55` | `BuildControl_SvResvd55` |  |  |  |
| 56 | `BCON.UPD.VALUE` | `BuildControl_UpdValue` |  |  |  |
| 57 | `BCON.MV.RESVD.57` | `BuildControl_MvResvd57` |  |  |  |
| 58 | `BCON.MV.RESVD.58` | `BuildControl_MvResvd58` |  |  |  |
| 59 | `BCON.MV.RESVD.59` | `BuildControl_MvResvd59` |  |  |  |
| 60 | `BCON.RESERVED.60` | `BuildControl_Reserved60` | TField |  |  |
| 61 | `BCON.RESERVED.61` | `BuildControl_Reserved61` | TField |  |  |
| 62 | `BCON.RESERVED.62` | `BuildControl_Reserved62` | TField |  |  |
| 63 | `BCON.RESERVED.63` | `BuildControl_Reserved63` | TField |  |  |
| 64 | `BCON.RESERVED.64` | `BuildControl_Reserved64` | TField |  |  |
| 65 | `BCON.RESERVED.65` | `BuildControl_Reserved65` | TField |  |  |
| 66 | `BCON.RESERVED.66` | `BuildControl_Reserved66` | TField |  |  |
| 67 | `BCON.RESERVED.67` | `BuildControl_Reserved67` | TField |  |  |
| 68 | `BCON.RESERVED.68` | `BuildControl_Reserved68` | TField |  |  |
| 69 | `BCON.FILE.VOC.ID` | `BuildControl_FileVocId` |  |  |  |
| 70 | `BCON.FILES.TO.CREATE` | `BuildControl_FilesToCreate` |  |  |  |
| 71 | `BCON.SHELL.CMD` | `BuildControl_ShellCmd` |  |  |  |
| 72 | `BCON.RELEASE.ORDER` | `BuildControl_ReleaseOrder` |  |  |  |
| 73 | `BCON.AUTH.SPL.INSTR` | `BuildControl_AuthSplInstr` | TField |  |  |
| 74 | `BCON.CREATE.LIB` | `BuildControl_CreateLib` | TField |  |  |
| 75 | `BCON.CREATE.BIN` | `BuildControl_CreateBin` | TField |  |  |
| 76 | `BCON.CREATE.REL.BP` | `BuildControl_CreateRelBp` | TField |  |  |
| 77 | `BCON.DL.SAVE.PATH` | `BuildControl_DlSavePath` | TField |  |  |
| 78 | `BCON.DL.RESTORE.PATH` | `BuildControl_DlRestorePath` | TField |  |  |
| 79 | `BCON.PROGRAM.OS` | `BuildControl_ProgramOs` | TField |  |  |
| 80 | `BCON.CLR.PROCESS.LOG` | `BuildControl_ClrProcessLog` | TField |  |  |
| 81 | `BCON.ACTIVITY` | `BuildControl_Activity` |  |  |  |
| 82 | `BCON.PROCESS.INFO` | `BuildControl_ProcessInfo` |  |  |  |
| 83 | `BCON.PROCESS.ERR` | `BuildControl_ProcessErr` |  |  |  |
| 84 | `BCON.SAVED.DATE` | `BuildControl_SavedDate` |  |  |  |
| 85 | `BCON.SAVED.VERSION` | `BuildControl_SavedVersion` |  |  |  |
| 86 | `BCON.SAVED.USER` | `BuildControl_SavedUser` |  |  |  |
| 87 | `BCON.RELEASE.DATE` | `BuildControl_ReleaseDate` |  |  |  |
| 88 | `BCON.RELEASE.VERSION` | `BuildControl_ReleaseVersion` |  |  |  |
| 89 | `BCON.RELEASE.USER` | `BuildControl_ReleaseUser` |  |  |  |
| 90 | `BCON.REL.STAGE` | `BuildControl_RelStage` |  |  |  |
| 91 | `BCON.VIEW.REPORT` | `BuildControl_ViewReport` | TField |  |  |
| 92 | `BCON.REMOVE.SOURCE` | `BuildControl_RemoveSource` | TField |  |  |
| 93 | `BCON.PRE.INSTALL` | `BuildControl_PreInstall` |  |  |  |
| 94 | `BCON.POST.INSTALL` | `BuildControl_PostInstall` |  |  |  |
| 95 | `BCON.DOC.ID.NEW` | `BuildControl_DocIdNew` | TField |  |  |
| 96 | `BCON.ADDNL.SYS.REQ` | `BuildControl_AddnlSysReq` |  |  |  |
| 97 | `BCON.RESERVED.97` | `BuildControl_Reserved97` | TField |  |  |
| 98 | `BCON.RESERVED.98` | `BuildControl_Reserved98` | TField |  |  |
| 99 | `BCON.RESERVED.99` | `BuildControl_Reserved99` | TField |  |  |
| 100 | `BCON.RESERVED.100` | `BuildControl_Reserved100` | TField |  |  |
| 101 | `BCON.RESERVED.101` | `BuildControl_Reserved101` | TField |  |  |
| 102 | `BCON.BCON.FUNCTIONALITY` | `BuildControl_BconFunctionality` | TField |  |  |
| 103 | `BCON.DEL.OTHER.COMP.RECS` | `BuildControl_DelOtherCompRecs` | TField |  |  |
| 104 | `BCON.LOCAL.REF` | `BuildControl_LocalRef` |  |  |  |
| 105 | `BCON.RECORD.STATUS` | `BuildControl_RecordStatus` | String |  |  |
| 106 | `BCON.CURR.NO` | `BuildControl_CurrNo` | String |  |  |
| 107 | `BCON.INPUTTER` | `BuildControl_Inputter` |  |  |  |
| 108 | `BCON.DATE.TIME` | `BuildControl_DateTime` |  |  |  |
| 109 | `BCON.AUTHORISER` | `BuildControl_Authoriser` | String |  |  |
| 110 | `BCON.CO.CODE` | `BuildControl_CoCode` | String |  |  |
| 111 | `BCON.DEPT.CODE` | `BuildControl_DeptCode` | String |  |  |
| 112 | `BCON.AUDITOR.CODE` | `BuildControl_AuditorCode` | String |  |  |
| 113 | `BCON.AUDIT.DATE.TIME` | `BuildControl_AuditDateTime` | String |  |  |
