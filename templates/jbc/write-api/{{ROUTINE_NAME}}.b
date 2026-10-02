*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : WRITE
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(recordId, newValue)
    $USING EB.Interface
    $USING EB.SystemTables

    ofsSourceId = '{{OFS_SOURCE}}'
    ofsRecord = '{{APP}},{{VERSION_NAME}}/I/PROCESS,//':EB.SystemTables.getIdCompany():',':recordId:',{{FIELD_NAME}}:1:1=':newValue
    ofsMsgId = ''
    options = ''
    EB.Interface.OfsPostMessage(ofsRecord, ofsMsgId, ofsSourceId, options)
RETURN
END
