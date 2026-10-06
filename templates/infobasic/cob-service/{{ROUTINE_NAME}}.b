*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : BATCH record routine
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}(Y.ID)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}
    $INSERT I_{{ROUTINE_NAME}}.COMMON

    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR NE '' THEN RETURN
    IF R.APP<{{FIELD}}> NE '{{SELECT_VALUE}}' THEN RETURN

    GOSUB PROCESS.RECORD
    RETURN

PROCESS.RECORD:
*   Record-level processing goes here.
    CRT '{{ROUTINE_NAME}}: ':Y.ID
    RETURN
END
