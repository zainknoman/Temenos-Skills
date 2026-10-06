*-----------------------------------------------------------------------------
* Program    : GOLDEN.GET.TYPED
* Type       : GET (typed)
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
FUNCTION GOLDEN.GET.TYPED(recordId)
    $USING ST.Customer

    outRecord = ''
    readErr = ''
    record = ST.Customer.Customer.Read(recordId, readErr)
    outRecord<GOLDEN.Api.GoldenRecord.recordId> = recordId
    IF readErr EQ '' THEN
        outRecord<GOLDEN.Api.GoldenRecord.fieldValue> = record<ST.Customer.Customer.EbCusSector>
    END
RETURN outRecord
END
