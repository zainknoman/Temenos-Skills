package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.checkId

import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public String checkId(String currentRecordId, TransactionContext transactionContext) {
        if (currentRecordId == null || currentRecordId.isEmpty() || currentRecordId.startsWith("{{ID_PREFIX}}")) {
            return currentRecordId;
        }
        return "{{ID_PREFIX}}" + currentRecordId;
    }
}
