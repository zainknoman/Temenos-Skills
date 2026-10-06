*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : PROGRAM
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
    PROGRAM {{ROUTINE_NAME}}
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}

    FN.APP = 'F.{{APP}}'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)

    SEL.CMD = 'SELECT ':FN.APP:' WITH {{FIELD_NAME}} EQ ':DQUOTE('{{SELECT_VALUE}}')
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)

    Y.COUNT = 0
    LOOP
        REMOVE Y.ID FROM SEL.LIST SETTING Y.POS
    WHILE Y.ID:Y.POS
        R.APP = ''
        Y.READ.ERR = ''
        CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
        IF Y.READ.ERR EQ '' AND R.APP<{{FIELD}}> EQ '{{SELECT_VALUE}}' THEN
            Y.COUNT += 1
        END
    REPEAT
    CRT '{{ROUTINE_NAME}}: ':Y.COUNT:' record(s)'
END
