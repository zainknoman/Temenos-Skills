package {{JAVA_PACKAGE}};
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: {{APP}}
// Hook type: ActivityLifecycle.postCoreTableUpdate

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.activityhook.TransactionData;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;
import com.temenos.t24.api.records.{{TARGET_APP_PACKAGE}}.{{TARGET_APP_CLASS}}Record;

public class {{CLASS_NAME}} extends ActivityLifecycle {

    @Override
    public void postCoreTableUpdate(AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
            List<TransactionData> transactionData, List<TStructure> transactionRecord) {

        if (!"AUTH".equals(arrangementContext.getActivityStatus())) {
            return;
        }
        TransactionData txn = new TransactionData();
        txn.setVersionId("{{TARGET_APP}},{{TARGET_VERSION}}");
        txn.setFunction("INPUT");
        txn.setNumberOfAuthoriser("0");
        txn.setSourceId("{{OFS_SOURCE}}");
        txn.setTransactionId("{{TARGET_ID}}");
        transactionData.add(txn);
        {{TARGET_APP_CLASS}}Record target = new {{TARGET_APP_CLASS}}Record();
        target.set{{TARGET_FIELD}}("{{TARGET_VALUE}}");
        transactionRecord.add(target.toStructure());
    }
}
