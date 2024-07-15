# Kyoku Bot
开发中的Kyoku二号机！

## 依赖
Kyoku Bot使用`Poetry`进行项目管理，需要Python版本`>=3.12`。

```shell
poetry install
```

## 运行

```shell
poetry run start
```

## 配置
Kyoku Bot的配置均位于`pyproject.toml`也就是poetry的项目配置文件中，默认的配置项如下：
```toml
[kyokubot.config]
# onebot连接部分
host = "0.0.0.0"
port = 8080
# 数据库设置部分，数据库可用postgresql, mysql, sqlite三种类型
# 请确保目标主机中有名为kyokubotdb的数据库且提供的用户名对其具有访问权限
# 如使用sqlite数据库那么其他配置项不起实际作用
# 暂时仅支持postgre sql数据库
db_type = "postgresql"
db_host= "localhost"
db_port = 5432
db_username = "kyokubot"
db_passwd = "kyokubot"  
```

## Q&A

### 为什么使用Poetry而不是pipenv？
Poetry是一个更加现代化的Python项目管理工具，它提供了更好的依赖管理和构建工具，同时也更加稳定。

更主要的原因是我懒，poetry对懒人真的非常友好。

### 配置数据库？

如果你真的不会配置`mysql`和`postgresql`这两个数据库，那么请使用`sqlite`数据库，只需要将`db_type`设置为`sqlite`即可。

使用`postgresql`和`mysql`时请不要忘记还要配置数据库对应的配置文件以允许使用密码访问（以及在有必要的情况下的外部访问支持）。

如果需要从外部访问数据库请务必记住要每隔一段时间更换密码！