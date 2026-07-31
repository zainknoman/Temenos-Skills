# DX.DIARY — Table Schema

> Source: `INSERTS/I_F.DX.DIARY` in `DX_CorporateActions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.DIA.SECURITY.NO` | `DxDiary_SecurityNo` | TField |  | The underyling security for the DX.CONTRACT.MASTER record identified in CONTRACT.CODE. This needs to be a valid security record that exists in the Security Master Validation Rules: Up to 12 numerical characters This is a Nochange Field |
| 2 | `DX.DIA.CONTRACT.CODE` | `DxDiary_ContractCode` | TField |  | Contract affected by this corporate action. This needs to be a valid contract record that exists in DX.CONTRACT.MASTER Validation Rules: Up to 12 numerical characters Input must exist on DX.CONTRACT.MASTER Application. |
| 3 | `DX.DIA.CONTRACT.SIZE` | `DxDiary_ContractSize` | TField |  | The nominal or Trading unit of the contract, specified according to the contract specifications set by the relative Exchange System generated field. |
| 4 | `DX.DIA.CURRENCY` | `DxDiary_Currency` | TField |  | This is the contract currency as defined in DX.CONTRACT.MASTER System generated field. |
| 5 | `DX.DIA.NARRATIVE` | `DxDiary_Narrative` |  |  |  |
| 6 | `DX.DIA.EVENT.TYPE` | `DxDiary_EventType` | TField |  | Type of Corporate action to be performed. Validation Rules: Must be a valid DIARY.TYPE record. Nochange Field |
| 7 | `DX.DIA.EX.DATE` | `DxDiary_ExDate` | TField |  | This is the Ex Dividend Date -the date on which Derivative entitlements take effect. Validation Rules: Valid Date in Standard T24 Date Format Input field |
| 8 | `DX.DIA.PAY.DATE` | `DxDiary_PayDate` | TField |  | This field is currently not used. This is a valid Date in Standard T24 Date Format Input field |
| 9 | `DX.DIA.VALUE.DATE` | `DxDiary_ValueDate` | TField |  | Not currently used. |
| 10 | `DX.DIA.REPLY.BY.DATE` | `DxDiary_ReplyByDate` | TField |  | This field is currently not used. |
| 11 | `DX.DIA.END.MATURITY.DATE` | `DxDiary_EndMaturityDate` | TField |  | Ending maturity date for contract consideration. Contracts with a maturity after this date will be excluded from entitlements Validation Rules: This is a Valid Date in Standard T24 Date Format Input field |
| 12 | `DX.DIA.DESCRIPTION` | `DxDiary_Description` | TField |  | Description of the diary event. |
| 13 | `DX.DIA.OLD.RATIO` | `DxDiary_OldRatio` | TField |  | This is number of old shares for the number of new shares entered in the next field to build up a new for old ratio Validation Rules: This is a Input Field This is Standard T24 Date Format |
| 14 | `DX.DIA.NEW.RATIO` | `DxDiary_NewRatio` | TField |  | This is the number of new shares for the number of old shares entered in the above field to build up a new for old ratio Validation Rules: Upto 16 integers Input field |
| 15 | `DX.DIA.OLD.STR.RATIO` | `DxDiary_OldStrRatio` | TField |  | This is the old strike in ratio of old to new strike price Validation Rules: Upto 15 integers Input field |
| 16 | `DX.DIA.NEW.STR.RATIO` | `DxDiary_NewStrRatio` | TField |  | This is new strike in ratio of old to new strike price Validation Rules: Upto 15 integers Input field |
| 17 | `DX.DIA.OLD.LOT.RATIO` | `DxDiary_OldLotRatio` | TField |  | This field shows the number of old option lots for the number of new option lots entered in the below field to build up a new for old ratio Validation Rules: Upto 15 integers Input field |
| 18 | `DX.DIA.NEW.LOT.RATIO` | `DxDiary_NewLotRatio` | TField |  | This field shows the number of new option lots for the number of old option lots entered in the below field to build up a new for old ratio Validation Rules: Upto 16 integers Input field |
| 19 | `DX.DIA.NEW.SEC.NO` | `DxDiary_NewSecNo` | TField |  | Validation Rules: Default to SECURITY.NO Upto 12 characters Input field. Must be a valid Security. Master record |
| 20 | `DX.DIA.NEW.CONT.CODE` | `DxDiary_NewContCode` | TField |  | New Option Contract Code Validation Rules: Upto 12 characters Input field. Must be a valid DX.Contract.Master record. |
| 21 | `DX.DIA.NEW.CONT.SIZE` | `DxDiary_NewContSize` | TField |  | Holds the new contract size after the occurrence of a corporate action. System generated field. |
| 22 | `DX.DIA.OLD.PRICE.RATIO` | `DxDiary_OldPriceRatio` | TField |  | This field accepts user input of old price ratio on Corporate actions. This forms the basis for calculation of New price to be updated in DX. ENTITLEMENT Validation rules |
| 23 | `DX.DIA.NEW.PRICE.RATIO` | `DxDiary_NewPriceRatio` | TField |  | This field accepts user input of new price ratio on Corporate actions. This forms the basis for calculation of New price to be updated in DX. ENTITLEMENT Validation rules : * Accepts input of upto 8 integers and 7 decimals |
| 24 | `DX.DIA.LAST.VALID.DATE` | `DxDiary_LastValidDate` | TField |  | The last date that the old contract can be traded |
| 25 | `DX.DIA.RESERVED13` | `DxDiary_Reserved13` |  |  |  |
| 26 | `DX.DIA.RESERVED12` | `DxDiary_Reserved12` | TField |  |  |
| 27 | `DX.DIA.AUTO.UPDATE` | `DxDiary_AutoUpdate` | TField |  | This field is held for information purposes only. YES/NO indicating update from an external source Validation Rules: Upto 3 characters, Input field. Can be either YES or NO. |
| 28 | `DX.DIA.SOURCE` | `DxDiary_Source` | TField |  | This field is for information purposes only. Indicates source of update. based on setting of AUTO.UPDATE - if AUTO.UPDATE is 'Yes', then defaults in 'EXTERNAL', otherwise 'MANUAL. System generated field only. |
| 29 | `DX.DIA.RERUN` | `DxDiary_Rerun` | TField |  | YES/NO field allowing a user to regenerate the DX.ENTITLEMENT records for a DX.DIARY. Validation Rules: Upto 3 characters, Input field Can be either YES or NO |
| 30 | `DX.DIA.ENTITLEMENT.FLAG` | `DxDiary_EntitlementFlag` | TField |  | This field indicates whether DX.ENTITLEMENT records have been generated or not. Set to 'Yes' if they have been generated. System updated field. |
| 31 | `DX.DIA.EVENT.STATUS` | `DxDiary_EventStatus` | TField |  | Status of the diary event - PENDING or AUTHORISED System generated field. |
| 32 | `DX.DIA.CONFIRM.REQ` | `DxDiary_ConfirmReq` | TField |  | This field is currently not used. |
| 33 | `DX.DIA.ADVICE.TYPE` | `DxDiary_AdviceType` | TField |  | This field is currently not used. |
| 34 | `DX.DIA.ADVICE.FORMAT` | `DxDiary_AdviceFormat` | TField |  | This field is currently not used. |
| 35 | `DX.DIA.PRE.ADVICE.REQ` | `DxDiary_PreAdviceReq` | TField |  | This field is currently not used. |
| 36 | `DX.DIA.DIA.AUTO.AUTH.DAT` | `DxDiary_DiaAutoAuthDat` | TField |  | This field is currently not used. |
| 37 | `DX.DIA.RESERVED11` | `DxDiary_Reserved11` | TField |  |  |
| 38 | `DX.DIA.ENT.AUTO.AUTH.DAT` | `DxDiary_EntAutoAuthDat` | TField |  | This field is currently not used. |
| 39 | `DX.DIA.ENTL.CREATED` | `DxDiary_EntlCreated` | TField |  | Number of created entitlements System generated field. |
| 40 | `DX.DIA.ENTL.AUTHORISED` | `DxDiary_EntlAuthorised` | TField |  | Number of authorised entitlements System generated field. |
| 41 | `DX.DIA.RESERVED5` | `DxDiary_Reserved5` | TField |  |  |
| 42 | `DX.DIA.ROUNDING` | `DxDiary_Rounding` | TField |  | This field specifies the type of rounding method to be applied, which can be one of the following: STANDARD - It will round either upwards or downwards whichever is nearer integer, to the required number of decimal places UP - DOWN - It will round downwards to the required number of decimal places Validation Rules: Defaults from DX.CONTRACT.MASTER, but can be amended manually |
| 43 | `DX.DIA.RND.FACTOR` | `DxDiary_RndFactor` | TField | No | Rounding factor is an optional input with the following restrictions on the integer and fractional part : 1. The fraction is restricted to the Strike price scale i.e. &lt; scale factor 2. Unless the Price Scale factor is 100, integer part cannot be used Validation Rules: Defaults from DX.CONTRACT.MASTER but can be amended manually |
| 44 | `DX.DIA.CREATE.CONT.Y.N` | `DxDiary_CreateContYN` | TField |  | This field specifies whether a new contract master record needs to be created or not. If set to 'Yes', the old contract is given the LAST.VALID.DATE as set here and a new contract is created, amended as per the corporate action. If set to 'No', the existing contract is amended as per the corporate action. Validation Rules: Valid inputs being Y or N, default being N |
| 45 | `DX.DIA.NEW.CONT.MNE` | `DxDiary_NewContMne` | TField |  | This field specifies the mnemonic of the new Contract master record that will be created. Validation Rules: Upto 10 alphanumeric characters |
| 46 | `DX.DIA.NEW.EXCH.CODE` | `DxDiary_NewExchCode` | TField |  | This field specifies the Exchange code of the new Contract master record created by corporate action Validation Rules: Upto 10 numeric values |
| 47 | `DX.DIA.CREATE.ENT.ONLINE` | `DxDiary_CreateEntOnline` | TField |  | Specifies whether to create ENTITLEMENT record Online or during COB. Holds values YES or NO. If set to 'Yes', the entitlements are set online. |
| 48 | `DX.DIA.EXOTIC.FIELD.NAME` | `DxDiary_ExoticFieldName` |  |  |  |
| 49 | `DX.DIA.EXOTIC.OLD.RATIO` | `DxDiary_ExoticOldRatio` |  |  |  |
| 50 | `DX.DIA.EXOTIC.NEW.RATIO` | `DxDiary_ExoticNewRatio` |  |  |  |
| 51 | `DX.DIA.RESERVED1` | `DxDiary_Reserved1` | TField |  |  |
| 52 | `DX.DIA.LOCAL.REF` | `DxDiary_LocalRef` |  |  |  |
| 53 | `DX.DIA.OVERRIDE` | `DxDiary_Override` |  |  |  |
| 54 | `DX.DIA.RECORD.STATUS` | `DxDiary_RecordStatus` | String |  |  |
| 55 | `DX.DIA.CURR.NO` | `DxDiary_CurrNo` | String |  |  |
| 56 | `DX.DIA.INPUTTER` | `DxDiary_Inputter` |  |  |  |
| 57 | `DX.DIA.DATE.TIME` | `DxDiary_DateTime` |  |  |  |
| 58 | `DX.DIA.AUTHORISER` | `DxDiary_Authoriser` | String |  |  |
| 59 | `DX.DIA.CO.CODE` | `DxDiary_CoCode` | String |  |  |
| 60 | `DX.DIA.DEPT.CODE` | `DxDiary_DeptCode` | String |  |  |
| 61 | `DX.DIA.AUDITOR.CODE` | `DxDiary_AuditorCode` | String |  |  |
| 62 | `DX.DIA.AUDIT.DATE.TIME` | `DxDiary_AuditDateTime` | String |  |  |
