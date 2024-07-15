# NOTE.md
## WTF is this?

用于记录一下敲这个bot的时候的一些想法，就这样。

## 开发笔记

### 2024.07.13

首先是考虑一下数据存储的问题，暂时是考虑使用PostgreSQL作为数据库，然后跟bot后端分开来进行部署。

当然，操作sql的库选择了sqlalchemy，这样就可以适配不同数据库（只要同属SQL系数据库就行），考虑到sql特性的支持程度，主要是适配PostgreSQL和SQLite。

用户数据结构要在开发功能之前基本决定好，所以要多准备一些（哪怕用不到的）存储项。

| uniqueId | username | roles     | QQId | oopzId | discordId | wechatId | points | coins | crystals | backpack  | registerDate   | lastSignDate   |
|----------|----------|-----------|------|--------|-----------|----------|--------|-------|----------|-----------|----------------|----------------|
| str      | str      | list[str] | int  | str    | str       | str      | int    | int   | int      | str(json) | int(timestamp) | int(timestamp) |

