# CAMPAIGN.FAILED.DEPOSITS — Table Schema

> Source: `INSERTS/I_F.CAMPAIGN.FAILED.DEPOSITS` in `HKDEPO_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMP.FAIL.PRODUCT.ID` | `CampaignFailedDeposits_ProductId` | TField |  | AA product of the deposit. |
| 2 | `CAMP.FAIL.TRANSACTION.AMT` | `CampaignFailedDeposits_TransactionAmt` | TField |  | Transaction amount of the deposit. |
| 3 | `CAMP.FAIL.SETTLEMENT.AC` | `CampaignFailedDeposits_SettlementAc` | TField |  | Payin account number. |
| 4 | `CAMP.FAIL.RESERVED.1` | `CampaignFailedDeposits_Reserved1` | TField |  |  |
| 5 | `CAMP.FAIL.RESERVED.2` | `CampaignFailedDeposits_Reserved2` | TField |  |  |
| 6 | `CAMP.FAIL.RESERVED.3` | `CampaignFailedDeposits_Reserved3` | TField |  |  |
| 7 | `CAMP.FAIL.RESERVED.4` | `CampaignFailedDeposits_Reserved4` | TField |  |  |
| 8 | `CAMP.FAIL.RESERVED.5` | `CampaignFailedDeposits_Reserved5` | TField |  |  |
| 9 | `CAMP.FAIL.RESERVED.6` | `CampaignFailedDeposits_Reserved6` | TField |  |  |
| 10 | `CAMP.FAIL.RESERVED.7` | `CampaignFailedDeposits_Reserved7` | TField |  |  |
| 11 | `CAMP.FAIL.RESERVED.8` | `CampaignFailedDeposits_Reserved8` | TField |  |  |
| 12 | `CAMP.FAIL.RESERVED.9` | `CampaignFailedDeposits_Reserved9` | TField |  |  |
| 13 | `CAMP.FAIL.RESERVED.10` | `CampaignFailedDeposits_Reserved10` | TField |  |  |
| 14 | `CAMP.FAIL.LOCAL.REF` | `CampaignFailedDeposits_LocalRef` |  |  |  |
