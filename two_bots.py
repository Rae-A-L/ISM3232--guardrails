# two_bots.py
# Author: Rae Anthony Lewis

from change_queue import ChangeQueue
from chatbot import SupportChatBot
from keyword_model import KeywordModel
from order_tool import OrderLookup
from stock_tool import StockLookup
from toolbox import Toolbox

order_tool = OrderLookup({"A100": {"status": "shipped", "address": "14 Bay Road"}})
stock_tool = StockLookup({"rain jacket": 12, "day pack": 0})
tools = Toolbox(order_tool, stock_tool, ChangeQueue(order_tool))

model = KeywordModel()

sunny = SupportChatBot("Sunny", "You are cheeful and brief.", tools, model)
river = SupportChatBot("River", "You are formal and detailed.", tools, model)

sunny.respond("hello")
sunny.respond("Where is order A100?")
river.respond("hello")

print(sunny.name, len(sunny.history))
print(river.name, len(river.history))
print(sunny.history[1]["content"])
print(river.history[1]["content"])
print(sunny.instructions)
print(river.instructions)
