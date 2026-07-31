# SC.GROUP.ORDERS — Table Schema

> Source: `INSERTS/I_F.SC.GROUP.ORDERS` in `SC_SctOrderGrouping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.GRP.ORD.ORDER.NUMBER` | `ScGroupOrders_OrderNumber` |  |  |  |
| 2 | `SC.GRP.ORD.TRANSMIT` | `ScGroupOrders_Transmit` | TField | Yes | This field allows 'Yes' or 'NO' to be input. This field can be used to control the generation of SC.EXE.SEC.ORDERS from a grouped order as also generation of delivery messages. The value in this field would be relevant only if there is a) Routing has not been set in SC.PARAMETER or b) no SC.ROUTING record has been linked to the relevant grouped SEC.OPEN.ORDER. Note: SC.ROUTING id can be linked to a STOCK.EXCHANGE record which in turn can be linked to the Sec.Open.Order. If 'YES' is input, then the grouped order will generate an SC.EXE.SEC.ORDERS only under the following circumstances. A) If GROUP.ORDER field in SC.PARAMETER record for the relevant company id has a value MANUAL/AUTOMATIC B) If grouped order carries the value &amp;#8220;TRANSMITTED&amp;#8221; in the field DEAL.STATUS.(This can be defaulted in the OFS.VERSION for SEC.OPEN.ORDER defined in SC.STD.SEC.TRADE-This is the OFS version used to authorize the grouped Sec.Open.Order when it is being generated). If 'NO' is input, then the grouped order will be created even if the value &amp;#8220;TRANSMITTED&amp;#8221; is not input in the DEAL.STATUS field. Validation Rules: Mandatory field 'YES' or 'NO' allowed as valid input. |
| 3 | `SC.GRP.ORD.GROUP.ORDER` | `ScGroupOrders_GroupOrder` | TField |  | Reference to the grouped Sec.open.order created through the SC.GROUP.ORDER. Validation Rules: No input- system updated field |
| 4 | `SC.GRP.ORD.AUTO.GROUP.ID` | `ScGroupOrders_AutoGroupId` | TField |  | If the SC.GROUP.ORDERS is created through AUTO-GROUPING, then the related SC.AUTO.GROUP.ORDERS id is updated in this field. Validation Rules: System updated field |
| 5 | `SC.GRP.ORD.PARENT.CHILD` | `ScGroupOrders_ParentChild` | TField |  | Allowed value is YES This is the flag to indicate whether the group order be created as parent child order or single order |
| 6 | `SC.GRP.ORD.TRANSMIT.DATE` | `ScGroupOrders_TransmitDate` | TField |  | This field denotes the date on which the grouped orders are transmitted. |
| 7 | `SC.GRP.ORD.TRANSMIT.TIME` | `ScGroupOrders_TransmitTime` | TField |  | This field denotes the time when the grouped orders are transmitted. |
| 8 | `SC.GRP.ORD.RESERVED.7` | `ScGroupOrders_Reserved7` | TField |  |  |
| 9 | `SC.GRP.ORD.RESERVED.6` | `ScGroupOrders_Reserved6` | TField |  |  |
| 10 | `SC.GRP.ORD.RESERVED.5` | `ScGroupOrders_Reserved5` | TField |  |  |
| 11 | `SC.GRP.ORD.RESERVED.4` | `ScGroupOrders_Reserved4` | TField |  |  |
| 12 | `SC.GRP.ORD.RESERVED.3` | `ScGroupOrders_Reserved3` | TField |  |  |
| 13 | `SC.GRP.ORD.RESERVED.2` | `ScGroupOrders_Reserved2` | TField |  |  |
| 14 | `SC.GRP.ORD.RESERVED.1` | `ScGroupOrders_Reserved1` | TField |  |  |
| 15 | `SC.GRP.ORD.RECORD.STATUS` | `ScGroupOrders_RecordStatus` | String |  |  |
| 16 | `SC.GRP.ORD.CURR.NO` | `ScGroupOrders_CurrNo` | String |  |  |
| 17 | `SC.GRP.ORD.INPUTTER` | `ScGroupOrders_Inputter` |  |  |  |
| 18 | `SC.GRP.ORD.DATE.TIME` | `ScGroupOrders_DateTime` |  |  |  |
| 19 | `SC.GRP.ORD.AUTHORISER` | `ScGroupOrders_Authoriser` | String |  |  |
| 20 | `SC.GRP.ORD.CO.CODE` | `ScGroupOrders_CoCode` | String |  |  |
| 21 | `SC.GRP.ORD.DEPT.CODE` | `ScGroupOrders_DeptCode` | String |  |  |
| 22 | `SC.GRP.ORD.AUDITOR.CODE` | `ScGroupOrders_AuditorCode` | String |  |  |
| 23 | `SC.GRP.ORD.AUDIT.DATE.TIME` | `ScGroupOrders_AuditDateTime` | String |  |  |
