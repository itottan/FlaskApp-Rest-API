"""
blocklist.py

このファイルには、JWTトークンのブロックリストのみが含まれています。
ユーザーがログアウトの時、トークンをブロックリストに追加します。
"""

# todo use db set list or redis
BLOCKLIST = set()