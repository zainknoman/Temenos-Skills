*-----------------------------------------------------------------------------
* Program    : GOLDEN.GET.SECTOR
* Type       : GET
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.GET.SECTOR(recordId, fieldValue)
    $USING ST.Customer

    fieldValue = ''
    readErr = ''
    record = ST.Customer.Customer.Read(recordId, readErr)
    IF readErr EQ '' THEN
        fieldValue = record<ST.Customer.Customer.EbCusSector>
    END
RETURN
END
