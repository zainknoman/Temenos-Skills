*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : CHECK.REC.RTN
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

    IF EB.SystemTables.getRNew({{FIELD}}) EQ '' THEN
        EB.SystemTables.setRNew({{FIELD}}, '{{DEFAULT_VALUE}}')
    END
RETURN
END
