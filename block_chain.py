import hashlib
import json
from time import time

class block_chain(object) :
  def __init__(self):
    self.chain = []
    self.pending_transactions = []
    self.new_block(previous_hash="The Times of today ... sell to banks", proff=100)

  def new_block(self, proff, previous_hash=None):
    block = {
      'index'         : len(self.chain) + 1,
      'timestamp'     : time(),
      'transactions'  : self.pending_transactions,
      'proof'         : previous_hash or self.hash(self.chain[-1])
    }
    self.pending_transactions = []
    self.chain.append(block)

    return block


  @property
  def last_block(self):

    return self.chain[-1]

  def new_transaction(self, sender, recipient, amount):
    transaction = {
      'sender'    : sender,
      'recipient' : recipient,
      'amount'    : amount
    }

    self.pending_transactions.append(transaction)
    return self.last_block['index'] + 1

  def hash(self, block):
    string_object = json.dumps(block, sort_keys=True)
    block_string = string_object.encode()

    raw_hash = hashlib.sha256(block_string)
    hex_hash = raw_hash.hexdigest()

    return hex_hash
  
if __name__ == "__main__":
  blockchain = block_chain()
  t1 = blockchain.new_transaction("Satoshi", "Mike", "5 BTC")
  t2 = blockchain.new_transaction("Mike", "Satoshi", "1 BTC")
  t3 = blockchain.new_transaction("Satoshi", "Hal Finney", "5 BTC")

  blockchain.new_block(12345)

  print("Block chain :", blockchain.chain)