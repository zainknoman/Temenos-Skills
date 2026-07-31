# LE.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.LE.DIRECTORY` in `LE_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LE.LDIR.ENTITY.NAME` | `LeDirectory_EntityName` |  |  |  |
| 2 | `LE.LDIR.OTH.ENTITY.NAME` | `LeDirectory_OthEntityName` | TField | No | An optional list of OtherName elements (providing all types of names other than the Primary Legal Name) for the Entity. Transliterated versions of names are provided in a separate element. Optional Field Validation Rules: Up to 320 Alphanumeric Characters. |
| 3 | `LE.LDIR.TRANSLITERATED.OTH.NAME` | `LeDirectory_TransliteratedOthName` | TField | No | An optional list of ASCII-transliterated (i.e. Latin or Romanized) representations of names for the Legal Entity. Optional Field Validation Rules: Up to 320 Alphanumeric Characters. |
| 4 | `LE.LDIR.ENTITY.ADDRESS.1` | `LeDirectory_EntityAddress1` |  |  |  |
| 5 | `LE.LDIR.ENTITY.ADDRESS.2` | `LeDirectory_EntityAddress2` |  |  |  |
| 6 | `LE.LDIR.ENTITY.ADDRESS.3` | `LeDirectory_EntityAddress3` |  |  |  |
| 7 | `LE.LDIR.ENTITY.CITY` | `LeDirectory_EntityCity` |  |  |  |
| 8 | `LE.LDIR.ENTITY.REGION` | `LeDirectory_EntityRegion` |  |  |  |
| 9 | `LE.LDIR.ENTITY.COUNTRY` | `LeDirectory_EntityCountry` |  |  |  |
| 10 | `LE.LDIR.ENTITY.POST.CODE` | `LeDirectory_EntityPostCode` |  |  |  |
| 11 | `LE.LDIR.HQ.ADDRESS.1` | `LeDirectory_HqAddress1` |  |  |  |
| 12 | `LE.LDIR.HQ.ADDRESS.2` | `LeDirectory_HqAddress2` |  |  |  |
| 13 | `LE.LDIR.HQ.ADDRESS.3` | `LeDirectory_HqAddress3` |  |  |  |
| 14 | `LE.LDIR.HQ.CITY` | `LeDirectory_HqCity` |  |  |  |
| 15 | `LE.LDIR.HQ.REGION` | `LeDirectory_HqRegion` |  |  |  |
| 16 | `LE.LDIR.HQ.COUNTRY` | `LeDirectory_HqCountry` |  |  |  |
| 17 | `LE.LDIR.HQ.POST.CODE` | `LeDirectory_HqPostCode` |  |  |  |
| 18 | `LE.LDIR.LEGAL.JURISDICTION` | `LeDirectory_LegalJurisdiction` | TField | No | The jurisdiction of legal formation and registration of the Entity (and on which the Legalform data element is also dependent). Optional Field Validation Rules: Upto 10 Alphanumeric Characters. |
| 19 | `LE.LDIR.ENTITY.CATEGORY` | `LeDirectory_EntityCategory` | TField | No | Indicates (where applicable) the category of Entity identified by this LEI Data Record, as a more specific category within the broad definition given in ISO 17442. Optional Field Validation Rules: Options Field with options: BRANCH - The Legal Entity is a branch of another Legal Entity FUND - The Legal Entity is a fund managed by another Legal Entity SOLE.PROPRIETER - The Legal Entity is an individual acting in a business capacity |
| 20 | `LE.LDIR.ENTITY.STATUS` | `LeDirectory_EntityStatus` | TField | Yes | The status of Legal Entity. Mandatory Field Validation Rules: Options Field with options: ACTIVE - As of the last report or update, the Legal Entity reported that it was legally registered and operating. INACTIVE - It has been determined that the Entity that was assigned the LEI is no longer legally registered and/or operating, whether as a result of business closure, acquisition by or merger with another (or new) Entity, or determination of illegitimacy. |
| 21 | `LE.LDIR.EXPIRED.DATE` | `LeDirectory_ExpiredDate` | TField | No | The date the Legal Entity ceased operation or was merged. This is associated with the entity expiration reason or otherwise omitted. Optional Field Validation Rules: Date field. |
| 22 | `LE.LDIR.EXPIRED.REASON` | `LeDirectory_ExpiredReason` | TField | Yes | The reason that a Legal Entity ceased to operate. This element SHALL be present if EntityExpirationDate is present, and omitted otherwise. Conditionally mandatory Field. If EXPIRED.DATE is mentioned then this field becomes mandatory Validation Rules: Upto 20 Alphanumeric Characters. |
| 23 | `LE.LDIR.ASSIGNED.DATE` | `LeDirectory_AssignedDate` | TField | Yes | The date at which the information was first collected by the Managing LOU. Mandatory Field. Validation Rules: Date Field. |
| 24 | `LE.LDIR.LAST.UPD.DATE` | `LeDirectory_LastUpdDate` | TField |  | The date at which the information was most recently updated by the Managing LOU. Noinput Field. Validation Rules: Date Field. Will be updated to TODAY after every update. |
| 25 | `LE.LDIR.REGISTRATION.STATUS` | `LeDirectory_RegistrationStatus` | TField | Yes | The status of the Legal Entity's LEI Record registration with the Managing LOU. Mandatory Field. Validation Rules: Following are the possible options for the status: PENDING.VALIDATION - An application for an LEI that has been submitted and which is being processed and validated ISSUED - An LEI Registration that has been validated and issued, and which identifies an Entity that was an operating Legal Entity as of the last update LAPSED - An LEI registration that has not been renewed by the NextRenewalDate and is not known by public sources to have ceased operation MERGED - An LEI registration for an Entity that has been merged into another Legal Entity, such that this Legal Entity no longer exists as an operating Entity RETIRED - An LEI registration for an Entity that has ceased operation, without having been merged into another Entity CANCELLED - An LEI registration that was abandoned prior to issuance of an LEI ANNULLED - An LEI registration that was marked as erroneous or invalid after it was issued DUPLICATE - An LEI Registration that has been determined to be a duplicate registration of the same Legal Entity as another LEI Registration; the DUPLICATE status is assigned to the non-surviving registration (i.e. the LEI that should no longer be used) TRANSFERRED - An LEI registration that has been transferred to a different LOU as the managing LOU PENDING.ARCHIVAL - An LEI registration is about to be transferred to a different LOU, after which its registration status will revert to a non-pending status PENDING.TRANSFER - An LEI registration that has been requested to be transferred to another LOU. The request is being processed at the sending LOU |
| 26 | `LE.LDIR.NEXT.RENEWAL.DATE` | `LeDirectory_NextRenewalDate` | TField | Yes | The next date by which the LEI information must be renewed and re-certified by the Legal Entity. Mandatory Field. Validation Rules: Date Field. |
| 27 | `LE.LDIR.ISSUER.LEI` | `LeDirectory_IssuerLei` | TField | No | The LEI code of the LEI Issuer that is responsible for administering this LEI Record. Optional Field. Validation Rules: Upto 20 Alphanumeric Characters. |
| 28 | `LE.LDIR.BSNSS.REG.NAME` | `LeDirectory_BsnssRegName` | TField | No | The name of the Entity at the indicated registration authority. Optional Field. Validation Rules: Upto 150 Alphanumeric Characters. |
| 29 | `LE.LDIR.BSNSS.REG.ENTITY.ID` | `LeDirectory_BsnssRegEntityId` | TField | No | The identifier of the Entity at the indicated registration authority. Optional Field. Validation Rules: Upto 150 Alphanumeric Characters. |
| 30 | `LE.LDIR.BIC.CODE` | `LeDirectory_BicCode` | TField | No | SWIFT BIC code of the entity. Optional Field. Validation Rules: Upto 11 Alphanumeric Characters. |
| 31 | `LE.LDIR.RESERVED.10` | `LeDirectory_Reserved10` | TField |  |  |
| 32 | `LE.LDIR.RESERVED.09` | `LeDirectory_Reserved09` | TField |  |  |
| 33 | `LE.LDIR.RESERVED.08` | `LeDirectory_Reserved08` | TField |  |  |
| 34 | `LE.LDIR.RESERVED.07` | `LeDirectory_Reserved07` | TField |  |  |
| 35 | `LE.LDIR.RESERVED.06` | `LeDirectory_Reserved06` | TField |  |  |
| 36 | `LE.LDIR.RESERVED.05` | `LeDirectory_Reserved05` | TField |  |  |
| 37 | `LE.LDIR.RESERVED.04` | `LeDirectory_Reserved04` | TField |  |  |
| 38 | `LE.LDIR.RESERVED.03` | `LeDirectory_Reserved03` | TField |  |  |
| 39 | `LE.LDIR.RESERVED.02` | `LeDirectory_Reserved02` | TField |  |  |
| 40 | `LE.LDIR.RESERVED.01` | `LeDirectory_Reserved01` | TField |  |  |
| 41 | `LE.LDIR.LOCAL.REF` | `LeDirectory_LocalRef` |  |  |  |
| 42 | `LE.LDIR.RECORD.STATUS` | `LeDirectory_RecordStatus` | String |  |  |
| 43 | `LE.LDIR.CURR.NO` | `LeDirectory_CurrNo` | String |  |  |
| 44 | `LE.LDIR.INPUTTER` | `LeDirectory_Inputter` |  |  |  |
| 45 | `LE.LDIR.DATE.TIME` | `LeDirectory_DateTime` |  |  |  |
| 46 | `LE.LDIR.AUTHORISER` | `LeDirectory_Authoriser` | String |  |  |
| 47 | `LE.LDIR.CO.CODE` | `LeDirectory_CoCode` | String |  |  |
| 48 | `LE.LDIR.DEPT.CODE` | `LeDirectory_DeptCode` | String |  |  |
| 49 | `LE.LDIR.AUDITOR.CODE` | `LeDirectory_AuditorCode` | String |  |  |
| 50 | `LE.LDIR.AUDIT.DATE.TIME` | `LeDirectory_AuditDateTime` | String |  |  |
