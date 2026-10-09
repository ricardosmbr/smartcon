import sys, time , pprint
from web3 import Web3, HTTPProvider
from django.conf import settings
from solcx import compile_source
from eth_account import Account
import string


class Contra:

  w3 = Web3(HTTPProvider(settings.PROVEDOR))
  def compile_source_file(self,file_path):
    with open(file_path, 'r') as f:
      source = f.read()
      ret = compile_source(source)
    return ret


class Fabrica(Contra):

  def __init__(self,file_path,key):
    print('compilando contrato')
    compiled_sol = self.compile_source_file(file_path)
    contract_id, contract_interface = compiled_sol.popitem()
    self.myabi=contract_interface['abi']
    contract_ = self.w3.eth.contract(
      abi=contract_interface['abi'],
      bytecode=contract_interface['bin']
    )
    acct = Account.from_key(key)
    # print('compilado contrato',acct.address)
    
    construct_txn = contract_.constructor().build_transaction({
      'from': acct.address,
      'nonce': self.w3.eth.get_transaction_count(acct.address),
      'gas': 2728712,
      'gasPrice': self.w3.to_wei('21', 'gwei')}
    )
    self.signed = acct.sign_transaction(construct_txn)
    # print(self.signed)

  def enviar(self):
    try:
      self.address = self.w3.eth.send_raw_transaction(self.signed.raw_transaction)
      return self.address
    except Exception as e:
      return e

  
  def Recibo(self,tx_hash):

    while True:
      self.tx_receipt = self.w3.eth.get_transaction_receipt(tx_hash)
      if self.tx_receipt:
        return self.tx_receipt
      time.sleep(2)


class EnviarToken(Contra):

  def __init__(self,address,abi,private,val,to_add):
    address = Web3.to_checksum_address(address)
    erc20 = self.w3.eth.contract(address=address,abi=abi)

    try:
      name = erc20.functions.name().call()
    except Exception as e:
      print(e)
    try:
      to_add = Web3.to_checksum_address(to_add)
    except Exception as e:
      print(e)
    acct = Account.from_key(private)
    transfer = erc20.functions.transfer(to_add, int(val))
    gas_price = self.w3.eth.gas_price
    tx_params = {
      'from': acct.address,
      'nonce': self.w3.eth.get_transaction_count(acct.address),
      'gasPrice': gas_price,
    }
    # Estimate this call's actual cost. A fixed 2.7M gas limit made the RPC
    # require far more ETH than a typical ERC-20 transfer consumes.
    gas_estimate = transfer.estimate_gas(tx_params)
    tx_params['gas'] = max(gas_estimate, int(gas_estimate * 1.2))
    tran = transfer.build_transaction(tx_params)
    self.signed = acct.sign_transaction(tran)

  def enviar(self):
    # Returning an exception makes it look like a transaction hash to callers.
    self.address = self.w3.eth.send_raw_transaction(self.signed.raw_transaction)
    return self.address


class TransferirEther(Contra):

  def __init__(self,address,key,valor,to_add):
    val = int(valor)
    address = self.w3.to_checksum_address(address)
    to_add = self.w3.to_checksum_address(to_add)
    transaction = {
      'to':to_add,
      'value':val,
      'gas': 2728712,
      'gasPrice': self.w3.to_wei('41', 'gwei'),
      'nonce':self.w3.eth.get_transaction_count(address),
      'chainId':settings.WEB3_CHAIN_ID
    }
    self.signed = Account.sign_transaction(transaction, key)

  def enviar(self):
    try:
      self.address_h = self.w3.eth.send_raw_transaction(self.signed.raw_transaction)
      return self.address_h
    except Exception as e:
      return e
