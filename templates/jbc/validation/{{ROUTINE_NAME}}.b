*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : VVR
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
    $USING {{APP_COMPONENT}}

    lvValue = EB.SystemTables.getRNew({{FIELD}})
    IF lvValue EQ '' THEN
        EB.SystemTables.setE('{{ERROR_TEXT}}')
    END
RETURN
END
