# EB.MASS.CHANGE.INSTRUCTION — Table Schema

> Source: `INSERTS/I_F.EB.MASS.CHANGE.INSTRUCTION` in `EI_MCI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MCI.DESCRIPTION` | `EbMassChangeInstruction_Description` |  |  |  |
| 2 | `EB.MCI.BUSINESS.OPERATION` | `EbMassChangeInstruction_BusinessOperation` | TField |  | This field links to the application EB.MCI.BUSINESS.OPERATION which allows to define. |
| 3 | `EB.MCI.PROCESSING.DATE` | `EbMassChangeInstruction_ProcessingDate` | TField |  | This field defines the execution date of the Mass Change Instruction. It Can be current or future dated, if the Processing date is future dated, the system will schedule the instruction to be carried out during SOD of that date. |
| 4 | `EB.MCI.EFFECTIVE.DATE` | `EbMassChangeInstruction_EffectiveDate` | TField |  | The field defines the "Effective Date" which the Mass Change Instruction should be executed. It can be Forward Dated or Back Dated as long as it is enabled and supported in the underlying Business Operation. If the Processing Date is in future, the Effective Date can still be less than the Processing Date (this simply means that on the Processing Date, the Mass Changes will be executed back dated) |
| 5 | `EB.MCI.TASK` | `EbMassChangeInstruction_Task` | TField |  | This field specifies the task to be performed by the system at the current stage of mass change instruction process. It includes new, Create List, Edit List, Verify, Execute and Undo. |
| 6 | `EB.MCI.TARGET` | `EbMassChangeInstruction_Target` | TField |  | This field defines T24 Table that will be updated with the Mass Changes. In the case of AA, this will always be AA.ARRANGEMENT. Besides AA.ARRANGEMENT, only CUSTOMER is allowed as the Target T24 Table. |
| 7 | `EB.MCI.TARGET.FIELD` | `EbMassChangeInstruction_TargetField` |  |  |  |
| 8 | `EB.MCI.TARGET.OPERAND` | `EbMassChangeInstruction_TargetOperand` |  |  |  |
| 9 | `EB.MCI.TARGET.VALUE` | `EbMassChangeInstruction_TargetValue` |  |  |  |
| 10 | `EB.MCI.TARGET.EXCLUDE` | `EbMassChangeInstruction_TargetExclude` |  |  |  |
| 11 | `EB.MCI.SOURCE` | `EbMassChangeInstruction_Source` | TField |  | This field specifies the T24 table which will be used as a source for the mass change instruction. Only one of CUSTOMER or ACCOUNT or AA.SDB.BOX is allowed to be the Source T24 Table for now. |
| 12 | `EB.MCI.SOURCE.FIELD` | `EbMassChangeInstruction_SourceField` |  |  |  |
| 13 | `EB.MCI.SOURCE.OPERAND` | `EbMassChangeInstruction_SourceOperand` |  |  |  |
| 14 | `EB.MCI.SOURCE.VALUE` | `EbMassChangeInstruction_SourceValue` |  |  |  |
| 15 | `EB.MCI.SOURCE.EXCLUDE` | `EbMassChangeInstruction_SourceExclude` |  |  |  |
| 16 | `EB.MCI.ATTR.ACTION` | `EbMassChangeInstruction_AttrAction` |  |  |  |
| 17 | `EB.MCI.ATTR.NAME` | `EbMassChangeInstruction_AttrName` |  |  |  |
| 18 | `EB.MCI.ATTR.MV` | `EbMassChangeInstruction_AttrMv` |  |  |  |
| 19 | `EB.MCI.ATTR.SV` | `EbMassChangeInstruction_AttrSv` |  |  |  |
| 20 | `EB.MCI.ATTR.NEW.VALUE` | `EbMassChangeInstruction_AttrNewValue` |  |  |  |
| 21 | `EB.MCI.RESERVED.11` | `EbMassChangeInstruction_Reserved11` |  |  |  |
| 22 | `EB.MCI.ATTR.COND` | `EbMassChangeInstruction_AttrCond` |  |  |  |
| 23 | `EB.MCI.RESERVED.10` | `EbMassChangeInstruction_Reserved10` |  |  |  |
| 24 | `EB.MCI.RESERVED.9` | `EbMassChangeInstruction_Reserved9` |  |  |  |
| 25 | `EB.MCI.ATTR.LOOKUP` | `EbMassChangeInstruction_AttrLookup` |  |  |  |
| 26 | `EB.MCI.RESERVED.8` | `EbMassChangeInstruction_Reserved8` |  |  |  |
| 27 | `EB.MCI.COND.NAME` | `EbMassChangeInstruction_CondName` |  |  |  |
| 28 | `EB.MCI.COND.FIELD` | `EbMassChangeInstruction_CondField` |  |  |  |
| 29 | `EB.MCI.COND.OPERAND` | `EbMassChangeInstruction_CondOperand` |  |  |  |
| 30 | `EB.MCI.COND.VALUE` | `EbMassChangeInstruction_CondValue` |  |  |  |
| 31 | `EB.MCI.RESERVED.7` | `EbMassChangeInstruction_Reserved7` |  |  |  |
| 32 | `EB.MCI.LOOK.NAME` | `EbMassChangeInstruction_LookName` |  |  |  |
| 33 | `EB.MCI.LOOK.FIELD` | `EbMassChangeInstruction_LookField` |  |  |  |
| 34 | `EB.MCI.LOOK.OPERAND` | `EbMassChangeInstruction_LookOperand` |  |  |  |
| 35 | `EB.MCI.LOOK.VALUE` | `EbMassChangeInstruction_LookValue` |  |  |  |
| 36 | `EB.MCI.RESERVED.6` | `EbMassChangeInstruction_Reserved6` |  |  |  |
| 37 | `EB.MCI.TARGET.SELECT.CMD` | `EbMassChangeInstruction_TargetSelectCmd` | TField |  | This field is reserved for future use. |
| 38 | `EB.MCI.SOURCE.SELECT.CMD` | `EbMassChangeInstruction_SourceSelectCmd` | TField |  | This field is reserved for future use. |
| 39 | `EB.MCI.TOTAL.TARGET.SEL` | `EbMassChangeInstruction_TotalTargetSel` | TField |  | This field is reserved for future use. |
| 40 | `EB.MCI.TOTAL.PROCESSED` | `EbMassChangeInstruction_TotalProcessed` | TField |  | This field is reserved for future use. |
| 41 | `EB.MCI.STATUS` | `EbMassChangeInstruction_Status` | TField |  | This field update the status of Mass Change Instruction whether its "Processing..." or "Completed Successfully" |
| 42 | `EB.MCI.TASK.HISTORY` | `EbMassChangeInstruction_TaskHistory` |  |  |  |
| 43 | `EB.MCI.CREATED.BY` | `EbMassChangeInstruction_CreatedBy` | TField |  |  |
| 44 | `EB.MCI.COMPANY.SELECT` | `EbMassChangeInstruction_CompanySelect` | TField |  | This field specifies which records to pickup for processing in multi-company setup. If this field is set to ALL then records will be selected for all books under the current lead company, with the current SMS restrictions being applied to what the user can actually access. If this field is set to NULL then records will be selected for the branch they log in to. |
| 45 | `EB.MCI.RESERVED.3` | `EbMassChangeInstruction_Reserved3` | TField |  | This field is reserved for future use. |
| 46 | `EB.MCI.RESERVED.2` | `EbMassChangeInstruction_Reserved2` | TField |  | This field is reserved for future use. |
| 47 | `EB.MCI.RESERVED.1` | `EbMassChangeInstruction_Reserved1` | TField |  | This field is reserved for future use. |
| 48 | `EB.MCI.LOCAL.REF` | `EbMassChangeInstruction_LocalRef` |  |  |  |
| 49 | `EB.MCI.OVERRIDE` | `EbMassChangeInstruction_Override` |  |  |  |
| 50 | `EB.MCI.RECORD.STATUS` | `EbMassChangeInstruction_RecordStatus` | String |  |  |
| 51 | `EB.MCI.CURR.NO` | `EbMassChangeInstruction_CurrNo` | String |  |  |
| 52 | `EB.MCI.INPUTTER` | `EbMassChangeInstruction_Inputter` |  |  |  |
| 53 | `EB.MCI.DATE.TIME` | `EbMassChangeInstruction_DateTime` |  |  |  |
| 54 | `EB.MCI.AUTHORISER` | `EbMassChangeInstruction_Authoriser` | String |  |  |
| 55 | `EB.MCI.CO.CODE` | `EbMassChangeInstruction_CoCode` | String |  |  |
| 56 | `EB.MCI.DEPT.CODE` | `EbMassChangeInstruction_DeptCode` | String |  |  |
| 57 | `EB.MCI.AUDITOR.CODE` | `EbMassChangeInstruction_AuditorCode` | String |  |  |
| 58 | `EB.MCI.AUDIT.DATE.TIME` | `EbMassChangeInstruction_AuditDateTime` | String |  |  |
