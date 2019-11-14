# spider-flow

mvn package && java -jar  xx.jar

### 项目结构
```
spider-flow
├── spider-flow-api -- 插件开发的依赖
├── spider-flow-core -- 核心包
├── spider-flow-web -- web界面
```

#### 特性
- [x] 支持css选择器、正则提取
- [x] 支持JSON/XML格式
- [x] 支持Xpath/JsonPath提取
- [x] 支持多数据源、SQL select/insert/update/delete
- [x] 支持爬取JS动态渲染的页面
- [x] 支持代理
- [x] 支持二进制格式
- [x] 支持保存/读取文件(csv、xls、jpg等)
- [x] 常用字符串、日期、文件、加解密等函数
- [x] 支持流程嵌套
- [x] 支持插件扩展(自定义执行器，自定义函数）
- [ ] 任务监控
- [x] 支持HTTP接口

#### 插件列表
- [x] [Selenium插件](https://gitee.com/jmxd/spider-flow-selenium)
- [x] [Redis插件](https://gitee.com/jmxd/spider-flow-redis)
- [x] [OSS插件](https://gitee.com/jmxd/spider-flow-oss)
- [x] [Mongodb插件](https://gitee.com/jmxd/spider-flow-mongodb)
- [ ] Hbase插件
- [x] [IP代理池插件](https://gitee.com/jmxd/spider-flow-proxypool)
- [x] [OCR识别插件](https://gitee.com/jmxd/spider-flow-ocr)
- [x] [电子邮箱插件](https://gitee.com/jmxd/spider-flow-mailbox)

