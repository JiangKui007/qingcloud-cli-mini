# QingCloud CLI mini 

### 简介

青云mini命令行，以青云API为基础。支持三种命令：创建主机(RunInstances)，获取主机(DescribeInstances)，销毁主机(TerminateInstances)

### 配置方式

#### 1、申请下载access_key文件

[access_key文件下载地址](https://console.qingcloud.com/access_keys/)

文件保存在`qingcloud-cli-mini` 根目录下，与`qingcloud.py` 同级。

#### 2、配置configuration.py 文件

将下载好的`access_keys`在系统中的绝对路径传递给`load_access_conf`函数。

配置程序默认的地区`zone`，这里是`sh1a`. 参见：[地区-机型列表](https://docs.qingcloud.com/product/api/common/includes/instance_type.html#instance-type)

完成配置。

#### 3、环境配置

python3.7.x、PyYAML 5.3 、requests 2.22.0

#### 4、使用方法示例

```bash
git clone https://github.com/JiangKui007/qingcloud-cli-mini.git
cd qingcloud-cli-mini
```


**启动一个ubuntu18.04的Linux实例**

示例：
```bash
python qingcloud.py iaas run-instances --image_id bionic1x64c --login_mode passwd --login_passwd Qc123456 -t s1.small.r1 -z sh1a -c 1 -C 1
```

[run-instances参数列表](https://docs.qingcloud.com/product/api/action/instance/run_instances.html)

**查看相关zone的实例**

示例：
```bash
python qingcloud.py iaas describe-instances -z sh1a
```

[describe-instances参数列表](https://docs.qingcloud.com/product/api/action/instance/describe_instances.html)

**销毁实例**

示例： 

```bash
python qingcloud.py iaas terminate-instances -z sh1a -i i-xqbryvk7
```
[ terminate-instances 参数列表](https://docs.qingcloud.com/product/api/action/instance/terminate_instances.html)





