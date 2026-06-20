# T24 Hook Reference — All Domains

> Generated 2026-06-20T03:17:58.699072+00:00. Covers all hook types across all JAR prefixes.

---

## Lifecycle Hooks (RecordLifecycle)

Fire during T24 record processing: input → validate → authorise → post-update.

### RecordLifecycle API — standard override points

| Method | Signature | When called |
|--------|-----------|-------------|
| `validateRecord` | `void validateRecord(TypeRecord record)` | Before the record is committed |
| `authoriseRecord` | `void authoriseRecord(TypeRecord record)` | When the record is submitted for authorisation |
| `postUpdateRequest` | `void postUpdateRequest(TypeRecord record)` | After the update is written to the database |
| `defaultFieldValues` | `void defaultFieldValues(TypeRecord record)` | To pre-populate field defaults on new records |
| `checkId` | `void checkId(TypeRecord record)` | To validate the record ID format |

*No concrete RecordLifecycle subclasses detected in analysed JARs (these are typically L3 customization classes, not shipped in product JARs).*

---

## AA Activity Hooks (ActivityLifecycle)

Fire during Arrangement Architecture activity processing.

*No ActivityLifecycle hooks found.*

---

## Service Hooks (ServiceLifecycle)

Fire during background service and batch processing.

*No ServiceLifecycle hooks found.*

---

## Validation Hooks

Classes ending `Validation`. Pattern: `record.setError("FIELD.NAME", "message")` / `record.getRNew().getFieldValue("FIELD.NAME")`

*No validation hooks found.*

---

## Authorization Hooks

Classes ending `Authorization`. Called when a record is submitted for authorisation.

*No authorization hooks found.*
