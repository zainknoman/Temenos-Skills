# IM.IMAGE.TYPE — Table Schema

> Source: `INSERTS/I_F.IM.IMAGE.TYPE` in `IM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IM.TYP.DESCRIPTION` | `ImImageType_Description` |  |  |  |
| 2 | `IM.TYP.DEFAULT.DRIVE` | `ImImageType_DefaultDrive` | TField |  | Identifies the PC or Network drive where images related to this type are stored.The Drive should be defined in MSDOS/WINDOWS format eg. C: D: etc. Validation Rules Two-character alphanumeric. Drive should be entered in the following format. Character 1 = A to Z Character 2 = : |
| 3 | `IM.TYP.PATH` | `ImImageType_Path` | TField |  | The path of the directory where the images of this type are stored.Used with/without the default drive to identify the location of images of the type defined in this record.For example \GLOBUS\IMAGES\CUSTOMER\PHOTO\The path must be entered in MSDOS, MS WINDOWS Format.A full path can be entered withou a default drive as long is this can be evaluated by T24 as a valid location. The path can alos be prefixed with Unix type indicators './' or '../.' etc which makes the path a relative one. Relative to the web browser root directory (Windows or Unix). Full Unix patsh can be entered but may need networking software installed so they can be accessed by browser/explorer. Validation Rules 1-35 alphanumeric characters. The first and Last character must be \. |
| 4 | `IM.TYP.FILE.LOCATION` | `ImImageType_FileLocation` | TField | Yes | The physical location (SERVER/LOCAL) of files to be uploaded/retrieved. Location could be either SERVER or LOCAL. DEFAULT.DRIVE and PATH field values will be combined as path to proceed file process based on the type of location. For SERVER location DEFAULT.DRIVE field should be empty, since T24 server's run directory will be taken as default drive. Validation Rules It's a mandatory,list box field and cannot provide any inputs by manual process. |
| 5 | `IM.TYP.UPLD.MAX.SIZE` | `ImImageType_UpldMaxSize` | TField | No | This field holds maximum size of file to be uploaded. Validation Rules Optional field. If set, then specifies a maximum size (in bytes) to be uploaded. If not set, then the system will not place any artificial limits on the upload file size. |
| 6 | `IM.TYP.RESERVED2` | `ImImageType_Reserved2` | TField |  |  |
| 7 | `IM.TYP.RESERVED3` | `ImImageType_Reserved3` | TField |  |  |
| 8 | `IM.TYP.RESERVED4` | `ImImageType_Reserved4` | TField |  |  |
| 9 | `IM.TYP.RESERVED5` | `ImImageType_Reserved5` | TField |  |  |
| 10 | `IM.TYP.RESERVED6` | `ImImageType_Reserved6` | TField |  |  |
| 11 | `IM.TYP.RESERVED7` | `ImImageType_Reserved7` | TField |  |  |
| 12 | `IM.TYP.RESERVED8` | `ImImageType_Reserved8` | TField |  |  |
| 13 | `IM.TYP.RESERVED9` | `ImImageType_Reserved9` | TField |  |  |
| 14 | `IM.TYP.RESERVED10` | `ImImageType_Reserved10` | TField |  |  |
| 15 | `IM.TYP.RECORD.STATUS` | `ImImageType_RecordStatus` | String |  |  |
| 16 | `IM.TYP.CURR.NO` | `ImImageType_CurrNo` | String |  |  |
| 17 | `IM.TYP.INPUTTER` | `ImImageType_Inputter` |  |  |  |
| 18 | `IM.TYP.DATE.TIME` | `ImImageType_DateTime` |  |  |  |
| 19 | `IM.TYP.AUTHORISER` | `ImImageType_Authoriser` | String |  |  |
| 20 | `IM.TYP.CO.CODE` | `ImImageType_CoCode` | String |  |  |
| 21 | `IM.TYP.DEPT.CODE` | `ImImageType_DeptCode` | String |  |  |
| 22 | `IM.TYP.AUDITOR.CODE` | `ImImageType_AuditorCode` | String |  |  |
| 23 | `IM.TYP.AUDIT.DATE.TIME` | `ImImageType_AuditDateTime` | String |  |  |
