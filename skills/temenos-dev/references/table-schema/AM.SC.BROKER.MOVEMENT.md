# AM.SC.BROKER.MOVEMENT — Table Schema

> Source: `INSERTS/I_F.AM.SC.BROKER.MOVEMENT` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BM.NOMINAL` | `AmScBrokerMovement_Nominal` | TField |  | The nominal for which the order should placed for. |
| 2 | `SC.BM.SECURITY.NO` | `AmScBrokerMovement_SecurityNo` | TField |  | The security for which the order should placed for. |
| 3 | `SC.BM.TRANSACTION.CODE` | `AmScBrokerMovement_TransactionCode` | TField |  | The transaction code for which the order should placed for. |
| 4 | `SC.BM.DEPOSITORY` | `AmScBrokerMovement_Depository` | TField |  | The depository for which the order details apply. |
| 5 | `SC.BM.SERVICE.REF` | `AmScBrokerMovement_ServiceRef` | TField |  | Key to identify the record. |
| 6 | `SC.BM.THREAD.KEY` | `AmScBrokerMovement_ThreadKey` | TField |  | Key to identify which service agent updated the record. |
| 7 | `SC.BM.NOMINEE.CODE` | `AmScBrokerMovement_NomineeCode` | TField |  | The nominee for which the order details apply. |
| 8 | `SC.BM.LOAD.COMPANY` | `AmScBrokerMovement_LoadCompany` | TField |  | This field will be updated only when SEC.ACC.MASTER is shared across companies. This field will indicate the company in whichSEC.OPEN.ORDER has to be created. |
| 9 | `SC.BM.PARENT.REFERENCE` | `AmScBrokerMovement_ParentReference` | TField |  |  |
