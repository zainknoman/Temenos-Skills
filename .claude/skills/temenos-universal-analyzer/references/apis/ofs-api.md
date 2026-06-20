# OFS API Reference

## Contents
1. [OFS Overview](#ofs-overview)
2. [OfsBuildRecord](#ofsbuildrecord)
3. [OfsCallBulkManager](#ofscallbulkmanager)
4. [Message Format](#message-format)
5. [Error Handling](#error-handling)
6. [Common OFS Patterns](#common-ofs-patterns)

---

## OFS Overview

OFS (Open Financial Services) is Temenos's programmatic transaction interface. It allows
any code (jBC, Java, external systems) to create, amend, authorise, or delete T24 records
by building and submitting OFS messages.

**Key classes**: OfsBuildRecord, OfsCallBulkManager

---

## OfsBuildRecord

<!-- Populate from OFS JAR decompilation -->

**Package**: (populate)

**JAR**: (populate)

| Method | Signature | Returns | Purpose |
|--------|----------|---------|---------|
| (populate) | | | Set transaction type (I/A/D) |
| (populate) | | | Set field value |
| (populate) | | | Set multi-value field |
| (populate) | | | Set sub-value |
| (populate) | | | Build message string |
| (populate) | | | Get response |
| (populate) | | | Get error text |

### Field Position Syntax

```
FIELD.NAME:1:1  = single value
FIELD.NAME:1    = first multi-value
FIELD.NAME:2    = second multi-value
FIELD.NAME:1/1  = first sub-value of first multi-value
```

---

## OfsCallBulkManager

<!-- Populate from OFS JAR decompilation -->

**Package**: (populate)

**JAR**: (populate)

| Method | Signature | Returns | Purpose |
|--------|----------|---------|---------|
| (populate) | | | Add OFS message to batch |
| (populate) | | | Execute batch |
| (populate) | | | Get batch results |

---

## Message Format

### OFS Message Structure

```
APPLICATION,FUNCTION,RECORD.ID/SESSION.TOKEN/ADDITIONAL.DATA/
FIELD.1:::VALUE.1/
FIELD.2:::VALUE.2/
```

### Transaction Types

| Code | Meaning |
|------|---------|
| I | Input (create) |
| A | Authorise |
| D | Delete |
| IA | Input and Authorise |
| R | Reverse |

---

## Error Handling

**Error response format**: (populate)

**Common error codes**: (populate)

**Retry strategy**: (populate)

---

## Common OFS Patterns

### Create a FUNDS.TRANSFER

```
* Build OFS for FT input
CALL OfsBuildRecord(ofsRecord)
* populate field assignments from discovered FT patterns
```

### Create an ARRANGEMENT via OFS

```
* Build OFS for AA open
* populate from discovered AA OFS patterns
```

### Authorise a record

```
* Build authorisation OFS
* populate
```
