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
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}

    IF R.NEW({{FIELD}}) EQ '' THEN
        R.NEW({{FIELD}}) = '{{DEFAULT_VALUE}}'
    END
    RETURN
END
