package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.validateField (deprecated)

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public TValidationResponse validateField(String application, String recordId, String fieldData,
            TStructure record) {

        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(record);
        if (fieldData == null || fieldData.isEmpty()) {
            rec.get{{FIELD}}().setError("{{ERROR_TEXT}}");
        }
        return rec.getValidationResponse();
    }
}
