*-----------------------------------------------------------------------------
* Program    : GOLDEN.SET.SECTOR
* Type       : WRITE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.SET.SECTOR(recordId, newValue)
    $USING EB.Interface
    $USING EB.SystemTables

    ofsSourceId = 'TEST.OFS'
    ofsRecord = 'CUSTOMER,GOLDEN.OFS/I/PROCESS,//':EB.SystemTables.getIdCompany():',':recordId:',SECTOR:1:1=':newValue
    ofsMsgId = ''
    options = ''
    EB.Interface.OfsPostMessage(ofsRecord, ofsMsgId, ofsSourceId, options)
RETURN
END
