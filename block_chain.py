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
  
if __name__ == "__main__":
    manolo_blockChain = block_chain()