# AM.DYNAMIC.MODEL — Table Schema

> Source: `INSERTS/I_F.AM.DYNAMIC.MODEL` in `AM_DynamicModelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.DYN.DESCRIPTION` | `AmDynamicModel_Description` |  |  |  |
| 2 | `AM.DYN.REFERENCE.CCY` | `AmDynamicModel_ReferenceCcy` | TField |  | The reference currency for the node.currency. Must be a valid currency (i.e. a valid CURRENCY record id). All nodes within this hierarchy must share the same reference currency. Once this has been input it cannot be changed. |
| 3 | `AM.DYN.NODE.NAME` | `AmDynamicModel_NodeName` | TField |  | The initial part of the record id. This is a system field for information only. |
| 4 | `AM.DYN.MODEL.TYPE` | `AmDynamicModel_ModelType` | TField |  | Options could be DYNAMIC or STATIC This field describes type of the model to be generated |
| 5 | `AM.DYN.OVERLAY` | `AmDynamicModel_Overlay` | TField |  | This field contains the ID of AM.SEGMENTED.HIERARCHY by using this field value, model is generated This field cannot be modified, populated from AM.NEW.MODEL |
| 6 | `AM.DYN.VALIDITY.DATE` | `AmDynamicModel_ValidityDate` | TField |  | Date for which this instance of the node is valid. Corresponds to the last part of the record id. This is a system field for information only. |
| 7 | `AM.DYN.START.DATE` | `AmDynamicModel_StartDate` | TField |  | Validity date of the first instance of this node (i.e. the VALIDITY.DATE of the first AM.DYNAMIC.MODEL created which shared the same ROOT.NODE as this record). This is a system field for information only. |
| 8 | `AM.DYN.LAST.CHANGE.DATE` | `AmDynamicModel_LastChangeDate` | TField |  | System date on which this node was last changed. This may differ from the validity date. |
| 9 | `AM.DYN.BUILD.MODEL.FLG` | `AmDynamicModel_BuildModelFlg` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `AM.DYN.RESERVED27` | `AmDynamicModel_Reserved27` | TField |  |  |
| 11 | `AM.DYN.ROOT.NODE` | `AmDynamicModel_RootNode` | TField | Yes | Indicates whether this is a root node or not. This field cannot be set to 'Yes' if this node has any PARENT.NODES. This is a mandatory field. |
| 12 | `AM.DYN.PORTFOLIO.ID` | `AmDynamicModel_PortfolioId` | TField | Yes | Portfolio to which this root node belongs. The rest of the hierarchy under this root node is implicitly linked to this portfolio. This field is mandatory if ROOT.NODE has been set to 'Yes', otherwise must be left blank. It should contain a valid SEC.ACC.MASTER id corresponding to a portfolio which has not already been assigned to a different node (a portfolio can only conform to one model). |
| 13 | `AM.DYN.PORTFOLIO.VALUE` | `AmDynamicModel_PortfolioValue` | TField | Yes | Total value of the portfolio specified in PORTFOLIO.ID which should be invested against this dynamic model hierarchy. Percentage Asset Allocation figures within the Dynamic Model records in this hierarchy will then split down this value to give the recommended values to invest and therefore determine the associated buy/sell orders. Mandatory for root nodes where the VALUE.TYPE has been set as 'Percentage'. Otherwise should be left blank. |
| 14 | `AM.DYN.SEGMENT` | `AmDynamicModel_Segment` | TField | Yes | Segment to which this Dynamic Model record belongs. This is a mandatory field and must contain a valid AM.SEGMENTS id. |
| 15 | `AM.DYN.ASSET.PATH` | `AmDynamicModel_AssetPath` | TField |  | This field contains the hierarchy of the model This field cannot be modified, populated from AM.NEW.MODEL ex: if OVERLAY = EQUITY then this field contain GEN.CASH OR GEN.BOND OR GEN.STOCK, GEN is the MODEL.ID given in AM.NEW.MODEL |
| 16 | `AM.DYN.RESERVED25` | `AmDynamicModel_Reserved25` | TField |  |  |
| 17 | `AM.DYN.MODEL.STATUS` | `AmDynamicModel_ModelStatus` | TField |  | The status of this Dynamic Model record. This will be either 'Active', 'Inactive', 'Error' or 'To Be Validated': Active: This record has been checked by the validation service and is active. Inactive: This record has been deactivated by use of the ACTIVE field. Error: An error has been detected in this record by the validation service. To Be Validated: Notifies the validation service that this record has been input or changed and the model hierarchy needs to be checked by the validation service. This is a system field for information only. |
| 18 | `AM.DYN.REASON` | `AmDynamicModel_Reason` |  |  |  |
| 19 | `AM.DYN.RESERVED24` | `AmDynamicModel_Reserved24` |  |  |  |
| 20 | `AM.DYN.RESERVED23` | `AmDynamicModel_Reserved23` |  |  |  |
| 21 | `AM.DYN.ACTIVE` | `AmDynamicModel_Active` | TField |  | Can be set to 'Yes' or 'No'. If set to 'Yes' this Dynamic Model record is made active (pending check by the validation service). If set to 'No', this record and any parent root nodes will become inactive. |
| 22 | `AM.DYN.VALUE.TYPE` | `AmDynamicModel_ValueType` | TField | Yes | The Node Value Type for this record. This can be either 'Nominal' or 'Percentage' and determines the way in which the individual components (assets) of the model are apportioned. If the Value Type is set to 'Nominal', absolute values are used for each asset, as set in NOMINAL. If the Value Type is set to 'Percentage', percentages as set in PCT.AST.ALOC are used against the individual assets which break down the PORTFOLIO.VALUE as set in the root node. This field is mandatory and all nodes in a hierarchy must share the same Value Type. |
| 23 | `AM.DYN.RESERVED22` | `AmDynamicModel_Reserved22` | TField |  |  |
| 24 | `AM.DYN.RESERVED21` | `AmDynamicModel_Reserved21` | TField |  |  |
| 25 | `AM.DYN.SEGMENT.LABEL` | `AmDynamicModel_SegmentLabel` |  |  |  |
| 26 | `AM.DYN.RESERVED20` | `AmDynamicModel_Reserved20` |  |  |  |
| 27 | `AM.DYN.RESERVED19` | `AmDynamicModel_Reserved19` |  |  |  |
| 28 | `AM.DYN.ASSET.TYPE` | `AmDynamicModel_AssetType` |  |  |  |
| 29 | `AM.DYN.SECURITY` | `AmDynamicModel_Security` |  |  |  |
| 30 | `AM.DYN.CCY` | `AmDynamicModel_Ccy` |  |  |  |
| 31 | `AM.DYN.CHILD.NODE` | `AmDynamicModel_ChildNode` |  |  |  |
| 32 | `AM.DYN.AMEND.PRICE` | `AmDynamicModel_AmendPrice` |  |  |  |
| 33 | `AM.DYN.AMEND.RATE` | `AmDynamicModel_AmendRate` |  |  |  |
| 34 | `AM.DYN.MODEL.PRICE` | `AmDynamicModel_ModelPrice` |  |  |  |
| 35 | `AM.DYN.MODEL.RATE` | `AmDynamicModel_ModelRate` |  |  |  |
| 36 | `AM.DYN.REF.PRICE` | `AmDynamicModel_RefPrice` |  |  |  |
| 37 | `AM.DYN.REF.RATE` | `AmDynamicModel_RefRate` |  |  |  |
| 38 | `AM.DYN.NOMINAL` | `AmDynamicModel_Nominal` |  |  |  |
| 39 | `AM.DYN.PCT.AST.ALOC` | `AmDynamicModel_PctAstAloc` |  |  |  |
| 40 | `AM.DYN.RESERVED12` | `AmDynamicModel_Reserved12` |  |  |  |
| 41 | `AM.DYN.DUMMY.NUM.01` | `AmDynamicModel_DummyNum01` |  |  |  |
| 42 | `AM.DYN.UPPER.TOL` | `AmDynamicModel_UpperTol` |  |  |  |
| 43 | `AM.DYN.LOWER.TOL` | `AmDynamicModel_LowerTol` |  |  |  |
| 44 | `AM.DYN.DUMMY.NUM.02` | `AmDynamicModel_DummyNum02` |  |  |  |
| 45 | `AM.DYN.DUMMY.NUM.03` | `AmDynamicModel_DummyNum03` |  |  |  |
| 46 | `AM.DYN.DUMMY.NUM.04` | `AmDynamicModel_DummyNum04` |  |  |  |
| 47 | `AM.DYN.DUMMY.NUM.05` | `AmDynamicModel_DummyNum05` |  |  |  |
| 48 | `AM.DYN.PARENT.NODES` | `AmDynamicModel_ParentNodes` |  |  |  |
| 49 | `AM.DYN.RESERVED10` | `AmDynamicModel_Reserved10` | TField |  |  |
| 50 | `AM.DYN.RESERVED09` | `AmDynamicModel_Reserved09` | TField |  |  |
| 51 | `AM.DYN.RESERVED08` | `AmDynamicModel_Reserved08` | TField |  |  |
| 52 | `AM.DYN.RESERVED07` | `AmDynamicModel_Reserved07` | TField |  |  |
| 53 | `AM.DYN.RESERVED06` | `AmDynamicModel_Reserved06` | TField |  |  |
| 54 | `AM.DYN.RESERVED05` | `AmDynamicModel_Reserved05` | TField |  |  |
| 55 | `AM.DYN.RESERVED04` | `AmDynamicModel_Reserved04` | TField |  |  |
| 56 | `AM.DYN.RESERVED03` | `AmDynamicModel_Reserved03` | TField |  |  |
| 57 | `AM.DYN.RESERVED02` | `AmDynamicModel_Reserved02` | TField |  |  |
| 58 | `AM.DYN.RESERVED01` | `AmDynamicModel_Reserved01` | TField |  |  |
| 59 | `AM.DYN.LOCAL.REF` | `AmDynamicModel_LocalRef` |  |  |  |
| 60 | `AM.DYN.OVERRIDE` | `AmDynamicModel_Override` |  |  |  |
| 61 | `AM.DYN.RECORD.STATUS` | `AmDynamicModel_RecordStatus` | String |  |  |
| 62 | `AM.DYN.CURR.NO` | `AmDynamicModel_CurrNo` | String |  |  |
| 63 | `AM.DYN.INPUTTER` | `AmDynamicModel_Inputter` |  |  |  |
| 64 | `AM.DYN.DATE.TIME` | `AmDynamicModel_DateTime` |  |  |  |
| 65 | `AM.DYN.AUTHORISER` | `AmDynamicModel_Authoriser` | String |  |  |
| 66 | `AM.DYN.CO.CODE` | `AmDynamicModel_CoCode` | String |  |  |
| 67 | `AM.DYN.DEPT.CODE` | `AmDynamicModel_DeptCode` | String |  |  |
| 68 | `AM.DYN.AUDITOR.CODE` | `AmDynamicModel_AuditorCode` | String |  |  |
| 69 | `AM.DYN.AUDIT.DATE.TIME` | `AmDynamicModel_AuditDateTime` | String |  |  |
