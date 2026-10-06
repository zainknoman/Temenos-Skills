*-----------------------------------------------------------------------------
* Program    : GOLDEN.CHECK.REC
* Type       : CHECK.REC.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.CHECK.REC
    $USING EB.SystemTables
    $USING ST.Customer

    IF EB.SystemTables.getRNew(ST.Customer.Customer.EbCusSector) EQ '' THEN
        EB.SystemTables.setRNew(ST.Customer.Customer.EbCusSector, '1001')
    END
RETURN
END
