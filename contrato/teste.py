import sys, time , pprint, os
from web3 import Web3, HTTPProvider
from solcx import compile_source
from eth_account import Account

import random

conta = Account.create(random.randint(1, 999999999))

w3 = Web3(HTTPProvider('https://rpc.sepolia.dev'))
#_key = '77843608035084c2deb8e8ec5f0d4f1887cefafebdb32da361cc36d54742d419'
#_address = '0x928783707f0a4ed28D3e9C78eC68BBF2378bDFc8'
#_etherscanToken 16D33MUUWFSXYJAVBCGJ5SGZ7N497PRIRX

#nonce = w3.eth.get_transaction_count(_address)

gas = w3.eth.gasPrice
gas_limit = w3.eth.getBlock("latest").gasLimit

'''
def compile_source_file(file_path):
  #print(file_path)
  with open(file_path, 'r') as f:
    source = f.read()
  return compile_source(source)


def deploy_contract(w3, contract_interface):
  tx_hash = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
  ).deploy(transaction)
  address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
  return address


def wait_for_receipt(w3, tx_hash, poll_interval):
  while True:
    tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
    if tx_receipt:
      return tx_receipt
    time.sleep(poll_interval)

path = '/home/ric/Programas/smartcon/smartcon/contract/1/Outro2 Token.sol'
contract_source_path = path
compiled_sol = compile_source_file(path)

contract_id, contract_interface = compiled_sol.popitem()
abi=contract_interface['abi']
#print(abi)

# contract address
address = w3.to_checksum_address('0xD37160f1f077F82125093A313E004778165628f5')
erc20 = w3.eth.contract(address=address,abi=abi)
#name = erc20.functions.payable().call()
name = erc20.functions.name().call()
print(name)
simbolo = erc20.functions.symbol().call()
print(simbolo)
decimal = erc20.functions.approve('0x97Ee5e0D75C635A56011567a8056b8B5B54D6829',1).call()
print(decimal)
total = erc20.all_functions()
for a in total:
  print(a)
conta_saldo = erc20.functions.balanceOf('0x97Ee5e0D75C635A56011567a8056b8B5B54D6829').call()
print(conta_saldo)
acct = Account.from_key('0x1d29f8e48634962b143ee12fdbb6301a3cdb62b4e86665b52f2f97bf6ee96049')

tran = erc20.functions.transferFrom('0x97Ee5e0D75C635A56011567a8056b8B5B54D6829','0x01f00A899A307F02e9A0BD2cA2f3ee2c1Cc4D0C1',120).build_transaction(
#tran = erc20.functions.approve('0x01f00A899A307F02e9A0BD2cA2f3ee2c1Cc4D0C1', 120).build_transaction(
  {
    'from': acct.address,
    'nonce': w3.eth.get_transaction_count(acct.address),
    'gas': 2028712,
    'gasPrice': w3.to_wei('41', 'gwei')
  }
)
signed = acct.sign_transaction(tran)
#print(signed)
teste = w3.eth.send_raw_transaction(signed.raw_transaction)
print(Web3.to_hex(teste))
'''
#("b'\xd0Q\xe7\xc8\xcc\xd9\x992X\xe7\rr\xfe\xee\xb2v\xf4:\x9c\xbb\xbd#\x03^K\xa3;\xc1X\xabt>'")
'''0xD37160f1f077F82125093A313E004778165628f5
https://sepolia.etherscan.io/
contract_ = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin'])
abi=contract_interface['abi']
#print('conta: ' + str(conta.key))
acct = Account.from_key(0x1d29f8e48634962b143ee12fdbb6301a3cdb62b4e86665b52f2f97bf6ee96049);
print(type(conta.key))
co = Web3.to_text(text=conta.key)
print(type(co))
print(conta.key)
#print(acct)

construct_txn = contract_.constructor().build_transaction({
    'from': acct.address,
    'nonce': w3.eth.get_transaction_count(acct.address),
    'gas': 1728712,
    'gasPrice': w3.to_wei('21', 'gwei')})

signed = acct.sign_transaction(construct_txn)
print(signed)
#w3.eth.send_raw_transaction(signed.raw_transaction)

'''
address = '0x01f00A899A307F02e9A0BD2cA2f3ee2c1Cc4D0C1'
key = '0x59f58a58d9b3e946b8ed0237cde0a81975a2d952b9df852a7b7ce30bc379f385'
to_add = '0x97Ee5e0D75C635A56011567a8056b8B5B54D6829'
val = 5000

address = w3.to_checksum_address(address)
to_add = w3.to_checksum_address(to_add)
transaction = {
  'to':to_add,
  'value':val,
  'gas': 2728712,
  'gasPrice': gas_limit,
  'nonce':w3.eth.get_transaction_count(address),
  'chainId':11155111
}
signed = Account.sign_transaction(transaction, key)
try:
  hash_ad = w3.eth.send_raw_transaction(signed.raw_transaction)
  hash_ad = w3.to_hex(hash_ad)
except Exception as e:
  print(e)

print(hash_ad)
