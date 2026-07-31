# SY.ENTITLEMENT — Table Schema

> Source: `INSERTS/I_F.SY.ENTITLEMENT` in `SY_CorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.ENT.SY.AC.DE.ID` | `SyEntitlement_SyAcDeId` | TField |  |  |
| 2 | `SY.ENT.SY.DIARY` | `SyEntitlement_SyDiary` | TField |  |  |
| 3 | `SY.ENT.TRADE.DATE` | `SyEntitlement_TradeDate` | TField |  |  |
| 4 | `SY.ENT.ELEMENT` | `SyEntitlement_Element` |  |  |  |
| 5 | `SY.ENT.ELEMENT.NEW.VALUE` | `SyEntitlement_ElementNewValue` |  |  |  |
| 6 | `SY.ENT.ELEMENT.OLD.RATIO` | `SyEntitlement_ElementOldRatio` |  |  |  |
| 7 | `SY.ENT.ELEMENT.NEW.RATIO` | `SyEntitlement_ElementNewRatio` |  |  |  |
| 8 | `SY.ENT.TRANS.VALUE` | `SyEntitlement_TransValue` |  |  |  |
| 9 | `SY.ENT.NEW.TRANS.VALUE` | `SyEntitlement_NewTransValue` |  |  |  |
| 10 | `SY.ENT.RESERVED.15` | `SyEntitlement_Reserved15` |  |  |  |
| 11 | `SY.ENT.RESERVED.14` | `SyEntitlement_Reserved14` |  |  |  |
| 12 | `SY.ENT.RESERVED.13` | `SyEntitlement_Reserved13` |  |  |  |
| 13 | `SY.ENT.RESERVED.12` | `SyEntitlement_Reserved12` |  |  |  |
| 14 | `SY.ENT.RESERVED.11` | `SyEntitlement_Reserved11` |  |  |  |
| 15 | `SY.ENT.NEW.SECURITY` | `SyEntitlement_NewSecurity` | TField |  |  |
| 16 | `SY.ENT.ACTIVITY.CODE` | `SyEntitlement_ActivityCode` | TField |  |  |
| 17 | `SY.ENT.MESSAGE.REF` | `SyEntitlement_MessageRef` | TField |  |  |
| 18 | `SY.ENT.RESERVED.8` | `SyEntitlement_Reserved8` | TField |  |  |
| 19 | `SY.ENT.RESERVED.7` | `SyEntitlement_Reserved7` | TField |  |  |
| 20 | `SY.ENT.RESERVED.6` | `SyEntitlement_Reserved6` | TField |  |  |
| 21 | `SY.ENT.RESERVED.5` | `SyEntitlement_Reserved5` | TField |  |  |
| 22 | `SY.ENT.RESERVED.4` | `SyEntitlement_Reserved4` | TField |  |  |
| 23 | `SY.ENT.RESERVED.3` | `SyEntitlement_Reserved3` | TField |  |  |
| 24 | `SY.ENT.RESERVED.2` | `SyEntitlement_Reserved2` | TField |  |  |
| 25 | `SY.ENT.RESERVED.1` | `SyEntitlement_Reserved1` | TField |  |  |
| 26 | `SY.ENT.LOCAL.REF` | `SyEntitlement_LocalRef` |  |  |  |
| 27 | `SY.ENT.OVERRIDE` | `SyEntitlement_Override` |  |  |  |
| 28 | `SY.ENT.RECORD.STATUS` | `SyEntitlement_RecordStatus` | String |  |  |
| 29 | `SY.ENT.CURR.NO` | `SyEntitlement_CurrNo` | String |  |  |
| 30 | `SY.ENT.INPUTTER` | `SyEntitlement_Inputter` |  |  |  |
| 31 | `SY.ENT.DATE.TIME` | `SyEntitlement_DateTime` |  |  |  |
| 32 | `SY.ENT.AUTHORISER` | `SyEntitlement_Authoriser` | String |  |  |
| 33 | `SY.ENT.CO.CODE` | `SyEntitlement_CoCode` | String |  |  |
| 34 | `SY.ENT.DEPT.CODE` | `SyEntitlement_DeptCode` | String |  |  |
| 35 | `SY.ENT.AUDITOR.CODE` | `SyEntitlement_AuditorCode` | String |  |  |
| 36 | `SY.ENT.AUDIT.DATE.TIME` | `SyEntitlement_AuditDateTime` | String |  |  |
