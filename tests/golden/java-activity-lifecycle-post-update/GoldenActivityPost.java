package com.temenos.t24.custom.golden;
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: AA.ARRANGEMENT.ACTIVITY
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
import com.temenos.t24.api.records.account.AccountRecord;

public class GoldenActivityPost extends ActivityLifecycle {

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
        txn.setVersionId("ACCOUNT,GOLDEN.UPDATE");
        txn.setFunction("INPUT");
        txn.setNumberOfAuthoriser("0");
        txn.setSourceId("TEST.OFS");
        txn.setTransactionId("SAMPLE.ID");
        transactionData.add(txn);
        AccountRecord target = new AccountRecord();
        target.setCategory("1001");
        transactionRecord.add(target.toStructure());
    }
}
