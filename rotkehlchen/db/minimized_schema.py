# This file contains minimized db schema and it should not be touched manually but only generated by tools/scripts/generate_minimized_db_schema.py
# Created at 2023-03-20 13:18:12 UTC with rotki version 1.26.4.dev1075+gd3fc1b8ff by nebolax
MINIMIZED_USER_DB_SCHEMA = {
    'trade_type': 'typeCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'location': 'locationCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'asset_movement_category': 'categoryCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'balance_category': 'categoryCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'assets': 'identifierTEXTNOTNULLPRIMARYKEY',
    'timed_balances': 'categoryCHAR(1)NOTNULLDEFAULT("A")REFERENCESbalance_category(category),timestampINTEGER,currencyTEXT,amountTEXT,usd_valueTEXT,FOREIGNKEY(currency)REFERENCESassets(identifier)ONUPDATECASCADE,PRIMARYKEY(timestamp,currency,category)',
    'timed_location_data': 'timestampINTEGER,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),usd_valueTEXT,PRIMARYKEY(timestamp,location)',
    'user_credentials': 'nameTEXTNOTNULL,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),api_keyTEXT,api_secretTEXT,passphraseTEXT,PRIMARYKEY(name,location)',
    'user_credentials_mappings': 'credential_nameTEXTNOTNULL,credential_locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),setting_nameTEXTNOTNULL,setting_valueTEXTNOTNULL,FOREIGNKEY(credential_name,credential_location)REFERENCESuser_credentials(name,location)ONDELETECASCADEONUPDATECASCADE,PRIMARYKEY(credential_name,credential_location,setting_name)',
    'external_service_credentials': 'nameVARCHAR[30]NOTNULLPRIMARYKEY,api_keyTEXT',
    'blockchain_accounts': 'blockchainVARCHAR[24]NOTNULL,accountTEXTNOTNULL,labelTEXT,PRIMARYKEY(blockchain,account)',
    'evm_accounts_details': 'accountVARCHAR[42]NOTNULL,chain_idINTEGERNOTNULL,keyTEXTNOTNULL,valueTEXTNOTNULL,PRIMARYKEY(account,chain_id,key,value)',
    'multisettings': 'nameVARCHAR[24]NOTNULL,valueTEXT,UNIQUE(name,value)',
    'manually_tracked_balances': 'idINTEGERPRIMARYKEY,assetTEXTNOTNULL,labelTEXTNOTNULL,amountTEXT,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),categoryCHAR(1)NOTNULLDEFAULT("A")REFERENCESbalance_category(category),FOREIGNKEY(asset)REFERENCESassets(identifier)ONUPDATECASCADE',
    'trades': 'idTEXTPRIMARYKEYNOTNULL,timestampINTEGERNOTNULL,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),base_assetTEXTNOTNULL,quote_assetTEXTNOTNULL,typeCHAR(1)NOTNULLDEFAULT("A")REFERENCEStrade_type(type),amountTEXTNOTNULL,rateTEXTNOTNULL,feeTEXT,fee_currencyTEXT,linkTEXT,notesTEXT,FOREIGNKEY(base_asset)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(quote_asset)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(fee_currency)REFERENCESassets(identifier)ONUPDATECASCADE',
    'evm_transactions': 'tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,timestampINTEGERNOTNULL,block_numberINTEGERNOTNULL,from_addressTEXTNOTNULL,to_addressTEXT,valueTEXTNOTNULL,gasTEXTNOTNULL,gas_priceTEXTNOTNULL,gas_usedTEXTNOTNULL,input_dataBLOBNOTNULL,nonceINTEGERNOTNULL,PRIMARYKEY(tx_hash,chain_id)',
    'evm_internal_transactions': 'parent_tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,trace_idINTEGERNOTNULL,timestampINTEGERNOTNULL,block_numberINTEGERNOTNULL,from_addressTEXTNOTNULL,to_addressTEXT,valueTEXTNOTNULL,FOREIGNKEY(parent_tx_hash,chain_id)REFERENCESevm_transactions(tx_hash,chain_id)ONDELETECASCADEONUPDATECASCADE,PRIMARYKEY(parent_tx_hash,chain_id,trace_id,from_address,to_address,value)',
    'evmtx_receipts': 'tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,contract_addressTEXT,/*canbenull*/statusINTEGERNOTNULLCHECK(statusIN(0,1)),typeINTEGERNOTNULL,FOREIGNKEY(tx_hash,chain_id)REFERENCESevm_transactions(tx_hash,chain_id)ONDELETECASCADEONUPDATECASCADE,PRIMARYKEY(tx_hash,chain_id)',
    'evmtx_receipt_logs': 'tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,log_indexINTEGERNOTNULL,dataBLOBNOTNULL,addressTEXTNOTNULL,removedINTEGERNOTNULLCHECK(removedIN(0,1)),FOREIGNKEY(tx_hash,chain_id)REFERENCESevmtx_receipts(tx_hash,chain_id)ONDELETECASCADEONUPDATECASCADE,PRIMARYKEY(tx_hash,chain_id,log_index)',
    'evmtx_receipt_log_topics': 'tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,log_indexINTEGERNOTNULL,topicBLOBNOTNULL,topic_indexINTEGERNOTNULL,FOREIGNKEY(tx_hash,chain_id,log_index)REFERENCESevmtx_receipt_logs(tx_hash,chain_id,log_index)ONDELETECASCADEONUPDATECASCADE,PRIMARYKEY(tx_hash,chain_id,log_index,topic_index)',
    'evmtx_address_mappings': 'addressTEXTNOTNULL,tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,blockchainTEXTNOTNULL,FOREIGNKEY(blockchain,address)REFERENCESblockchain_accounts(blockchain,account)ONDELETECASCADE,FOREIGNKEY(tx_hash,chain_id)referencesevm_transactions(tx_hash,chain_id)ONUPDATECASCADEONDELETECASCADE,PRIMARYKEY(address,tx_hash,chain_id)',
    'margin_positions': 'idTEXTPRIMARYKEY,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),open_timeINTEGER,close_timeINTEGER,profit_lossTEXT,pl_currencyTEXTNOTNULL,feeTEXT,fee_currencyTEXT,linkTEXT,notesTEXT,FOREIGNKEY(pl_currency)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(fee_currency)REFERENCESassets(identifier)ONUPDATECASCADE',
    'asset_movements': 'idTEXTPRIMARYKEY,locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),categoryCHAR(1)NOTNULLDEFAULT("A")REFERENCESasset_movement_category(category),addressTEXT,transaction_idTEXT,timestampINTEGER,assetTEXTNOTNULL,amountTEXT,fee_assetTEXT,feeTEXT,linkTEXT,FOREIGNKEY(asset)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(fee_asset)REFERENCESassets(identifier)ONUPDATECASCADE',
    'used_query_ranges': 'nameVARCHAR[24]NOTNULLPRIMARYKEY,start_tsINTEGER,end_tsINTEGER',
    'evm_tx_mappings': 'tx_hashBLOBNOTNULL,chain_idINTEGERNOTNULL,valueINTEGERNOTNULL,FOREIGNKEY(tx_hash,chain_id)referencesevm_transactions(tx_hash,chain_id)ONUPDATECASCADEONDELETECASCADE,PRIMARYKEY(tx_hash,chain_id,value)',
    'settings': 'nameVARCHAR[24]NOTNULLPRIMARYKEY,valueTEXT',
    'tags': 'nameTEXTNOTNULLPRIMARYKEYCOLLATENOCASE,descriptionTEXT,background_colorTEXT,foreground_colorTEXT',
    'tag_mappings': 'object_referenceTEXT,tag_nameTEXT,FOREIGNKEY(tag_name)REFERENCEStags(name)PRIMARYKEY(object_reference,tag_name)',
    'aave_events': 'addressVARCHAR[42]NOTNULL,event_typeVARCHAR[10]NOTNULL,block_numberINTEGERNOTNULL,timestampINTEGERNOTNULL,tx_hashBLOBNOTNULL,log_indexINTEGERNOTNULL,asset1TEXTNOTNULL,asset1_amountTEXTNOTNULL,asset1_usd_valueTEXTNOTNULL,asset2TEXT,asset2amount_borrowrate_feeamountTEXT,asset2usd_value_accruedinterest_feeusdvalueTEXT,borrow_rate_modeVARCHAR[10],FOREIGNKEY(asset1)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(asset2)REFERENCESassets(identifier)ONUPDATECASCADE,PRIMARYKEY(event_type,tx_hash,log_index)',
    'yearn_vaults_events': 'addressVARCHAR[42]NOTNULL,event_typeVARCHAR[10]NOTNULL,from_assetTEXTNOTNULL,from_amountTEXTNOTNULL,from_usd_valueTEXTNOTNULL,to_assetTEXTNOTNULL,to_amountTEXTNOTNULL,to_usd_valueTEXTNOTNULL,pnl_amountTEXT,pnl_usd_valueTEXT,block_numberINTEGERNOTNULL,timestampINTEGERNOTNULL,tx_hashBLOBNOTNULL,log_indexINTEGERNOTNULL,versionINTEGERNOTNULLDEFAULT1,FOREIGNKEY(from_asset)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(to_asset)REFERENCESassets(identifier)ONUPDATECASCADE,PRIMARYKEY(event_type,tx_hash,log_index)',
    'xpubs': 'xpubTEXTNOTNULL,derivation_pathTEXTNOTNULL,labelTEXT,blockchainTEXTNOTNULL,PRIMARYKEY(xpub,derivation_path,blockchain)',
    'xpub_mappings': 'addressTEXTNOTNULL,xpubTEXTNOTNULL,derivation_pathTEXTNOTNULL,account_indexINTEGER,derived_indexINTEGER,blockchainTEXTNOTNULL,FOREIGNKEY(blockchain,address)REFERENCESblockchain_accounts(blockchain,account)ONDELETECASCADEFOREIGNKEY(xpub,derivation_path,blockchain)REFERENCESxpubs(xpub,derivation_path,blockchain)ONDELETECASCADEPRIMARYKEY(address,xpub,derivation_path,blockchain)',
    'amm_events': 'tx_hashBLOBNOTNULL,log_indexINTEGERNOTNULL,addressVARCHAR[42]NOTNULL,timestampINTEGERNOTNULL,typeTEXTNOTNULL,pool_addressVARCHAR[42]NOTNULL,token0_identifierTEXTNOTNULL,token1_identifierTEXTNOTNULL,amount0TEXT,amount1TEXT,usd_priceTEXT,lp_amountTEXT,FOREIGNKEY(token0_identifier)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(token1_identifier)REFERENCESassets(identifier)ONUPDATECASCADE,PRIMARYKEY(tx_hash,log_index)',
    'eth2_validators': 'validator_indexINTEGERNOTNULLPRIMARYKEY,public_keyTEXTNOTNULLUNIQUE,ownership_proportionTEXTNOTNULL',
    'eth2_deposits': 'tx_hashBLOBNOTNULL,tx_indexINTEGERNOTNULL,from_addressVARCHAR[42]NOTNULL,timestampINTEGERNOTNULL,pubkeyTEXTNOTNULL,withdrawal_credentialsTEXTNOTNULL,amountTEXTNOTNULL,usd_valueTEXTNOTNULL,FOREIGNKEY(pubkey)REFERENCESeth2_validators(public_key)ONUPDATECASCADEONDELETECASCADE,PRIMARYKEY(tx_hash,pubkey,amount)/*multipledepositscanexistforsamepubkey*/',
    'eth2_daily_staking_details': 'validator_indexINTEGERNOTNULL,timestampintegerNOTNULL,start_usd_priceTEXTNOTNULL,end_usd_priceTEXTNOTNULL,pnlTEXTNOTNULL,start_amountTEXTNOTNULL,end_amountTEXTNOTNULL,missed_attestationsINTEGER,orphaned_attestationsINTEGER,proposed_blocksINTEGER,missed_blocksINTEGER,orphaned_blocksINTEGER,included_attester_slashingsINTEGER,proposer_attester_slashingsINTEGER,deposits_numberINTEGER,amount_depositedTEXT,FOREIGNKEY(validator_index)REFERENCESeth2_validators(validator_index)ONUPDATECASCADEONDELETECASCADE,PRIMARYKEY(validator_index,timestamp)',
    'history_events': 'identifierINTEGERNOTNULLPRIMARYKEY,entry_typeINTEGERNOTNULL,event_identifierBLOBNOTNULL,sequence_indexINTEGERNOTNULL,timestampINTEGERNOTNULL,locationTEXTNOTNULL,location_labelTEXT,assetTEXTNOTNULL,amountTEXTNOTNULL,usd_valueTEXTNOTNULL,notesTEXT,typeTEXTNOTNULL,subtypeTEXTNOTNULL,FOREIGNKEY(asset)REFERENCESassets(identifier)ONUPDATECASCADE,UNIQUE(event_identifier,sequence_index)',
    'evm_events_info': 'identifierINTEGERPRIMARYKEY,counterpartyTEXT,productTEXT,addressTEXT,extra_dataTEXT,FOREIGNKEY(identifier)REFERENCEShistory_events(identifier)ONUPDATECASCADEONDELETECASCADE',
    'history_events_mappings': 'parent_identifierINTEGERNOTNULL,nameTEXTNOTNULL,valueINTEGERNOTNULL,FOREIGNKEY(parent_identifier)referenceshistory_events(identifier)ONUPDATECASCADEONDELETECASCADE,PRIMARYKEY(parent_identifier,name,value)',
    'ledger_action_type': 'typeCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'ledger_actions': 'identifierINTEGERNOTNULLPRIMARYKEY,timestampINTEGERNOTNULL,typeCHAR(1)NOTNULLDEFAULT("A")REFERENCESledger_action_type(type),locationCHAR(1)NOTNULLDEFAULT("A")REFERENCESlocation(location),amountTEXTNOTNULL,assetTEXTNOTNULL,rateTEXT,rate_assetTEXT,linkTEXT,notesTEXT,FOREIGNKEY(asset)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(rate_asset)REFERENCESassets(identifier)ONUPDATECASCADE',
    'action_type': 'typeCHAR(1)PRIMARYKEYNOTNULL,seqINTEGERUNIQUE',
    'ignored_actions': 'typeCHAR(1)NOTNULLDEFAULT("A")REFERENCESaction_type(type),identifierTEXT,PRIMARYKEY(type,identifier)',
    'balancer_events': 'tx_hashBLOBNOTNULL,log_indexINTEGERNOTNULL,addressVARCHAR[42]NOTNULL,timestampINTEGERNOTNULL,typeTEXTNOTNULL,pool_address_tokenTEXTNOTNULL,lp_amountTEXTNOTNULL,usd_valueTEXTNOTNULL,amount0TEXTNOTNULL,amount1TEXTNOTNULL,amount2TEXT,amount3TEXT,amount4TEXT,amount5TEXT,amount6TEXT,amount7TEXT,FOREIGNKEY(pool_address_token)REFERENCESassets(identifier)ONUPDATECASCADE,PRIMARYKEY(tx_hash,log_index)',
    'nfts': 'identifierTEXTNOTNULLPRIMARYKEY,nameTEXT,last_priceTEXT,last_price_assetTEXT,manual_priceINTEGERNOTNULLCHECK(manual_priceIN(0,1)),owner_addressTEXT,blockchainTEXTGENERATEDALWAYSAS("ETH")VIRTUAL,is_lpINTEGERNOTNULLCHECK(is_lpIN(0,1)),image_urlTEXT,collection_nameTEXT,FOREIGNKEY(blockchain,owner_address)REFERENCESblockchain_accounts(blockchain,account)ONDELETECASCADE,FOREIGNKEY(identifier)REFERENCESassets(identifier)ONUPDATECASCADE,FOREIGNKEY(last_price_asset)REFERENCESassets(identifier)ONUPDATECASCADE',
    'ens_mappings': 'addressTEXTNOTNULLPRIMARYKEY,ens_nameTEXTUNIQUE,last_updateINTEGERNOTNULL,last_avatar_updateINTEGER',
    'address_book': 'addressTEXTNOTNULL,blockchainTEXT,nameTEXTNOTNULL,PRIMARYKEY(address,blockchain)',
    'rpc_nodes': 'identifierINTEGERNOTNULLPRIMARYKEY,nameTEXTNOTNULL,endpointTEXTNOTNULL,ownedINTEGERNOTNULLCHECK(ownedIN(0,1)),activeINTEGERNOTNULLCHECK(activeIN(0,1)),weightTEXTNOTNULL,blockchainTEXTNOTNULL',
    'user_notes': 'identifierINTEGERNOTNULLPRIMARYKEY,titleTEXTNOTNULL,contentTEXTNOTNULL,locationTEXTNOTNULL,last_update_timestampINTEGERNOTNULL,is_pinnedINTEGERNOTNULLCHECK(is_pinnedIN(0,1))',
}
