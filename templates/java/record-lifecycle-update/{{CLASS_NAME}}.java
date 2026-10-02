package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.updateRecord

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.complex.eb.templatehook.TransactionData;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;
import com.temenos.t24.api.records.{{TARGET_APP_PACKAGE}}.{{TARGET_APP_CLASS}}Record;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public void updateRecord(String application, String currentRecordId, TStructure currentRecord,
            TStructure unauthorisedRecord, TStructure liveRecord, TransactionContext transactionContext,
            List<TransactionData> transactionData, List<TStructure> currentRecords) {

        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(currentRecord);
        String targetId = rec.get{{FIELD}}().getValue();
        if (targetId == null || targetId.isEmpty()) {
            return;
        }
        TransactionData txn = new TransactionData();
        txn.setVersionId("{{TARGET_APP}},{{TARGET_VERSION}}");
        txn.setFunction("I");
        txn.setNumberOfAuthoriser("0");
        txn.setTransactionId(targetId);
        transactionData.add(txn);

        {{TARGET_APP_CLASS}}Record target = new {{TARGET_APP_CLASS}}Record();
        target.set{{TARGET_FIELD}}("{{TARGET_VALUE}}");
        currentRecords.add(target.toStructure());
    }
}
