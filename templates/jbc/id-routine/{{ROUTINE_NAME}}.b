*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : ID.RTN
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}
    $USING EB.SystemTables

    recordId = EB.SystemTables.getIdNew()
    IF recordId EQ '' THEN RETURN
    IF recordId[1, LEN('{{ID_PREFIX}}')] NE '{{ID_PREFIX}}' THEN
        EB.SystemTables.setE('{{ERROR_TEXT}}')
    END
RETURN
END
