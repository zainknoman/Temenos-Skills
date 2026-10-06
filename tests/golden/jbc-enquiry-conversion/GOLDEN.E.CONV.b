*-----------------------------------------------------------------------------
* Program    : GOLDEN.E.CONV
* Type       : ENQUIRY CONVERSION
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.E.CONV
    $USING EB.Reports
    $USING ST.Customer

    recordId = EB.Reports.getOData()
    IF recordId EQ '' THEN RETURN
    readErr = ''
    record = ST.Customer.Customer.Read(recordId, readErr)
    IF readErr EQ '' THEN
        EB.Reports.setOData(record<ST.Customer.Customer.EbCusSector>)
    END ELSE
        EB.Reports.setOData('')
    END
RETURN
END
