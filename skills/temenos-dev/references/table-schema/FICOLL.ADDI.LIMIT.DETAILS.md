# FICOLL.ADDI.LIMIT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FICOLL.ADDI.LIMIT.DETAILS` in `FICOLL_RiskViewSimulation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.ADDILIMITDETS.NOT.SIGNEDOFF.AMT` | `FicollAddiLimitDetails_NotSignedoffAmt` | TField |  | Amount granted but not signed |
| 2 | `FICOLL.ADDILIMITDETS.PENDING.REVIEW.AMT` | `FicollAddiLimitDetails_PendingReviewAmt` | TField |  | Amount requested pending review |
| 3 | `FICOLL.ADDILIMITDETS.REPAID.OUTSTANDING.AMT` | `FicollAddiLimitDetails_RepaidOutstandingAmt` | TField |  | Amount repaid on the outstanding |
| 4 | `FICOLL.ADDILIMITDETS.NEW.GRANTED.AMT` | `FicollAddiLimitDetails_NewGrantedAmt` | TField |  | New amount granted |
| 5 | `FICOLL.ADDILIMITDETS.CREDIT.NOT.GRANTED` | `FicollAddiLimitDetails_CreditNotGranted` | TField |  | Credit application not yet granted amount |
| 6 | `FICOLL.ADDILIMITDETS.EXTERNAL.REFERENCE` | `FicollAddiLimitDetails_ExternalReference` | TField |  | Origination system Dossier number for each record |
| 7 | `FICOLL.ADDILIMITDETS.LIMIT.REFERENCE` | `FicollAddiLimitDetails_LimitReference` | TField |  | Limit reference ID of Credit not granted field information |
| 8 | `FICOLL.ADDILIMITDETS.DATE` | `FicollAddiLimitDetails_Date` | TField |  | Record input date |
| 9 | `FICOLL.ADDILIMITDETS.LOCAL.REF` | `FicollAddiLimitDetails_LocalRef` |  |  |  |
| 10 | `FICOLL.ADDILIMITDETS.OVERRIDE` | `FicollAddiLimitDetails_Override` |  |  |  |
| 11 | `FICOLL.ADDILIMITDETS.RECORD.STATUS` | `FicollAddiLimitDetails_RecordStatus` | String |  |  |
| 12 | `FICOLL.ADDILIMITDETS.CURR.NO` | `FicollAddiLimitDetails_CurrNo` | String |  |  |
| 13 | `FICOLL.ADDILIMITDETS.INPUTTER` | `FicollAddiLimitDetails_Inputter` |  |  |  |
| 14 | `FICOLL.ADDILIMITDETS.DATE.TIME` | `FicollAddiLimitDetails_DateTime` |  |  |  |
| 15 | `FICOLL.ADDILIMITDETS.AUTHORISER` | `FicollAddiLimitDetails_Authoriser` | String |  |  |
| 16 | `FICOLL.ADDILIMITDETS.CO.CODE` | `FicollAddiLimitDetails_CoCode` | String |  |  |
| 17 | `FICOLL.ADDILIMITDETS.DEPT.CODE` | `FicollAddiLimitDetails_DeptCode` | String |  |  |
| 18 | `FICOLL.ADDILIMITDETS.AUDITOR.CODE` | `FicollAddiLimitDetails_AuditorCode` | String |  |  |
| 19 | `FICOLL.ADDILIMITDETS.AUDIT.DATE.TIME` | `FicollAddiLimitDetails_AuditDateTime` | String |  |  |
