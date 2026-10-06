*-----------------------------------------------------------------------------
* Program    : GOLDEN.QUERY.SECTOR
* Type       : QUERY
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.QUERY.SECTOR(selValue, rows)
    $USING EB.DataAccess
    $USING ST.Customer

    rows = ''
    selCmd = 'SELECT F.CUSTOMER WITH SECTOR EQ ':DQUOTE(selValue)
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    LOOP
        REMOVE recordId FROM idList SETTING more
    WHILE recordId:more
        readErr = ''
        record = ST.Customer.Customer.Read(recordId, readErr)
        IF readErr EQ '' THEN
            rows<-1> = recordId:'*':record<ST.Customer.Customer.EbCusMnemonic>
        END
    REPEAT
RETURN
END
