#print(w3.eth.get_block('latest'))
# print(w3.eth.get_transaction('0x7abada63af4f4c1a5297f25234aad90a0af2e518a3e48194d117715aef9b054f'))
print("............")
# print(w3.eth.get_transaction_receipt('0x7abada63af4f4c1a5297f25234aad90a0af2e518a3e48194d117715aef9b054f'))
"""
bb = w3.eth.get_block(78640, True)
trxlist = []
bk = {
    "difficulty": bb["difficulty"], "extraData": bb["extraData"].hex(), "gasLimit": bb["gasLimit"],
    "gasUsed": bb["gasUsed"], "hash": bb["hash"].hex(), "logsBloom": bb["logsBloom"].hex(),
    "miner": bb["miner"], "mixHash": bb["mixHash"].hex(), "nonce": bb["nonce"], "number": bb["number"],
    "parentHash": bb["parentHash"].hex(), "receiptsRoot": bb["receiptsRoot"].hex(),
    "sha3Uncles": bb["sha3Uncles"].hex(), "size": bb["size"], "stateRoot": bb["stateRoot"].hex(),
    "timestamp": bb["timestamp"], "totalDifficulty": bb["totalDifficulty"], "transactions": trxlist,
    "transactionsRoot": bb["transactionsRoot"].hex(), "uncles": bb["uncles"]
}
print("bk")
# print(bb)
print(".....")
for i in bb['transactions']:
    td = {"blockHash": i["blockHash"].hex(), "blockNumber": i["blockNumber"], "from": i["from"],
          "gas": i["gas"], "gasPrice": i["gasPrice"],"timeStamp":bb["timestamp"],"hash": i["hash"].hex(), "input": i["input"],
          "nonce": i["nonce"], "to": i["to"], "transactionIndex": i["transactionIndex"],
          "value": i["value"], "type": i["type"], "chainId": i["chainId"], "v": i["v"], "r": i["r"].hex(),
          "s": i["s"].hex(), "gwei": float(i["gasPrice"])/1000000000,
          "gasFee": (i["gas"]*float(i["gasPrice"]))/1000000000000000000
          }
    trxlist.append(td)
    print(td)
    print("..........")
print("BK OBJ")
print(bk)
print("...bb end...")
"""



print(config["coinName"])
print(config["symbol"])

print(w3.eth.get_block_number())

print("Filter")
print(w3.eth.filter('latest'))
print("Filter End")
print("...Bal...")
print(w3.eth.get_balance('0x831faE0AD75bA71a42655e90f425EcD2Be79Af6C') /
      1000000000000000000)  # devide Bal / 1000000000000000000
print(round(w3.eth.gas_price * 21000 / 1000000000000000000, 18))