# DX.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.DX.CUSTOMER` in `DX_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CU.CUSTOMER.TYPE` | `DxCustomer_CustomerType` | TField | Yes | This field illustrates the capacity in which a client is acting. A client may well act in one or all of these capacities, hence the multi valued field to cater for this eventuality. Only 'CUSTOMER', 'BROKER', 'COUNTERPARTY'and 'EXCHANGE' may be entered. CUSTOMER would either Own-book or a customer of the bank.(Portfolio's would be required). BROKER someone who executes or clears trades on behalf of the bank/customer. This does not require any portfolio's to be set up. COUNTERPARTY This is used in the same way as Broker although portfolio's can be set-up. EXCHANGE if an Exchange member then the Exchange on which the user has membership need to be set-up in DX.CUSTOMER (For Future Use) Validation Rules: Up to 12 alpha characters. Input must be one of the following: CUSTOMER, BROKER,COUNTERPARTY, EXCHANGE Mandatory input field |
| 2 | `DX.CU.EXTERNAL.FREQ` | `DxCustomer_ExternalFreq` |  |  |  |
| 3 | `DX.CU.EXTERN.REPS` | `DxCustomer_ExternReps` |  |  |  |
| 4 | `DX.CU.INTERNAL.FREQ` | `DxCustomer_InternalFreq` |  |  |  |
| 5 | `DX.CU.INTERN.REPS` | `DxCustomer_InternReps` |  |  |  |
| 6 | `DX.CU.EXCHANGE` | `DxCustomer_Exchange` |  |  |  |
| 7 | `DX.CU.SPEC.OR.HEDGE` | `DxCustomer_SpecOrHedge` |  |  |  |
| 8 | `DX.CU.EXCH.MEMBER` | `DxCustomer_ExchMember` |  |  |  |
| 9 | `DX.CU.MARG.WEIGHTING` | `DxCustomer_MargWeighting` |  |  |  |
| 10 | `DX.CU.MVRESERVED1` | `DxCustomer_Mvreserved1` |  |  |  |
| 11 | `DX.CU.MVRESERVED2` | `DxCustomer_Mvreserved2` |  |  |  |
| 12 | `DX.CU.MVRESERVED3` | `DxCustomer_Mvreserved3` |  |  |  |
| 13 | `DX.CU.MVRESERVED4` | `DxCustomer_Mvreserved4` |  |  |  |
| 14 | `DX.CU.AU.CT.CLASS` | `DxCustomer_AuCtClass` |  |  |  |
| 15 | `DX.CU.AU.SETT.TYPE` | `DxCustomer_AuSettType` |  |  |  |
| 16 | `DX.CU.AU.SETT.DELAY` | `DxCustomer_AuSettDelay` |  |  |  |
| 17 | `DX.CU.MAN.SETT.NAR` | `DxCustomer_ManSettNar` |  |  |  |
| 18 | `DX.CU.MVRESERVED5` | `DxCustomer_Mvreserved5` |  |  |  |
| 19 | `DX.CU.MVRESERVED6` | `DxCustomer_Mvreserved6` |  |  |  |
| 20 | `DX.CU.RESERVED17` | `DxCustomer_Reserved17` | TField |  |  |
| 21 | `DX.CU.RESERVED16` | `DxCustomer_Reserved16` | TField |  |  |
| 22 | `DX.CU.RESERVED15` | `DxCustomer_Reserved15` | TField |  |  |
| 23 | `DX.CU.RESERVED14` | `DxCustomer_Reserved14` | TField |  |  |
| 24 | `DX.CU.RESERVED13` | `DxCustomer_Reserved13` | TField |  |  |
| 25 | `DX.CU.RESERVED12` | `DxCustomer_Reserved12` | TField |  |  |
| 26 | `DX.CU.RESERVED11` | `DxCustomer_Reserved11` | TField |  |  |
| 27 | `DX.CU.GROUP` | `DxCustomer_Group` | TField |  | The Group(s) this customer is a part off. Validation Rules: Up to 35 Alpha characters Must be a valid ID on DX.GROUPING |
| 28 | `DX.CU.MARGIN.ACC.CCY` | `DxCustomer_MarginAccCcy` |  |  |  |
| 29 | `DX.CU.MARGIN.ACCOUNT` | `DxCustomer_MarginAccount` |  |  |  |
| 30 | `DX.CU.MVRESERVED9` | `DxCustomer_Mvreserved9` |  |  |  |
| 31 | `DX.CU.MVRESERVED10` | `DxCustomer_Mvreserved10` |  |  |  |
| 32 | `DX.CU.STATEMENT.TYPE` | `DxCustomer_StatementType` | TField |  | The Type(s) of combined equity statement required by the customer. Choose from the drop down menu 'BOTH'_'DAILY'_'MONTHLY'_'NONE' Validation Rules: Up to 7 Alpha characters Input must be one of the following : BOTH/DAILY/MONTHLY/NONE |
| 33 | `DX.CU.TRADING.STATUS` | `DxCustomer_TradingStatus` | TField |  | The trading status of the customer, a Regulatory Classification. Choose from the drop down menu 'HOUSE'_'SEGREGATED'_'RESERVED' Validation Rules: Up to 10 alpha characters Input must be one of the following : HOUSE/SEGREGATED/RESERVED |
| 34 | `DX.CU.REPORTING.CCY` | `DxCustomer_ReportingCcy` | TField | Yes | The Currency used for this customer when reporting during revaluation. Validation Rules: Up to 3 CCY characters available Defaulted from SEC.ACC.MASTER portfolio 1. If no portfolio exists then default from the COMPANY&amp;#146;s local currency. Mandatory Input |
| 35 | `DX.CU.CLR.BROKER` | `DxCustomer_ClrBroker` | TField |  | Holds the clearing broker id. Assigned to SEC.CUST.NO in DX.TRADE, when this customer is given in EXECUTING.BROKER field of DX.TRADE |
| 36 | `DX.CU.BROKER.REMITTANCE` | `DxCustomer_BrokerRemittance` | TField |  |  |
| 37 | `DX.CU.BROKER.FTT` | `DxCustomer_BrokerFtt` | TField |  | Allowed option is YES or NULL.System will check whether the broker side FTT is applicable.Option 'YES' is allowed only when BROKER.REMIT Field is not set. |
| 38 | `DX.CU.RESERVED7` | `DxCustomer_Reserved7` |  |  |  |
| 39 | `DX.CU.RESERVED6` | `DxCustomer_Reserved6` | TField |  |  |
| 40 | `DX.CU.RESERVED5` | `DxCustomer_Reserved5` | TField |  |  |
| 41 | `DX.CU.RESERVED4` | `DxCustomer_Reserved4` | TField |  |  |
| 42 | `DX.CU.RESERVED3` | `DxCustomer_Reserved3` | TField |  |  |
| 43 | `DX.CU.RESERVED2` | `DxCustomer_Reserved2` | TField |  |  |
| 44 | `DX.CU.RESERVED1` | `DxCustomer_Reserved1` | TField |  |  |
| 45 | `DX.CU.LOCAL.REF` | `DxCustomer_LocalRef` |  |  |  |
| 46 | `DX.CU.OVERRIDE` | `DxCustomer_Override` |  |  |  |
| 47 | `DX.CU.RECORD.STATUS` | `DxCustomer_RecordStatus` | String |  |  |
| 48 | `DX.CU.CURR.NO` | `DxCustomer_CurrNo` | String |  |  |
| 49 | `DX.CU.INPUTTER` | `DxCustomer_Inputter` |  |  |  |
| 50 | `DX.CU.DATE.TIME` | `DxCustomer_DateTime` |  |  |  |
| 51 | `DX.CU.AUTHORISER` | `DxCustomer_Authoriser` | String |  |  |
| 52 | `DX.CU.CO.CODE` | `DxCustomer_CoCode` | String |  |  |
| 53 | `DX.CU.DEPT.CODE` | `DxCustomer_DeptCode` | String |  |  |
| 54 | `DX.CU.AUDITOR.CODE` | `DxCustomer_AuditorCode` | String |  |  |
| 55 | `DX.CU.AUDIT.DATE.TIME` | `DxCustomer_AuditDateTime` | String |  |  |
