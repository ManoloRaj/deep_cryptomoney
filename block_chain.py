import hashlib
import json
from time import time

class block_chain(object) :
  def __init__(self):
    self.chain = []
    self.pending_transactions = []
    self.new_block(previous_hash="The Times of today ... sell to banks", proff=100)

  
if __name__ == "__main__":
    pass