# INLEND.SFMS.HEADER.DETAILS — Table Schema

> Source: `INSERTS/I_F.INLEND.SFMS.HEADER.DETAILS` in `INSFMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFMS.HDR.BUSINESS.LINE` | `InlendSfmsHeaderDetails_BusinessLine` | TField |  | This field contains the value LC, BG as dropdown values. This field depicts as to which line of business the message belongs to. |
| 2 | `SFMS.HDR.DELIVERY.NOTIFICATON.FLAG` | `InlendSfmsHeaderDetails_DeliveryNotificatonFlag` | TField |  | Users to specify whether delivery notification is required for the message.1.YES 2.NO |
| 3 | `SFMS.HDR.OPEN.NOTIFICATON.FLAG` | `InlendSfmsHeaderDetails_OpenNotificatonFlag` | TField |  | Users to specify whether open notification is required for the message. 1.YES 2.NO |
| 4 | `SFMS.HDR.NON.DELIVERY.WARNING` | `InlendSfmsHeaderDetails_NonDeliveryWarning` | TField |  | Flag to inform the user whether the non-delivery warning message is required or not. The possible values are: 1.Yes 2.No The default value for non- delivery warning flag is 2. |
| 5 | `SFMS.HDR.OBSOLESCENE.PERIOD` | `InlendSfmsHeaderDetails_ObsolescenePeriod` | TField |  | Users to specify the period after which a non-delivery warning is to be sent to the sender, applicable only if non-delivery warning flag is specified. If Non-delivery warning flag is 2, then this value should be set to 000. If Non-delivery warning flag is 1, then obsolescence value should be greater than or equal to 002. |
| 6 | `SFMS.HDR.POSSIBLE.DUPLICATE.EMISSION` | `InlendSfmsHeaderDetails_PossibleDuplicateEmission` | TField |  | Flag to indicate possible duplicate emission 1.YES 2.NO |
| 7 | `SFMS.HDR.TEST.AND.TRAIN` | `InlendSfmsHeaderDetails_TestAndTrain` | TField |  | Flag to indicate test and training message. 1.YES 2.NO |
| 8 | `SFMS.HDR.SERVICE.IDENTIFIER` | `InlendSfmsHeaderDetails_ServiceIdentifier` | TField |  | Destination Bank Application identifier. If not applicable, it should be defaulted to XXX. |
| 9 | `SFMS.HDR.LOCAL.REF` | `InlendSfmsHeaderDetails_LocalRef` |  |  |  |
| 10 | `SFMS.HDR.TAGS.SUPPRESSED` | `InlendSfmsHeaderDetails_TagsSuppressed` |  |  |  |
| 11 | `SFMS.HDR.TAGS.INCLUDED` | `InlendSfmsHeaderDetails_TagsIncluded` |  |  |  |
| 12 | `SFMS.HDR.SWIFT.MSG.TAG` | `InlendSfmsHeaderDetails_SwiftMsgTag` |  |  |  |
| 13 | `SFMS.HDR.EQUIVALENT.IFIN.TAG` | `InlendSfmsHeaderDetails_EquivalentIfinTag` |  |  |  |
| 14 | `SFMS.HDR.REORDER.MSG.FLAG` | `InlendSfmsHeaderDetails_ReorderMsgFlag` | TField |  | Enabling this Flag denotes, SFMS tags order needs to be aligned with the SWIFT tags order defined in DE.FORMAT.SWIFT for the message in context. |
| 15 | `SFMS.HDR.RESERVED.6` | `InlendSfmsHeaderDetails_Reserved6` |  |  |  |
| 16 | `SFMS.HDR.RESERVED.7` | `InlendSfmsHeaderDetails_Reserved7` |  |  |  |
| 17 | `SFMS.HDR.RESERVED.8` | `InlendSfmsHeaderDetails_Reserved8` |  |  |  |
| 18 | `SFMS.HDR.RESERVED.9` | `InlendSfmsHeaderDetails_Reserved9` |  |  |  |
| 19 | `SFMS.HDR.RESERVED.10` | `InlendSfmsHeaderDetails_Reserved10` | TField |  | Reserved for future purpose |
| 20 | `SFMS.HDR.OVERRIDE` | `InlendSfmsHeaderDetails_Override` |  |  |  |
| 21 | `SFMS.HDR.RECORD.STATUS` | `InlendSfmsHeaderDetails_RecordStatus` | String |  |  |
| 22 | `SFMS.HDR.CURR.NO` | `InlendSfmsHeaderDetails_CurrNo` | String |  |  |
| 23 | `SFMS.HDR.INPUTTER` | `InlendSfmsHeaderDetails_Inputter` |  |  |  |
| 24 | `SFMS.HDR.DATE.TIME` | `InlendSfmsHeaderDetails_DateTime` |  |  |  |
| 25 | `SFMS.HDR.AUTHORISER` | `InlendSfmsHeaderDetails_Authoriser` | String |  |  |
| 26 | `SFMS.HDR.CO.CODE` | `InlendSfmsHeaderDetails_CoCode` | String |  |  |
| 27 | `SFMS.HDR.DEPT.CODE` | `InlendSfmsHeaderDetails_DeptCode` | String |  |  |
| 28 | `SFMS.HDR.AUDITOR.CODE` | `InlendSfmsHeaderDetails_AuditorCode` | String |  |  |
| 29 | `SFMS.HDR.AUDIT.DATE.TIME` | `InlendSfmsHeaderDetails_AuditDateTime` | String |  |  |
