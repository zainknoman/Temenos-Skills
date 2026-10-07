package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: FUNDS.TRANSFER
// Hook type: RecordLifecycle.postUpdateRequest

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.servicehook.TransactionData;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.fundstransfer.FundsTransferRecord;
import com.temenos.t24.api.records.customer.CustomerRecord;
import com.temenos.t24.api.records.customer.RelationCodeClass;

public class GoldenPostUpdateGroup extends RecordLifecycle {

    @Override
    public void postUpdateRequest(String application, String currentRecordId, TStructure currentRecord,
            List<TransactionData> transactionData, List<TStructure> currentRecords,
            TransactionContext transactionContext) {

        FundsTransferRecord rec = new FundsTransferRecord(currentRecord);
        String targetId = rec.getDebitAcctNo().getValue();
        if (targetId == null || targetId.isEmpty()) {
            return;
        }
        TransactionData txn = new TransactionData();
        txn.setVersionId("CUSTOMER,GOLDEN.UPDATE");
        txn.setFunction("INPUT");
        txn.setNumberOfAuthoriser("0");
        txn.setSourceId("TEST.OFS");
        txn.setTransactionId(targetId);
        transactionData.add(txn);

        CustomerRecord target = new CustomerRecord();
        RelationCodeClass groupRelationCode = target.getRelationCode().isEmpty() ? new RelationCodeClass() : target.getRelationCode(0);
        groupRelationCode.setRelationCode("1");
        target.setRelationCode(groupRelationCode, 0);
        currentRecords.add(target.toStructure());
    }
}
