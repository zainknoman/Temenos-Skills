*-----------------------------------------------------------------------------
* Program    : GOLDEN.INPUT.RTN
* Type       : INPUT.ROUTINE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.INPUT.RTN
    $USING EB.SystemTables
    $USING EB.ErrorProcessing
    $USING ST.Customer

    fieldValue = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusSector)
    IF fieldValue EQ '' THEN
        EB.SystemTables.setAf(ST.Customer.Customer.EbCusSector)
        EB.SystemTables.setEtext('SECTOR IS MANDATORY')
        EB.ErrorProcessing.StoreEndError()
    END
RETURN
END
